meta_descriptions = {
    "The pattern language of software architecture":
        "This is an online version of the Architectural Metapatterns book which explores system topologies and arranges architectural patterns into a pattern language.",
    "Introduction":
        "This book part covers introductory topics that range from the book's structure to the underlying theory that enabled the research presented in the book.",
    "About this book":
        "This is the introduction to the Architectural Metapatterns book. It discusses the book's rationale, structure, and the types of diagrams used in the text.",
    "Metapatterns":
        "This chapter explores metapatterns (clusters of closely related patterns), design space, and the abstractness-subdomain-sharding system of coordinates.",
    "Foundations of software architecture":
        "This book part discusses such fundamental topics as complexity, non-functional requirements(forces), communication paradigms, and types of software systems.",
    "Modules and complexity":
        "This chapter graphically explores the basic concepts of software architecture: complexity, modularity, encapsulation, bounded contexts, coupling, and cohesion.",
    "Forces, asynchronicity, and distribution":
        "This chapter explores non-functional requirements (forces), their conflicts, and the ways to address them in modular, asynchronous, or distributed systems.",
    "Four kinds of software":
        "This chapter discusses the internal structure and architectural patterns for control, interactive, streaming, and computational software.",
    "Arranging communication":
        "This chapter discusses communication paradigms: orchestration, choreography, or shared data. It shows their applicability, benefits, and drawbacks.",
    "Programming and architectural paradigms":
        "This section discusses the object-oriented, functional, and procedural programing paradigms and their relation to common architectural styles.",
    "Orchestration":
        "This section discusses orchestration, where a single component coordinates the entire system, and mutual orchestration, where components call each other.",
    "Choreography":
        "This section discusses choreography, where a system component processes inputs and produces outputs without any knowledge about other components.",
    "Shared data":
        "This section illustrates the use of shared data for integration of system components with an example of a ticketing service.",
    "Comparison of communication styles":
        "This section discusses the use cases, benefits, and drawbacks of orchestration, choreography, and integration through shared data.",
    "Basic metapatterns":
        "This book part discusses basic system topologies: Monolith, Shards, Layers, Services, and Pipeline. They are building blocks for more complex architectures.",
    "Monolith":
        "This chapter explores monolithic architectures: Reactor, Proactor, Half-Sync/Half-Async (coroutines), and (Re)Actor-with-Extractors (phased simulation).",
    "Shards":
        "This chapter explores sharded systems that run multiple instances of a component: partitions, replicas, replicated load-balanced services, lambdas, and actors.",
    "Layers":
        "This chapter explores layered architectures (Layers and Tiers) and individual layers: interface, application, domain, utilities, middleware, and persistence.",
    "Services":
        "This chapter explores architectures with subdomain modules or services: Modulith, Actors, Service-Based Architecture, Microservices, and Nanoservices.",
    "Pipeline":
        "This chapter explores pipelined architectures that process streams: Pipes and Filters, Choreographed Event-Driven Architecture, Data Mesh, and Nanoservices.",
    "Extension metapatterns":
        "This book part discusses architectural components that integrate systems of services: Middleware, Shared Repository, Proxy, and Orchestrator.",
    "Middleware":
        "This chapter discusses Middleware and its variants: Message Bus, Event Mediator, Service Mesh, Enterprise Service Bus, and Persistent Event Log.",
    "Shared Repository":
        "This chapter discusses Shared Repository and its variants: Integration Database, Blackboard, Data Grid, shared memory, shared file system, and Stamp Coupling.",
    "Proxy":
        "This chapter discusses proxies such as: Firewall, Response Cache, Load Balancer, Sharding Proxy, Reverse Proxy, Adapter, API Gateway, and even User Interface.",
    "Orchestrator":
        "This chapter discusses Orchestrator and its variants: API Composer, MapReduce, Process Manager, Saga, Coordinator, Integration Service, and Front Controller.",
    "Sandwich":
        "This chapter explores sandwiched architectures: Blackboard System, Space-Based Architecture, Service-Based Architecture, CQRS, Nanoservices, and Lambdas.",
    "Fragmented metapatterns":
        "This book part discusses fragmented topologies: Layered Services, Polyglot Persistence, Backends for Frontends, Service-Oriented Architecture, and Hierarchy.",
    "Layered Services":
        "This chapter discusses layered services, their orchestrated and choreographed variants, and Command-Query Responsibility Segregation (CQRS) systems.",
    "Polyglot Persistence":
        "This chapter discusses Polyglot Persistence and its variants: read-only replicas, Cache-Aside, Memory Image, Reporting Database, CQRS View, and Query Service.",
    "Backends for Frontends (BFF)":
        "This chapter discusses Backends for Frontends (BFF) which dedicates a component (proxy, orchestrator, or an API Gateway) to each kind of a system's client.",
    "Service-Oriented Architecture (SOA)":
        "This chapter explores Service-Oriented Architecture (SOA) and its variants: Distributed Monolith, Domain-Oriented Microservice Architecture, and Nanoservices.",
    "Hierarchy":
        "This chapter explores hierarchical architectures: Cell-Based Architecture, Presentation-Abstraction-Control (PAC), HMVC, and Network of Networks.",
    "Implementation metapatterns":
        "This book part discusses architectural patterns used inside a system component, namely Plugins, Hexagonal Architecture, Microkernel, and Mesh.",
    "Plugins":
        "This chapter explores the highly customizable Plugins architecture and its subtypes: Plugin, Ambassador Plugin, Extension, Addin, and Addon.",
    "Hexagonal Architecture":
        "This chapter explores Hexagonal Architecture and its subtypes: Ports and Adapters, Onion Architecture, MVC, MVP and MVVM, Pedestal, and Cell (Cluster).",
    "Microkernel":
        "This chapter explores Microkernel architecture and its variants: Interpreter, Virtualizer, Configurator, Saga engine, AUTOSAR Classic, and operating system.",
    "Mesh":
        "This chapter explores meshes, their types and examples: peer-to-peer networks, Service Mesh, Space-Based Architecture, Leaf-Spine Architecture, and Actors.",
    "Analytics":
        "This book part compares architectural patterns, highlights ambiguous cases, shows how an system evolves over time, and revisits coupling and cohesion.",
    "Comparison of architectural patterns":
        "This chapter explores the ways patterns share functionality or data among their components, build pipelines, and use dependency inversion or indirection.",
    "Sharing functionality or data among services":
        "This section discusses various ways, including separation, delegation, and replication, to share functionality or data in a complex or distributed system.",
    "Pipelines in architectural patterns":
        "This section discusses architectural patterns that involve pipelined data processing, namely Pipes and Filters, Event-Driven Architecture, MVC, and CQRS.",
    "Dependency inversion in architectural patterns":
        "This section discusses dependency inversion in Plugins, Hexagonal Architecture, Microkernel, Hierarchy, Layers, and Services.",
    "Indirection in commands and queries":
        "This section discusses indirection as implemented with Anticorruption Layer or Open Host Service in OLTP and with CQRS View or Reporting Database in OLAP.",
    "Ambiguous patterns":
        "This chapter explores ambiguous patterns: Monolith, Reactor, Microkernel, Domain Services, Service-Based Architecture, Cell, and Nanoservices.",
    "Architecture and product life cycle":
        "This chapter explores how the architecture of a software project expands from Monolith through Layers to Layered Services and contracts back over its lifetime.",
    "Real-world inspirations for architectural patterns":
        "This chapter discusses inspirations and parallels for architectural patterns found in the world around us, devices we use, and the code we write.",
    "The heart of software architecture":
        "This chapter explores how cohesion and decoupling make the entirety of software architecture: its principles, patterns, and guidelines.",
    "Cohesers and decouplers":
        "This section discusses hierarchical decomposition, the influence of a project's modularity on its properties, and lists common cohesers and decouplers.",
    "Deconstructing patterns":
        "This section analizes SOLID principles, Gang of Four design patterns, and architectural metapatterns from the basic principles of coupling and cohesion.",
    "Choose your own architecture":
        "This section is a guide to choosing an architectural style based on project size, domain features, target performance, and flexibility requirements.",
    "Appendices":
        "This book part contains miscellaneous information which ranges from marginally useful (e.g. pattern evolutions) to copyright and revisions history.",
    "Acknowledgements":
        "Thanks to all the people who made the Architectural Metapatterns book possible.",
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

image_descriptions = {
    "4Kinds/3D action.png":
        "",
    "4Kinds/4 Kinds.png":
        "",
    "4Kinds/Camera.png":
        "",
    "4Kinds/Computational - main.png":
        "",
    "4Kinds/Control - main.png":
        "",
    "4Kinds/Control - variants.png":
        "",
    "4Kinds/Database.png":
        "",
    "4Kinds/Interactive - main.png":
        "",
    "4Kinds/Interactive - variants 1.png":
        "",
    "4Kinds/Interactive - variants 2.png":
        "",
    "4Kinds/Streaming - main.png":
        "",
    "Communication/Add Remove with Shared Message.png":
        "",
    "Communication/Blackboard.png":
        "",
    "Communication/Cell-Based Architecture.png":
        "",
    "Communication/Cross-link Pipeline.png":
        "",
    "Communication/Downstream Dependencies.png":
        "",
    "Communication/Facade - Parallel.png":
        "",
    "Communication/Facade.png":
        "",
    "Communication/Gateway to API Gateway.png":
        "",
    "Communication/Hierarchy - Dependencies.png":
        "",
    "Communication/Mediator.png":
        "",
    "Communication/Microkernel - Dependencies.png":
        "",
    "Communication/Monolith to Services.png":
        "",
    "Communication/Multi-choreography.png":
        "",
    "Communication/Mutual Orchestration - 1.png":
        "",
    "Communication/Mutual Orchestration - 2.png":
        "",
    "Communication/Mutual Orchestration - 3.png":
        "",
    "Communication/Mutual Orchestration - 4.png":
        "",
    "Communication/Notification inside the DB.png":
        "",
    "Communication/Notification to Notification.png":
        "",
    "Communication/Orchestrator - Dependencies.png":
        "",
    "Communication/Orchestrator add a Use Case.png":
        "",
    "Communication/Paradigms - Data-centric - Notifications.png":
        "",
    "Communication/Paradigms - Data-centric - Variants.png":
        "",
    "Communication/Paradigms - Data-centric.png":
        "",
    "Communication/Paradigms - Functional - Variants.png":
        "",
    "Communication/Paradigms - Functional.png":
        "",
    "Communication/Paradigms - Object-oriented - Variants.png":
        "",
    "Communication/Paradigms - Object-oriented.png":
        "",
    "Communication/Pipeline Early Response.png":
        "",
    "Communication/Pipeline Enricher.png":
        "",
    "Communication/Pipeline Error.png":
        "",
    "Communication/Pipeline Gateway.png":
        "",
    "Communication/Pipeline Not Parallel.png":
        "",
    "Communication/Purchase and Return.png":
        "",
    "Communication/Queues.png":
        "",
    "Communication/Services to Orchestrator.png":
        "",
    "Communication/Services to Pipeline.png":
        "",
    "Communication/Services to Shared Data.png":
        "",
    "Communication/Shared Data - Dependencies.png":
        "",
    "Communication/Shared Data add a Service.png":
        "",
    "Communication/Shared Message Format.png":
        "",
    "Communication/Shared files.png":
        "",
    "Communication/Upstream Dependencies.png":
        "",
    "Conclusion/Ambiguous-Cells.png":
        "",
    "Conclusion/Ambiguous-DomainServices.png":
        "",
    "Conclusion/Ambiguous-FrontController.png":
        "",
    "Conclusion/Ambiguous-Microkernel.png":
        "",
    "Conclusion/Ambiguous-Monolith.png":
        "",
    "Conclusion/Ambiguous-Nanoservices.png":
        "",
    "Conclusion/Ambiguous-ServiceBasedArchitecture.png":
        "",
    "Conclusion/DI-1.png":
        "",
    "Conclusion/DI-2.png":
        "",
    "Conclusion/DI-3.png":
        "",
    "Conclusion/Indirection-Command.png":
        "",
    "Conclusion/Indirection-Query.png":
        "",
    "Conclusion/Lifecycle-1.png":
        "",
    "Conclusion/Lifecycle-2.png":
        "",
    "Conclusion/Lifecycle-3.png":
        "",
    "Conclusion/Lifecycle-4.png":
        "",
    "Conclusion/Lifecycle-5.png":
        "",
    "Conclusion/Lifecycle-6.png":
        "",
    "Conclusion/Pipelineliness-CQRS.png":
        "",
    "Conclusion/Pipelineliness-EventDrivenArchitecture.png":
        "",
    "Conclusion/Pipelineliness-MVC.png":
        "",
    "Conclusion/Pipelineliness-PipesAndFilters.png":
        "",
    "Conclusion/Sharing-DedicatedService.png":
        "",
    "Conclusion/Sharing-Delegate.png":
        "",
    "Conclusion/Sharing-DirectCall.png":
        "",
    "Conclusion/Sharing-Duplicate.png":
        "",
    "Contents/Backends for Frontends.png":
        "",
    "Contents/Hexagonal Architecture.png":
        "",
    "Contents/Hierarchy.png":
        "",
    "Contents/Layered Services.png":
        "",
    "Contents/Layers.png":
        "",
    "Contents/Mesh.png":
        "",
    "Contents/Microkernel.png":
        "",
    "Contents/Middleware.png":
        "",
    "Contents/Monolith.png":
        "",
    "Contents/Orchestrator.png":
        "",
    "Contents/Pipeline.png":
        "",
    "Contents/Plugins.png":
        "",
    "Contents/Polyglot Persistence.png":
        "",
    "Contents/Proxy.png":
        "",
    "Contents/Sandwich.png":
        "",
    "Contents/Service-Oriented Architecture.png":
        "",
    "Contents/Services.png":
        "",
    "Contents/Shards.png":
        "",
    "Contents/Shared Repository.png":
        "",
    "Dependencies/Backends for Frontends.png":
        "",
    "Dependencies/CQRS.png":
        "",
    "Dependencies/Hexagonal Architecture.png":
        "",
    "Dependencies/Hierarchy.png":
        "",
    "Dependencies/Layers-1.png":
        "",
    "Dependencies/Layers-2.png":
        "",
    "Dependencies/Layers-3.png":
        "",
    "Dependencies/Microkernel.png":
        "",
    "Dependencies/Middleware.png":
        "",
    "Dependencies/Orchestrator.png":
        "",
    "Dependencies/Pipeline.png":
        "",
    "Dependencies/Plugins.png":
        "",
    "Dependencies/PolyglotPersistence.png":
        "",
    "Dependencies/Sandwich.png":
        "",
    "Dependencies/Service-Oriented Architecture.png":
        "",
    "Dependencies/Services-1.png":
        "",
    "Dependencies/Services-2.png":
        "",
    "Dependencies/Services-3.png":
        "",
    "Dependencies/Services-4.png":
        "",
    "Dependencies/SharedRepository-1.png":
        "",
    "Dependencies/SharedRepository-2.png":
        "",
    "Evolutions/2/Middleware add Middleware.png":
        "",
    "Evolutions/2/Middleware to Bus of Buses.png":
        "",
    "Evolutions/2/Orchestrator add Orchestrator.png":
        "",
    "Evolutions/2/Orchestrator to Backends for Frontends.png":
        "",
    "Evolutions/2/Orchestrator to Hierarchy.png":
        "",
    "Evolutions/2/Orchestrator to Layered Services.png":
        "",
    "Evolutions/2/Proxy add Proxy.png":
        "",
    "Evolutions/2/Proxy to Backends for Frontends.png":
        "",
    "Evolutions/2/Sandwich add remove Service.png":
        "",
    "Evolutions/2/Sandwich split merge Services.png":
        "",
    "Evolutions/2/Sandwich to Layered Services.png":
        "",
    "Evolutions/2/Sandwich to Layers.png":
        "",
    "Evolutions/2/Shared Database to Polyglot Persistence.png":
        "",
    "Evolutions/2/Shared Database to Services.png":
        "",
    "Evolutions/2/Shared Database to Space-Based Architecture.png":
        "",
    "Evolutions/2/Shared Database_ Shard.png":
        "",
    "Evolutions/3/BFF.png":
        "",
    "Evolutions/3/CQRS.png":
        "",
    "Evolutions/3/Hierarchy - 1.png":
        "",
    "Evolutions/3/Polyglor Persistence - 1.png":
        "",
    "Evolutions/3/SOA - 1.png":
        "",
    "Evolutions/3/SOA - 2.png":
        "",
    "Evolutions/3/SOA - 3.png":
        "",
    "Evolutions/3/Three-Layered Services - 1.png":
        "",
    "Evolutions/3/Three-Layered Services - 2.png":
        "",
    "Evolutions/3/Three-Layered Services - 3.png":
        "",
    "Evolutions/3/Two-Layered Services - 1.png":
        "",
    "Evolutions/3/Two-Layered Services - 2.png":
        "",
    "Evolutions/3/Two-Layered Services - 3.png":
        "",
    "Evolutions/Layers/Layers Merge.png":
        "",
    "Evolutions/Layers/Layers Split Domain to Services.png":
        "",
    "Evolutions/Layers/Layers Split in Two.png":
        "",
    "Evolutions/Layers/Layers Split to Event-Driven Architecture.png":
        "",
    "Evolutions/Layers/Layers to Backends for Frontends.png":
        "",
    "Evolutions/Layers/Layers to Hierarchy.png":
        "",
    "Evolutions/Layers/Layers to Layers.png":
        "",
    "Evolutions/Layers/Layers to Polyglot Persistence.png":
        "",
    "Evolutions/Layers/Layers to Space-Based Architecture.png":
        "",
    "Evolutions/Layers/Layers_ Shard.png":
        "",
    "Evolutions/Monolith/Monolith Split Service.png":
        "",
    "Evolutions/Monolith/Monolith add Database.png":
        "",
    "Evolutions/Monolith/Monolith add Orchestrator.png":
        "",
    "Evolutions/Monolith/Monolith add Proxy.png":
        "",
    "Evolutions/Monolith/Monolith to Hexagonal.png":
        "",
    "Evolutions/Monolith/Monolith to Instance per Client.png":
        "",
    "Evolutions/Monolith/Monolith to Interpreter.png":
        "",
    "Evolutions/Monolith/Monolith to Isolated Shards with Load Balancer.png":
        "",
    "Evolutions/Monolith/Monolith to Layers - Further 1.png":
        "",
    "Evolutions/Monolith/Monolith to Layers - Further 2.png":
        "",
    "Evolutions/Monolith/Monolith to Layers.png":
        "",
    "Evolutions/Monolith/Monolith to Mesh of Shards.png":
        "",
    "Evolutions/Monolith/Monolith to Pipeline.png":
        "",
    "Evolutions/Monolith/Monolith to Plugins.png":
        "",
    "Evolutions/Monolith/Monolith to Services - Further 1.png":
        "",
    "Evolutions/Monolith/Monolith to Services - Further 2.png":
        "",
    "Evolutions/Monolith/Monolith to Services.png":
        "",
    "Evolutions/Monolith/Monolith to Shards - Further 1.png":
        "",
    "Evolutions/Monolith/Monolith to Shards - Further 2.png":
        "",
    "Evolutions/Monolith/Monolith to Stateless Shards with Shared DB.png":
        "",
    "Evolutions/Monolith/Monolith_ Services and Pipeline.png":
        "",
    "Evolutions/Services/Pipeline promote Front Controller.png":
        "",
    "Evolutions/Services/Pipeline use Orchestrator.png":
        "",
    "Evolutions/Services/Services add Middleware.png":
        "",
    "Evolutions/Services/Services add Proxy.png":
        "",
    "Evolutions/Services/Services to Sandwich.png":
        "",
    "Evolutions/Services/Services to Shared Database.png":
        "",
    "Evolutions/Services/Services use Orchestrator.png":
        "",
    "Evolutions/Services/Services_ Cluster.png":
        "",
    "Evolutions/Services/Services_ Merge.png":
        "",
    "Evolutions/Services/Services_ Split.png":
        "",
    "Evolutions/Shards/Shards - General.png":
        "",
    "Evolutions/Shards/Shards add Load Balancer.png":
        "",
    "Evolutions/Shards/Shards add Middleware.png":
        "",
    "Evolutions/Shards/Shards add Shared DB.png":
        "",
    "Evolutions/Shards/Shards split Shared Service.png":
        "",
    "Evolutions/Shards/Shards to Shared DB.png":
        "",
    "Evolutions/Shards/Shards to Space-Based Architecture.png":
        "",
    "Evolutions/Shards/Shards use Orchestrator.png":
        "",
    "Heart/Basic.png":
        "",
    "Heart/Extension.png":
        "",
    "Heart/Features-1.png":
        "",
    "Heart/Features-2.png":
        "",
    "Heart/Features-3.png":
        "",
    "Heart/Flexibility-1.png":
        "",
    "Heart/Flexibility-2.png":
        "",
    "Heart/Fragmented.png":
        "",
    "Heart/Hierarchy.png":
        "",
    "Heart/Implementation.png":
        "",
    "Heart/Lifecycle.png":
        "",
    "Heart/Pain.png":
        "",
    "Heart/Performance-1.png":
        "",
    "Heart/Performance-2.png":
        "",
    "Heart/Performance-3.png":
        "",
    "Heart/Performance-4.png":
        "",
    "Heart/Performance-5.png":
        "",
    "Heart/Size-1.png":
        "",
    "Heart/Size-2.png":
        "",
    "Intro/3-Tier.png":
        "",
    "Intro/CQRS with notes.png":
        "",
    "Intro/Example-Defined.png":
        "",
    "Intro/Example-Undefined.png":
        "",
    "Intro/Field Gateway.png":
        "",
    "Intro/Floppy-Async.png":
        "",
    "Intro/Floppy-Sync.png":
        "",
    "Intro/Modules-1.png":
        "",
    "Intro/Modules-2.png":
        "",
    "Intro/Modules-3.png":
        "",
    "Intro/Modules-4.png":
        "",
    "Intro/Modules-5.png":
        "",
    "Intro/Modules-6.png":
        "",
    "Intro/Modules-7.png":
        "",
    "Intro/Modules-8.png":
        "",
    "Main/Backends for Frontends.png":
        "",
    "Main/Hexagonal Architecture.png":
        "",
    "Main/Hierarchy.png":
        "",
    "Main/Layered Services.png":
        "",
    "Main/Layers.png":
        "",
    "Main/Mesh.png":
        "",
    "Main/Microkernel.png":
        "",
    "Main/Middleware.png":
        "",
    "Main/Monolith.png":
        "",
    "Main/Orchestrator.png":
        "",
    "Main/Pipeline.png":
        "",
    "Main/Plugins.png":
        "",
    "Main/Polyglot Persistence.png":
        "",
    "Main/Proxy.png":
        "",
    "Main/Sandwich.png":
        "",
    "Main/Service-Oriented Architecture.png":
        "",
    "Main/Services.png":
        "",
    "Main/Shards.png":
        "",
    "Main/Shared Repository.png":
        "",
    "Misc/Diagrams.png":
        "",
    "Misc/Layers of Services.png":
        "",
    "Misc/Orchestrator.png":
        "",
    "Performance/Hexagonal Architecture.png":
        "",
    "Performance/Hierarchy - optimizations.png":
        "",
    "Performance/Hierarchy - speed.png":
        "",
    "Performance/Layered Services - channels.png":
        "",
    "Performance/Layered Services - sharding.png":
        "",
    "Performance/Layers-aggregation.png":
        "",
    "Performance/Layers-batching.png":
        "",
    "Performance/Layers-caching.png":
        "",
    "Performance/Layers-injection.png":
        "",
    "Performance/Orchestrator.png":
        "",
    "Performance/Plugins-injection.png":
        "",
    "Performance/Sandwich.png":
        "",
    "Performance/Services.png":
        "",
    "Performance/Shards.png":
        "",
    "Relations/BFF.png":
        "",
    "Relations/Hexagonal Architecture.png":
        "",
    "Relations/Hierarchy.png":
        "",
    "Relations/Layers.png":
        "",
    "Relations/Microkernel.png":
        "",
    "Relations/Middleware.png":
        "",
    "Relations/Monolith.png":
        "",
    "Relations/Orchestrator.png":
        "",
    "Relations/Plugins.png":
        "",
    "Relations/Polyglot Persistence.png":
        "",
    "Relations/Proxy.png":
        "",
    "Relations/Sandwich.png":
        "",
    "Relations/Services.png":
        "",
    "Relations/Shards.png":
        "",
    "Relations/Shared Repository.png":
        "",
    "Variants/1/Actors.png":
        "",
    "Variants/1/Application - Derived.png":
        "",
    "Variants/1/Communication - Derived.png":
        "",
    "Variants/1/DDD.png":
        "",
    "Variants/1/Data - Derived.png":
        "",
    "Variants/1/Data - Evolutions.png":
        "",
    "Variants/1/Data Mesh.png":
        "",
    "Variants/1/Distributed Monolith.png":
        "",
    "Variants/1/Domain - Derived.png":
        "",
    "Variants/1/Drivers.png":
        "",
    "Variants/1/ECB as SOA.png":
        "",
    "Variants/1/ECB.png":
        "",
    "Variants/1/Embedded.png":
        "",
    "Variants/1/Event-Driven Architecture.png":
        "",
    "Variants/1/Generic Code - Derived.png":
        "",
    "Variants/1/Half-Sync Half-Async.png":
        "",
    "Variants/1/Hexagonal Monolith.png":
        "",
    "Variants/1/Interface - Derived.png":
        "",
    "Variants/1/Interface - Kinds.png":
        "",
    "Variants/1/Lambdalith.png":
        "",
    "Variants/1/Layer Roles.png":
        "",
    "Variants/1/Layered Monolith.png":
        "",
    "Variants/1/Microservices.png":
        "",
    "Variants/1/Modular Monolith.png":
        "",
    "Variants/1/MonolithAsUnzoomed.png":
        "",
    "Variants/1/Nanoservices - API Layer.png":
        "",
    "Variants/1/Nanoservices.png":
        "",
    "Variants/1/Pipes and Filters.png":
        "",
    "Variants/1/Proactor.png":
        "",
    "Variants/1/Reactor - Multiple Threads.png":
        "",
    "Variants/1/Reactor - Single Thread.png":
        "",
    "Variants/1/Reactor with Extractors.png":
        "",
    "Variants/1/Service - Cell.png":
        "",
    "Variants/1/Service - Hexagonal.png":
        "",
    "Variants/1/Service - Layered.png":
        "",
    "Variants/1/Service - Monolithic.png":
        "",
    "Variants/1/Service - Scaled.png":
        "",
    "Variants/1/Service-Based Architecture.png":
        "",
    "Variants/1/Shards - Create on Demand.png":
        "",
    "Variants/1/Shards - Pool.png":
        "",
    "Variants/1/Shards - Replica.png":
        "",
    "Variants/1/Shards - Sharding.png":
        "",
    "Variants/1/Subtypes of Monolith.png":
        "",
    "Variants/1/Subtypes of Services.png":
        "",
    "Variants/1/Three-Tier.png":
        "",
    "Variants/1/True Monolith.png":
        "",
    "Variants/2/API Composer.png":
        "",
    "Variants/2/API Gateway.png":
        "",
    "Variants/2/Adapter.png":
        "",
    "Variants/2/Blackboard.png":
        "",
    "Variants/2/CQRS to Layered Services.png":
        "",
    "Variants/2/CQRS.png":
        "",
    "Variants/2/Cache.png":
        "",
    "Variants/2/Data Grid.png":
        "",
    "Variants/2/Dispatcher.png":
        "",
    "Variants/2/Enterprise Service Bus.png":
        "",
    "Variants/2/Event Mediator.png":
        "",
    "Variants/2/Firewall.png":
        "",
    "Variants/2/Front Controller.png":
        "",
    "Variants/2/Full Proxy.png":
        "",
    "Variants/2/Half Proxy.png":
        "",
    "Variants/2/Integration Service.png":
        "",
    "Variants/2/Load Balancer.png":
        "",
    "Variants/2/Message Bus.png":
        "",
    "Variants/2/Middleware - Shared Event Store.png":
        "",
    "Variants/2/Middleware - Structure.png":
        "",
    "Variants/2/Multifunctional - Service Mesh.png":
        "",
    "Variants/2/Multifunctional - Space-Based Architecture.png":
        "",
    "Variants/2/Nanoservices.png":
        "",
    "Variants/2/Orchestrator - BFF.png":
        "",
    "Variants/2/Orchestrator - Closed.png":
        "",
    "Variants/2/Orchestrator - Hierarchy.png":
        "",
    "Variants/2/Orchestrator - Layered.png":
        "",
    "Variants/2/Orchestrator - Monolythic.png":
        "",
    "Variants/2/Orchestrator - Open.png":
        "",
    "Variants/2/Orchestrator - SOA.png":
        "",
    "Variants/2/Orchestrator - Scaled.png":
        "",
    "Variants/2/Process Manager.png":
        "",
    "Variants/2/Proxy placement - Ambassador.png":
        "",
    "Variants/2/Proxy placement - Sidecar.png":
        "",
    "Variants/2/Proxy placement - Standalone.png":
        "",
    "Variants/2/Saga.png":
        "",
    "Variants/2/Service-Based Architecture.png":
        "",
    "Variants/2/Service-Based to Layered Services.png":
        "",
    "Variants/2/Shared Database - Event Log.png":
        "",
    "Variants/2/Shared Database.png":
        "",
    "Variants/2/Shared files.png":
        "",
    "Variants/2/Shared memory.png":
        "",
    "Variants/2/Sidecars.png":
        "",
    "Variants/2/Stamp Coupling.png":
        "",
    "Variants/2/User Interface.png":
        "",
    "Variants/3/BFF - API gateways.png":
        "",
    "Variants/3/BFF - Event mediators.png":
        "",
    "Variants/3/BFF - Gateways + Orchestrators.png":
        "",
    "Variants/3/BFF - Gateways.png":
        "",
    "Variants/3/BFF - Orchestrators.png":
        "",
    "Variants/3/CQRS - pipeline view.png":
        "",
    "Variants/3/CQRS - subtypes.png":
        "",
    "Variants/3/CQRS.png":
        "",
    "Variants/3/Cache-Aside.png":
        "",
    "Variants/3/Cell-Based Architecture.png":
        "",
    "Variants/3/DOMA.png":
        "",
    "Variants/3/Distributed Monolith.png":
        "",
    "Variants/3/Enterprise SOA.png":
        "",
    "Variants/3/Hierarchy - Bottom-up.png":
        "",
    "Variants/3/Hierarchy - Top-down.png":
        "",
    "Variants/3/Historical Data.png":
        "",
    "Variants/3/Memory Image.png":
        "",
    "Variants/3/PAC.png":
        "",
    "Variants/3/PP - Derived Storage.png":
        "",
    "Variants/3/PP - File Storage.png":
        "",
    "Variants/3/PP - Private and Shared.png":
        "",
    "Variants/3/PP - Specialized.png":
        "",
    "Variants/3/Query Service.png":
        "",
    "Variants/3/Read-only Replica.png":
        "",
    "Variants/3/Reporting DB and CQRS View.png":
        "",
    "Variants/3/SOA - AUTOSAR.png":
        "",
    "Variants/3/Search Index.png":
        "",
    "Variants/3/Three-Layered Services.png":
        "",
    "Variants/3/Two-Layered Services.png":
        "",
    "Variants/4/AUTOSAR classic.png":
        "",
    "Variants/4/Actors.png":
        "",
    "Variants/4/Addin.png":
        "",
    "Variants/4/Addon.png":
        "",
    "Variants/4/Ambassador Plugin.png":
        "",
    "Variants/4/Cell - Basic - Evolutions.png":
        "",
    "Variants/4/Cell - Basic - Subtypes.png":
        "",
    "Variants/4/Cell - Full-Featured - Plugins.png":
        "",
    "Variants/4/Cell.png":
        "",
    "Variants/4/Config file.png":
        "",
    "Variants/4/Extension.png":
        "",
    "Variants/4/Framework.png":
        "",
    "Variants/4/Hexagonal - Adapters with Components.png":
        "",
    "Variants/4/Hexagonal - Adapters with the Core.png":
        "",
    "Variants/4/Hexagonal - Driven.png":
        "",
    "Variants/4/Hexagonal - Driving and Driven.png":
        "",
    "Variants/4/Hexagonal - Driving.png":
        "",
    "Variants/4/Hexagonal - Full Isolation.png":
        "",
    "Variants/4/Interpreter.png":
        "",
    "Variants/4/Layered Hexagonal.png":
        "",
    "Variants/4/Leaf-Spine.png":
        "",
    "Variants/4/MVC - subtypes.png":
        "",
    "Variants/4/MVC.png":
        "",
    "Variants/4/MVP - subtypes.png":
        "",
    "Variants/4/MVP.png":
        "",
    "Variants/4/Monolithic Hexagonal.png":
        "",
    "Variants/4/OS.png":
        "",
    "Variants/4/P2P.png":
        "",
    "Variants/4/Pedestal.png":
        "",
    "Variants/4/Plugins.png":
        "",
    "Variants/4/Saga engine.png":
        "",
    "Variants/4/Service Mesh.png":
        "",
    "Variants/4/Space-Based Architecture.png":
        "",
    "Variants/4/Virtualizer.png":
        "",
    "Web/4Kinds.png":
        "",
    "Web/About.png":
        "",
    "Web/Ambiguous.png":
        "",
    "Web/Backends for Frontends.png":
        "",
    "Web/Choreography.png":
        "",
    "Web/Communication.png":
        "",
    "Web/Comparison.png":
        "",
    "Web/Complexity.png":
        "",
    "Web/DI.png":
        "",
    "Web/Forces.png":
        "",
    "Web/Heart.png":
        "",
    "Web/Heart2.png":
        "",
    "Web/Heart3.png":
        "",
    "Web/Hexagonal Architecture.png":
        "",
    "Web/Hierarchy.png":
        "",
    "Web/Indirection.png":
        "",
    "Web/Layered Services.png":
        "",
    "Web/Layers.png":
        "",
    "Web/Life cycle.png":
        "",
    "Web/Mesh.png":
        "",
    "Web/Metapatterns.png":
        "",
    "Web/Microkernel.png":
        "",
    "Web/Middleware.png":
        "",
    "Web/Monolith.png":
        "",
    "Web/Orchestration.png":
        "",
    "Web/Orchestrator.png":
        "",
    "Web/Pipeline.png":
        "",
    "Web/Pipelineliness.png":
        "",
    "Web/Plugins.png":
        "",
    "Web/Polyglot Persistence.png":
        "",
    "Web/Proxy.png":
        "",
    "Web/Real-world.png":
        "",
    "Web/Sandwich.png":
        "",
    "Web/Service-Oriented Architecture.png":
        "",
    "Web/Services.png":
        "",
    "Web/Shards.png":
        "",
    "Web/Shared Repository.png":
        "",
    "Web/Shared data.png":
        "",
    "Web/Sharing.png":
        "",
}