import os.path
import re

import document
import plugins

from custom.metapatterns_seo import *


toc_images = {
    "About this book":                                      "/diagrams/Web/About.png",
    "Metapatterns":                                         "/diagrams/Web/Metapatterns.png",
    "Modules and complexity":                               "/diagrams/Web/Complexity.png",
    "Forces, asynchronicity, and distribution":             "/diagrams/Web/Forces.png",
    "Four kinds of software":                               "/diagrams/Web/4Kinds.png",
    "Arranging communication":                              "/diagrams/Web/Communication.png",
    "Programming and architectural paradigms":              "/diagrams/Web/Paradigms.png",
    "Orchestration":                                        "/diagrams/Web/Orchestration.png",
    "Choreography":                                         "/diagrams/Web/Choreography.png",
    "Shared data":                                          "/diagrams/Web/Shared data.png",
    "Monolith":                                             "/diagrams/Web/Monolith.png",
    "Shards":                                               "/diagrams/Web/Shards.png",
    "Layers":                                               "/diagrams/Web/Layers.png",
    "Services":                                             "/diagrams/Web/Services.png",
    "Pipeline":                                             "/diagrams/Web/Pipeline.png",
    "Middleware":                                           "/diagrams/Web/Middleware.png",
    "Shared Repository":                                    "/diagrams/Web/Shared Repository.png",
    "Proxy":                                                "/diagrams/Web/Proxy.png",
    "Orchestrator":                                         "/diagrams/Web/Orchestrator.png",
    "Sandwich":                                             "/diagrams/Web/Sandwich.png",
    "Layered Services":                                     "/diagrams/Web/Layered Services.png",
    "Polyglot Persistence":                                 "/diagrams/Web/Polyglot Persistence.png",
    "Backends for Frontends (BFF)":                         "/diagrams/Web/Backends for Frontends.png",
    "Service-Oriented Architecture (SOA)":                  "/diagrams/Web/Service-Oriented Architecture.png",
    "Hierarchy":                                            "/diagrams/Web/Hierarchy.png",
    "Plugins":                                              "/diagrams/Web/Plugins.png",
    "Hexagonal Architecture":                               "/diagrams/Web/Hexagonal Architecture.png",
    "Microkernel":                                          "/diagrams/Web/Microkernel.png",
    "Mesh":                                                 "/diagrams/Web/Mesh.png",
    "Comparison of architectural patterns":                 "/diagrams/Web/Comparison.png",
    "Sharing functionality or data among services":         "/diagrams/Web/Sharing.png",
    "Pipelines in architectural patterns":                  "/diagrams/Web/Pipelineliness.png",
    "Dependency inversion in architectural patterns":       "/diagrams/Web/DI.png",
    "Indirection in commands and queries":                  "/diagrams/Web/Indirection.png",
    "Ambiguous patterns":                                   "/diagrams/Web/Ambiguous.png",
    "Architecture and product life cycle":                  "/diagrams/Web/Life cycle.png",
    "Real-world inspirations for architectural patterns":   "/diagrams/Web/Real-world.png",
    "The heart of software architecture":                   "/diagrams/Web/Heart.png",
    "Cohesers and decouplers":                              "/diagrams/Web/Heart.png",
    "Deconstructing patterns":                              "/diagrams/Web/Heart2.png",
    "Choose your own architecture":                         "/diagrams/Web/Heart3.png"
}

override_images = {
    "Performance/Hierarchy - speed.svg":            "Performance/Hierarchy - speed.negated.dark.svg",
    "Communication/Pipeline Early Response.svg":    "Communication/Pipeline Early Response.negated.dark.svg",
    "Variants/2/User Interface.svg":                "Variants/2/User Interface.negated.dark.svg",
    "Web/Real-world.svg":                           "Web/Real-world.negated.dark.svg"
}

wide_previews = {
    "Programming and architectural paradigms",
    "Comparison of communication styles"
}

hidden_chapters = {
    "Acknowledgements",
    "Copyright",
    "Disclaimer",
    "History of changes", 
}

extra_split = {
    "The heart of software architecture", 
    "Evolutions of architectures"
}

definition_lists = {
    "Glossary"
}

