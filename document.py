"Internal representation of a book as a tree of sections (parts, chapters, etc.)"

from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional
import os


def string_to_filename(string):
    return string.rstrip(". ")


DEFAULT_NAME = "Introduction"


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
    def __init__(self, text: str, style: Style = Style(), link: Optional[str] = None):
        self.text = text
        self.style = style
        self.link = link


class TocItem:
    def __init__(self, name: str, link: str, level: int):
        self.name = name
        self.link = link
        self.level = level


class NavItem:
    def __init__(self, name, link):
        self.name = name
        self.link = link
    
    def to_paragraph(self):
        return Paragraph.from_link(self.name, self.link)


class Content:
    pass


class Paragraph(Content):
    def __init__(self):
        self.spans = []
        self.bookmarks = []
        self.grayed_out = False
    
    @staticmethod
    def from_link(text, link):
        output = Paragraph()
        output.spans.append(Span(text, link=link))
        return output
        
    def to_string(self):
        return "".join([s.text for s in self.spans])

  
class Header(Paragraph):
    def __init__(self, text = None):
        super(Header, self).__init__()
        self.outline_level = 0
        if text:
            self.spans.append(Span(text))

   
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


class Image(Content):
    def __init__(self, link, scale):
        self.link = link
        self.scale = scale
        

class ToC(Content):
    def __init__(self):
        self.items = []
        

class NavBar(Content):
    def __init__(self):
        self.prev = None
        self.next = None
        self.up = None
        
        
class Strategy:
    def __init__(self, file_extension, make_ref_for_header, make_ref_for_text, resolve_refs_conflict, process_internal_link):
        self.file_extension = file_extension
        self.make_ref_for_header = make_ref_for_header
        self.make_ref_for_text = make_ref_for_text
        self.resolve_refs_conflict = resolve_refs_conflict
        self.process_internal_link = process_internal_link


