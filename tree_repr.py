"Internal representation of a book as a tree of sections (parts, chapters, etc.)"

from dataclasses import dataclass


@dataclass(repr=False, eq=False, frozen=True)
class Style:
    bold:           bool = False
    italic:         bool = False
    underline:      bool = False
    strikethrough:  bool = False


# A chunk of text in a given style
@dataclass(repr=False, eq=False, frozen=True)
class Span:
    text:   str
    style:  Style


class _Section:
    def __init__(self, outline_level, parent, header):
        self.outline_level = outline_level
        self.parent = parent
        self.header = header
        self.paragraphs = []
        self.children = []
        
    def dump(self, writer):
        if self.header:
            writer.add_header(self.header, self.outline_level)
        for p in self.paragraphs:
            writer.add_paragraph(p)
        for child in self.children:
            child.dump(writer)


class Document:
    def __init__(self):
        self._root = _Section(0, None, [])
        self._current_section = self._root
        
    def dump(self, writer):
        self._root.dump(writer)
    
    def add_paragraph(self, spans):
        self._current_section.paragraphs.append(spans)
    
    def add_header(self, spans, outline_level):
        assert(outline_level)
        # Find a place for the new section in the tree
        parent_section = self._current_section
        while outline_level <= parent_section.outline_level:
            parent_section = parent_section.parent
        # Create the new section
        new_section = _Section(outline_level, parent_section, spans)
        parent_section.children.append(new_section)
        self._current_section = new_section
