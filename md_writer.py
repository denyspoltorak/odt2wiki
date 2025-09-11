"Markdown writers"

import document
import os.path

    
class MarkdownWriter:
    PARAGRAPH_SEPARATOR = "\n\n"
    
    @classmethod
    def set_customization(cls, customization):
        cls._customization = customization
    
    def __init__(self, split_level):
        self._output = []
        self._split_level = split_level
     
    def get_output(self) -> str:
        return "".join(self._output)

    def add(self, content: document.Content) -> None:
        match content:
            case document.Paragraph():
                self._add_paragraph(content, True)
            case document.List():
                self._add_list(content)
            case document.Table():
                self._add_table(content)
            case document.Image():
                self._add_image(content)
            case document.ToC():
                self._add_toc(content)
            case document.NavBar():
                self._add_nav_bar(content)
            case _:
                assert False
        self._output.append(self.PARAGRAPH_SEPARATOR)
    
    # Methods to add document parts
    def add_header(self, header: document.Header) -> None:
        self._add_header(header)
        self._output.append(self.PARAGRAPH_SEPARATOR)
    
    def _add_header(self, header):
        # Promote the file-level header
        promoted = max(header.outline_level - self._split_level + 1, 1)
        self._output.append("#" * promoted + " ")
        self._add_paragraph(header, False)
      
    def _add_paragraph(self, paragraph, write_anchor):
        if write_anchor and paragraph.bookmarks:
            assert len(paragraph.bookmarks) == 1
            anchor_name = paragraph.bookmarks[0].split("#")[1]
            self._output.append(f'<a name="{anchor_name}"></a>\n')
        if paragraph.grayed_out:
            self._output.append("> ")
        self._output.append(self._add_spans(paragraph.spans))
        
    # List
    def _add_list(self, l, offset = 0):
        prefix = " " * offset
        index = 1
        # Differentiate between bulleted and numbered lists
        match l.kind:
            case document.ListStyle.BULLET:
                method = self._make_list_bullet
                offset += 2
            case document.ListStyle.NUMBER:
                method = self._make_list_number
                offset += 4
            case _:
                assert False
        # Process the list items
        for i in l.items:
            match i:
                case document.Paragraph():
                    self._output.append(prefix + method(index))
                    self._add_paragraph(i, True)
                    self._output.append("\n")
                case document.List():
                    self._add_list(i, offset)
                case _:
                    assert False
            index += 1
    
    @staticmethod
    def _make_list_bullet(index):
        return "- "

    @staticmethod
    def _make_list_number(index):
        assert index < 100
        return f"{str(index)+'.':<4}"
    
    # Table
    def _add_table(self, table):
        # Add table header
        assert table.is_valid()
        self._output.append(self._make_table_row(table.rows[0]))
        if len(table.rows) > 1:
            self._output.append(self._make_table_separator(table.num_columns))
        # Add the content
        for r in range(1, len(table.rows)):
            self._output.append(self._make_table_row(table.rows[r]))
    
    def _make_table_row(self, row):
        output = ["|",]
        for cell in row:
            output.append(self._add_spans(cell.spans) if cell else "")
            output.append("|")
        return " ".join(output) + "\n"
    
    @staticmethod
    def _make_table_separator(num_columns):
        output = ["|",]
        for _ in range(num_columns):
            output.append("---")
            output.append("|")
        return " ".join(output) + "\n"

    # Image
    def _add_image(self, image):
        assert image.link
        assert image.scale <= 1
        presentation = os.path.splitext(os.path.basename(image.link))[0].replace("_", ":")
        lines = self._make_image_html(self._escape_link(image.link), presentation, image.scale)
        self._output.append("\n".join(lines))
        
    @staticmethod
    def _make_image_html(link, presentation, scale):
        output = []
        output.append('<div align="center">')
        output.append(f'<a href="{link}">')
        output.append(f'<img src="{link}" alt="{presentation}" width={scale:.0%}/>')
        output.append('</a>')
        output.append('</div>')
        return output
    
    # Table of Contents
    def _add_toc(self, toc):
        for i in toc.items:
            assert i.level > 0
            assert i.name
            assert i.link
            if i.level > 1:
                self._output.append("  " * (i.level - 2) + "- " + f"[{i.name}]({i.link})\n")
            else:        
                self._output.append(f"\n### [{i.name}]({i.link})\n\n")
    
    def _add_nav_bar(self, navbar):
        if navbar.prev or navbar.next or navbar.up:
            links = []
            # Prev
            if navbar.prev:
                item = navbar.prev.to_paragraph()
                item.spans.insert(0, document.Span("<< "))
                links.append(item)
            else:
                links.append(None)
            # Up
            if navbar.up:
                item = navbar.up.to_paragraph()
                item.spans.insert(0, document.Span("^ "))
                item.spans.append(document.Span(" ^"))
                links.append(item)
            else:
                links.append(None)
            # Next
            if navbar.next:
                item = navbar.next.to_paragraph()
                item.spans.append(document.Span(" >>"))
                links.append(item)
            else:
                links.append(None)
            # Output
            self._output.append(self._make_table_row(links))
            self._output.append(self._make_table_separator(3))
    
    def _add_spans(self, spans):
        output = []
        move_spaces = 0
        # Current style
        style = document.Style()
        link = ""
        # Process the spans
        for s in spans:
            # Don't allow for spaces between markup tags and the text
            left_stripped_text = s.text.lstrip()
            move_spaces += len(s.text) - len(left_stripped_text)
            if not left_stripped_text:
                continue
            output.append(self._change_style(style, s.style, link, s.link, move_spaces))
            style = s.style
            link = s.link
            fully_stripped_text = left_stripped_text.rstrip()
            assert fully_stripped_text
            move_spaces = len(left_stripped_text) - len(fully_stripped_text)
            output.append(self._escape_text(fully_stripped_text))
        output.append(self._change_style(style, document.Style(), link, "", move_spaces))
        # Merge
        result = "".join(output)
        assert result
        return result
      
    @staticmethod
    def _make_html_color_name(color):
        if not color:
            return ""
        elif color.r > 2 * color.g and color.r > 2 * color.b:
            return "red"
        elif color.g > 2 * color.r and color.g > 2 * color.b:
            return "green"
        else:
            return ""
    
    def _change_style(self, old, new, old_link, new_link, add_spaces):
        output = []
        old_color_name = self._make_html_color_name(old.color)
        new_color_name = self._make_html_color_name(new.color)
        old_underline = old.underline and not old_link
        new_underline = new.underline and not new_link
        # Close the old style
        if old_link != new_link:
            # A style cannot cross a link's border - reset
            output.extend(self._close_style(old_color_name, old_underline, old.bold, old.italic, old.strikethrough))
        else:
            # Apply the style diff
            if old_color_name and old_color_name != new_color_name:
                output.append("</span>")
            if old_underline and not new_underline:
                output.append("</ins>")
            if old.bold and not new.bold:
                output.append("**")
            if old.italic and not new.italic:
                output.append("*")
            if old.strikethrough and not new.strikethrough:
                output.append("~")
        if old_link and old_link != new_link:
            output.append(self._close_link(old_link))
        # Insert whitespaces which we move from inside the tags
        output.append(" " * add_spaces)
        # Open the new style
        if new_link and new_link != old_link:
            output.append(self._open_link(new_link))
        if old_link != new_link:
            # A style cannot cross a link's border - reload
            output.extend(self._open_style(new_color_name, new_underline, new.bold, new.italic, new.strikethrough))
        else:
            # Apply the style diff
            if new.strikethrough and not old.strikethrough:
                output.append("~")
            if new.italic and not old.italic:
                output.append("*")
            if new.bold and not old.bold:
                output.append("**")
            if new_underline and not old_underline:
                output.append("<ins>")
            if new_color_name and new_color_name != old_color_name:
                output.append(f'<span style="color:{new_color_name}">')
        # Merge
        return "".join(output)
    
    @staticmethod
    def _close_style(color, underline, bold, italic, strikethrough):
        output = []
        if color:
            output.append("</span>")
        if underline:
            output.append("</ins>")
        if bold:
            output.append("**")
        if italic:
            output.append("*")
        if strikethrough:
            output.append("~")
        return output

    @staticmethod
    def _open_style(color, underline, bold, italic, strikethrough):
        output = []
        if strikethrough:
            output.append("~")
        if italic:
            output.append("*")
        if bold:
            output.append("**")
        if underline:
            output.append("<ins>")
        if color:
            output.append(f'<span style="color:{color}">')
        return output
    
    @staticmethod
    def _open_link(link):
        return "["
    
    @staticmethod
    def _close_link(link):
        return f"]({link})"
    
    @staticmethod
    def _strip_link(link):
        assert link.startswith("<")
        assert link.endswith(">")
        return link.strip("<>")
    
    @staticmethod
    def _escape_text(text):
        output = []
        for l in text:
            if l in "\\`*_~(){}[]<>#+-.!|":
                output.append("\\")
            output.append(l)
        return "".join(output)
    
    @staticmethod
    def _escape_link(link):
        return link.replace(" ", "%20")