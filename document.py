"Internal representation of a book as a tree of sections (parts, chapters, etc.)"

from dataclasses import dataclass
from enum import Enum, IntEnum, auto
from typing import Optional
import os


DEFAULT_NAME = "Introduction"
LOCAL_TOC_NAME = "Contents:"


def is_link_external(link):
    return link.startswith("http") or link.startswith("mailto")


class SectionType(IntEnum):
    NONE = auto()
    FOLDER = auto()
    FILE = auto()
    INTERNAL = auto()


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
        

# Customization

# Customization by the output dialect
class Strategy:
    def __init__(self, 
                 file_extension, 
                 needs_navigation,
                 make_ref_for_header, 
                 make_ref_for_text, 
                 resolve_refs_conflict, 
                 process_internal_link, 
                 string_to_filename,
                 index_filename):
        self.file_extension = file_extension
        self.needs_navigation = needs_navigation
        self.make_ref_for_header = make_ref_for_header
        self.make_ref_for_text = make_ref_for_text
        self.resolve_refs_conflict = resolve_refs_conflict
        self.process_internal_link = process_internal_link
        self.string_to_filename = string_to_filename
        self.index_filename = index_filename

# Per-document customization
class Customization:
    # Does this split_level section need to be split even further into subsections?
    @staticmethod
    def needs_split(section):
        return False
    
    # Does this folder-level section need a local ToC to provide links to its children?
    @staticmethod
    def needs_local_toc(section):
        return False


class TocMaker:
    def __init__(self, strategy, level_offset = 0):
        self._strategy = strategy
        self._level_offset = level_offset
        self._toc = ToC()
    
    def make(self, root):
        for c in root.children:
            c.traverse(self)
        return self._toc
    
    def __call__(self, section):
        assert section.header.outline_level
        if section.type < SectionType.INTERNAL:
            name = section.header.to_string()
            level = section.header.outline_level
            self._toc.items.append(TocItem(name, 
                                           self._strategy.process_internal_link(section.rel_filename), 
                                           level - self._level_offset))