class Section:
    def __init__(self, parent, header, split_level, strategy):
        self.parent = parent
        self.split_level = split_level
        self.strategy = strategy
        self.header = header
        self.content = []
        self.children = []
        self.rel_filename = None
        self.abs_filename = None
        self.path_to_root = ""
        
    @staticmethod
    def create(name, abs_path, split_level, content, strategy):
        output = Section(None, Header(name), split_level, strategy)
        output.rel_filename = name + strategy.file_extension
        output.abs_filename = output._join_paths(abs_path, output.rel_filename)
        output.content = content
        return output
        
    def create_folders(self, abs_root, root_to_parent):
        assert not self.rel_filename
        assert not self.abs_filename
        assert not self.path_to_root
        header_text = self.header.to_string()
        filename = string_to_filename(header_text)
        assert filename
        # Create the root folder
        if not self.header.outline_level:
            assert not root_to_parent
            os.mkdir(abs_root)
            self.rel_filename = filename + self.strategy.file_extension
        # Create top-level folders
        elif self.header.outline_level < self.split_level:
            root_to_parent = self._join_paths(root_to_parent, filename)
            os.mkdir(self._join_paths(abs_root, root_to_parent))
            self.rel_filename = self._join_paths(root_to_parent, filename + self.strategy.file_extension)
            self.path_to_root = self._join_paths(self.parent.path_to_root, "..")
        # Remember the file to create
        elif self.header.outline_level == self.split_level:
            self.rel_filename = self._join_paths(root_to_parent, filename + self.strategy.file_extension)
            self.path_to_root = self.parent.path_to_root
        # Inherit the file from parent
        else:
            self.rel_filename = self.parent.rel_filename
            self.path_to_root = self.parent.path_to_root
        # Fill derived variables
        self.abs_filename = self._join_paths(abs_root, self.rel_filename)
        # Propagate to child sections in any case
        for child in self.children:
            child.create_folders(abs_root, root_to_parent)
    
    def match_images(self, external_images, internal_images):
        # Update paths in all our images
        for c in self.content:
            if isinstance(c, Image):
                assert(c.link)
                link = external_images.get(c.link, None)
                if link:
                    c.link = link
                else:
                    link = internal_images.get(c.link, None)
                    assert link
                    c.link = os.path.join(self.path_to_root, link)
        # Update child sections
        for child in self.children:
            child.match_images(external_images, internal_images)
    
    def collect_bookmarks(self, direct, reverse, reverse_duplicates, remap):
        # Extract bookmark from the header
        if self.header.bookmarks:
            self._process_bookmarks(self.header.bookmarks, 
                                    self.header.to_string(), 
                                    direct, 
                                    reverse, 
                                    reverse_duplicates, 
                                    self.strategy.make_ref_for_header,
                                    self.header.outline_level <= self.split_level)
        else:
            assert self.header.spans[0].text == DEFAULT_NAME, self.header.spans[0].text
        # Extract bookmarks from the section's text
        for c in self.content:
            if isinstance(c, Paragraph):
                if c.bookmarks:
                    self._process_bookmarks(c.bookmarks, 
                                            c.to_string(), 
                                            remap, 
                                            reverse, 
                                            reverse_duplicates, 
                                            self.strategy.make_ref_for_text)
        # Traverse children
        for child in self.children:
            child.collect_bookmarks(direct, reverse, reverse_duplicates, remap)
    
    def replace_bookmarks(self, direct, remap):
        if self.header.bookmarks:
            self.header.bookmarks = [self._replace_single_bookmark(self.header.bookmarks, direct),]
        else:
            assert self.header.spans[0].text == DEFAULT_NAME, self.header.spans[0].text
        for c in self.content:
            self._replace_bookmarks_in_content(c, remap)
        for child in self.children:
            child.replace_bookmarks(direct, remap)
            
    def replace_links(self, mapping):
        for s in self.header.spans:
            if s.link:
                s.link = self._replace_single_link(s.link, mapping)
        for c in self.content:
            self._replace_links_in_content(c, mapping)
        for child in self.children:
            child.replace_links(mapping)
        
    def dump(self, writer_factory, writer = None):
        assert self.abs_filename
        # Start a new file if this is a book chapter or part
        if self.header.outline_level <= self.split_level:
            writer = writer_factory()
        # Write our content
        if self.header.outline_level:
            writer.add_header(self.header, self.split_level)
        for c in self.content:
            writer.add(c)
        for child in self.children:
            child.dump(writer_factory, writer)
        # Save it to the file
        if self.header.outline_level <= self.split_level:
            writer.add(self._make_navigation())
            with open(self.abs_filename, "x") as output:
                output.write(writer.get_output())
    
    def traverse(self, handler):
        handler(self)
        for child in self.children:
            child.traverse(handler)
        
    def _process_bookmarks(self, bookmarks, text, direct, reverse, reverse_duplicates, make_ref, is_title = False):
        assert bookmarks
        ref = make_ref(self.rel_filename, text, is_title)
        # Add mappings from ODT to markdown anchors
        for b in bookmarks:
            assert b not in direct
            direct[b] = ref
        # Add mapping from markdown to ODT anchors
        if ref in reverse:
            if ref not in reverse_duplicates:
                reverse_duplicates[ref] = [reverse[ref],]
            reverse_duplicates[ref].append(bookmarks)
        else:
            reverse[ref] = bookmarks
            
    def _replace_bookmarks_in_content(self, c, mapping):
        match c:
            case Paragraph():
                if c.bookmarks:
                    c.bookmarks = [self._replace_single_bookmark(c.bookmarks, mapping),]
            case List():
                for i in c.items:
                    self._replace_bookmarks_in_content(i, mapping)
    
    def _replace_links_in_content(self, c, mapping):
        match c:
            case Paragraph():
                for s in c.spans:
                    if s.link:
                        s.link = self._replace_single_link(s.link, mapping)
            case List():
                for i in c.items:
                    self._replace_links_in_content(i, mapping)
            case Table():
                for r in c.rows:
                    for col in r:
                        self._replace_links_in_content(col, mapping)
    
    def _replace_single_bookmark(self, bookmarks, mapping):
        assert bookmarks
        new_bookmark = mapping[bookmarks[0]]
        for i in range(1, len(bookmarks)):
            assert mapping[bookmarks[i]] == new_bookmark
        assert new_bookmark.startswith(self.rel_filename)
        return new_bookmark[len(self.rel_filename):]
    
    def _replace_single_link(self, link, mapping):
        new_link = mapping.get(link)
        if new_link:
            if new_link.startswith(self.rel_filename):
                return self.strategy.process_internal_link(new_link[len(self.rel_filename):])
            else:
                return self.strategy.process_internal_link(self._join_paths(self.path_to_root, new_link))
        else:
            assert link.startswith("http") or link.startswith("mailto"), link
            return link
        
    def _make_navigation(self):
        navigation = NavBar()
        for c in self.children:
            if c.header.outline_level <= self.split_level:
                navigation.next = self._make_nav_item(c)
                break
        if self.parent:
            navigation.up = self._make_nav_item(self.parent)
            index = self.parent.children.index(self)
            if index > 0 and self.parent.children[index - 1].header.outline_level <= self.split_level:
                navigation.prev = self._make_nav_item(self.parent.children[index - 1])
            else:
                navigation.prev = self._make_nav_item(self.parent)
            if not navigation.next:
                next_section = self._find_next_in_parent(self)
                if next_section:
                    navigation.next = self._make_nav_item(next_section)
        return navigation
    
    def _find_next_in_parent(self, current):
        while current.parent:
            index = current.parent.children.index(current)
            if index < len(current.parent.children) - 1:
                return current.parent.children[index + 1]
            current = current.parent
        return None
    
    def _make_nav_item(self, other):
        return NavItem(other.header.to_string(), 
                       self.strategy.process_internal_link(self._join_paths(self.path_to_root, other.rel_filename)))
    
    @staticmethod   
    def _join_paths(l, r):
        if l and r:
            return os.path.join(l, r)
        elif l:
            return l
        elif r:
            return r
        else:
            return ""


