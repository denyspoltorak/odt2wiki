import os.path

import document
import plugins


meta_descriptions = {
    "Introduction",
    "About this book",
    "Metapatterns",
    "Part 1. Foundations",
    "Modules and complexity",
    "Forces, asynchronicity, and distribution",
    "Four kinds of software",
    "Arranging communication",
    "Programming and architectural paradigms",
    "Orchestration",
    "Choreography",
    "Shared data",
    "Comparison of the options",
    "Part 2. Basic Metapatterns",
    "Monolith",
    "Shards",
    "Layers",
    "Services",
    "Pipeline",
    "Part 3. Extension Metapatterns",
    "Middleware",
    "Shared Repository",
    "Proxy",
    "Orchestrator",
    "Combined Component",
    "Part 4. Fragmented Metapatterns",
    "Layered Services",
    "Polyglot Persistence",
    "Backends for Frontends (BFF)",
    "Service-Oriented Architecture (SOA)",
    "Hierarchy",
    "Part 5. Implementation Metapatterns",
    "Plugins",
    "Hexagonal Architecture",
    "Microkernel",
    "Mesh",
    "Part 6. Analytics",
    "Comparison of architectural patterns",
    "Sharing functionality or data among services",
    "Pipelines in architectural patterns",
    "Dependency inversion in architectural patterns",
    "Indirection in commands and queries",
    "Ambiguous patterns",
    "Architecture and product life cycle",
    "Real-world inspirations for architectural patterns",
    "The heart of software architecture",
    "Cohesers and decouplers",
    "Deconstructing patterns",
    "Choose your own architecture",
    "Part 7. Appendices",
    "Appendix A. Acknowledgements.",
    "Appendix B. Books referenced.",
    "Appendix C. Copyright.",
    "Appendix D. Disclaimer.",
    "Appendix E. Evolutions.",
    "Monolith: to Shards",
    "Monolith: to Layers",
    "Monolith: to Services",
    "Monolith: to Plugins",
    "Shards: share data",
    "Shards: share logic",
    "Layers: make more layers",
    "Layers: help large projects",
    "Layers: improve performance",
    "Layers: gain flexibility",
    "Services: add or remove services",
    "Services: add layers",
    "Pipeline:",
    "Middleware:",
    "Shared Repository:",
    "Proxy:",
    "Orchestrator:",
    "Combined Component:",
    "Appendix F. Format of a metapattern.",
    "Appendix G. Glossary.",
    "Appendix H. History of changes.",
    "Appendix I. Index of patterns."
}

hidden_chapters = {
    "Appendix A. Acknowledgements.",
    "Appendix C. Copyright.",
    "Appendix D. Disclaimer.",
    "Appendix H. History of changes.", 
}


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
    subtitle = "The Pattern Language of Software Architecture"
    
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
    
    @staticmethod
    def is_hidden(section):
        return section.header.to_string() in hidden_chapters


export = MetapatternsCustomization