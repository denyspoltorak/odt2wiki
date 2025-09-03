import document
import md_writer


def _process_internal_link(link):
    return f'{{{{< relref "{link}" >}}}}' if link else "#"

def _string_to_filename(string):
    return "".join([l.lower() if l.isalnum() else "-" for l in string.rstrip(". ")])

def _index_filename(string):
    return "_index"


class HugoMarkdownWriter(md_writer.MarkdownWriter):
    METADATA_SEPARATOR = "+++"
    
    def __init__(self, creator, split_level = 0):
        super().__init__(split_level)
        self._make_metadata(creator)
        
    def _strip_link(self, link):
        assert link.startswith('{{< relref "')
        assert link.enswith('" >}}')
        return link[len('{{< relref "'):-len('" >}}')]
    
    def _add_nav_bar(self, navbar):
        self._output.append("<nav>\n\n")
        super()._add_nav_bar(navbar)
        self._output.append("\n</nav>\n\n")
    
    def _make_metadata(self, creator):
        output = [self.METADATA_SEPARATOR,]
        weight = 1 + creator.parent.children.index(creator) if creator.parent else 1
        output.append(f"weight = {weight}")
        output.append(f'title = "{creator.header.to_string()}"')
        if creator.type == document.SectionType.FOLDER:
            output.append("bookCollapseSection = true")
        output.append(self.METADATA_SEPARATOR)
        self._output.append("\n".join(output))
        self._output.append(self.PARAGRAPH_SEPARATOR)
        

hugo_strategy = document.Strategy(  ".md",
                                    True, #False,    # Hugo Book will release its navbar in v12 in May 2026.
                                    md_writer.make_ref_for_header, 
                                    md_writer.make_ref_for_text, 
                                    md_writer.resolve_refs_conflict,
                                    _process_internal_link,
                                    _string_to_filename,
                                    _index_filename)