class TocMaker:
    def __init__(self, strategy):
        self._strategy = strategy
        self._toc = ToC()
    
    def make(self, root):
        root.traverse(self)
        return self._toc
    
    def __call__(self, section):
        if section.header.outline_level <= section.split_level:
            name = section.header.to_string()
            level = section.header.outline_level
            self._toc.items.append(TocItem(name, 
                                           self._strategy.process_internal_link(section.rel_filename), 
                                           max(level, 1)))


class Document:
    def __init__(self, destination: str, split_level: int, strategy: Strategy):
        self._destination = destination
        self._split_level = split_level
        self._strategy = strategy
        self._root = Section(None, Header(DEFAULT_NAME), split_level, strategy)
        self._current_section = self._root
        
    def create_folders(self) -> None:
        self._root.create_folders(self._destination, "")
        
    def link_images(self, external_images: dict[str, str], internal_images: dict[str, str]) -> None:
        self._root.match_images(external_images, internal_images)
        
    def crosslink(self):
        # Translate bookmarks (links) into markdown format (anchors) and find duplicate anchors
        direct = {}             # link, anchor              - ODT to markdown headers links map
        reverse = {}            # anchor, list[link]        - markdown to ODT multiple links map
        reverse_duplicates = {} # anchor, list[list[link]]  - duplicate markdown links
        remap = {}              # link, anchor              - these anchors are not headers, therefore they will be output as HTML
        self._root.collect_bookmarks(direct, reverse, reverse_duplicates, remap)
        assert not direct.keys() & remap.keys()
        # Rename duplicates
        print(f"Resolving {len(reverse_duplicates)} anchor conflicts:")
        for k in reverse_duplicates.keys():
            print(k)
        print()
        for anchor, links in reverse_duplicates.items():
            mapping = self._strategy.resolve_refs_conflict(anchor, links)
            for l, p in mapping:
                assert l in direct
                assert l not in remap   # We cannot resolve conflicts from headers and conflicts from text paragraphs together
                direct[l] = p
        # Commit the changes
        self._root.replace_bookmarks(direct, remap)
        self._root.replace_links(direct | remap)
        
    def dump(self, writer_factory) -> None:
        self._root.dump(writer_factory)
        
    def root(self):
        return self._root
    
    def push_root(self, new_root):
        assert isinstance(new_root, Section)
        assert new_root.header.outline_level == 0
        assert self._root.header.outline_level == 0
        children = self._root.children
        self._root.children = []
        self._root.parent = new_root
        new_root.children.append(self._root)
        for c in children:
            assert c.header.outline_level
            if c.header.outline_level == 1:
                new_root.children.append(c)
                c.parent = new_root
            else:
                self._root.children.append(c)
        self._root.header.outline_level = 1
        self._root = new_root
    
    def add(self, content: Content) -> None:
        assert isinstance(content, Content)
        if isinstance(content, Header):
            self._add_header(content)
        else:
            self._current_section.content.append(content)
    
    def _add_header(self, header):
        assert header.outline_level
        # Find a place for the new section in the tree
        parent_section = self._current_section
        while header.outline_level <= parent_section.header.outline_level:
            parent_section = parent_section.parent
        # Create the new section
        new_section = Section(parent_section, header, self._split_level, self._strategy)
        parent_section.children.append(new_section)
        self._current_section = new_section
