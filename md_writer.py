"Markdown writers"

import tree_repr


class GitHubMdWriter:
    PARAGRAPH_SEPARATOR = "\n\n"
    
    def __init__(self):
        self._output = []
    
    def get_output(self):
        return "".join(self._output)
    
    # Methods to add elements to the markdown
    def add_paragraph(self, spans):
        self._add_spans(spans)
        self._output.append(self.PARAGRAPH_SEPARATOR)
    
    def add_header(self, spans, outline_level):
        assert(outline_level)
        self._output.append("#" * outline_level + " ")
        self.add_paragraph(spans)
        
    def _add_spans(self, spans):
        output = []
        move_spaces = 0
        # Current style
        style = tree_repr.Style()
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
        output.append(self._change_style(style, tree_repr.Style(), move_spaces))
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