class Section:
    strategy = None
    split_level = None
    
    @classmethod
    def set_strategy(cls, strategy, customization, split_level):
        cls.strategy = strategy
        cls.customization = customization
        cls.split_level = split_level
        
    def __init__(self, parent, header):
        self.parent = parent
        self.next = None
        self.prev = None
        self.header = header
        self.content = []
        self.children = []
        self.rel_filename = None
        self.abs_filename = None
        self.path_to_root = ""
        self.type = SectionType.NONE
        
    @staticmethod
    def create(name, content = [], abs_path = None):
        output = Section(None, Header(name))
        output.content = content
        if abs_path:
            output.rel_filename = name + output.strategy.file_extension
            output.abs_filename = output._join_paths(abs_path, output.rel_filename)
            output.type = SectionType.FILE
        return output
        
    def create_folders(self, abs_root, root_to_parent, enforce_file = False):
        assert not self.rel_filename
        assert not self.abs_filename
        assert not self.path_to_root
        assert self.type == SectionType.NONE
        header_text = self.header.to_string()
        filename = self.strategy.string_to_filename(header_text)
        children_should_be_files = False
        assert filename
        # Create the root folder
        if not self.header.outline_level:
            assert not root_to_parent
            os.mkdir(abs_root)
            self.rel_filename = self.strategy.index_filename(filename) + self.strategy.file_extension
            self.type = SectionType.FOLDER if self.split_level else SectionType.FILE
        # Create top-level folders
        elif self.header.outline_level < self.split_level:
            root_to_parent = self._init_folder(abs_root, root_to_parent, filename)
        # Remember the file to create
        elif self.header.outline_level == self.split_level:
            if self.customization.needs_split(self):
                print(f"'{header_text}' was split by customization")
                root_to_parent = self._init_folder(abs_root, root_to_parent, filename)
                children_should_be_files = True
            else:
                self._init_file(root_to_parent, filename)
        else:
            if enforce_file:
                self._init_file(root_to_parent, filename)
            else:
                # Inherit the file from parent
                self.rel_filename = self.parent.rel_filename
                self.path_to_root = self.parent.path_to_root
                self.type = SectionType.INTERNAL
        # Fill derived variables
        self.abs_filename = self._join_paths(abs_root, self.rel_filename)
        # Propagate to child sections in any case
        for child in self.children:
            child.create_folders(abs_root, root_to_parent, children_should_be_files)
        assert self.type != SectionType.NONE
    
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
        assert self.type != SectionType.NONE
        # Extract bookmark from the header
        if self.header.bookmarks:
            self._process_bookmarks(self.header.bookmarks, 
                                    self.header.to_string(), 
                                    direct, 
                                    reverse, 
                                    reverse_duplicates, 
                                    self.strategy.make_ref_for_header,
                                    self.type < SectionType.INTERNAL)
        else:
            assert not self.parent or self.header.spans[0].text == DEFAULT_NAME, self.header.to_string()
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
            assert not self.parent or self.header.spans[0].text == DEFAULT_NAME, self.header.to_string()
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
        assert self.type != SectionType.NONE
        # Start a new file if this is a book chapter or part
        if self.type < SectionType.INTERNAL:
            writer = writer_factory(self, max(self.header.outline_level, self.split_level))
        # Write our content
        if self.header.outline_level:   # don't write title for the landing page
            writer.add_header(self.header)
        for c in self.content:
            writer.add(c)
        for child in self.children:
            child.dump(writer_factory, writer)
        # Optionally add a ToC with links to our child sections
        if self.header.outline_level and self.type == SectionType.FOLDER and self.customization.needs_local_toc(self):
            print(f"Added a ToC to '{self.header.to_string()}'")
            toc_header = Header(LOCAL_TOC_NAME)
            toc_header.outline_level = max(self.header.outline_level, self.split_level) + 1
            writer.add_header(toc_header)
            writer.add(TocMaker(self.strategy, self.header.outline_level - 1).make(self))
        # Save it to the file
        if self.type < SectionType.INTERNAL:
            assert (not self.prev) == (not self.next)
            if self.next and self.split_level and self.strategy.needs_navigation:   # No navbar for stand-alone ToC or a single-file project
                writer.add(self._make_navigation())
            with open(self.abs_filename, "x") as output:
                output.write(writer.get_output())
    
    def traverse(self, handler):
        handler(self)
        for child in self.children:
            child.traverse(handler)
            
    def _init_folder(self, abs_root, root_to_parent, filename):
        root_to_parent = self._join_paths(root_to_parent, filename)
        os.mkdir(self._join_paths(abs_root, root_to_parent))
        self.rel_filename = self._join_paths(root_to_parent, self.strategy.index_filename(filename) + self.strategy.file_extension)
        self.path_to_root = self._join_paths(self.parent.path_to_root, "..")
        self.type = SectionType.FOLDER
        return root_to_parent
    
    def _init_file(self, root_to_parent, filename):
        self.rel_filename = self._join_paths(root_to_parent, filename + self.strategy.file_extension)
        self.path_to_root = self.parent.path_to_root
        self.type = SectionType.FILE
        
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
            assert is_link_external(link), link
            return link
        
    def _make_navigation(self):
        assert self.prev and self.next
        assert self.type != SectionType.NONE
        navigation = NavBar()
        # Find the next chapter
        other = self
        while other.next.type == SectionType.INTERNAL:
            other = other.next
            assert other != self
        navigation.next = self._make_nav_item(other.next)
        # Find the prev chapter
        other = self
        while other.prev.type == SectionType.INTERNAL:
            other = other.prev
            assert other != self
        navigation.prev = self._make_nav_item(other.prev)
        # Find the parent
        if self.parent:
            navigation.up = self._make_nav_item(self.parent)
        # Done
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


class Document:
    def __init__(self, destination: str, split_level: int, strategy: Strategy, customization: Customization):
        Section.set_strategy(strategy, customization, split_level)
        self._destination = destination
        self._strategy = strategy
        self._root = Section(None, Header(DEFAULT_NAME))
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
        assert new_root.type == SectionType.NONE
        assert self._root.type == SectionType.NONE
        assert not self._current_section
        assert self._root.prev.next == self._root
        # Update the navigation list
        new_root.next = self._root
        new_root.prev = self._root.prev
        self._root.prev = new_root
        new_root.prev.next = new_root
        # Update the DOM tree
        children = self._root.children
        self._root.children = []
        self._root.parent = new_root
        # Prepend the moved elements into the existing tree
        new_root.children.insert(0, self._root)     # push front
        for c in reversed(children):
            assert c.header.outline_level
            if c.header.outline_level == 1:
                new_root.children.insert(1, c)      # insert after self
                c.parent = new_root
            else:
                self._root.children.insert(0, c)    # compensate for the reverse
        self._root.header.outline_level = 1
        self._root = new_root
    
    def add(self, content: Content) -> None:
        assert isinstance(content, Content)
        assert self._current_section
        if isinstance(content, Header):
            self._add_header(content)
        else:
            self._current_section.content.append(content)
    
    def finalize(self) -> None:
        assert self._current_section
        assert not self._root.prev
        assert not self._current_section.next
        self._root.prev = self._current_section
        self._current_section.next = self._root
        self._current_section = None        
    
    def _add_header(self, header):
        assert header.outline_level
        assert self._current_section
        assert not self._current_section.next
        # Find a place for the new section in the tree
        parent_section = self._current_section
        while header.outline_level <= parent_section.header.outline_level:
            parent_section = parent_section.parent
        # Create the new section
        new_section = Section(parent_section, header)
        parent_section.children.append(new_section)
        self._current_section.next = new_section
        new_section.prev = self._current_section
        self._current_section = new_section
