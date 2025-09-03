import os.path

import document
import md_writer


def _strip_filename(filename):
    filename = os.path.basename(filename)
    assert filename.endswith(".md"), filename
    return filename[:-3]


def _process_internal_link(link):
    if not link:
        return "#"
    else:
        index = link.find("#")
        if index == -1:
            # 'filename'
            return f"<{_strip_filename(link)}>"
        elif index == 0:
            # '#section'
            return link
        else:
            # 'filename#section'
            return f"<{_strip_filename(link[:index])}{link[index:]}>"


class GithubMarkdownWriter(md_writer.MarkdownWriter):
    def __init__(self, creator, split_level = 0, *, collapse_level = 0, toc_collapse_level = 0):
        super().__init__(split_level)
        self._collapse_level = collapse_level
        self._toc_collapse_level = toc_collapse_level
        self._collapsing = False
        
    def get_output(self) -> str:
        if self._collapsing:
            self._output.append("</details>\n")
            self._collapsing = False
        return super().get_output()

    def add_header(self, header: document.Header) -> None:
        assert header.outline_level
        # Skip chapter names as GitHub wiki shows file names anyway, and file names are the same as chapter names
        if header.outline_level > self._split_level:
            # Close the previous section
            if self._collapsing and header.outline_level <= self._collapse_level:
                self._output.append("</details>\n\n")
                self._collapsing = False
            # Write the new section
            if header.outline_level == self._collapse_level:
                self._output.append("<details>\n<summary>\n\n")
                self._collapsing = True
            super()._add_header(header)
            if self._collapsing:
                self._output.append("\n</summary>")
            self._output.append(self.PARAGRAPH_SEPARATOR)
    
    def _add_toc(self, toc):
        assert self._toc_collapse_level in (0, 1) # Cannot collapse inside a list
        assert toc.items[0].level == 1
        for i in toc.items:
            assert i.level > 0
            assert i.name
            assert i.link
            assert i.link.startswith("<")
            assert i.link.endswith(">")
            if i.level > 1:
                if ":" in i.link:
                    link_text = f"[[{i.name}|{i.link[1:-1]}]]"
                else:
                    link_text = f"[{i.name}]({i.link})"
                self._output.append("  " * (i.level - 2) + "- " + link_text + "\n")
            else:        
                if self._collapsing:
                    self._output.append("\n</details>\n\n")
                if self._toc_collapse_level:
                    self._collapsing = True
                    # Markdown does not work inside <summary>
                    self._output.append(f'<details>\n<summary><a href="{self._strip_link(i.link)}">{i.name}</a></summary>\n\n')
                else:
                    self._output.append(f"\n### [{i.name}]({i.link})\n\n")
    
    @staticmethod
    def _open_link(link):
        if link.startswith("<"):
            assert link.endswith(">")
            if ":" in link:
                return "[[" # GitHub supports colons only in MediaWiki syntax. However, that syntax does not support other markdown in links.
        return "["
    
    @staticmethod
    def _close_link(link):
        if link.startswith("<"):
            assert link.endswith(">")
            if ":" in link:
                return f"|{link[1:-1]}]]"
        return f"]({link})"


github_strategy = document.Strategy(".md",
                                    True,
                                    md_writer.make_ref_for_header, 
                                    md_writer.make_ref_for_text, 
                                    md_writer.resolve_refs_conflict,
                                    _process_internal_link,
                                    md_writer.string_to_filename,
                                    md_writer.index_filename)