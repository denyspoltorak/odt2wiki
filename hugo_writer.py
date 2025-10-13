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
        self._first_header = True
        self._make_metadata(creator)
        
    def add_header(self, header: document.Header) -> None:
        header = self._add_header(header)
        if self._first_header:
            header += " {anchor=false}"
            self._first_header = False
        self._output.append(header)
        
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
           
    def _make_image_html(self, image, presentation, scale, caption):
        # Generate the HTML code      
        output = []
        output.append('<figure>')
        output.append(f'<a href="{self._escape_link(image.original)}">')
        output.extend(self._add_picture(image, presentation, scale))
        output.append('</a>')
        if caption:
            output.append("<figcaption>" + caption + "</figcaption>")
        output.append('</figure>')
        return "\n".join(output)
    
    def _add_picture(self, image, presentation, scale = None):
        output = []
        # Prepare
        dimensions = f' width="{image.width}" height="{image.height}"' if image.width else ""
        img_scale = f' style="width:{scale:.0%}"' if scale else ""
        dark_link = self._customization.get_dark_image(image.link) if image.link != image.original else None
        # Multiple image versions for light and dark themes
        if dark_link:
            assert dark_link != image.link
            output.append('<picture>')
            output.append(f'<source srcset="{self._escape_link(image.link)}" media="(prefers-color-scheme: light)"/>')
            output.append(f'<source srcset="{self._escape_link(dark_link)}" media="(prefers-color-scheme: dark)"/>')
        # The fallback - or the only - image
        output.append(f'<img src="{self._escape_link(image.original)}" alt="{presentation}" loading="lazy"{dimensions}{img_scale}/>')
        if dark_link:
            output.append('</picture>')
        return output
    
    def _add_toc(self, toc):
        output = []
        grid = self._customization.toc_grid_depth_and_style(toc.root)
        if grid:
            # Add a CSS grid ToC
            max_level, css_class = grid
            output.append(f'<nav class="{css_class}">')
            for i in toc.items:
                assert i.level > 0
                assert i.name
                assert i.link
                if i.level < max_level:
                    # A grid-wide header
                    output.append(f'<a class="{self._customization.grid_wide_class}" href="{i.link}">')
                    output.append("<h3>" + i.name + "</h3>")
                    output.append('</a>')
                elif i.level == max_level:
                    picture = self._customization.get_toc_image(i.name)
                    if isinstance(picture, plugins.Wide):
                        # A grid-wide normal text
                        output.append(f'<a class="{self._customization.grid_wide_class}" href="{i.link}">')
                        output.append(i.name)
                        output.append('</a>')
                    elif picture:
                        # A single-cell image and text
                        output.append(f'<a href="{i.link}">')
                        output.extend(self._add_picture(picture, i.name))
                        output.append(i.name.split("(")[0].strip())    # Make the name shorter
                        output.append('</a>')
                    else:
                        # A single-cell normal text
                        output.append(f'<a href="{i.link}">')
                        output.append(i.name.split("(")[0].strip())    # Make the name shorter
                        output.append('</a>')
                # Else skip the item as it is too deep in the ToC tree
        else:
            # Add a list-based ToC
            output.append("<nav>")
            output.append(super()._add_toc(toc))
        # Finalize
        output.append("</nav>")
        return self.PARAGRAPH_SEPARATOR.join(output)
    
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
        if not creator.parent:
            output.append('layout = "landing"')
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
            assert not image.endswith(".svg")
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
    needs_navigation = False
    
    @staticmethod
    def process_internal_link(link):
        return f'{{{{< relref "{link}" >}}}}' if link else "#"

    @staticmethod
    def string_to_filename(string):
        return "".join([l.lower() if l.isalnum() else "-" for l in string.rstrip(". ")])
    
    @staticmethod
    def index_filename(string):
        return "_index"
