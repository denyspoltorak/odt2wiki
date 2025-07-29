"See https://docs.oasis-open.org/office/v1.2/cs01/OpenDocument-v1.2-cs01-part1.html"

import xml.etree.ElementTree
import collections
from abc import abstractmethod


# Utils

# Remove namespace
def _extract(name):
    return name.split("}")[1]


# Classes that collect data from traversing an ElementTree

# Collects unique tags and their content from the entire XML treee
class _UniqueTagsVisitor:
    def __init__(self):
        self._tags = collections.defaultdict(set)
        
    def traverse(self, element):
        # Remember the tag and the element's attributes
        tag = _extract(element.tag)
        attrs = self._tags[tag]
        if element.text:
            attrs.add("+text")
        for key in element.attrib.keys():
            attrs.add(_extract(key))
        # Traverse children
        for child in element:
            self.traverse(child)
    
    def results(self):
        return self._tags
    

# Collects unique tags into a tree of dictionaries
class _TagsTreeVisitor:
    def __init__(self):
        self._tree = {}
        
    def traverse(self, root):
        self._recurse(self._tree, root)
    
    def results(self):
        return self._tree

    @staticmethod
    def _recurse(dic, element):
        # Make sure we remeber the current element's tag
        tag = _extract(element.tag)
        if tag not in dic:
            dic[tag] = {}
        # Visit the current element's children
        for child in element:
            _TagsTreeVisitor._recurse(dic[tag], child)


# Parent for text extraction
class _ContentVisitor:
    def traverse(self, root):
        tag = _extract(root.tag)
        assert(tag == "document-content")
        for child in root:
            child_tag = _extract(child.tag)
            if child_tag == "automatic-styles":
                self.traverse_styles(child)
            elif child_tag == "body":
                self.traverse_body(child)
        
    def traverse_styles(self, styles):
        pass
    
    def traverse_body(self, body):
        assert(len(body) == 1)
        text = body[0]
        assert(_extract(text.tag) == "text")
        self.traverse_text(text)
        
    @abstractmethod
    def traverse_text(self, text):
        ...
        

# Plain text extraction
class _TextVisitor(_ContentVisitor):
    def __init__(self):
        self._paragraphs = []
        self._unhandled = set()
        # Dispatch tables
        self._text_child_handlers = {
            "p": self._on_p,
            "h": self._on_p,
            "list": self._on_list,
            "table": self._on_table
        }
        self._paragraph_child_handlers = {
            "a": self._on_a,
            "span": self._on_span,
            "frame": self._on_frame,
            "s": self._on_s,
            "tab": self._on_tab
        }
        
    def traverse_text(self, text):
        for child in text:
            tag = _extract(child.tag)
            handler = self._text_child_handlers.get(tag)
            if handler:
                self._paragraphs.append(handler(child))
            else:
                self._unhandled.add(tag)

    def results(self):
        print("Unhandles tags: " + ", ".join(sorted(self._unhandled)))
        return "\n".join(self._paragraphs)
    
    # Top-level elements
    def _on_p(self, p):
        paragraph = []
        # Add the prefix text
        if p.text:
            paragraph.append(p.text)
        # Add child elements
        for child in p:
            tag = _extract(child.tag)
            handler = self._paragraph_child_handlers.get(tag)
            if handler:
                handler(paragraph, child)
            else:
                self._unhandled.add(tag)
            # Add any text found text between this and the following element
            if child.tail:
                paragraph.append(child.tail)
        # Merge the paragraph into a string
        return "".join(paragraph)
    
    def _on_table(self, table):
        return "TABLE"
        
    def _on_list(self, l):
        return "LIST"
        
    # Low-level elements
    @staticmethod
    def _on_a(paragraph, a):
        if a.text:
            paragraph.append(a.text)
        for child in a:
            tag = _extract(child.tag)
            if tag == "span":
                _TextVisitor._on_span(paragraph, child)
            if child.tail:
                paragraph.append(child.tail)
    
    @staticmethod
    def _on_span(paragraph, span):
        assert(span.text)
        paragraph.append(span.text)
    
    @staticmethod
    def _on_s(paragraph, s):
        count = 1
        for (k, v) in s.attrib.items():
            if _extract(k) == "c":
                count = int(v)
                assert(count)
        paragraph.append(" " * count)
        
    @staticmethod
    def _on_tab(paragraph, tab):
        paragraph.append("\t")
        
    @staticmethod
    def _on_frame(paragraph, frame):
        paragraph.append(" IMAGE ")
        

# Public interface

def parse(content):
    return xml.etree.ElementTree.fromstring(content)


def unique_tags(root):
    visitor = _UniqueTagsVisitor()
    visitor.traverse(root)
    return visitor.results()


def tree_of_tags(root):
    visitor = _TagsTreeVisitor()
    visitor.traverse(root)
    return visitor.results()


def extract_text(root):
    visitor = _TextVisitor()
    visitor.traverse(root)
    return visitor.results()