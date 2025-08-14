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


def _strip_filename(filename):
    filename = os.path.basename(filename)
    assert filename.endswith(".md")
    return filename[:-3]


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
    

def _change_style(old, new, old_link, new_link, add_spaces):
    output = []
    old_color_name = _make_html_color_name(old.color)
    new_color_name = _make_html_color_name(new.color)
    old_underline = old.underline and not old_link
    new_underline = new.underline and not new_link
    # Close the old style
    if old_link != new_link:
        # A style cannot cross a link's border - reset
        output.extend(_close_style(old_color_name, old_underline, old.bold, old.italic, old.strikethrough))
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
        output.append(f"]({old_link})")
    # Insert whitespaces which we move from inside the tags
    output.append(" " * add_spaces)
    # Open the new style
    if new_link and new_link != old_link:
        output.append("[")
    if old_link != new_link:
        # A style cannot cross a link's border - reload
        output.extend(_open_style(new_color_name, new_underline, new.bold, new.italic, new.strikethrough))
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


def _add_spans(spans):
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
        output.append(_change_style(style, s.style, link, s.link, move_spaces))
        style = s.style
        link = s.link
        fully_stripped_text = left_stripped_text.rstrip()
        assert fully_stripped_text
        move_spaces = len(left_stripped_text) - len(fully_stripped_text)
        output.append(_escape(fully_stripped_text))
    output.append(_change_style(style, document.Style(), link, "", move_spaces))
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
    
    @staticmethod
    def make_ref_for_header(rel_path, header):
        # https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#section-links
        output = []
        for c in header.strip():
            if c.isalnum():
                output.append(c.lower())
            elif c == " ":
                output.append("-")
        return rel_path + "#" + "".join(output)
    
    @staticmethod
    def make_ref_for_text(rel_path, text):
        return rel_path + "#" + "".join([c.lower() for c in text.split()[0] if c.isalnum()])
    
    @staticmethod
    def resolve_refs_conflict(anchor, links):
        # https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#section-links
        assert len(links) > 1
        output = []
        for l in links[0]:
            output.append((l, anchor))
        for i in range(1, len(links)):
            new_anchor = anchor + "-" + str(i)
            for l in links[i]:
                output.append((l, new_anchor))
        return output
    
    @staticmethod
    def process_internal_link(link):
        if link.startswith("#"):
            return link
        else:
            # Github wiki wants stripped filenames - without directories and extensions
            filename, anchor = link.split("#")
            return _strip_filename(filename) + "#" + anchor
    
    def get_output(self) -> str:
        if self._collapsing:
            self._output.append("</details>\n")
            self._collapsing = False
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
            case _:
                assert False
        self._output.append(self.PARAGRAPH_SEPARATOR)
    
    # Methods to add document parts
    def add_header(self, header: document.Header, split_level: int) -> None:
        assert header.outline_level
        # Close the previous section
        if self._collapsing and header.outline_level <= self._collapse_level:
            self._output.append("</details>\n\n")
            self._collapsing = False
        # Write the new section
        if header.outline_level == self._collapse_level:
            self._output.append("<details>\n<summary>\n\n")
            self._collapsing = True
        # Promote the file-level header
        promoted = max(header.outline_level - split_level + 1, 1)
        self._output.append("#" * promoted + " ")
        self._add_paragraph(header, False)
        if self._collapsing:
            self._output.append("\n</summary>")
        self._output.append(self.PARAGRAPH_SEPARATOR)
      
    def _add_paragraph(self, paragraph, write_anchor):
        if write_anchor and paragraph.bookmarks:
            assert len(paragraph.bookmarks) == 1
            anchor_name = paragraph.bookmarks[0].split("#")[1]
            self._output.append(f'<a name="{anchor_name}"></a>\n')
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
                    self._add_paragraph(i, True)
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
        presentation = os.path.splitext(os.path.basename(image.link))[0].replace("_", ":")
        #self._output.append(f"![{presentation}]({image.link})")
        self._output.append(f'<p align="center">\n<img src="{image.link}" alt="{presentation}" width={image.scale:.0%}/>\n</p>')
    
    def _add_toc(self, toc):
        assert toc.items[0].level == 1
        for i in toc.items:
            assert i.level > 0
            assert i.name
            assert i.link
            item_text = f"[{i.name}]({_strip_filename(i.link)})\n"
            if i.level > 1:
                output = "  " * (i.level - 2) + "- " + item_text
            else:
                output = "\n" + item_text
            self._output.append(output)