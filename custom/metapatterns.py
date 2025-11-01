import os.path
import re

import document
import plugins


meta_descriptions = {
    "The pattern language of software architecture":
        "Explore how patterns relate to each other and work together.",
    "Introduction":
        "Architectural Metapatterns is a structured collection of patterns featuring hundreds of NoUML diagrams.",
    "About this book":
        "There are too many patterns to remember, therefore we need a system to sort them out and remove duplicates.",
    "Metapatterns":
        "A metapattern is a group of patterns related in their structure and function.",
    "Foundations of software architecture":
        "Learn basic principles of software architecture such as complexity, forces, and the ways to build large systems.",
    "Modules and complexity":
        "Complexity is how much you must know about a system to understand it.",
    "Forces, asynchronicity, and distribution":
        "Forces are our expectations about a system’s properties.",
    "Four kinds of software":
        "Control, interactive, streaming and computational software differ in design.",
    "Arranging communication":
        "Components can be integrated through orchestration, choreography, or shared data.",
    "Programming and architectural paradigms":
        "The object-oriented, functional, and procedural paradigms also emerge in system design.",
    "Orchestration":
        "A single component, called Orchestrator, coordinates other system components.",
    "Choreography":
        "Components communicate with each other without any explicit supervisor.",
    "Shared data":
        "Components communicate by changing a shared state.",
    "Comparison of communication styles":
        "Orchestration helps with complex use cases, shared data supports data-centric domains, while choreography is highly scalable.",
    "Basic metapatterns":
        "Basic architectures include: Monolith, Shards, Layers, Services, and Pipeline.",
    "Monolith":
        "A Monolith is an unstructured application, fast to write but hard to maintain.",
    "Shards":
        "Shards are multiple instances of a component or subsystem.",
    "Layers":
        "Layers (or distributed Tiers) separate the high-level logic from the low-level details.",
    "Services":
        "Services deal with large projects by dividing them into subdomain-aligned components of smaller sizes.",
    "Pipeline":
        "A Pipeline represents a data processing algorithm as a sequence of steps.",
    "Extension metapatterns":
        "A Middleware, Shared Repository, Proxy, an Orchestrator or a Combined Component extends the underlying system of services or shards.",
    "Middleware":
        "A Middleware provides a system of services with means of communication, scalability, and error recovery.",
    "Shared Repository":
        "A Shared Repository encapsulates a system’s data, allowing for data-centric development.",
    "Proxy":
        "A Proxy represents a system to its clients and takes care of some aspects of the communication.",
    "Orchestrator":
        "An Orchestrator is a high-level layer which integrates other components.",
    "Combined Component":
        "A Combined Component is a layer which implements multiple cross-cutting concerns.",
    "Fragmented metapatterns":
        "Layered Services, Polyglot Persistence, Backends for Frontends, Service-Oriented Architecture, or Hierarchy builds a system from many smaller components.",
    "Layered Services":
        "Layered Services is an umbrella architecture for common implementations of systems of services.",
    "Polyglot Persistence":
        "Polyglot Persistence is the pattern for using multiple databases.",
    "Backends for Frontends (BFF)":
        "Backends for Frontends dedicate a component to each kind of a system's client.",
    "Service-Oriented Architecture (SOA)":
        "Service-Oriented Architecture builds a system from layers of services.",
    "Hierarchy":
        "Hierarchy distributes responsibilities throughout a tree of components.",
    "Implementation metapatterns":
        "Plugins, Hexagonal Architecture, Microkernel, and Mesh present internal designs of components.",
    "Plugins":
        "Plugins allow for customization of a component’s behavior",
    "Hexagonal Architecture":
        "Hexagonal Architecture isolates a component’s business logic from its external dependencies by inserting adapters.",
    "Microkernel":
        "A microkernel mediates between resource providers and resource consumers.",
    "Mesh":
        "A Mesh or Grid is a virtual layer of interconnected components which makes a distributed Middleware.",
    "Analytics":
        "The analytics compares architectural patterns, highlights ambiguous patterns, and shows how a project’s architecture evolves over time.",
    "Comparison of architectural patterns":
        "Patterns vary in the ways they share functionality or data among system components, build pipelines, and in their use of dependency inversion or indirection.",
    "Sharing functionality or data among services":
        "Functionality or data may be shared among components through direct access, building a dedicated service, delegation, and replication.",
    "Pipelines in architectural patterns":
        "Pipeline is a unidirectional data flow. Depending on the pattern, it may preserve the data type, data identity, or temporal order of the data stream.",
    "Dependency inversion in architectural patterns":
        "Plugins, Hexagonal Architecture, Microkernel, and Hierarchy rely on dependency inversion. Other patterns, such as Layers and Services, occasionally use it.",
    "Indirection in commands and queries":
        "Indirection is implemented with Anticorruption Layer or Open Host Service in OLTP and with CQRS View or Reporting Database in OLAP systems.",
    "Ambiguous patterns":
        "There are patterns with meanings which vary from source to source. They include Monolith, Reactor, Microkernel, Domain Services, Cells, and Nanoservices.",
    "Architecture and product life cycle":
        "The architecture of a software project evolves over its lifetime. It starts monolithic, transforms into Layers and Services, then merges back to a Monolith.",
    "Real-world inspirations for architectural patterns":
        "Styles and patterns of software architecture have real-world inspirations and parallels. Learning about them may help us to invent new patterns when needed.",
    "The heart of software architecture":
        "The closing chapter shows how cohesion and decoupling make the entirety of software architecture: its principles, patterns, and guidelines.",
    "Cohesers and decouplers":
        "Some architectural constraints or forces cause the code to be kept together, others pull it apart, and still others prefer components of a definite size.",
    "Deconstructing patterns":
        "Both SOLID principles, Gang of Four design patterns, and architectural metapatterns emerge from the interplay of coupling and cohesion.",
    "Choose your own architecture":
        "This is a guide to choosing an architectural style based on project size, domain features, target performance, and flexibility requirements.",
    "Appendices":
        "This part contains miscellaneous information which ranges from marginally useful (e.g. pattern evolutions) to copyright and revisions history.",
    "Acknowledgements":
        "Thanks to the people who made Architectural Metapatterns possible.",
    "Books referenced":
        "The list of books which Architectural Metapatterns references.",
    "Copyright":
        "Creative Commons Attribution 4.0 International Public License.",
    "Disclaimer":
        "IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES.",
    "Evolutions of architectures":
        "Avenues to evolve many software and system architectures. Each evolution lists its goal, preconditions, benefits, and drawbacks.",
    "Evolutions of a Monolith that lead to Shards":
        "Multiple stateful or stateless instances of a Monolith can be deployed to improve performance. The systems may need a Sharding Proxy or Load Balancer.",
    "Evolutions of a Monolith that result in Layers":
        "A Monolith can be split into Layers, or a specialized layer, such as a Proxy or an Orchestrator, may be added between an existing Monolith and its clients.",
    "Evolutions of a Monolith that make Services":
        "A Monolith can be divided into modules, Services, or a Pipeline to support development by multiple teams, improve its codebase, and employ more hardware.",
    "Evolutions of a Monolith that rely on Plugins":
        "Plugins or Interpreter make a monolithic component customizable. Hexagonal Architecture protects its business logic from unstable external dependencies. ",
    "Evolutions of Shards that share data":
        "The main issue with Shards is coordination between the instances. It is solved by deploying a Shared Repository or wrapping the shared data with a service.",
    "Evolutions of Shards that share logic":
        "Intershard communication is helped by a Middleware or is made unnecessary by employing a Sharding Proxy or an Orchestrator.",
    "Evolutions of Layers that make more layers":
        "It is often possible to split the business logic layer in two, namely, integration or application logic (scenarios) and domain logic (business rules).",
    "Evolutions of Layers that help large projects":
        "When layered software grows large, its business logic should be subdivided into Services, Pipeline, or Hierarchy.",
    "Evolutions of Layers to improve performance":
        "There are a few ways to improve the performance of a layered system: merge the layers, scale them, or use specialized databases (Polyglot Persistence).",
    "Evolutions of Layers to gain flexibility":
        "The upper Proxy or Orchestrator layer can be split into a service per client, making Backends for Frontends. This allows for per-client customization.",
    "Evolutions of Services that add or remove services":
        "A new service can be added, an existing one can be split in two, or multiple services can be merged if they become tightly coupled.",
    "Evolutions of Services that add layers":
        "A system of services can be extended with a Middleware, Service Mesh, Proxies, Shared Database, or an Orchestrator which implement cross-cutting concerns.",
    "Evolutions of a Pipeline":
        "A Front Controller may be used to track states of running requests. Alternatively, adding an Orchestrator benefits complex scenarios.",
    "Evolutions of a Middleware":
        "It is possible to add a second specialized Middleware or integrate several systems through a hierarchy of Middlewares.",
    "Evolutions of a Shared Repository":
        "A shared database can be sharded or divided into private databases. Space-Based Architecture or Polyglot Persistence help to improve performance.",
    "Evolutions of a Proxy":
        "A new system-wide proxy may be stacked with the existing one or you can deploy a proxy per client type.",
    "Evolutions of an Orchestrator":
        "An Orchestrator can be subdivided into Backends for Frontends or Layered Services. Alternatively, you can use a layered or hierarchical Orchestrator.",
    "Evolutions of a Combined Component":
        "A stack of single-purpose layers can replace a Combined Component, buying you flexibility at the cost of development effort and, often, performance.",
    "Format of a metapattern":
        "This section formalizes the format of each of the metapattern chapters.",
    "Glossary":
        "The glossary of terms used throughout the Architectural Metapatterns book.",
    "History of changes":
        "The list of versions of Architectural Metapatterns and its predecessors.",
    "Index of patterns":
        "The index of patterns described in the Architectural Metapatterns book."
}

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
    "Combined Component":                                   "/diagrams/Web/Combined Component.png",
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