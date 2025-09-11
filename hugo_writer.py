import document
import plugins
import md_writer


class HugoMarkdownWriter(md_writer.MarkdownWriter):
    METADATA_SEPARATOR = "+++"
    
    def __init__(self, creator, split_level = 0):
        super().__init__(split_level)
        self._in_list = 0
        self._make_metadata(creator)
        
    def _strip_link(self, link):
        assert link.startswith('{{< relref "')
        assert link.enswith('" >}}')
        return link[len('{{< relref "'):-len('" >}}')]
    
    def _add_paragraph(self, paragraph, write_anchor):
        assert self._in_list >= 0
        aside = False
        if paragraph.grayed_out and not self._in_list:
            aside = True
            self._output.append("<aside>\n\n")
        super()._add_paragraph(paragraph, write_anchor)
        if aside:
            self._output.append("\n\n</aside>")
            
    def _add_list(self, l, offset = 0):
        self._in_list += 1
        super()._add_list(l, offset)
        self._in_list -= 1
           
    @staticmethod
    def _make_image_html(link, presentation, scale):
        output = []
        output.append('<figure style="text-align:center">')
        #self._output.append('<div align="center">')
        output.append(f'<a href="{link}" style="outline:none">')
        output.append(f'<img src="{link}" alt="{presentation}" width={scale:.0%}/>')
        output.append('</a>')
        #self._output.append('</div>')
        output.append('</figure>')
        return output
    
    def _add_toc(self, toc):
        self._output.append("<nav>\n\n")
        super()._add_toc(toc)
        self._output.append("\n</nav>\n\n")
    
    def _add_nav_bar(self, navbar):
        self._output.append("<nav>\n\n")
        super()._add_nav_bar(navbar)
        self._output.append("\n</nav>\n\n")
           
    def _make_metadata(self, creator):
        # Open a front matter
        output = [self.METADATA_SEPARATOR,]
        # Set up front matter fields
        weight = 1 + creator.parent.children.index(creator) if creator.parent else 1
        output.append(f"weight = {weight}")
        output.append(f'title = "{creator.header.to_string()}"')
        if creator.type == document.SectionType.FOLDER:
            output.append("bookCollapseSection = true")
        if self._customization.is_hidden(creator):
            print(f"Hiding '{creator.header.to_string()}' from search engines")
            output.append("bookSearchExclude = true")
            output.append("[sitemap]")
            output.append("  disable = true")
        # Write the front matter
        output.append(self.METADATA_SEPARATOR)
        self._output.append("\n".join(output))
        self._output.append(self.PARAGRAPH_SEPARATOR)
        

class HugoStrategy(plugins.Strategy):
    @staticmethod
    def process_internal_link(link):
        return f'{{{{< relref "{link}" >}}}}' if link else "#"

    @staticmethod
    def string_to_filename(string):
        return "".join([l.lower() if l.isalnum() else "-" for l in string.rstrip(". ")])
    
    @staticmethod
    def index_filename(string):
        return "_index"
