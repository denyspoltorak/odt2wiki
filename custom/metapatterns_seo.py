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
    "Sandwich":
        "In Sandwich, the domain layer is subdivided while the integration and data layers remain monolithic.",
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
    "Evolutions of Services that restructure services":
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
    "Evolutions of a Sandwich":
        "A Sandwich allows for easy changes in its domain layer and can be transformed into Layers or Layered Services.",
    "Format of a metapattern":
        "This section formalizes the format of each of the metapattern chapters.",
    "Glossary":
        "The glossary of terms used throughout the Architectural Metapatterns book.",
    "History of changes":
        "The list of versions of Architectural Metapatterns and its predecessors.",
    "Index of patterns":
        "The index of patterns described in the Architectural Metapatterns book."
}