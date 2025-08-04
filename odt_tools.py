"Tools for investigating ODT files"

import xml.etree.ElementTree
from collections import defaultdict


# Remove namespace
def extract(name):
    return name.split("}")[1]


# Parse XML
def parse(content):
    return xml.etree.ElementTree.fromstring(content)


# Collects unique tags and their content from the entire XML treee
class UniqueTagsVisitor:
    def __init__(self):
        self._tags = defaultdict(set)
        
    def traverse(self, element):
        # Remember the tag and the element's attributes
        tag = extract(element.tag)
        attrs = self._tags[tag]
        for key in element.attrib.keys():
            attrs.add(extract(key))
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
class TagsTreeVisitor:
    def __init__(self):
        self._tree = {}
        
    def traverse(self, root):
        self._recurse(self._tree, root)
    
    def results(self):
        return self._tree

    @staticmethod
    def _recurse(dic, element):
        # Make sure we remeber the current element's tag
        tag = extract(element.tag)
        if tag not in dic:
            dic[tag] = {}
        # Visit the current element's children
        for child in element:
            TagsTreeVisitor._recurse(dic[tag], child)


# Plain text extraction
class TextVisitor():
    def __init__(self):
        self._content = []
        self._unhandled = set()
        # Dispatch tables
        self._text_child_handlers = {
            "p": self._on_p,
            "h": self._on_h,
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
        self._list_item_handlers = {
            "p": self._on_p,
            "list": self._on_list,
        }
        
    def results(self):
        print("Unhandles tags: " + ", ".join(sorted(self._unhandled)))
        return "\n".join(self._content)
    
    def traverse(self, root):
        tag = extract(root.tag)
        assert(tag == "document-content")
        for child in root:
            child_tag = extract(child.tag)
            if child_tag  == "body":
                assert(len(child) == 1)
                text = child[0]
                assert(extract(text.tag) == "text")
                self._traverse_text(text)
    
    def _traverse_text(self, text):
        for child in text:
            tag = extract(child.tag)
            handler = self._text_child_handlers.get(tag)
            if handler:
                self._content.append(handler(child))
            else:
                self._unhandled.add(tag)
    
    # Top-level elements
    def _on_h(self, h):
        return "\n" + self._on_p(h)
    
    def _on_p(self, p):
        paragraph = []
        # Add the prefix text
        if p.text:
            paragraph.append(p.text)
        # Add child elements
        for child in p:
            tag = extract(child.tag)
            handler = self._paragraph_child_handlers.get(tag)
            if handler:
                handler(paragraph, child)
            else:
                self._unhandled.add(tag)
            # Add any text found between this and the following element
            if child.tail:
                paragraph.append(child.tail)
        # Merge the paragraph into a string
        return "".join(paragraph)
    
    def _on_table(self, table):
        rows = []
        # Extract cells
        assert(not table.text)
        for child in table:
            match extract(child.tag):
                case "table-header-rows":
                    assert(not child.text)
                    for r in child:
                        assert(extract(r.tag) == "table-row")
                        rows.append(self._on_table_row(r))
                case "table-row":
                    rows.append(self._on_table_row(child))
        assert(len(rows) > 1)
        for i in range(len(rows) - 1):
            assert(len(rows[i]) == len(rows[i + 1]))
        # Output transposed
        output = ["",]
        for c in range(len(rows[0])):
            for r in range(len(rows)):
                text = rows[r][c]
                if text:
                    output.append(text)
            output.append("")
        return "\n".join(output)
        
    def _on_list(self, l):
        output = []
        assert(not l.text)
        for child in l:
            tag = extract(child.tag)
            assert(tag == "list-item")
            for grandchild in child:
                grandtag = extract(grandchild.tag)
                handler = self._list_item_handlers.get(grandtag)
                assert(handler)
                output.append(handler(grandchild))
                assert(not grandchild.tail)
            assert(not child.tail)
        return "\n".join(output)
        
    # Low-level elements
    def _on_table_row(self, row):
        assert(not row.text)
        output = []
        for cell in row:
            assert(extract(cell.tag) == "table-cell")
            assert(len(cell) == 1)
            assert(extract(cell[0].tag) == "p")
            output.append(self._on_p(cell[0]))
        return output
    
    @staticmethod
    def _on_a(paragraph, a):
        if a.text:
            paragraph.append(a.text)
        for child in a:
            tag = extract(child.tag)
            if tag == "span":
                TextVisitor._on_span(paragraph, child)
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
            if extract(k) == "c":
                count = int(v)
                assert(count)
        paragraph.append(" " * count)
        
    @staticmethod
    def _on_tab(paragraph, tab):
        paragraph.append("\t")
        
    @staticmethod
    def _on_frame(paragraph, frame):
        paragraph.append(" IMAGE ")
        