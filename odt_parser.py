"See https://docs.oasis-open.org/office/v1.2/cs01/OpenDocument-v1.2-cs01-part1.html"

import xml.etree.ElementTree
import abc


# Utils

# Remove namespace
def _extract(name):
    return name.split("}")[1]


# Classes that collect data from traversing an ElementTree

# Parent
class _Visitor(abc.ABC):
    @abc.abstractclassmethod
    def traverse(self, element):
        ...
        

# Collects unique tags and their content from the entire XML treee
class _UniqueTagsVisitor(_Visitor):
    def __init__(self):
        self._tags = {}
        
    def traverse(self, element):
        value = None
        
        # Found new kind of tag - remember it and an example of the tag's data
        tag = _extract(element.tag)
        if tag not in self._tags:
            value = "(" + ", ".join(_extract(key) for key in element.attrib.keys()) + ")"
            if element.text:
                value += element.text
        
        # Traverse children
        for child in element:
            self.traverse(child)
            if value and child.tail:
                value += child.tail
        
        # Save the new tag
        if value:
            self._tags[tag] = value
    
    def results(self):
        return self._tags
    

# Collects unique tags into a tree of dictionaries
class _TagsTreeVisitor(_Visitor):
    def __init__(self):
        self._tree = {}
        
    def traverse(self, root):
        self._recurse(self._tree, root)
    
    def results(self):
        return self._tree

    @staticmethod
    def _recurse(dict, element):
        
        # Make sure we remeber the current element's tag
        tag = _extract(element.tag)
        if tag not in dict:
            dict[tag] = {}
        
        # Visit the current element's children
        for child in element:
            _TagsTreeVisitor._recurse(dict[tag], child)


# Public interface

def parse(content):
    return xml.etree.ElementTree.fromstring(content)


def unique_tags(root):
    context = _UniqueTagsVisitor()
    context.traverse(root)
    return context.results()


def tree_of_tags(root):
    context = _TagsTreeVisitor()
    context.traverse(root)
    return context.results()