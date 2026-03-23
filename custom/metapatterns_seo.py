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