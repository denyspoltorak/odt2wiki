"Internal representation of a book as a tree of sections (parts, chapters, etc.)"

from dataclasses import dataclass, KW_ONLY


# A piece of text in a given style
@dataclass(eq=False, frozen=True)
class Span:
    text:           str
    _:              KW_ONLY
    bold:           bool = False
    italic:         bool = False
    underline:      bool = False
    strikethrough:  bool = False
    # color
    # hyperlink


class Paragraph:
    def __init__(self):
        self.spans = []


class Section(Paragraph):
    def __init__(self, parent, outline_level):
        self.paragraphs = []
        self.parent = parent
        self.outline_level = outline_level


class Document:
    def __init__(self):
        self.sections = []