grid_tocs = {
    "The pattern language of software architecture":    (2, "grid5"),
    "Introduction":                                     (2, "grid3"),
    "Foundations of software architecture":             (2, "grid3"),
    "Arranging communication":                          (2, "grid3"),
    "Analytics":                                        (2, "grid3"),
    "Comparison of architectural patterns":             (2, "grid3"),
    "The heart of software architecture":               (2, "grid3")
}


assert hidden_chapters.issubset(meta_descriptions.keys())
assert extra_split.issubset(meta_descriptions.keys())
assert definition_lists.issubset(meta_descriptions.keys())
assert set(grid_tocs.keys()).issubset(meta_descriptions.keys())
assert set(toc_images.keys()).issubset(meta_descriptions.keys())
assert wide_previews.issubset(meta_descriptions.keys())


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
    subtitle = "The pattern language of software architecture"
    grid_wide_class = "grid-row"
    large_favicon = "/diagrams/Web/Favicon-plain.png"
    image_path = "/diagrams/Web/"
    og_path = "/diagrams/Web/og/"
    
    def __init__(self, mode):
        self._hugo = (mode == "hugo")
        self._extra_images = None
        self._useful_image_names = {v for v in toc_images.values() if isinstance(v, str)}
        
    def set_extra_images(self, images):
        assert images
        assert not self._extra_images
        self._extra_images = {k: images[v] for k, v in toc_images.items() if v in images}
    
    def preprocess(self, section):
        title = section.header.to_string()
        # Strip technical terms "Part N" or "Appendix X" with the associated full stops
        found = re.fullmatch(r"(?:Part\s\d+\.\s+|Appendix\s\w\.\s+)(.+?)(?:\.?)", title)
        if found:
            assert len(section.header.spans) == 1
            title = section.header.spans[0].text = found[1]
        # Find figure captions
        elements = []
        for c in section.content:
            if isinstance(c, document.Paragraph) \
                    and c.centered \
                    and len(c.spans) == 1 \
                    and elements \
                    and isinstance(elements[-1], document.Image):
                elements[-1].caption = c.spans[0].text
            else:
                elements.append(c)
        section.content = elements
        # Convert to definition list
        if self._hugo:
            if title in definition_lists:
                dl = document.DefinitionList()
                for c in section.content:
                    assert isinstance(c, document.Paragraph)
                    item = c.split(" – ")
                    assert len(item) == 2
                    dl.items.append(item)
                section.content = [dl,]
    
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
        if section.header.to_string() in extra_split:
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
    def toc_grid_depth_and_style(section):
        return grid_tocs.get(section.header.to_string())
    
    @staticmethod
    def is_hidden(section):
        return section.header.to_string() in hidden_chapters
    
    def get_sitemap_priority(self, section):
        title = section.header.to_string()
        parent_title = section.parent.header.to_string() if section.parent else ""
        if title == "Metapatterns" or "metapatterns" in parent_title:
            return 0.8  # Patterns and theory
        if title.startswith("Evolutions") and title != "Evolutions":
            return 0.3  # Pattern evolutions
        if "metapatterns" in title or self.needs_split(section):
            return 0.2  # Part and split chapter intros
        if parent_title in {"Appendices", "The pattern language of software architecture"}:
            return 0.1  # Appendices and book part summaries
        return 0.5      # Analytical and overbiew articles
    
    @staticmethod
    def get_description(section):
        title = section.header.to_string()
        assert title in meta_descriptions, title
        return meta_descriptions[title]
    
    @staticmethod
    def get_image_alt_text(image):
        assert image in image_descriptions, image
        result = image_descriptions[image]
        assert result, image
        return result
    
    def get_preview_image(self, section):
        title = section.header.to_string()
        # Reuse images from the table of contents on the landing page
        link = toc_images.get(title, self.large_favicon)
        assert link.startswith(self.image_path)
        return link.replace(self.image_path, self.og_path)

    def get_toc_image(self, section_name):
        if section_name in wide_previews:
            return plugins.Wide()
        return self._extra_images.get(section_name)

    @staticmethod
    def get_dark_image(light_image):
        # Special cases
        for k, v in override_images.items():
            if light_image.endswith(k):
                return light_image.replace(k, v)
        # The default dark file name
        if light_image.endswith(".svg"):
            return light_image[:-4] + ".dark.svg"
        else:
            return None
        
    def is_useful_image(self, image):
        return image in self._useful_image_names


export = MetapatternsCustomization