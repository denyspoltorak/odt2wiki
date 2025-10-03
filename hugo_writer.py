import document
import plugins
import md_writer


class HugoMarkdownWriter(md_writer.MarkdownWriter):
    METADATA_SEPARATOR = "+++"
    
    _color_styles = {
        md_writer.ColorId.RED:      "book-red",
        md_writer.ColorId.GREEN:    "book-green"
    }
    
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
        result = ""
        if paragraph.grayed_out and not self._in_list:
            aside = True
            result += ("<aside>" + self.PARAGRAPH_SEPARATOR)
        result += super()._add_paragraph(paragraph, write_anchor)
        if aside:
            result += self.PARAGRAPH_SEPARATOR + "</aside>"
        return result
            
    def _add_list(self, l, offset = 0):
        self._in_list += 1
        result = super()._add_list(l, offset)
        self._in_list -= 1
        return result
           
    def _make_image_html(self, link, original_link, presentation, scale, caption, width, height):
        # Check if we need <picture> for multiple versions of the image
        dark_link = self._customization.get_dark_image(link)
        img_link = original_link if dark_link else link   
        # Generate the HTML code      
        output = []
        output.append('<figure>')
        output.append(f'<a href="{self._escape_link(original_link)}">')
        # Add light and dark themes
        if dark_link:
            assert dark_link != link
            output.append('<picture>')
            output.append(f'<source srcset="{self._escape_link(link)}" media="(prefers-color-scheme: light), (prefers-color-scheme: no-preference)"/>')
            output.append(f'<source srcset="{self._escape_link(dark_link)}" media="(prefers-color-scheme: dark)"/>')
        # Add the fallback image and image dimensions
        if width:
            assert height
            output.append(f'<img src="{self._escape_link(img_link)}" alt="{presentation}" loading="lazy" width="{width}" height="{height}" style="width:{scale:.0%}"/>')
        else:
            assert not height
            output.append(f'<img src="{self._escape_link(img_link)}" alt="{presentation}" loading="lazy" style="width:{scale:.0%}"/>')
        # Close the created elements
        if dark_link:
            output.append('</picture>')
        output.append('</a>')
        if caption:
            output.append("<figcaption>" + caption + "</figcaption>")
        output.append('</figure>')
        return "\n".join(output)
    
    def _add_toc(self, toc):
        return "<nav>" + self.PARAGRAPH_SEPARATOR + super()._add_toc(toc) + self.PARAGRAPH_SEPARATOR + "</nav>"
    
    def _add_nav_bar(self, navbar):
        return "<nav>" + self.PARAGRAPH_SEPARATOR + super()._add_nav_bar(navbar) + self.PARAGRAPH_SEPARATOR + "</nav>"
    
    def _make_color_style(self, color):
        return f'class="{self._color_styles[color]}"'
           
    def _make_metadata(self, creator):
        # Open a front matter
        output = [self.METADATA_SEPARATOR,]
        # Set up front matter fields
        weight = 1 + creator.parent.children.index(creator) if creator.parent else 1
        output.append(f"weight = {weight}")
        title = creator.header.to_string()
        # SEO and OpenGraph
        if len(title) > 60:
            print(f"'The title of {title}' is longler than the SEO-recommended 60 symbols")
        output.append(f'title = "{title}"')
        description = self._customization.get_description(creator)
        if description:
            assert len(description) <= 160
            output.append(f'description = "{description}"')
        image = self._customization.get_preview_image(creator)
        if image:
            output.append(f'images = ["{self._escape_link(image)}"]')
        # ToC
        if creator.type == document.SectionType.FOLDER:
            output.append("bookCollapseSection = true")
        # Sitemap and search disable
        output.append("[sitemap]")
        if self._customization.is_hidden(creator):
            print(f"Hiding '{title}' from search engines")
            output.append("  disable = true")
            output.append("bookSearchExclude = true")
        else:
            output.append(f"  priority = {self._customization.get_sitemap_priority(creator)}")
        # Write the front matter
        output.append(self.METADATA_SEPARATOR)
        self._output.append("\n".join(output))
        

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
