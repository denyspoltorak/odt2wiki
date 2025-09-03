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
    def __init__(self, creator, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def add_header(self, header: document.Header) -> None:
        assert header.outline_level
        # Skip chapter names as GitHub wiki shows file names anyway, and file names are the same as chapter names
        if header.outline_level > self._split_level:
            super().add_header(header)


github_strategy = document.Strategy(".md",
                                    True,
                                    md_writer.make_ref_for_header, 
                                    md_writer.make_ref_for_text, 
                                    md_writer.resolve_refs_conflict,
                                    _process_internal_link,
                                    md_writer.string_to_filename,
                                    md_writer.index_filename)