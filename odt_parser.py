"See https://docs.oasis-open.org/office/v1.2/cs01/OpenDocument-v1.2-cs01-part1.html"

import xml.etree.ElementTree
from collections import defaultdict
from dataclasses import dataclass
from typing import Optional
from matplotlib import style



# Utils

# Remove namespace
def _extract(name):
    return name.split("}")[1]


# Classes that collect data from traversing an ElementTree

# Collects unique tags and their content from the entire XML treee
class _UniqueTagsVisitor:
    def __init__(self):
        self._tags = defaultdict(set)
        
    def traverse(self, element):
        # Remember the tag and the element's attributes
        tag = _extract(element.tag)
        attrs = self._tags[tag]
        for key in element.attrib.keys():
            attrs.add(_extract(key))
        if element.text:
            attrs.add("+text")
        # Traverse children
        for child in element:
            self.traverse(child)
            if child.tail:
                attrs.add("+text")
    
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
        

# Data classes
@dataclass(repr=False, eq=False, kw_only=True)
class _Style:
    bold:           Optional[bool] = None
    italic:         Optional[bool] = None
    underline:      Optional[bool] = None
    strikethrough:  Optional[bool] = None
    
    def __ior__(self, other):
        if self.bold is None:
            self.bold = other.bold
        if self.italic is None:
            self.italic = other.italic
        if self.underline is None:
            self.underline = other.underline
        if self.strikethrough is None:
            self.strikethrough = other.strikethrough  
        

@dataclass(repr=False, eq=False)
class _Span:
    text:   str
    style:  _Style
        
        
class _Paragraph:
    def __init__(self):
        self.spans = []
        self.outline_level = 0        
    
    
# Full-featured extraction classes
class _ParagraphVisitor:
    def __init__(self):
        self.unhandled_tags = set()
        self.unhandled_attrs = {}


class _FullVisitor(_ContentVisitor):
    def __init__(self):
        self._paragraph_visitor = _ParagraphVisitor()
        self._paragraphs = []
        self._styles = {}
        self._unhandled_tags = set()
        self._unhandled_attrs = defaultdict(set)
        
    def to_tree(self):
        self._print_warnings()
        pass
    
    def _print_warnings(self):
        print()
        print("Unhandled tags: " + ", ".join(sorted(self._unhandled_tags)))
        print()
        print("Unhandled attrs:")
        for (k, v) in sorted(self._unhandled_attrs.items()):
            print("\t" + k + ":\t" + ", ".join(sorted(v)))
        print()
    
    # Style extraction
    def traverse_styles(self, styles):
        assert(not styles.attrib)
        for child in styles:
            child_tag = _extract(child.tag)
            assert(child_tag == "style")
            (name, data) = self._process_style(child)
            assert(name)
            assert(name not in self._styles)
            if data is not None:
                self._styles[name] = data
    
    # Information retrieval
    def traverse_text(self, text):
        for child in text:
            child_tag = _extract(child.tag)
            match child_tag:
                case "h":
                    self._process_h(child)
                case "p":
                    self._process_p(child)
                case _:
                    self._unhandled_tags.add(child_tag)

    def _process_h(self, header):
        paragraph = _Paragraph()
        style = None
        # Parse attributes
        for (k, v) in header.attrib.items():
            attr_name = _extract(k)
            match attr_name:
                case "outline-level":
                    assert(not paragraph.outline_level)
                    paragraph.outline_level = int(v)
                case "style-name":
                    assert(not style)
                    style = self._styles.get(v, _Style())
                case _:
                    self._unhandled_attrs["h"].add(attr_name)
        assert(paragraph.outline_level)
        assert(style)
        # Parse text
        if header.text:
            paragraph.spans.append(_Span(header.text, style))
        for child in header:
            child_tag = _extract(child.tag)
            if child_tag == "a":
                span = self._process_a(child)
                span.style |= style
                paragraph.spans.append(span)
            else:
                self._unhandled_tags.add(child_tag)
            if child.tail:
                paragraph.spans.append(_Span(child.tail, style))
        # Commit
        assert(paragraph.spans)
        self._paragraphs.append(paragraph)

    def _process_p(self, par):
        paragraph = _Paragraph()
        style = None
        # Parse style
        for (k, v) in par.attrib.items():
            assert(_extract(k) == "style-name")
            assert(not style)
            style = self._styles.get(v, _Style())
        assert(style)
        # Parse text
        if par.text:
            paragraph.spans.append(_Span(par.text, style))
        for child in par:
            child_tag = _extract(child.tag)
            match child_tag:
                case "a":
                    span = self._process_a(child)
                    span.style |= style
                    paragraph.spans.append(span)
                case "span":
                    span = self._process_span(child)
                    span.style |= style
                    paragraph.spans.append(span)
                case "tab":
                    paragraph.spans.append(_Span("\t", style))
                case "s":
                    paragraph.spans.append(_Span(self._process_s(child), style))
                case _:
                    self._unhandled_tags.add(child_tag)
            if child.tail:
                paragraph.spans.append(_Span(child.tail, style))
        # Commit
        if paragraph.spans:
            self._paragraphs.append(paragraph)

    # Low-level methods
    def _process_style(self, style):
        name = None
        output = None
        # Style's metadata
        for (k, v) in style.attrib.items():
            attr_name = _extract(k)
            match attr_name:
                case "name":
                    assert(not name)
                    name = v
                case _:
                    self._unhandled_attrs["style"].add(attr_name)
        assert(name)
        # Style's data
        for child in style:
            child_tag = _extract(child.tag)
            match child_tag:
                case "text-properties":
                    assert(output is None)
                    output = self._process_text_properties(child)
                case _:
                    self._unhandled_tags.add(child_tag)
        return name, output
            
    def _process_text_properties(self, props):               
        output = _Style()
        for (k, v) in props.attrib.items():
            attr_name = _extract(k)
            match attr_name:
                case "font-weight":
                    assert(output.bold is None)
                    output.bold = (v == "bold")
                case "font-style":
                    assert(output.italic is None)
                    output.italic = (v == "italic")
                case "text-underline-style":
                    assert(output.underline is None)
                    output.underline = (v == "solid")
                case "text-line-through-style":
                    assert(output.strikethrough is None)
                    output.strikethrough = (v == "solid")
                case _:
                    self._unhandled_attrs["text-properties"].add(attr_name)
        return output

    def _process_a(self, a):
        assert(not a.text)
        assert(len(a) == 1)
        span = a[0]
        assert(_extract(span.tag) == "span")
        return self._process_span(span)
    
    def _process_span(self, span):
        style = None
        for (k, v) in span.attrib.items():
            assert(_extract(k) == "style-name")
            style = self._styles.get(v, _Style())
        assert(style)
        assert(span.text)
        return _Span(span.text, style)
    
    def _process_s(self, s):
        count = 1
        for (k, v) in s.attrib.items():
            assert(count == 1)
            assert(_extract(k) == "c")
            count = int(v)
            assert(count)
        return " " * count


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


def extract_tree_repr(root):
    visitor = _FullVisitor()
    visitor.traverse(root)
    return visitor.to_tree()