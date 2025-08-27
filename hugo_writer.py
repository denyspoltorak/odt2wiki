import document
import md_writer


METADATA_SEPARATOR = "+++"


def _process_internal_link(link):
    return f'{{{{< relref "{link}" >}}}}' if link else "#"

def _string_to_filename(string):
    return "".join([l.lower() if l.isalnum() else "-" for l in string.rstrip(". ")])

def _index_filename(string):
    return "_index"


class HugoMarkdownWriter(md_writer.MarkdownWriter):
    def __init__(self, creator, **kwargs):
        super().__init__(**kwargs)
        self._make_metadata(creator)
        
    def _strip_link(self, link):
        assert link.startswith('{{< relref "')
        assert link.enswith('" >}}')
        return link[len('{{< relref "'):-len('" >}}')]
    
    def _add_nav_bar(self, navbar):
        assert False
    
    def _make_metadata(self, creator):
        output = [METADATA_SEPARATOR,]
        weight = 1 + creator.parent.children.index(creator) if creator.parent else 1
        output.append(f"weight = {weight}")
        if creator.header.outline_level == 1:
            output.append("bookCollapseSection = true")
        output.append(METADATA_SEPARATOR)
        self._output.append("\n".join(output))
        self._output.append(md_writer.PARAGRAPH_SEPARATOR)
        

hugo_strategy = document.Strategy(  ".md",
                                    False,
                                    md_writer.make_ref_for_header, 
                                    md_writer.make_ref_for_text, 
                                    md_writer.resolve_refs_conflict,
                                    _process_internal_link,
                                    _string_to_filename,
                                    _index_filename)