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
    "Part 1. Foundations of software architecture":
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
    "Comparison of communication styles":
        "Orchestration is good when there are many complex scenarios, choreography - for simple highly loaded systems, shared data - for data-centric domains.",
    "Part 2. Basic metapatterns":
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
    "Part 3. Extension metapatterns":
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
    "Part 4. Fragmented metapatterns":
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
    "Part 5. Implementation metapatterns":
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
        "Patterns vary in ways to share functionality or data among system components, build pipelines, and in their use of dependency inversion or indirection.",
    "Sharing functionality or data among services":
        "Functionality or data may be shared among componets through: direct access, building a dedicated service, delegation, and replication.",
    "Pipelines in architectural patterns":
        "Pipeline is a unidirectional data flow. Depending on pattern, it may or may not preserve: data type, data identity and temporal order of the data stream.",
    "Dependency inversion in architectural patterns":
        "Plugins, Hexagonal Architecture, Microkernel and Hierarchy rely on dependency inversion. Other patterns, such as Layers and Services, occasionally use it.",
    "Indirection in commands and queries":
        "Indirection is implemented with Anticorruption Layer or Open Host Service in OLTP and with CQRS View or Reporting Database in OLAP systems.",
    "Ambiguous patterns":
        "There are patterns whose meaning varies from source to source. They include Monolith, Reactor, Microkernel, Domain Services, Cells, and Nanoservices.",
    "Architecture and product life cycle":
        "Architecture of a software project evolves over its lifetime. It starts monolithic, transforms into Layers and Services, then merges back to a Monolith.",
    "Real-world inspirations for architectural patterns":
        "Styles and patterns of software architecture have real-world inspirations and parallels. Learning about them may help us to invent new patterns when needed.",
    "The heart of software architecture":
        "The closing chapter shows how cohesion and decoupling make the entirety of software architecture: its principles, patterns and guidelines.",
    "Cohesers and decouplers":
        "Some architectural constraints or forces cause the code to be kept together, others pull it apart, still others prefer components of a definite size.",
    "Deconstructing patterns":
        "Both SOLID principles, Gang of Four design patterns, and architectural metapatterns emerge from the interplay of coupling and cohesion.",
    "Choose your own architecture":
        "This is a guide to choosing an architectural style based on project size, domain features, target performance and flexibility requirements.",
    "Part 7. Appendices":
        "This part contains miscellaneous information which ranges from marginally useful (e.g. pattern evolutions) to copyright and revisions history.",
    "Appendix A. Acknowledgements.":
        "Thanks to the people who made Architectural Metapatterns possible.",
    "Appendix B. Books referenced.":
        "The list of books which Architectural Metapatterns references.",
    "Appendix C. Copyright.":
        "Creative Commons Attribution 4.0 International Public License.",
    "Appendix D. Disclaimer.":
        "IN NO EVENT SHALL THE COPYRIGHT HOLDERS OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES.",
    "Appendix E. Evolutions.":
        "Avenues to evolve many software and system architectures. Each evolution lists its goal, preconditions, benefits and drawbacks.",
    "Evolutions of a Monolith that lead to Shards":
        "Multiple stateful or stateless instances of a Monolith can be deployed to improve performance. The systems may need a Sharding Proxy or Load Balancer.",
    "Evolutions of a Monolith that result in Layers":
        "A Monolith can be split into Layers, or a specialized layer, such as a Proxy or an Orchestrator, may be added between an existing Monolith and its clients.",
    "Evolutions of a Monolith that make Services":
        "A Monolith can be divided into modules, Services or a Pipeline to support development by multiple teams, improve its codebase, and employ more hardware.",
    "Evolutions of a Monolith that rely on Plugins":
        "Plugins or Interpreter make a monolithic component customizable. Hexagonal Architecture protects its business logic from unstable external dependencies. ",
    "Evolutions of Shards that share data":
        "The main issue with Shards is coordination between the instances. It is solved by deploying a Shared Repository or wrapping the shared data with a service.",
    "Evolutions of Shards that share logic":
        "Intershard communication is helped by a Middleware or is made unnecessary by employing a Sharding Proxy or an Orchestrator.",
    "Evolutions of Layers that make more layers":
        "It is often possible to split the business logic layer in two, namely, integration or application logic (scenarios) and domain logic (business rules).",
    "Evolutions of Layers that help large projects":
        "When a layered software grows large, its business logic should be subdivided into Services, Pipeline or Hierarchy.",
    "Evolutions of Layers to improve performance":
        "There are a few ways to improve performance of a layered system: merge the layers, scale them, or use specialized databases (Polyglot Persistence).",
    "Evolutions of Layers to gain flexibility":
        "The upper Proxy or Orchestrator layer can be split into a service per client, making Backends for Frontends. This allows for per-client customization.",
    "Evolutions of Services that add or remove services":
        "A new service can be added, an existing one can be split in two, or multiple services can be merged if they become tightly coupled.",
    "Evolutions of Services that add layers":
        "A system of services can be extended with a Middleware, Service Mesh, Proxies, Shared Database or an Orchestrator which implement cross-cutting concerns.",
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
    "Appendix F. Format of a metapattern.":
        "This section formalized the format of each of the metapattern chapters.",
    "Appendix G. Glossary.":
        "The glossary of terms used throughout the Architectural Metapatterns book.",
    "Appendix H. History of changes.":
        "The list of versions of Architectural Metapatterns and its predecessors.",
    "Appendix I. Index of patterns.":
        "The index of patterns described in the Architectural Metapatterns book."
}

hidden_chapters = {
    "Appendix A. Acknowledgements.",
    "Appendix C. Copyright.",
    "Appendix D. Disclaimer.",
    "Appendix H. History of changes.", 
}

extra_split = {
    "The heart of software architecture", 
    "Appendix E. Evolutions."
}


assert hidden_chapters.issubset(meta_descriptions.keys())
assert extra_split.issubset(meta_descriptions.keys())


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
    def is_hidden(section):
        return section.header.to_string() in hidden_chapters
    
    @staticmethod
    def get_description(section):
        title = section.header.to_string()
        assert title in meta_descriptions, title
        return meta_descriptions[title]


export = MetapatternsCustomization