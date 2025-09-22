"Markdown writers"

import document
import os.path
from enum import Enum, auto, unique


@unique
class ColorId(Enum):
    DEFAULT = auto()
    RED = auto()
    GREEN = auto()
    
    def __bool__(self):
        return self is not ColorId.DEFAULT

    
class MarkdownWriter:
    PARAGRAPH_SEPARATOR = "\n\n"
    
    _color_names = {
        ColorId.RED:      "crimson",
        ColorId.GREEN:    "green"
    }
    
    @classmethod
    def set_customization(cls, customization):
        cls._customization = customization
    
    def __init__(self, split_level):
        self._output = []
        self._split_level = split_level
     
    def get_output(self) -> str:
        return self.PARAGRAPH_SEPARATOR.join(self._output)

    def add(self, content: document.Content) -> None:
        match content:
            case document.Paragraph():
                result = self._add_paragraph(content, True)
            case document.List():
                result = self._add_list(content)
            case document.DefinitionList():
                result = self._add_definition_list(content)
            case document.Table():
                result = self._add_table(content)
            case document.Image():
                result = self._add_image(content)
            case document.ToC():
                result = self._add_toc(content)
            case document.NavBar():
                result = self._add_nav_bar(content)
            case _:
                assert False
        assert result, content
        self._output.append(result)
    
    # Methods to add document parts
    def add_header(self, header: document.Header) -> None:
        self._output.append(self._add_header(header))
    
    def _add_header(self, header):
        # Promote the file-level header
        promoted = max(header.outline_level - self._split_level + 1, 1)
        return "#" * promoted + " " + self._add_paragraph(header, False)
      
    def _add_paragraph(self, paragraph, write_anchor):
        result = ""
        if write_anchor and paragraph.bookmarks:
            assert len(paragraph.bookmarks) == 1
            anchor_name = paragraph.bookmarks[0].split("#")[1]
            result += f'<a name="{anchor_name}"></a>\n'
        if paragraph.grayed_out:
            result += "> "
        return result + self._add_spans(paragraph.spans)
        
    # List
    def _add_list(self, l, offset = 0):
        prefix = " " * offset
        index = 1
        result = ""
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
                    result += (prefix + method(index))
                    result += self._add_paragraph(i, True)
                    result += "\n"
                case document.List():
                    result += self._add_list(i, offset)
                case _:
                    assert False
            index += 1
        return result
    
    @staticmethod
    def _make_list_bullet(index):
        return "- "

    @staticmethod
    def _make_list_number(index):
        assert index < 100
        return f"{str(index)+'.':<4}"
    
    # Definition List
    def _add_definition_list(self, dl):
        output = [f'{self._add_spans(i[0].spans)}\n: {self._add_spans(i[1].spans)}' for i in dl.items]
        return self.PARAGRAPH_SEPARATOR.join(output)

    # Table
    def _add_table(self, table):
        # Add table header
        assert table.is_valid()
        output = []
        output.append(self._make_table_row(table.rows[0]))
        if len(table.rows) > 1:
            output.append(self._make_table_separator(table.num_columns))
        # Add the content
        for r in range(1, len(table.rows)):
            output.append(self._make_table_row(table.rows[r]))
        return "\n".join(output)
    
    def _make_table_row(self, row):
        output = ["|",]
        for cell in row:
            output.append(self._add_spans(cell.spans) if cell else "")
            output.append("|")
        return " ".join(output)
    
    @staticmethod
    def _make_table_separator(num_columns):
        output = ["|",]
        for _ in range(num_columns):
            output.append("---")
            output.append("|")
        return " ".join(output)

    # Image
    def _add_image(self, image):
        assert image.link
        assert image.scale <= 1
        presentation = os.path.splitext(os.path.basename(image.link))[0].replace("_", ":")
        return self._make_image_html(self._escape_link(image.link), presentation, image.scale, image.caption, image.width, image.height)
        
    def _make_image_html(self, link, presentation, scale, caption, width, height):
        output = []
        output.append('<div align="center">')
        output.append(f'<a href="{link}">')
        output.append(f'<img src="{link}" alt="{presentation}" loading="lazy" width={scale:.0%}/>')
        output.append('</a>')
        if caption:
            output.append("\n" + self._add_paragraph(document.Paragraph(caption), True) + "\n")
        output.append('</div>')
        return "\n".join(output)
    
    # Table of Contents
    def _add_toc(self, toc):
        output = []
        for i in toc.items:
            assert i.level > 0
            assert i.name
            assert i.link
            if i.level > 1:
                output.append("  " * (i.level - 2) + "- " + f"[{i.name}]({i.link})")
            else:        
                output.append(f"\n### [{i.name}]({i.link})\n")
        return "\n".join(output)
    
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
            return self._make_table_row(links) + "\n" + self._make_table_separator(3)
        else:
            return ""
    
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
    def _get_color_id(color):
        if not color:
            return ColorId.DEFAULT
        elif color.r > 2 * color.g and color.r > 2 * color.b:
            return ColorId.RED
        elif color.g > 2 * color.r and color.g > 2 * color.b:
            return ColorId.GREEN
        else:
            return ColorId.DEFAULT
    
    def _make_color_style(self, color):
        return f'<span style="color:{self._color_names[color]}">'
    
    def _change_style(self, old, new, old_link, new_link, add_spaces):
        output = []
        old_color = self._get_color_id(old.color)
        new_color = self._get_color_id(new.color)
        old_underline = old.underline and not old_link
        new_underline = new.underline and not new_link
        # Close the old style
        if old_link != new_link:
            # A style cannot cross a link's border - reset
            output.extend(self._close_style(old_color, old_underline, old.bold, old.italic, old.strikethrough))
        else:
            # Apply the style diff
            if old_color and old_color != new_color:
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
            output.extend(self._open_style(new_color, new_underline, new.bold, new.italic, new.strikethrough))
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
            if new_color and new_color != old_color:
                output.append(f'<span {self._make_color_style(new_color)}>')
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

    def _open_style(self, color, underline, bold, italic, strikethrough):
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
            output.append(f'<span {self._make_color_style(color)}>')
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