import xml.etree.ElementTree
import abc


# Utils

# Remove namespace
def _extract(name):
    return name.split("}")[1]


# Classes that collect data from traversing an ElementTree

# Parent
class _Context(abc.ABC):
    @abc.abstractclassmethod
    def traverse(self, element):
        ...
        

# Collects unique tags and their content from the entire XML treee
class _UniqueTagsContext(_Context):
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
    

# Public interface

def parse(content):
    return xml.etree.ElementTree.fromstring(content)


def unique_tags(root):
    context = _UniqueTagsContext()
    context.traverse(root)
    return context.results()