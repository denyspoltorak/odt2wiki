"See https://docs.oasis-open.org/office/v1.2/cs01/OpenDocument-v1.2-cs01-part1.html"

from collections import defaultdict

from odt_tools import extract, ContentVisitor
import tree_repr



# Utils




# Classes that collect data from traversing an ElementTree


        

# Data classes
class _Style:
    def __init__(self, bold=None, italic=None, underline=None, strikethrough=None):
        self.bold = bold
        self.italic = italic
        self.underline = underline
        self.strikethrough = strikethrough
    
    def __ior__(self, other):
        if self.bold is None:
            self.bold = other.bold
        if self.italic is None:
            self.italic = other.italic
        if self.underline is None:
            self.underline = other.underline
        if self.strikethrough is None:
            self.strikethrough = other.strikethrough
        return self
    
    def normalize(self):
        return tree_repr.Style(self.bold, self.italic, self.underline, self.strikethrough)
        

class _Span:
    def __init__(self, text, style):
        self.text = text
        self.style = style
        
        
class _Paragraph:
    def __init__(self):
        self.spans = []


class _Header(_Paragraph):
    def __init__(self):
        super(_Header, self).__init__()
        self.outline_level = 0


# Full-featured extraction class
class FullVisitor(ContentVisitor):
    def __init__(self):
        self._content = []
        self._styles = {}
        self._unhandled_tags = set()
        self._unhandled_attrs = defaultdict(set)
        
    def to_tree(self):
        self._print_warnings()
        # Export to an intermediary representation
        document = tree_repr.Document()
        for elem in self._content:
            spans = []
            for s in elem.spans:
                spans.append(tree_repr.Span(s.text, s.style.normalize()))
            if isinstance(elem, _Header):
                document.add_header(spans, elem.outline_level)
            elif isinstance(elem, _Paragraph):
                document.add_paragraph(spans)
            else:
                assert(False)      
        return document
    
    def _print_warnings(self):
        print()
        print("Unhandled tags: " + ", ".join(sorted(self._unhandled_tags)))
        print()
        print("Unhandled attrs:")
        for (k, v) in sorted(self._unhandled_attrs.items()):
            print("\t" + k + ":\t" + ", ".join(sorted(v)))
        print()
    
    # _Style extraction
    def traverse_styles(self, styles):
        assert(not styles.attrib)
        for child in styles:
            child_tag = extract(child.tag)
            assert(child_tag == "style")
            (name, data) = self._process_style(child)
            assert(name)
            assert(name not in self._styles)
            if data is not None:
                self._styles[name] = data
    
    # Information retrieval
    def traverse_text(self, text):
        for child in text:
            child_tag = extract(child.tag)
            match child_tag:
                case "h":
                    self._process_h(child)
                case "p":
                    self._process_p(child)
                case _:
                    self._unhandled_tags.add(child_tag)

    def _process_h(self, header):
        output = _Header()
        style = None
        # Parse attributes
        for (k, v) in header.attrib.items():
            attr_name = extract(k)
            match attr_name:
                case "outline-level":
                    assert(not output.outline_level)
                    output.outline_level = int(v)
                case "style-name":
                    assert(not style)
                    style = self._styles.get(v, _Style())
                case _:
                    self._unhandled_attrs["h"].add(attr_name)
        assert(output.outline_level)
        assert(style)
        # Parse text
        if header.text:
            header.spans.append(_Span(header.text, style))
        for child in header:
            child_tag = extract(child.tag)
            if child_tag == "a":
                span = self._process_a(child)
                span.style |= style
                output.spans.append(span)
            else:
                self._unhandled_tags.add(child_tag)
            if child.tail:
                output.spans.append(_Span(child.tail, style))
        # Commit
        assert(output.spans)
        self._content.append(output)

    def _process_p(self, paragraph):
        output = _Paragraph()
        style = None
        # Parse style
        for (k, v) in paragraph.attrib.items():
            assert(extract(k) == "style-name")
            assert(not style)
            style = self._styles.get(v, _Style())
        assert(style)
        # Parse text
        if paragraph.text:
            output.spans.append(_Span(paragraph.text, style))
        for child in paragraph:
            child_tag = extract(child.tag)
            match child_tag:
                case "a":
                    span = self._process_a(child)
                    span.style |= style
                    output.spans.append(span)
                case "span":
                    span = self._process_span(child)
                    span.style |= style
                    output.spans.append(span)
                case "tab":
                    output.spans.append(_Span("\t", style))
                case "s":
                    output.spans.append(_Span(self._process_s(child), style))
                case _:
                    self._unhandled_tags.add(child_tag)
            if child.tail:
                output.spans.append(_Span(child.tail, style))
        # Commit
        if output.spans:
            self._content.append(output)

    # Low-level methods
    def _process_style(self, style):
        name = None
        output = None
        # _Style's metadata
        for (k, v) in style.attrib.items():
            attr_name = extract(k)
            match attr_name:
                case "name":
                    assert(not name)
                    name = v
                case _:
                    self._unhandled_attrs["style"].add(attr_name)
        assert(name)
        # _Style's data
        for child in style:
            child_tag = extract(child.tag)
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
            attr_name = extract(k)
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
        assert(extract(span.tag) == "span")
        return self._process_span(span)
    
    def _process_span(self, span):
        style = None
        for (k, v) in span.attrib.items():
            assert(extract(k) == "style-name")
            style = self._styles.get(v, _Style())
        assert(style)
        assert(span.text)
        return _Span(span.text, style)
    
    def _process_s(self, s):
        count = 1
        for (k, v) in s.attrib.items():
            assert(count == 1)
            assert(extract(k) == "c")
            count = int(v)
            assert(count)
        return " " * count