"Markdown writers"

import document


class GitHubMdWriter:
    PARAGRAPH_SEPARATOR = "\n\n"
    
    def __init__(self):
        self._output = []
    
    def get_output(self) -> str:
        return "".join(self._output)
    
    def add(self, content: document.Content) -> None:
        match content:
            case document.Header():
                self._add_header(content)
            case document.Paragraph():
                self._add_paragraph(content)
            case document.List():
                self._add_list(content)
            case _:
                assert(False)
        self._output.append(self.PARAGRAPH_SEPARATOR)
    
    # Methods to add document parts
    def _add_header(self, header):
        assert(header.outline_level)
        self._output.append("#" * header.outline_level + " ")
        self._add_paragraph(header)
        
    def _add_paragraph(self, paragraph):
        self._add_spans(paragraph.spans)
        
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
                assert(False)
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
                    assert(False)
            index += 1
    
    # Low-level methods
    def _add_spans(self, spans):
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
            output.append(self._change_style(style, s.style, move_spaces))
            style = s.style
            fully_stripped_text = left_stripped_text.rstrip()
            assert(fully_stripped_text)
            move_spaces = len(left_stripped_text) - len(fully_stripped_text)
            output.append(self._escape(fully_stripped_text))
        output.append(self._change_style(style, document.Style(), move_spaces))
        # Merge
        result = "".join(output)
        assert(result)
        self._output.append(result)
            
    @staticmethod
    def _change_style(old, new, add_spaces):
        output = []
        # Close the old style
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
        # Merge
        return "".join(output)
    
    @staticmethod
    def _escape(text):
        output = []
        for l in text:
            if l in "\\`*_~(){}[]<>#+-.!|":
                output.append("\\")
            output.append(l)
        return "".join(output)
    
    @staticmethod
    def _make_list_bullet(index):
        return "- "
    
    @staticmethod
    def _make_list_number(index):
        assert(index < 100)
        return f"{str(index)+'.':<4}"
        