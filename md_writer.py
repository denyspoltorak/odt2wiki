"Markdown writers"

import document
import os.path


def _escape(text):
    output = []
    for l in text:
        if l in "\\`*_~(){}[]<>#+-.!|":
            output.append("\\")
        output.append(l)
    return "".join(output)


def _make_list_bullet(index):
    return "- "


def _make_list_number(index):
    assert index < 100
    return f"{str(index)+'.':<4}"


def _make_table_row(row):
    output = ["|",]
    for cell in row:
        output.append(_add_spans(cell.spans) if cell else "")
        output.append("|")
    return " ".join(output) + "\n"
    

def _make_table_separator(num_columns):
    output = ["|",]
    for _ in range(num_columns):
        output.append("---")
        output.append("|")
    return " ".join(output) + "\n"


def _make_html_color_name(color):
    if not color:
        return ""
    elif color.r > 2 * color.g and color.r > 2 * color.b:
        return "red"
    elif color.g > 2 * color.r and color.g > 2 * color.b:
        return "green"
    else:
        return ""

def _change_style(old, new, add_spaces):
    output = []
    old_color_name = _make_html_color_name(old.color)
    new_color_name = _make_html_color_name(new.color)
    # Close the old style
    if old_color_name and old_color_name != new_color_name:
        output.append("</span>")
    if old.underline and not new.underline:
        output.append("</ins>")
    if old.bold and not new.bold:
        output.append("**")
    if old.italic and not new.italic:
        output.append("_")
    if old.strikethrough and not new.strikethrough:
        output.append("~")
    # Insert whitespaces which we move from inside the tags
    output.append(" " * add_spaces)
    # Open the new style
    if new.strikethrough and not old.strikethrough:
        output.append("~")
    if new.italic and not old.italic:
        output.append("_")
    if new.bold and not old.bold:
        output.append("**")
    if new.underline and not old.underline:
        output.append("<ins>")
    if new_color_name and new_color_name != old_color_name:
        output.append(f'<span style="color:{new_color_name}">')
    # Merge
    return "".join(output)


def _add_spans(spans):
    output = []
    move_spaces = 0
    # Current style
    style = document.Style()
    # Process the spans
    for s in spans:
        # Don't allow for spaces between markup tags and the text
        left_stripped_text = s.text.lstrip()
        move_spaces += len(s.text) - len(left_stripped_text)
        if not left_stripped_text:
            continue
        output.append(_change_style(style, s.style, move_spaces))
        style = s.style
        fully_stripped_text = left_stripped_text.rstrip()
        assert fully_stripped_text
        move_spaces = len(left_stripped_text) - len(fully_stripped_text)
        output.append(_escape(fully_stripped_text))
    output.append(_change_style(style, document.Style(), move_spaces))
    # Merge
    result = "".join(output)
    assert result
    return result


class GitHubMdWriter:
    PARAGRAPH_SEPARATOR = "\n\n"
    
    def __init__(self, collapse_level):
        self._output = []
        self._collapse_level = collapse_level
        self._collapsing = False
    
    def get_output(self) -> str:
        if self._collapsing:
            self._output.append("</details>\n")
            self._collapsing = False
        return "".join(self._output)
    
    def add(self, content: document.Content) -> None:
        match content:
            case document.Header():
                self._add_header(content)
            case document.Paragraph():
                self._add_paragraph(content)
            case document.List():
                self._add_list(content)
            case document.Table():
                self._add_table(content)
            case document.Image():
                self._add_image(content)
            case _:
                assert False
        self._output.append(self.PARAGRAPH_SEPARATOR)
    
    # Methods to add document parts
    def _add_header(self, header):
        assert header.outline_level
        # Close the previous section
        if self._collapsing and header.outline_level <= self._collapse_level:
            self._output.append("</details>\n")
            self._collapsing = False
        # Write the new section
        if header.outline_level == self._collapse_level:
            self._output.append("<details>\n<summary>")
            self._collapsing = True
        self._output.append("#" * header.outline_level + " ")
        self._add_paragraph(header)
        if self._collapsing:
            self._output.append("</summary>")
        
    def _add_paragraph(self, paragraph):
        if paragraph.grayed_out:
            self._output.append("> ")
        self._output.append(_add_spans(paragraph.spans))
        
    def _add_list(self, l, offset = 0):
        prefix = " " * offset
        index = 1
        # Differentiate between bulleted and numbered lists
        match l.kind:
            case document.ListStyle.BULLET:
                method = _make_list_bullet
                offset += 2
            case document.ListStyle.NUMBER:
                method = _make_list_number
                offset += 4
            case _:
                assert False
        # Process the list items
        for i in l.items:
            match i:
                case document.Paragraph():
                    self._output.append(prefix + method(index))
                    self._add_paragraph(i)
                    self._output.append("\n")
                case document.List():
                    self._add_list(i, offset)
                case _:
                    assert False
            index += 1
    
    def _add_table(self, table):
        # Add table header
        assert table.is_valid()
        self._output.append(_make_table_row(table.rows[0]))
        if len(table.rows) > 1:
            self._output.append(_make_table_separator(table.num_columns))
        # Add the content
        for r in range(1, len(table.rows)):
            self._output.append(_make_table_row(table.rows[r]))

    def _add_image(self, image):
        assert image.link
        assert image.scale <= 1
        presentation = os.path.splitext(os.path.basename(image.link))[0]
        #self._output.append(f"![{presentation}]({image.link})")
        self._output.append(f'<img src="{image.link}" alt="{presentation}" width={image.scale:.0%} align="middle"/>')