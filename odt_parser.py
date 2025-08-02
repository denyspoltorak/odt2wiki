"See https://docs.oasis-open.org/office/v1.2/cs01/OpenDocument-v1.2-cs01-part1.html"

from collections import defaultdict
from xml.etree.ElementTree import Element

from odt_tools import extract, ContentVisitor
import document

# Data classes
class _Style:
    def __init__(self):
        self.bold = None
        self.italic = None
        self.underline = None
        self.strikethrough = None
        self.colored_background = None
    
    def __ior__(self, other):
        if self.bold is None:
            self.bold = other.bold
        if self.italic is None:
            self.italic = other.italic
        if self.underline is None:
            self.underline = other.underline
        if self.strikethrough is None:
            self.strikethrough = other.strikethrough
        if self.colored_background is None:
            self.colored_background = other.colored_background
        return self
    
    def normalize(self):
        return document.Style(self.bold, self.italic, self.underline, self.strikethrough)
        

class _Span:
    def __init__(self, text, style):
        self.text = text
        self.style = style


# Full-featured extraction class
class FullVisitor(ContentVisitor):
    def __init__(self):
        self._content = []
        self._styles = {}
        self._list_styles = {}
        self._unhandled_tags = set()
        self._unhandled_attrs = defaultdict(set)
        
    def preload_styles(self, root: Element) -> None:
        tag = extract(root.tag)
        assert(tag == "document-styles")
        for child in root:
            child_tag = extract(child.tag)
            if child_tag == "styles":
                for grandchild in child:
                    grandchild_tag = extract(grandchild.tag)
                    if grandchild_tag == "list-style":
                        (name, kind) = self._process_list_style(grandchild)
                        assert(not name in self._list_styles)
                        self._list_styles[name] = kind
        
    def to_document(self) -> document.Document:
        self._print_warnings()
        # Export to an intermediary representation
        doc = document.Document()
        for elem in self._content:
            doc.add(elem)
        return doc
    
    # _Style extraction
    def traverse_styles(self, styles: Element) -> None:
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
    def traverse_text(self, text: Element) -> None:
        for child in text:
            child_tag = extract(child.tag)
            match child_tag:
                case "h":
                    self._content.append(self._process_h(child))
                case "p":
                    content = self._process_p(child)
                    if content:
                        self._content.append(content)
                case "list":
                    self._content.append(self._process_list(child))
                case "table":
                    self._content.append(self._process_table(child))
                case _:
                    self._unhandled_tags.add(child_tag)

    def _process_h(self, header):
        output = document.Header()
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
        output.spans = self._convert_spans(output.spans)
        return output

    def _process_p(self, paragraph):
        output = document.Paragraph()
        style = None
        # Parse style
        for (k, v) in paragraph.attrib.items():
            assert(extract(k) == "style-name")
            assert(not style)
            style = self._styles.get(v, _Style())
        assert(style)
        output.grayed_out = style.colored_background
        # Parse text
        if paragraph.text:
            output.spans.append(_Span(paragraph.text, style))
        for child in paragraph:
            child_tag = extract(child.tag)
            match child_tag:
                case "a":
                    span = self._process_a(child)
                    span.style |= style
                    output.grayed_out = output.grayed_out or span.style.colored_background
                    output.spans.append(span)
                case "span":
                    span = self._process_span(child)
                    span.style |= style
                    output.grayed_out = output.grayed_out or span.style.colored_background
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
        output.spans = self._convert_spans(output.spans)
        return output if output.spans else None
            
    def _process_list(self, l, kind = None):
        output = document.List()
        # Parse style
        for (k, v) in l.attrib.items():
            if(extract(k) == "style-name"):
                assert(not output.kind)
                output.kind = self._list_styles.get(v)
        if not output.kind:
            output.kind = kind
        assert(output.kind)
        # Parse items
        assert(not l.text)
        for child in l:
            assert(extract(child.tag) == "list-item")
            item = self._process_list_item(child, output.kind)
            if item:
                output.items.extend(item)
            assert(not child.tail)
        # Commit
        assert(output.items)
        return output
    
    def _process_table(self, table):
        output = document.Table()
        # Extract cells
        assert(not table.text)
        for child in table:
            match extract(child.tag):
                case "table-header-rows":
                    assert(not child.text)
                    for r in child:
                        assert(extract(r.tag) == "table-row")
                        output.rows.append(self._process_table_row(r))
                        assert(not r.tail)
                case "table-row":
                    output.rows.append(self._process_table_row(child))
            assert(not child.tail)
        # Validate and return
        assert(len(output.rows))
        output.num_columns = len(output.rows[0])
        for i in range(1, len(output.rows)):
            assert(len(output.rows[i]) == output.num_columns)
        return output

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
    
    def _process_list_style(self, list_style):
        name = None
        kind = None
        # Extract style name
        for (k, v) in list_style.attrib.items():
            assert(extract(k) == "name")
            assert(not name)
            name = v
        assert(name)
        # Extract list kind
        for child in list_style:
            for (k, v) in child.attrib.items():
                if extract(k) == "level" and int(v) == 1:
                    match extract(child.tag):
                        case "list-level-style-bullet":
                            new_kind = document.ListStyle.BULLET
                        case "list-level-style-number":
                            new_kind = document.ListStyle.NUMBER
                        case _:
                            assert(False)
                    if kind:
                        assert(kind == new_kind)
                    else:
                        kind = new_kind
        assert(kind)
        return name, kind
            
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
                case "background-color":
                    assert(output.colored_background is None)
                    output.colored_background = (v != "#ffffff")
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
    
    def _process_list_item(self, li, kind):
        output = []
        assert(not li.attrib)
        assert(not li.text)
        for child in li:
            match extract(child.tag):
                case "p":
                    result = self._process_p(child)
                    if result:
                        output.append(result)
                case "list":
                    output.append(self._process_list(child, kind))
        return output
    
    def _process_table_row(self, row):
        assert(not row.text)
        output = []
        for cell in row:
            assert(extract(cell.tag) == "table-cell")
            assert(len(cell) == 1)
            assert(extract(cell[0].tag) == "p")
            output.append(self._process_p(cell[0]))
        return output
            
    def _print_warnings(self):
        print()
        print("Unhandled tags: " + ", ".join(sorted(self._unhandled_tags)))
        print()
        print("Unhandled attrs:")
        for (k, v) in sorted(self._unhandled_attrs.items()):
            print("\t" + k + ":\t" + ", ".join(sorted(v)))
        print()
        
    @staticmethod
    def _convert_spans(spans):
        output = []
        for s in spans:
            converted_style = s.style.normalize()
            if len(output) and output[-1].style == converted_style:
                output[-1].text += s.text
            else:
                output.append(document.Span(s.text, converted_style))
        return output