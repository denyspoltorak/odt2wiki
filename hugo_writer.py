import document
import md_writer


def _process_internal_link(link):
    return f'{{{{< relref "{link}" >}}}}' if link else "#"

def _string_to_filename(string):
    return "".join([l.lower() if l.isalnum() else "-" for l in string.rstrip(". ")])


class HugoMarkdownWriter(md_writer.MarkdownWriter):
    def _strip_link(self, link):
        assert link.startswith('{{< relref "')
        assert link.enswith('" >}}')
        return link[len('{{< relref "'):-len('" >}}')]
        

hugo_strategy = document.Strategy(  ".md",
                                    md_writer.make_ref_for_header, 
                                    md_writer.make_ref_for_text, 
                                    md_writer.resolve_refs_conflict,
                                    _process_internal_link,
                                    _string_to_filename)