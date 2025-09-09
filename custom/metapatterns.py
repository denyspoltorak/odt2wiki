import os.path

import document
import plugins


meta_descriptions = {
    "The pattern language of software architecture":
        "The Metapatterns website is a compendium and classification of architectural patterns based on the assumption that structure determines function.",
    "Introduction":
        "This part defines metapatterns, explains the notation for NoSQL diagrams used throughout the book, and provides a theory for pattern classification.",
    "About this book":
        "The story behind Architectural Metapatterns, the kinds of diagrams and notation used throughout the book, and why we need a classification of patterns.",
    "Metapatterns":
        "A metapattern is a cluster of patterns with related structure and function. We draw designs along the abstractness, subdomain and sharding axes.",
    "Part 1. Foundations":
        "This part reviews the basics of software architecture: forces, complexity, distribution, and the ways to connect multiple components in a system.",
    "Modules and complexity":
        "Complexity is the number of concepts which one must keep in mind to understand a system. Breaking a system into components may lower its complexity.",
    "Forces, asynchronicity, and distribution":
        "Forces are non-functional requirement for a system. Conflicting forces are satisfied by splitting a system into asynchronous or distributed components.",
    "Four kinds of software":
        "Control, interactive, streaming and computational software differ in their architectures and design patterns. Complex systems mix these four approaches.",
    "Arranging communication":
        "Components can be integrated through orchestration, choreography or shared data. These approaches emerge at every level: from code to system design.",
    "Programming and architectural paradigms":
        "The object-oriented, functional, and procedural paradigms are the code-level manifestations of orchestration, choreography, and shared data, correspondingly.",
    "Orchestration":
        "In orchestration there is a high-level component, called orchestrator, which uses (orchestrates) other components in order to implement application logic.",
    "Choreography":
        "In choreography user requests or input events pass through a chain of components that handle individual steps of the scenario which the system implements.",
    "Shared data":
        "Communication through shared data benefits data-centric domains where multiple services need to operate on a common dataset.",
    "Comparison of the options":
        "Orchestration is good when there are many complex scenarios, choreography - for simple highly loaded systems, shared data - for data-centric domains.",
    "Part 2. Basic Metapatterns":
        "Basic architectures include: Monolith, Shards, Layers, Services, and Pipeline. They are building blocks for more complex designs.",
    "Monolith":
        "A Monolith is a cohesive system which keeps all of its business logic, generic code and data together. This architecture fits short-lived tiny projects.",
    "Shards":
        "Shards are multiple instances of a subsystem or component. They can be stateful or stateless. Stateful shards with identical data are called replicas.",
    "Layers":
        "A layered system is subdivided by the level of abstraction. It is common to have presentation, application, domain, and infrastructure layers.",
    "Services":
        "Services are components dedicated to subdomains. They may vary in size, internal structure and technologies. A service can be further subdivided into a Cell.",
    "Pipeline":
        "A pipeline is a chain of components that implement individual steps of data or event processing. Its parts tend to be highly independent and scalable.",
    "Part 3. Extension Metapatterns":
        "A system of services can be extended with one or more specialized layers such as a Proxy, a Middleware, an Orchestrator, or a Shared Repository.",
    "Middleware":
        "A Middleware provides system components with means of communication. It may also manage their deployment, scaling and failure recovery.",
    "Shared Repository":
        "A Shared Repository stores all or a part of the system's data. It may provide notifications on data change and atomic transactions.",
    "Proxy":
        "A Proxy represents a system to its clients. It implements cross-cutting concerns, such as caching or protocol translation, and routes client requests.",
    "Orchestrator":
        "An Orchestrator integrates lower-level components. It runs a client request as a series of calls to other components while keeping their states consistent.",
    "Combined Component":
        "A Combined Component implements two or more of the following extension patterns: Middleware, Shared Repository, Proxy, and Orchestrator.",
    "Part 4. Fragmented Metapatterns":
        "Fragmented architectures make use of small specialized components. Examples include Layered Services, BFF, SOA, Polyglot Persistence, and Hierarchy.",
    "Layered Services":
        "Layered Services may orchestrate each other, rely on choreography, or make a CQRS system. The communication between services happens at different layers.",
    "Polyglot Persistence":
        "Polyglot Persistence is the pattern for using multiple databases, which may be mutually independent or derived. The specialization improves performance.",
    "Backends for Frontends (BFF)":
        "Backends for Frontends dedicates a component to each kind of a system's client. That grants flexibility in workflows and technologies.",
    "Service-Oriented Architecture (SOA)":
        "Service-Oriented Architecture is an application of object-oriented design at the system level. It builds a system from small reusable components.",
    "Hierarchy":
        "A Hierarchy distributes responsibilities throughout a tree of components. It is fault tolerant, and the components remain simple and are easy to replace.",
    "Part 5. Implementation Metapatterns":
        "Implementation patterns study internals of a component. Plugins, Microkernel and Hexagonal Architecture grant flexibility while Mesh provides fault tolerance.",
    "Plugins":
        "Plugins let a client customize select aspects of a system's behavior. Addons build their application logic on top of whatever the modified system provides.",
    "Hexagonal Architecture":
        "Hexagonal Architecture isolates a component's business logic from its environment through hiding all the component's dependencies behind Adapters.",
    "Microkernel":
        "A microkernel mediates between resource providers and resource consumers. It both makes the providers expendable and sandboxes the consumers.",
    "Mesh":
        "A Mesh or Grid is a virtual layer of interconnected components which makes a distributed Middleware. It features supreme fault tolerance ande scalability.",
    "Part 6. Analytics":
        "This part compares different aspects of patterns which were covered in the previous chapters and outlines a few general topics of software architecture.",
    "Comparison of architectural patterns":
        "",
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
    subtitle = "The pattern language of software architecture"
    
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