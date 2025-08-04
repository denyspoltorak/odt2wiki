"Internal representation of a book as a tree of sections (parts, chapters, etc.)"

from dataclasses import dataclass
from enum import Enum, auto
import os


def string_to_filename(string): #https://stackoverflow.com/questions/295135/turn-a-string-into-a-valid-filename
    return "".join([x if x.isalnum() else "_" for x in string]) 


UNNAMED_FILENAME = "intro"


class ListStyle(Enum):
    BULLET = auto()
    NUMBER = auto()


@dataclass(frozen=True)
class Color:
    r:  int = 0
    g:  int = 0
    b:  int = 0
    
    def __bool__(self):
        return self.r != 0 or self.g != 0 or self.b != 0


@dataclass(frozen=True)
class Style:
    bold:           bool = False
    italic:         bool = False
    underline:      bool = False
    strikethrough:  bool = False
    color:          Color = Color()


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
        
    def to_string(self):
        return "".join([s.text for s in self.spans])

  
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
    
    def is_valid(self):
        return self.num_columns and self.rows and all([len(r) == self.num_columns for r in self.rows])


class _Section:
    def __init__(self, parent, header):
        self.parent = parent
        self.header = header
        self.content = []
        self.children = []
        self.name = None
        self.filename = None
        
    def create_folders(self, destination, split_level, file_extension):
        assert(not self.name)
        assert(not self.filename)
        self.name = self.header.to_string()
        # Create top-level folders
        if self.header.outline_level < split_level or (not self.header.outline_level and not split_level):
            filename = string_to_filename(self.name)
            if self.name:
                destination = os.path.join(destination, filename)
            os.mkdir(destination)
            self.filename = os.path.join(destination, UNNAMED_FILENAME)
        # Remember files
        elif self.header.outline_level == split_level:
            self.filename = os.path.join(destination, string_to_filename(self.name))
        else:
            self.filename = destination
        self.filename += file_extension
        # Propagate to child sections in any case
        for child in self.children:
            child.create_folders(destination, split_level, file_extension)
        
    def dump(self, writer, writer_factory, split_level):
        assert(self.name is not None)
        assert(self.filename)
        # Start a new file if this is a book chapter or part
        if self.header.outline_level <= split_level:
            writer = writer_factory()
        # Write our content
        if self.header.outline_level:
            writer.add(self.header)
        for c in self.content:
            writer.add(c)
        for child in self.children:
            child.dump(writer, writer_factory, split_level)
        # Save it to the file
        if self.header.outline_level <= split_level:
            with open(self.filename, "x") as output:
                output.write(writer.get_output())

class Document:
    def __init__(self, destination: str, split_level: int):
        self._destination = destination
        self._split_level = split_level
        self._root = _Section(None, Header())
        self._current_section = self._root
        
    def create_folders(self, file_extension: str) -> None:
        self._root.create_folders(self._destination, self._split_level, file_extension)
        
    def dump(self, writer_factory) -> None:
        self._root.dump(None, writer_factory, self._split_level)
    
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
