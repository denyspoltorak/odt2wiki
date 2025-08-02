"Internal representation of a book as a tree of sections (parts, chapters, etc.)"

from dataclasses import dataclass
from enum import Enum, auto


class ListStyle(Enum):
    BULLET = auto()
    NUMBER = auto()


@dataclass(repr=False, frozen=True)
class Style:
    bold:           bool = False
    italic:         bool = False
    underline:      bool = False
    strikethrough:  bool = False


# A chunk of text in a given style
class Span:
    def __init__(self, text: str, style: Style):
        self.text = text
        self.style = style
        

class Content:
    pass


class Paragraph(Content):
    def __init__(self):
        self.spans = []
        self.grayed_out = False

  
class Header(Paragraph):
    def __init__(self):
        super(Header, self).__init__()
        self.outline_level = 0

   
class List(Content):
    def __init__(self):
        self.kind = None
        self.items = []
        

class Table(Content):
    def __init__(self):
        self.num_columns = 0
        self.rows = []


class _Section:
    def __init__(self, parent, header):
        self.parent = parent
        self.header = header
        self.content = []
        self.children = []
        
    def dump(self, writer):
        if self.header.outline_level:
            writer.add(self.header)
        for c in self.content:
            writer.add(c)
        for child in self.children:
            child.dump(writer)


class Document:
    def __init__(self):
        self._root = _Section(None, Header())
        self._current_section = self._root
        
    def dump(self, writer):
        self._root.dump(writer)
    
    def add(self, content: Content) -> None:
        assert(isinstance(content, Content))
        if isinstance(content, Header):
            self._add_header(content)
        else:
            self._current_section.content.append(content)
    
    def _add_header(self, header):
        assert(header.outline_level)
        # Find a place for the new section in the tree
        parent_section = self._current_section
        while header.outline_level <= parent_section.header.outline_level:
            parent_section = parent_section.parent
        # Create the new section
        new_section = _Section(parent_section, header)
        parent_section.children.append(new_section)
        self._current_section = new_section
