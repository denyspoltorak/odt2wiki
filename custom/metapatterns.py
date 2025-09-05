import os.path

import document
import plugins


class LinksCollector:
    def __init__(self):
        self.links = set()
        
    def __contains__(self, item):
        return item in self.links
    
    def visit(self, section):
        for s in section.header.spans:
            self._process_span(s)
        for c in section.content:
            if isinstance(c, document.Paragraph):
                for s in c.spans:
                    self._process_span(s)
        for child in section.children:
            if not child.has_file():
                self.visit(child)
    
    def _process_span(self, span):
        if span.link and not document.is_link_external(span.link) and not span.link.startswith("#"):
            filename = os.path.basename(span.link.strip('<>{} "').split("#")[0])
            if filename.endswith(".md"):
                filename = filename[:-3]
            self.links.add(filename)


class MetapatternsCustomization(plugins.Customization):
    @staticmethod
    def needs_split(section):
        # Split a chapter if it contains subchapters
        num_summaries = 0
        for c in section.children:
            for gc in c.children:
                if gc.header.to_string() == "Summary":
                    num_summaries += 1
        if num_summaries > 1:
            return True
        # Split select long chapters
        if section.header.to_string() in ("The heart of software architecture", "Appendix E. Evolutions."):
            return True
        # Otherwise use default rules
        return False
    
    @staticmethod
    def needs_local_toc(section):
        assert section.type == document.SectionType.FOLDER
        # Add Table of Contents if this folder type section does not reference all of its children files
        files = []
        for c in section.children:
            if c.has_file():
                filename = os.path.basename(c.rel_filename)
                assert filename.endswith(".md")
                files.append(filename[:-3])
        collector = LinksCollector()
        collector.visit(section)
        return not all(f in collector for f in files)


export = MetapatternsCustomization