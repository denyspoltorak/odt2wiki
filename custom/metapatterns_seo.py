meta_descriptions = {
    "The pattern language of software architecture":
        "Architectural Metapatterns is a compendium that organizes architectural patterns according to their structure and function into a universal pattern language.",
    "Introduction":
        "Architectural Metapatterns is a compendium of architectueral patterns, an atlas of system topologies, and one of the largest pattern languages.",
    "About this book":
        "Architectural Metapatterns contains introductory topics, 19 chapters each dedicated to a cluster of closely related patterns, analytics, and pattern evolutions.",
    "Metapatterns":
        "Architectural patterns can be organized according to their structure and function, which reveals relations between the patterns and creates a pattern language.",
    "System topologies":
        "System and software architectures are organized by their partitioning into monolithic, layered, service-based, fragmented, and plugins topologies.",
    "Foundations of software architecture":
        "Introductory topics of software architecture review complexity, non-functional requirements (forces), communication paradigms, and types of software systems.",
    "Modules and complexity":
        "The basic concepts of software architecture: complexity, modularity, encapsulation, bounded contexts, coupling, and cohesion are explored with diagrams.",
    "Forces, asynchronicity, and distribution":
        "Modularity, asynchronous communication and distribution allow a system to meet conflicting forces. However, that impairs debugging and performance.",
    "Four kinds of software":
        "There are four kinds of software with different architectures: control, interactive, streaming and computational. Let's discuss their code and patterns.",
    "Arranging communication":
        "The components of a software system can be integrated through orchestration, choreography, or shared data. Each approach has benefits and drawbacks.",
    "Programming and architectural paradigms":
        "The object-oriented, functional, and procedural paradigms re-emerge at the system level as microservies, pipelines, and Space-Based Architecture.",
    "Orchestration":
        "Orchestration relies on a facade or mediator to integrate the entire system. It sacrifices performance for support of high number of complex scenarios.",
    "Choreography":
        "Choreography builds a pipeline to process requests. It may work through commands, publish/subscribe, or shared message format. Early response is preferred.",
    "Shared data":
        "Communication through shared data allows for the services that operate the data to be independent. The data layer is used for persistence, messaging, or both.",
    "Comparison of communication styles":
        "Orchestration tackles complex use cases, choreography provides good performance for data transformations, while shared data supports data-centric domains.",
    "Basic metapatterns":
        "Monolith, Shards, Layers, Services, and Pipeline are the basic building blocks for any complex architecture.",
    "Monolith":
        "The monolithic architecture is good for tiny projects. It may act as a Reactor, Proactor, Half-Sync/Half-Async (coroutines), or (Re)Actor-with-Extractors.",
    "Shards":
        "Shards are instances of a component or subsystem. They can be stateful, stateless (form a pool), or created on demand. The main issue is data synchronization.",
    "Layers":
        "Layers or tiers subdivide a system into high-level and low-level components such as: interface, application, domain, utilities, middleware, and persistence.",
    "Services":
        "Services dedicate a component and a team to each subdomain. Examples include Service-Based Architecture, Microservices, Modulith, Actors, and Nanoservices.",
    "Pipeline":
        "Pipelines are good for building highly scalable systems. They include Pipes and Filters, Choreographed Event-Driven Architecture, Data Mesh, and Nanoservices.",
    "Extension metapatterns":
        "Middleware, Shared Repository, Proxy, and Orchestrator extract some aspects of a system into a dedicated layer. Sandwich subdivides only the domain logic.",
    "Middleware":
        "Middleware takes care of messaging, scalability, and error recovery. Its examples include Message Bus, Event Mediator, Service Mesh, and Enterprise Service Bus.",
    "Shared Repository":
        "Shared Repository is about persistence and communication through data. It covers: Integration Database, Blackboard, and Data Grid of Space-Based Architecture.",
    "Proxy":
        "A Proxy represents a system to its clients and implements an aspect of its behavior. Proxies include: Firewall, Load Balancer, Adapter, and Response Cache.",
    "Orchestrator":
        "An Orchestrator integrates the underlying components. It combines the aspects of facade and mediator and is known as API Composer, Process Manager, or Saga.",
    "Sandwich":
        "A Sandwich is a system midway between Layers and Services. Its examples include: Blackboard System, Space-Based Architecture, and Vertical Slice Architecture.",
    "Fragmented metapatterns":
        "Layered Services, Polyglot Persistence, Backends for Frontends, Service-Oriented Architecture, and Hierarchy comprise systems of fine-grained components,",
    "Layered Services":
        "Layered Services are about the internals of systems of services. They include: orchestrated 3-layered services, choreographed 2-layered services, and CQRS.",
    "Polyglot Persistence":
        "Polyglot Persistence is about using multiple databases, which may be of different kinds (SQL vs NoSQL), or dedicated to read and write requests (as in CQRS).",
    "Backends for Frontends (BFF)":
        "Backends for Frontends (BFF) dedicates a Proxy, Orchestrator, or an API Gateway to each kind of a system's client, allowing for drastically different clients.",
    "Service-Oriented Architecture (SOA)":
        "Service-Oriented Architecture (SOA) employs 3 or 4 layers of reusable services. It fits huge projects but the naive implementation may be slow and error-prone.",
    "Hierarchy":
        "Hierarchy distributes complexity over a tree of components. Examples include Cell-Based Architecture, Vertical Slice Architecture, HMVC, and Bus of Buses.",
    "Implementation metapatterns":
        "Plugins, Hexagonal Architecture (including MVC and MVP), Microkernel, and Mesh are patterns used to implement system components.",
    "Plugins":
        "Plugins, Addons, and Addins provide for customization of an application. An Ambassador Plugin injects the business logic of one service into another service.",
    "Hexagonal Architecture":
        "Hexagonal Architecture (Ports and Adapters) and the derived Model-View-Controller (MVC) and Cell aim to protect business logic from external dependencies.",
    "Microkernel":
        "Microkernel shares resources of providers among consumers. It is the pattern for operating systems, interpreters, hypervisors, and software frameworks.",
    "Mesh":
        "Mesh is a system of interconnected components (nodes) of one or two types. Meshes include: peer-to-peer networks, Service Mesh, and Space-Based Architecture.",
    "Analytics":
        "We will compare architectural patterns, highlight ambiguous pattern names, show how a system evolves over time, and revisit coupling and cohesion.",
    "Comparison of architectural patterns":
        "The classification of architectural patterns into metapatterns is applied to compare them and reveal how various architectures approach certain problem.",
    "Sharing functionality or data among services":
        "When you need to share code, library, or data between services, you can: co-locate everything, dedicate a shared service, delegate, or replicate the aspect.",
    "Pipelines in architectural patterns":
        "A data or event stream may or may not preserve the data type, order, and identity, as seen in Pipes and Filters, EDA, CQRS, and MVC.",
    "Dependency inversion in architectural patterns":
        "Dependency inversion on the system level is used in Plugins, Hexagonal Architecture, Microkernel, Hierarchy, and, to a certain extent, in Layers or Services.",
    "Indirection in commands and queries":
        "OLTP systems use Anticorruption Layer, Open Host Service, and Orchestrator as adapters. Data Mesh relies on CQRS View, Reporting Database, or Query Service.",
    "The multiform read-write separation":
        "Patterns that separate read and write paths include: read-only database replicas, response cache, CQRS, Data Mesh, MVCC, and (Re)Actor-with-Extractors.",
    "Latency optimizations on the system level":
        "Architectural level latency optimizations co-locate or bypass components, preprocess and preload data, and rely on non-blocking access or request hedging.",
    "Ambiguous patterns":
        "The meaning of Monolith, Reactor, Microkernel, Domain Services, Service-Based Architecture, Cell, or Nanoservices varies depending on which book you read.",
    "Architecture and product life cycle":
        "Software architecture changes as a project grows, matures, and dies. It starts small, then expands into fragmens, then collapses back to a monolithic state.",
    "Real-world inspirations for architectural patterns":
        "There are parallels between our daily life, software design and patterns. The article shows how the same ideas bloom in software and in the physical world.",
    "The heart of software architecture":
        "The interplay of cohesion and decoupling gives birth to the entirety of software architecture: its principles, patterns, and guidelines.",
    "Cohesers and decouplers":
        "We tackle complexity through hierarchical decomposition. Cohesers push you to merge all the code together while decouplers favor fine-grained components.",
    "Deconstructing patterns":
        "The SOLID principles, Gang of Four design patterns, and architectural metapatterns are tracked down to the foundational ideas of decoupling and cohesion.",
    "Choose your own architecture":
        "Some guidelines to choosing an architectural style based on project size, domain features, target performance, and flexibility requirements.",
    "Appendices":
        "Miscellaneous information which ranges from marginally useful (e.g. pattern evolutions) to copyright and revision history.",
    "Acknowledgements":
        "Thanks to all the people who made the Architectural Metapatterns book possible.",
    "Books referenced":
        "The list of books which Architectural Metapatterns references.",
    "Copyright":
        "The full text of Creative Commons Attribution 4.0 International Public License.",
    "Disclaimer":
        "The disclaimer for readers of Architectural Metapatterns.",
    "Evolutions of architectures":
        "Avenues to evolve many software and system architectures. Each evolution lists its goal, preconditions, benefits, and drawbacks.",
    "Evolutions of a Monolith that lead to Shards":
        "Multiple stateful or stateless instances of a Monolith can be deployed to improve performance. The systems may need a Sharding Proxy or Load Balancer.",
    "Evolutions of a Monolith that result in Layers":
        "A Monolith can be split into Layers. Or, a specialized layer, such as a Proxy or an Orchestrator, may be added between an existing Monolith and its clients.",
    "Evolutions of a Monolith that make Services":
        "A Monolith can be divided into modules, Services, or a Pipeline to support development by multiple teams, improve its codebase, and deploy more hardware.",
    "Evolutions of a Monolith that rely on Plugins":
        "Plugins or an Interpreter make a monolithic component customizable. Hexagonal Architecture protects its business logic from unstable external dependencies.",
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
        "The formal description of the format of each of the metapattern chapters.",
    "Glossary":
        "The glossary of terms used throughout the Architectural Metapatterns book.",
    "History of changes":
        "The list of versions of Architectural Metapatterns and its predecessors.",
    "Index of patterns":
        "The index of patterns described in the Architectural Metapatterns book."
}

image_descriptions = {
    "4Kinds/3D action.png":
        "Architecture of a 3D game.",
    "4Kinds/4 Kinds.png":
        "Control, interactive, streaming, and computational systems.",
    "4Kinds/Camera.png":
        "Internal components of a camera with interactive, control, and streaming communication highlighted.",
    "4Kinds/Computational - main.png":
        "A computational system makes multiple calls to the underlying OS during a single run.",
    "4Kinds/Control - main.png":
        "Event processing in a control system.",
    "4Kinds/Control - variants.png":
        "A control system can be monolithic or actor-based, or make a pedestal or hierarchy.",
    "4Kinds/Database.png":
        "Internals of a database with client sessions, a parser, task, metadata manager, and tables.",
    "4Kinds/Interactive - main.png":
        "An interactive system workflow with an event coming from the presentation layer to the model and back.",
    "4Kinds/Interactive - variants 1.png":
        "Event processing may be blocking or non-blocking.",
    "4Kinds/Interactive - variants 2.png":
        "Model-View-Controller and Model-View-Presenter.",
    "4Kinds/Streaming - main.png":
        "A streaming system is a pipeline of data processing steps.",
    "Communication/Add Remove with Shared Message.png":
        "Adding and removing services in a pipeline with shared message format.",
    "Communication/Blackboard.png":
        "Blackboard Architecture contains a scheduler, services, and the blackboard.",
    "Communication/Cell-Based Architecture.png":
        "A Cell-Based Architecture comprises clusters of services.",
    "Communication/Cross-link Pipeline.png":
        "Cross-linking independent pipelines.",
    "Communication/Downstream Dependencies.png":
        "Adding an upstream component in a command-based pipeline.",
    "Communication/Facade - Parallel.png":
        "A facade initiates communication with every service that it orchestrates simultaneously in a fan-out manner.",
    "Communication/Facade.png":
        "A facade uses request/confirm pairs of messages to communicate with the services which it orchestrates.",
    "Communication/Gateway to API Gateway.png":
        "An API Gateway runs subrequests in parallel while a pipeline runs them consecutively.",
    "Communication/Hierarchy - Dependencies.png":
        "In a hierarchy each child component depends on the SPI of their parent.",
    "Communication/Mediator.png":
        "A mediator receives an input from one component, processes it, and initiates actions in other components.",
    "Communication/Microkernel - Dependencies.png":
        "In a Microkernel each managed service depends on a dedicated SPI of the microkernel.",
    "Communication/Monolith to Services.png":
        "A monolithic system is subdivided into several services but it is an open question how the resulting components interact.",
    "Communication/Multi-choreography.png":
        "A set of services participates in multiple pipelines.",
    "Communication/Mutual Orchestration - 1.png":
        "A set of services which call each other while executing requests from their clients.",
    "Communication/Mutual Orchestration - 2.png":
        "Each service depends on every other service which it calls.",
    "Communication/Mutual Orchestration - 3.png":
        "In layered services only the application layers of the services call each other.",
    "Communication/Mutual Orchestration - 4.png":
        "In layered services only the application layers of the services are interdependent.",
    "Communication/Notification inside the DB.png":
        "A ticketing service whose components rely on database notifications.",
    "Communication/Notification to Notification.png":
        "A ticketing service whose components use direct messaging.",
    "Communication/Orchestrator - Dependencies.png":
        "An orchestrator depends on every service which it uses.",
    "Communication/Orchestrator add a Use Case.png":
        "Adding a new use case to an orchestrated system changes only the orchestrator.",
    "Communication/Paradigms - Data-centric - Notifications.png":
        "Components of a data-centric system rely on data change notifications.",
    "Communication/Paradigms - Data-centric - Variants.png":
        "Services with a shared database and a Space-Based Architecture.",
    "Communication/Paradigms - Data-centric.png":
        "In a procedural system logic and data make independent hierarchies.",
    "Communication/Paradigms - Functional - Variants.png":
        "Event-Driven Architecture and Data Mesh.",
    "Communication/Paradigms - Functional.png":
        "A pipeline with components transforming the data that passes through them.",
    "Communication/Paradigms - Object-oriented - Variants.png":
        "Microservices, orchestrated services, and Service-Oriented Architecture.",
    "Communication/Paradigms - Object-oriented.png":
        "An object-oriented system built through composition.",
    "Communication/Pipeline Early Response.png":
        "The first service of a pipeline responds to the client immediately while forwarding the client's request to other services.",
    "Communication/Pipeline Enricher.png":
        "A request collects data from every service in a pipeline as it passes those services.",
    "Communication/Pipeline Error.png":
        "Rollback of changes done by services arranged into a pipeline.",
    "Communication/Pipeline Gateway.png":
        "The very component that receives a client request must send back the response.",
    "Communication/Pipeline Not Parallel.png":
        "An orchestrator can run subrequests in parallel which is impossible for a pipeline.",
    "Communication/Purchase and Return.png":
        "Both purchase and refund services read and write the entire system's data.",
    "Communication/Queues.png":
        "A queue per service, separate input and output queues, a queue per channel, and a single system queue.",
    "Communication/Services to Orchestrator.png":
        "After a monolith is subdivided into services, an orchestrator is added to communicate with the client and with each service.",
    "Communication/Services to Pipeline.png":
        "After a monolith is subdivided into services, the services are assembled into a pipeline.",
    "Communication/Services to Shared Data.png":
        "After a monolith is subdivided into services, a shared database is used to integrate them.",
    "Communication/Shared Data - Dependencies.png":
        "Each service depends only on the shared database.",
    "Communication/Shared Data add a Service.png":
        "Adding a service to a system integrated through shared data does not require changes to other services.",
    "Communication/Shared Message Format.png":
        "Each component depends on the message header and the message field(s) it accesses.",
    "Communication/Shared files.png":
        "Stepwise processing of a batch of files.",
    "Communication/Upstream Dependencies.png":
        "Downstream services are easily added to a pub/sub pipeline, turning it into a tree.",
    "Conclusion/Ambiguous-Cells.png":
        "WSO2 Cells and Amazon Cells.",
    "Conclusion/Ambiguous-DomainServices.png":
        "Domain services according to Domain-Driven Design and Fundamentals of Software Architecture.",
    "Conclusion/Ambiguous-FrontController.png":
        "Front Controller according to Patterns of Enterprise Application Architecture and Software Architecture: the Hard Parts.",
    "Conclusion/Ambiguous-Microkernel.png":
        "Microkernel according to Pattern-Oriented Software Architecture and Plugins Architecture",
    "Conclusion/Ambiguous-Monolith.png":
        "Monolith as a single component, a co-deployed system, a synchronous distributed system, a Layered Architecture, and modules with a shared database.",
    "Conclusion/Ambiguous-Nanoservices.png":
        "Nanoservices as an API layer over a shared database, a pipeline, a Space-Based Architecture, actors, and a Service-Based Architecture.",
    "Conclusion/Ambiguous-ServiceBasedArchitecture.png":
        "Service-Based Architecture, microservices, and Service-Oriented Architecture.",
    "Conclusion/DI-1.png":
        "Plugins depend on the core's SPIs wjile adapters of Hexagonal Architecture depend on both the core's SPIs and APIs of the adapted components.",
    "Conclusion/DI-2.png":
        "Dependencies in an operating system, hierarchy, and Cell-Based Architecture.",
    "Conclusion/DI-3.png":
        "Standard APIs separate frontend and backend, and backend and database. CQRS views or adapters protect a service from dependencies on other services.",
    "Conclusion/Indirection-Command.png":
        "Dependencies for an anticorruption layer, open host service, and orchestrated services.",
    "Conclusion/Indirection-Plugin.png":
        "A service injects a plugin into another service and streams data for use by the plugin.",
    "Conclusion/Indirection-Query.png":
        "Dependencies for a CQRS view, reporting database, and query service.",
    "Conclusion/Latency-Bypass.png":
        "A hierarchical control system, Model-View-Controller, and and an OS with kernel bypass featuring early response.",
    "Conclusion/Latency-Colocate.png":
        "An ambassador sharding proxy, mesh nodes in sidecars, and an actor framework optimize latency by co-locating system components.",
    "Conclusion/Latency-EarlyResponse.png":
        "In a rate limiter, response cache, or a pipeline the component which receives a client request may respond immediately.",
    "Conclusion/Latency-Omit.png":
        "In a half-proxy or open orchestrator a system layer may be omitted. A telephone server leaves conversation after the phones establish a direct connection.",
    "Conclusion/Latency-Preloading.png":
        "A Space-Based Architecture, CQRS, and CQRS view.",
    "Conclusion/Lifecycle-1.png":
        "A monolith.",
    "Conclusion/Lifecycle-2.png":
        "Layers and Hexagonal Architecture.",
    "Conclusion/Lifecycle-3.png":
        "Layered services, orchestrated services, and a top-down hierarchy.",
    "Conclusion/Lifecycle-4.png":
        "Layered Services evolve into a pragmatic architecture.",
    "Conclusion/Lifecycle-5.png":
        "Layers with multiple databases.",
    "Conclusion/Lifecycle-6.png":
        "A monolith with multiple databases.",
    "Conclusion/Pipelineliness-CQRS.png":
        "A CQRS system makes a data pipeline.",
    "Conclusion/Pipelineliness-EventDrivenArchitecture.png":
        "Parcel delivery example with different pipelines for individual parcels and trucks of parcels.",
    "Conclusion/Pipelineliness-MVC.png":
        "Events from the mouse pass to the controller and the model, and those from the model - to the view and display.",
    "Conclusion/Pipelineliness-PipesAndFilters.png":
        "Pipes and Filters where a data stream originates with the source, passes several filters, and ends in a sink.",
    "Conclusion/RW-Cache.png":
        "The cache layer remembers responses from the application and reuses them for incoling client queries.",
    "Conclusion/RW-Control.png":
        "The control layer repeatedly queries the model layer and finally decides to send a request which is propagated down to the hardware components.",
    "Conclusion/RW-CQRS-Options.png":
        "The domain-level separation of CQRS can be combined with the data-level separation of read-only database replicas or a pair of OLTP and OLTP databases.",
    "Conclusion/RW-MVCC.png":
        "The database creates a snapshot of its data for every incoming write request. A read request is served from the latest snapshot. Unused snapshots are deleted.",
    "Conclusion/RW-OLTP-OLAP.png":
        "Write requests go to the OLTP database. Read requests go to the OLAP database. The OLTP database streams changes to the OLAP database.",
    "Conclusion/Sharing-DedicatedService.png":
        "A shared logger deployed as a service in Service-Oriented Architecture. A shared counter deployed as a stand-alone shared database in polyglot persistence.",
    "Conclusion/Sharing-Delegate.png":
        "Message loggers in a proxy and middleware. A request counter in a gateway of a pipeline.",
    "Conclusion/Sharing-DirectCall.png":
        "A logger and counter accessible for direct calls inside a monolith or in an infrastructure layer of Layered Architecture.",
    "Conclusion/Sharing-Duplicate.png":
        "Replicated loggers in each instance of a service in shards, in code imported by every nanoservice, and in sidecars of microservices. A replicated counter in a data grid.",
    "Contents/Backends for Frontends.png":
        "Services with backends for frontends.",
    "Contents/Hexagonal Architecture.png":
        "Hexagonal Architecture.",
    "Contents/Hierarchy.png":
        "Top-down hierarchy.",
    "Contents/Layered Services.png":
        "Layered services.",
    "Contents/Layers.png":
        "Layered architecture.",
    "Contents/Mesh.png":
        "Services comminicating through a mesh.",
    "Contents/Microkernel.png":
        "Microkernel.",
    "Contents/Middleware.png":
        "Services with a middleware.",
    "Contents/Monolith.png":
        "Monolith.",
    "Contents/Orchestrator.png":
        "Services with an orchestrator.",
    "Contents/Pipeline.png":
        "Pipeline.",
    "Contents/Plugins.png":
        "Plugins Architecture.",
    "Contents/Polyglot Persistence.png":
        "Services with polyglot persistence.",
    "Contents/Proxy.png":
        "Services with a proxy.",
    "Contents/Sandwich.png":
        "Sandwich Architecture.",
    "Contents/Service-Oriented Architecture.png":
        "Service-Oriented Architecture.",
    "Contents/Services.png":
        "Services Architecture.",
    "Contents/Shards.png":
        "Shards.",
    "Contents/Shared Repository.png":
        "Services with a shared repository.",
    "Dependencies/Backends for Frontends.png":
        "Each backend for frontend depends on every service which it calls.",
    "Dependencies/CQRS.png":
        "In CQRS each service depends on its database while the OLAP database depends on the source of its event feed.",
    "Dependencies/Hexagonal Architecture.png":
        "In Hexagonal Architecture each adapter depends on the core and the component or protocol it adapts.",
    "Dependencies/Hierarchy.png":
        "In a hierarchy a child component depends on an SPI of its parent component. If the children are polymorphic, their parent has a single SPI.",
    "Dependencies/Layers-1.png":
        "Individual layers may depend on other layers' APIs, SPIs, or both. In the last case the layer between the SPI and API is an adapter.",
    "Dependencies/Layers-2.png":
        "Dependencies for open and closed layers.",
    "Dependencies/Layers-3.png":
        "A load balancer helps access multiple instances of a component directly below it.",
    "Dependencies/Microkernel.png":
        "Applications depend on the API of the microkernel. Providers depend on its SPIs.",
    "Dependencies/Middleware.png":
        "Each service depends on the middleware and on every service which it uses.",
    "Dependencies/Orchestrator.png":
        "A facade depends on every service. Contrariwise, every service depends on a mediator.",
    "Dependencies/Pipeline.png":
        "Commands cause downstream dependencies. Notifications cause upstream dependencies. Every component depends on a shared message.",
    "Dependencies/Plugins.png":
        "Each plugin depends on an interface of the core.",
    "Dependencies/PolyglotPersistence.png":
        "The business logic depends on every database. A derived database depends on its data source.",
    "Dependencies/Sandwich.png":
        "The integration layer depends on every service. Every service depends on the data layer.",
    "Dependencies/Service-Oriented Architecture.png":
        "Tasks depend on entities. Entities depend on utilities and libraries.",
    "Dependencies/Services-1.png":
        "With request/confirm a service depends on whatever it uses.",
    "Dependencies/Services-2.png":
        "With pub/sub a service depends on its notification sources.",
    "Dependencies/Services-3.png":
        "A CQRS view breaks dependencies between services.",
    "Dependencies/Services-4.png":
        "Adapters isolate a service from its dependencies.",
    "Dependencies/SharedRepository-1.png":
        "If the shared repository supports notifications, services depend only on the repository. Otherwise each service also depends on its event sources.",
    "Dependencies/SharedRepository-2.png":
        "Each service may have a private Database Abstraction Layer, or there may be one shared Database Abstraction Layer colocated with the shared repository.",
    "Evolutions/2/Middleware add Middleware.png":
        "A specialized middleware added to a system that already has a generic middleware.",
    "Evolutions/2/Middleware to Bus of Buses.png":
        "A low-level middleware interconnects several higher-level middlewares.",
    "Evolutions/2/Orchestrator add Orchestrator.png":
        "An orchestrator is subdivided into a pair of simple and complex orchestrators.",
    "Evolutions/2/Orchestrator to Backends for Frontends.png":
        "An orchestrator is subdivided into backends for brontends.",
    "Evolutions/2/Orchestrator to Hierarchy.png":
        "An orchestrator is subdivided into a hierarchy.",
    "Evolutions/2/Orchestrator to Layered Services.png":
        "An orchestrator is subdivided into subdomain components which become the application layers of respective services.",
    "Evolutions/2/Proxy add Proxy.png":
        "A proxy is added on top of an existing proxy.",
    "Evolutions/2/Proxy to Backends for Frontends.png":
        "A proxy is subdivided into backends for frontends.",
    "Evolutions/2/Sandwich add remove Service.png":
        "One of the domain-level services is removed and another one is added.",
    "Evolutions/2/Sandwich split merge Services.png":
        "One domain-level service is split in half while two other services are merged together.",
    "Evolutions/2/Sandwich to Layered Services.png":
        "The integration and data layers are divided into subdomains, producing three-layered services.",
    "Evolutions/2/Sandwich to Layers.png":
        "The entire domain layer is merged, resulting in a Layered Architecture.",
    "Evolutions/2/Shared Database to Polyglot Persistence.png":
        "The shared database is migrated to specialized databases.",
    "Evolutions/2/Shared Database to Services.png":
        "The shared database is split into databases dedicated to subdomains, resulting in layered services.",
    "Evolutions/2/Shared Database to Space-Based Architecture.png":
        "The shared database is migrated to a data grid, resulting in Space-Based Architecture",
    "Evolutions/2/Shared Database_ Shard.png":
        "The shared database is sharded so that each database instance holds a subset of data,",
    "Evolutions/3/BFF.png":
        "Backends for frontends can be merged into an orchestrator, can share code via sidecars, or put shared functionality into a dedicated orchestration layer or into cell gateways.",
    "Evolutions/3/CQRS.png":
        "CQRS behind an API Gateway, with a single backend, multiple OLAP databases, layered backends, cells for backends, and data grid for a database.",
    "Evolutions/3/Hierarchy - 1.png":
        "The upper layer of a top-down hierarchy is subdivided into backends for frontends.",
    "Evolutions/3/Polyglor Persistence - 1.png":
        "The backend layer that uses OLAP and OLTP databases is subdivided into a CQRS system.",
    "Evolutions/3/SOA - 1.png":
        "The shared components are replicated into services which use them.",
    "Evolutions/3/SOA - 2.png":
        "The shared components are replicated into sidecars.",
    "Evolutions/3/SOA - 3.png":
        "Services with an orchestrator, backends for frontends, and Cell-Based Architecture.",
    "Evolutions/3/Three-Layered Services - 1.png":
        "Three-layered services with partially merged application layer, partially merged databases and shared databases, and a Sandwich Architecture.",
    "Evolutions/3/Three-Layered Services - 2.png":
        "Three-layered services employing CQRS views and a query service.",
    "Evolutions/3/Three-Layered Services - 3.png":
        "The domain layer of a large three-layered service is split into sub-subdomain components, resulting in a sandwich cell.",
    "Evolutions/3/Two-Layered Services - 1.png":
        "Two-layered services with partially merged domain layer, partially merged databases, and shared databases.",
    "Evolutions/3/Two-Layered Services - 2.png":
        "Two-layered services employing CQRS views and a query service.",
    "Evolutions/3/Two-Layered Services - 3.png":
        "The domain layer of a large two-layered service is split in half.",
    "Evolutions/Layers/Layers Merge.png":
        "The application and domain layers are merged.",
    "Evolutions/Layers/Layers Split Domain to Services.png":
        "The domain layer is split into subdomain components, making a sandwich.",
    "Evolutions/Layers/Layers Split in Two.png":
        "A backend is subdivided into application and domain layers.",
    "Evolutions/Layers/Layers Split to Event-Driven Architecture.png":
        "A backend is subdivided into a pipeline.",
    "Evolutions/Layers/Layers to Backends for Frontends.png":
        "The application layer is split into backends for frontends.",
    "Evolutions/Layers/Layers to Hierarchy.png":
        "The lower layers of a system are subdivided, resulting in a hierarchy.",
    "Evolutions/Layers/Layers to Layers.png":
        "Communication between lower layers is more fine-grained than between higher layers.",
    "Evolutions/Layers/Layers to Polyglot Persistence.png":
        "The database layer is subdivided into specialized databases, resulting in polyglot persistence.",
    "Evolutions/Layers/Layers to Space-Based Architecture.png":
        "The database is migrated to a data grid, resulting in a scalable Space-Based Architecture.",
    "Evolutions/Layers/Layers_ Shard.png":
        "The application and domain layers are independently sharded.",
    "Evolutions/Monolith/Monolith Split Service.png":
        "A service is split from a monolith.",
    "Evolutions/Monolith/Monolith add Database.png":
        "The data of a monolithic system is moved to a database, leaving the business logic stateless.",
    "Evolutions/Monolith/Monolith add Orchestrator.png":
        "An orchestrator is added to a monolithic system, allowing for higher-level client requests.",
    "Evolutions/Monolith/Monolith add Proxy.png":
        "A part of generic functionality of a monolith is moved to a proxy.",
    "Evolutions/Monolith/Monolith to Hexagonal.png":
        "The database, external libraries, and a protocol support component are separated from the business logic and isolated with adapters.",
    "Evolutions/Monolith/Monolith to Instance per Client.png":
        "Each user is allocated a temporary instance of a subsystem which loads their data at the start of the session and persists any changes to the database.",
    "Evolutions/Monolith/Monolith to Interpreter.png":
        "The high-level logic is rewritten as scripts which are run by an interpreter.",
    "Evolutions/Monolith/Monolith to Isolated Shards with Load Balancer.png":
        "Multiple instances of a monolith, each a subset of the system's data, are run behind a sharding proxy.",
    "Evolutions/Monolith/Monolith to Layers - Further 1.png":
        "Backends for frontends over layers, Service-Oriented Architecture, sandwich, layered services, hierarchy, and layers with polyglot persistence.",
    "Evolutions/Monolith/Monolith to Layers - Further 2.png":
        "Layers with plugins, layers with scripts, and Hexagonal Architecture with a layered core.",
    "Evolutions/Monolith/Monolith to Layers.png":
        "A monolith is split into application, domain and database layers.",
    "Evolutions/Monolith/Monolith to Mesh of Shards.png":
        "Several instances of a monolith are run as intercommunicating shards, each of which holds a subset of the system's data.",
    "Evolutions/Monolith/Monolith to Pipeline.png":
        "A monolith is transformed into a pipeline.",
    "Evolutions/Monolith/Monolith to Plugins.png":
        "Plugins customize the monolith's behavior.",
    "Evolutions/Monolith/Monolith to Services - Further 1.png":
        "Services with a proxy, orchestrator, middleware, and a shared database.",
    "Evolutions/Monolith/Monolith to Services - Further 2.png":
        "A scaled service, layered service, cell, and a service that implements Hexagonal Architecture.",
    "Evolutions/Monolith/Monolith to Services.png":
        "A monolith is subdivided into services.",
    "Evolutions/Monolith/Monolith to Shards - Further 1.png":
        "Layers with individual scaling, services with a middleware and individual scaling, and pipeline scaled as a whole.",
    "Evolutions/Monolith/Monolith to Shards - Further 2.png":
        "Space-Based Architecture with replicated data and Shards with multiple orchestrators.",
    "Evolutions/Monolith/Monolith to Stateless Shards with Shared DB.png":
        "A monolith is transformed into stateless instances which run behind a load balancer and access a shared database.",
    "Evolutions/Monolith/Monolith_ Services and Pipeline.png":
        "In services a single component executes a client request while in pipeline there is no use case owner.",
    "Evolutions/Services/Pipeline promote Front Controller.png":
        "The first service of a pipeline subscribes to notifications from other services and thus becomes a front controller.",
    "Evolutions/Services/Pipeline use Orchestrator.png":
        "Adding an orchestrator transforms a pipeline into orchestrated services.",
    "Evolutions/Services/Services add Middleware.png":
        "The communication aspect of services can be covered by a dedicated middleware.",
    "Evolutions/Services/Services add Proxy.png":
        "Generic aspects of services move to a shared proxy.",
    "Evolutions/Services/Services to Sandwich.png":
        "The application and data parts of services are separated from the domain logic and merged into system-wide layers, resulting in a sandwich.",
    "Evolutions/Services/Services to Shared Database.png":
        "The data of individual services is merged into a shared repository.",
    "Evolutions/Services/Services use Orchestrator.png":
        "The application logic is extracted from individual services into a shared orchestrator.",
    "Evolutions/Services/Services_ Cluster.png":
        "Services are grouped into cells, reducing their interdependencies.",
    "Evolutions/Services/Services_ Merge.png":
        "Two services are merged.",
    "Evolutions/Services/Services_ Split.png":
        "A service is split in half.",
    "Evolutions/Shards/Shards - General.png":
        "Scaled layers, services with a middleware, pipeline, plugins, Hexagonal Architecture, and scripts.",
    "Evolutions/Shards/Shards add Load Balancer.png":
        "A sharding proxy relieves clients from the need to find the appropriate shard.",
    "Evolutions/Shards/Shards add Middleware.png":
        "A middleware manages shards and lets them communicate to each other.",
    "Evolutions/Shards/Shards add Shared DB.png":
        "A coupled subset of the system's data is stored in a shared repository, while the bulk of the data is sharded.",
    "Evolutions/Shards/Shards split Shared Service.png":
        "Coupled business logic and data is separated from shards into a shared singletone service.",
    "Evolutions/Shards/Shards to Shared DB.png":
        "The data of shards moves to a shared database. The shards become stateless and are deployed behind a load balancer.",
    "Evolutions/Shards/Shards to Space-Based Architecture.png":
        "The data of the shards moves to a data grid, resulting in a Space-Based Architecture.",
    "Evolutions/Shards/Shards use Orchestrator.png":
        "The high-level logic of shards moves to a shared orchestrator which integrates the data stored within and processed by individual shards.",
    "Heart/Basic.png":
        "Monolith, shards, layers, services, and a pipeline, with cohesive and decoupled components highlighted.",
    "Heart/Extension.png":
        "Services with a middleware, shared repository, proxy, an orchestrator, and a Sandwich Architecture, with cohesive and decoupled components highlighted.",
    "Heart/Features-1.png":
        "Services with a monolithic orchestrator, backends for frontends, an orchestrator per use case, a hierarchical orchestrator, and a layered orchestrator.",
    "Heart/Features-2.png":
        "Services with a shared database and Space-Based Architecture.",
    "Heart/Features-3.png":
        "Services with a middleware, proxy, and backends for frontends.",
    "Heart/Flexibility-1.png":
        "Plugins, Hexagonal Architecture, and a microkernel.",
    "Heart/Flexibility-2.png":
        "An anticorruption layer, open host service, and a CQRS view.",
    "Heart/Fragmented.png":
        "Layered services, services with polyglot persistence, backends for frontends, Service-Oriented Architecture, and Top-Down Hierarchy, with cohesive and decoupled components highlighted.",
    "Heart/Hierarchy.png":
        "The hierarchical decomposition of logic into methods of classes in a service is compared to that of data in a B-tree.",
    "Heart/Implementation.png":
        "Plugins, Hexagonal Architecture, a microkernel, and mesh, with cohesive and decoupled components highlighted.",
    "Heart/Lifecycle.png":
        "A monolith transforming into layered services, whose application layers partially merge and domain layers split, only to finally glue into layers with multiple databases.",
    "Heart/Pain.png":
        "A chart that shows that unstructured code is the least painful solution for a tiny project while something large is unbearable if not decomposed into services.",
    "Heart/Performance-1.png":
        "Stateless instances with a load balancer and a shared database, shards behind a sharding proxy, and replicas behind a load balancer.",
    "Heart/Performance-2.png":
        "Services with polyglot persistence and a cell with a scaled pipeline.",
    "Heart/Performance-3.png":
        "Scaled single-layer nanoservices, microservices, and processing units of Space-Based Architecture.",
    "Heart/Performance-4.png":
        "Whole-system replicas of services with an API gateway, actors running in a distributed framework, and a peer-to-peer mesh.",
    "Heart/Performance-5.png":
        "Shortcuts in the control flow of Model-View-Presenter, Model-View-Controller, layers optimized through business logic injection, and the top-down hierarchy in a control system.",
    "Heart/Size-1.png":
        "Monolith, layers, services, Service-Oriented Architecture, and Cell-Based Architecture.",
    "Heart/Size-2.png":
        "A sandwich, top-down hierarchy, and pipeline.",
    "Intro/3-Tier.png":
        "Frontend, backend, and database layers differ in their scalability, security, and operational costs.",
    "Intro/CQRS with notes.png":
        "A CQRS system in abstractness-subdomain-sharding coordinates with a detailed legend.",
    "Intro/Example-Defined.png":
        "Services with a middleware, services with a shared database, and Model-View-Controller.",
    "Intro/Example-Undefined.png":
        "Two high-level components interact with one low-level component.",
    "Intro/Field Gateway.png":
        "Normal and autonomous operation of a field gateway of a fire alarm system.",
    "Intro/Floppy-Async.png":
        "Asynchronous communication unblocks the system UI and format windows while a driver formats a floppy.",
    "Intro/Floppy-Sync.png":
        "Synchronous communication freezes the system UI and format windows while a driver formats a floppy.",
    "Intro/Modules-1.png":
        "Complexity represented as the number of interconnected nodes.",
    "Intro/Modules-2.png":
        "A module hides a cluster of the original nodes but creates new interface nodes which add to the complexity of the modules that use them.",
    "Intro/Modules-3.png":
        "Some of the interface nodes are grouped to lower the complexity.",
    "Intro/Modules-4.png":
        "Subdividing a complex module with many internal connections results in two complex modules because many new interface nodes are created.",
    "Intro/Modules-5.png":
        "Merging loosely coupled modules only marginally reduces the overall number of nodes in the system.",
    "Intro/Modules-6.png":
        "When a module is hidden inside another module, there is no clear way to expose it to external clients.",
    "Intro/Modules-7.png":
        "The interface of the internal module is duplicated in the interface of the wrapping module.",
    "Intro/Modules-8.png":
        "The internal module itself is duplicated outside of the module which wraps it.",
    "Main/Backends for Frontends.png":
        "Services with backends for frontends.",
    "Main/Hexagonal Architecture.png":
        "Hexagonal Architecture.",
    "Main/Hierarchy.png":
        "Top-down hierarchy.",
    "Main/Layered Services.png":
        "Layered services.",
    "Main/Layers.png":
        "Layered architecture.",
    "Main/Mesh.png":
        "Services communicating through a mesh.",
    "Main/Microkernel.png":
        "Microkernel.",
    "Main/Middleware.png":
        "Services with a middleware.",
    "Main/Monolith.png":
        "Monolith.",
    "Main/Orchestrator.png":
        "Services with an orchestrator.",
    "Main/Pipeline.png":
        "Pipeline.",
    "Main/Plugins.png":
        "Plugins Architecture.",
    "Main/Polyglot Persistence.png":
        "Services with polyglot persistence.",
    "Main/Proxy.png":
        "Services with a proxy.",
    "Main/Sandwich.png":
        "Sandwich Architecture.",
    "Main/Service-Oriented Architecture.png":
        "Service-Oriented Architecture.",
    "Main/Services.png":
        "Services Architecture.",
    "Main/Shards.png":
        "Shards.",
    "Main/Shared Repository.png":
        "Services with a shared repository.",
    "Misc/Diagrams.png":
        "A structural, sequence, and dependency diagrams in NoSQL notation as used throughout the Architectural Metapatterns book.",
    "Misc/Layers of Services.png":
        "Backends for frontends and services with polyglot persistence.",
    "Misc/Orchestrator.png":
        "Control flows in a facade and mediator.",
    "Performance/Hexagonal Architecture.png":
        "A data stream between the adapters of Hexagonal Architecture.",
    "Performance/Hierarchy - optimizations.png":
        "Aggregation of data in mid-level nodes, autonomous decision-making by mid-level nodes, and direct communication between low-level nodes of a hierarchy.",
    "Performance/Hierarchy - speed.png":
        "Comparison of latency for decision-making at various levels of a hierarchy.",
    "Performance/Layered Services - channels.png":
        "Data streams in three-layered services: from data layer to data layer, from domain layer to data layer, and between two domain-level components.",
    "Performance/Layered Services - sharding.png":
        "The use of scaled stateless services and load balancers in layered services.",
    "Performance/Layers-aggregation.png":
        "Aggregation of events from hardware by the lowest layer of a layered system.",
    "Performance/Layers-batching.png":
        "Sending a batch of commands all the way down to the lowest layer of a system.",
    "Performance/Layers-caching.png":
        "Caching the latest known state of the system in its highest layer.",
    "Performance/Layers-injection.png":
        "Moving a part of the business logic from the highest layer to the lowest layer of the system.",
    "Performance/Orchestrator.png":
        "Caching, early response, parallel execution, and direct communication between services as optimization techniques for orchestrated services.",
    "Performance/Plugins-injection.png":
        "Business logic injection in layers and services.",
    "Performance/Sandwich.png":
        "Control and data flow is identical in sandwich and layers.",
    "Performance/Services.png":
        "The performance of services is the best when the request is limited to a single service and the worst when the state of several services needs to be synchronized.",
    "Performance/Shards.png":
        "The performance of shards is the best when the request is limited to a single shard and the worst when the state of several shards needs to be synchronized.",
    "Relations/BFF.png":
        "Backends for frontends over a monolith, layers, shards, and services.",
    "Relations/Hexagonal Architecture.png":
        "Hexagonal Architecture with a monolithic core, layered core, and a cell.",
    "Relations/Hierarchy.png":
        "Orchestrator of orchestrators, middleware of middlewares, and services of services.",
    "Relations/Layers.png":
        "Splitting a layer into services and splitting a service into layers.",
    "Relations/Microkernel.png":
        "Microkernel as a middleware and as an orchestrator; applications of Microkernel Architecture as backends for frontends.",
    "Relations/Middleware.png":
        "Middleware for services, shards, and Service-Oriented Architecture.",
    "Relations/Monolith.png":
        "Intermediary architectures between the monolith and distributed shards, layers, and services.",
    "Relations/Orchestrator.png":
        "Orchestrator for a monolith, layers, shards and services.",
    "Relations/Plugins.png":
        "A monolith with plugins; layers with plugins; a cell with a plugin.",
    "Relations/Polyglot Persistence.png":
        "Polyglot persistence for a monolith, layers, shards, and services.",
    "Relations/Proxy.png":
        "A proxy for a monolith, shards, layers, and services.",
    "Relations/Sandwich.png":
        "Transitions between layers, a sandwich, a Service-Based Architecture, and layered services.",
    "Relations/Services.png":
        "Splitting an orchestrator into backends for frontends.",
    "Relations/Shards.png":
        "Scaling a single service or the entire system.",
    "Relations/Shared Repository.png":
        "A shared repository for services, shards, and Service-Oriented Architecture.",
    "Topologies/Topologies Map.png":
        "A map of system topologies arranged according to the amount of their partitioning into layers and services.",
    "Topologies/Barebone Services.png":
        "Services, three-layered services, a pipeline, and two-layered services.",
    "Topologies/True Monoliths.png":
        "A monolith, shards, and replicas.",
    "Topologies/Layered Services.png":
        "Orchestrated three-layered services and choreographed two-layered services.",
    "Topologies/Ordinary Layers.png":
        "DDD-style layers, layers with polyglot persistence, layers with backends for frontends, and a monolith with a database.",
    "Topologies/Monoliths with Layers.png":
        "A monolith with backends for frontends, managed shards, peer-to-peer mesh, a monolith with a database, and a monolith with polyglot persistence.",
    "Topologies/Monoliths with Plugins.png":
        "A monolith with plugins, Model-View-Controller, and Hexagonal Architecture.",
    "Topologies/Partitioning.png":
        "Technical partitioning into layers, domain partitioning into services, and multiple instances of a system.",
    "Topologies/Hierarchies of Services.png":
        "A Cell-Based Architecture and hierarchical middleware.",
    "Topologies/Other Layered.png":
        "Model-View-Presenter, Onion Architecture, and Sandwich Architecture.",
    "Topologies/Hexagonal Architecture.png":
        "Ports and Adapters and Onion Architecture.",
    "Topologies/Underdeveloped Moduliths.png":
        "A Monolith with libraries and modulith with shared code.",
    "Topologies/Separated Presentation.png":
        "Model-View-Presenter and Model-View-Controller.",
    "Topologies/Scaled Layers.png":
        "A three-tier system, MapReduce, managed shards, scaled service, and a peer-to-peer mesh.",
    "Topologies/Layers of Services.png":
        "Services with polyglot persistence, services with backends for frontends, and Service-Oriented Architecture.",
    "Topologies/Control Patterns.png":
        "A pedestal and microkernel.",
    "Topologies/Plugin Architecture.png":
        "A plugin, library, and extension called by a core.",
    "Topologies/Partially Merged Services.png":
        "A sandwich and modulith with shared code.",
    "Topologies/Services with Extensions.png":
        "Services with a gateway; orchestrated services; services with: an API gateway, backends for frontends, a shared repository, middleware, and polyglot persistence; and of a service mesh.",
    "Variants/1/Actors.png":
        "Actors running over an actor framework.",
    "Variants/1/Application - Derived.png":
        "Backends for frontends between a gateway and a monolithic service; a pipeline with use case logic hardwired into the graph of connections.",
    "Variants/1/Communication - Derived.png":
        "Multiple instances of a communication library represented as a virtual middleware layer.",
    "Variants/1/DDD.png":
        "The four layers of Domain-Driven Design: presentation, application, domain, and infrastructure.",
    "Variants/1/Data - Derived.png":
        "A three-tier system, hierarchical control system, and Space-Based Architecture.",
    "Variants/1/Data - Evolutions.png":
        "A load-balanced service over a database evolves into a monolith with two specialized databases or into a load-balanced stateless service over database replicas with a single leader.",
    "Variants/1/Data Mesh.png":
        "A data mesh builds an extra graph of services that stream and process analytical data.",
    "Variants/1/Distributed Monolith.png":
        "A distributed monolith as three layers of services.",
    "Variants/1/Domain - Derived.png":
        "Services, a sandwich, hierarchy, and Command-Query Responsibility Segregation.",
    "Variants/1/Drivers.png":
        "Applications call a System Call Interface which dispatches their requests to device drivers.",
    "Variants/1/ECB as SOA.png":
        "The boundary, control and entity layers, each subdivided into several services.",
    "Variants/1/ECB.png":
        "The boundary, control and entity layers.",
    "Variants/1/Embedded.png":
        "An embedded system with the following pairs of layers: user interface and human-machine interface, software development kit and hardware abstraction layer, firmware and hardware.",
    "Variants/1/Event-Driven Architecture.png":
        "Event-Driven Architecture as a branched pipeline built from a group of services.",
    "Variants/1/Generic Code - Derived.png":
        "Services, Service-Oriented Architecture, and microservices with sidecars, with components that carry generic code highlighted.",
    "Variants/1/Half-Sync Half-Async.png":
        "A system subdivided into two layers: the upper one with a coroutine per request and the lower one with a generic event handling thread.",
    "Variants/1/Hexagonal Monolith.png":
        "Hexagonal Architecture with adapters between its core and each component the core interacts with.",
    "Variants/1/Interface - Derived.png":
        "An API gateway and backends for frontends.",
    "Variants/1/Interface - Kinds.png":
        "A service wrapped with: a gateway with its API, a user interface, an anticorruption layer, a plugin, and an open host service with a published language.",
    "Variants/1/Lambdalith.png":
        "Instances of a stateless component between a load balancer and a database.",
    "Variants/1/Layer Roles.png":
        "A stack of layers: client or user, interface, application, domain, generic code, communication, data, and operating system and hardware.",
    "Variants/1/Layered Monolith.png":
        "Application, domain, and infrastructure layers.",
    "Variants/1/Microservices.png":
        "Multiple instances of several services connected to their sidecars which are connected to a shared mesh engine. Instances of each service access its single database.",
    "Variants/1/Modular Monolith.png":
        "A diagram of subdomain services.",
    "Variants/1/MonolithAsUnzoomed.png":
        "A Sandwich Architecture looks like a monolith when the details of its internal structure are omitted.",
    "Variants/1/Nanoservices - API Layer.png":
        "Nanoservices dedicated to Get and Post methods between a client and a shared database.",
    "Variants/1/Nanoservices.png":
        "Many nanoservices access a shared database to implement CRUD functionality.",
    "Variants/1/Pipes and Filters.png":
        "A pipeline chaining: source, three filters, and sink.",
    "Variants/1/Proactor.png":
        "A single thread handles messages that belong to several use cases in an interleaved manner.",
    "Variants/1/Reactor - Multiple Threads.png":
        "Two threads, each runs a single request and blocks on accessing an operating system.",
    "Variants/1/Reactor - Single Thread.png":
        "A single thread that blocks on calls to an operating system executes a request and then another request which has to wait in a queue.",
    "Variants/1/Reactor with Extractors.png":
        "In the extraction phase components call each other and add actions to their queues. In the reaction phase they execute the actions from their queues but don't interact. The phases alternate.",
    "Variants/1/Service - Cell.png":
        "Three subservices behind a cell gateway. Two of them share a database.",
    "Variants/1/Service - Hexagonal.png":
        "A core connected to: a protocol adapter, a database abstraction layer with a database behind it, and an adapter with a library behind it.",
    "Variants/1/Service - Layered.png":
        "The integration, core and database layers.",
    "Variants/1/Service - Monolithic.png":
        "A monolithic component.",
    "Variants/1/Service - Scaled.png":
        "Stateless instances between a load balancer and a database; stateful shards behind a sharding proxy.",
    "Variants/1/Service-Based Architecture.png":
        "Three interconnected services, two of which share a database.",
    "Variants/1/Shards - Create on Demand.png":
        "A new stateful instance is created when a new client connects to the system.",
    "Variants/1/Shards - Pool.png":
        "A load balancer connects a new client to a free instance of a stateless backend that accesses a database shared among all the backend instances.",
    "Variants/1/Shards - Replica.png":
        "A load balancer connects a new client to a free replica which propagates the changes made by the client to other replicas.",
    "Variants/1/Shards - Sharding.png":
        "A sharding proxy connects a new client to a shard that contains data for the first letter of the client's name.",
    "Variants/1/Subtypes of Monolith.png":
        "Control flow diagrams for a reactor, proactor, and Half-Sync/Half-Async.",
    "Variants/1/Subtypes of Services.png":
        "A monolithic service, layered service, hexagonal services, scaled service, and a cell interconnected into a single system.",
    "Variants/1/Three-Tier.png":
        "Four instances of the presentation layer accessing two instances of the logic layer accessing a single database.",
    "Variants/1/True Monolith.png":
        "A square that represents a non-modular monolith.",
    "Variants/2/API Composer.png":
        "An API composer calls services in parallel. A Scatter/Gather or MapReduce calls shards in parallel.",
    "Variants/2/API Gateway.png":
        "An API gateway both translates from the client's to the system's protocol and calls services in parallel.",
    "Variants/2/Adapter.png":
        "An adapter between a client and a service provider translates between their protocols.",
    "Variants/2/Blackboard.png":
        "A Blackboard System includes a control which orchestrates knowledge sources which access a blackboard with shared data.",
    "Variants/2/CQRS to Layered Services.png":
        "The single database of a sandwich-like CQRS with a shared database is subdivided into OLTP and OLAP databases, forming layered services.",
    "Variants/2/CQRS.png":
        "A large read and smaller write models between a user interface and database.",
    "Variants/2/Cache.png":
        "A cache proxies requests and remembers responses to shortcircuit the processing of future requests.",
    "Variants/2/Data Grid.png":
        "A layer of scaled processing units each connected to a node of an in-memory database over a data replication engine which communicates with a persistent database through readers and writers.",
    "Variants/2/Dispatcher.png":
        "A dispatcher exposes an interface which merges the interfaces of the services below the dispatcher.",
    "Variants/2/Enterprise Service Bus.png":
        "An Enterprise Service Bus is between the fragmented task and entity layers of Service-Oriented Architecture. It mediates all calls and messages between the system components.",
    "Variants/2/Event Mediator.png":
        "An event mediator calls event processors one by one.",
    "Variants/2/Firewall.png":
        "A firewall lets a request from a good client pass through while requests from a malicious client are blocked. A rate limiter blocks some client requests.",
    "Variants/2/Front Controller.png":
        "A front controller is the first service of a pipeline which receives status notifications from every other service and responds to the client's get status query.",
    "Variants/2/Full Proxy.png":
        "A full proxy mediates all messages between a client and a server.",
    "Variants/2/Half Proxy.png":
        "A half-proxy intercepts only the session establishment request and is transparent to the following in-session communication between the client and server.",
    "Variants/2/Integration Service.png":
        "An integration service is a full-featured service that stands between the client and the remaining services of the system.",
    "Variants/2/Load Balancer.png":
        "A load balancer forwards a client's request to any idle instance of a stateless service. A sharding proxy forwards a client's request to the shard that contains the client's data.",
    "Variants/2/Message Bus.png":
        "A message bus has an adapter per service to allow each service to use its own protocol.",
    "Variants/2/Middleware - Shared Event Store.png":
        "Both persistent event log and shared event store merge the functionality of middleware and shared repository.",
    "Variants/2/Middleware - Structure.png":
        "In middleware each service is co-located with a generic component which may either be a node of a mesh or forward the service's requests to a centralized broker as a proxy.",
    "Variants/2/Multifunctional - Service Mesh.png":
        "Scaled services reside on a shared layer of sidecars which is placed on top of a shared mesh engine. All instances of each service access the service's database.",
    "Variants/2/Multifunctional - Space-Based Architecture.png":
        "Space-Based Architecture comprises the following layers: a messaging grid, a processing grid, scaled processing units, a data grid, a deployment manager, and a persistent database.",
    "Variants/2/Nanoservices.png":
        "Nanoservices form a sandwich-shaped architecture. The upper layer is an API Gateway for an orchestrated system or a gateway for pipelined nanoservices. The lower layer is a shared datastore.",
    "Variants/2/Orchestrator - BFF.png":
        "Each client communicates with its own orchestrator.",
    "Variants/2/Orchestrator - Closed.png":
        "An orchestrator mediates every request from every client.",
    "Variants/2/Orchestrator - Hierarchy.png":
        "A top-level orchestrator communicates with lower-level Orchestrators each of which manages a group of services.",
    "Variants/2/Orchestrator - Layered.png":
        "A simple orchestrator calls services or a complex orchestrator, which also calls the same services.",
    "Variants/2/Orchestrator - Monolythic.png":
        "An orchestrator communicates with several services.",
    "Variants/2/Orchestrator - Open.png":
        "An orchestrator mediates a multi-step client request while it is transparent to simpler requests.",
    "Variants/2/Orchestrator - SOA.png":
        "There are several orchestrators which use the same set of services.",
    "Variants/2/Orchestrator - Scaled.png":
        "Multiple instances of a stateless orchestrator are behind a load balancer and they persist their actions into a dedicated shared database.",
    "Variants/2/Process Manager.png":
        "The orchestrator calls several services one by one.",
    "Variants/2/Proxy placement - Ambassador.png":
        "An ambassador runs on the client side and translates the client's protocol into the one in use with the service.",
    "Variants/2/Proxy placement - Sidecar.png":
        "A sidecar is co-located with the services and translates from the client's protocol to the service's API.",
    "Variants/2/Proxy placement - Standalone.png":
        "A standalone proxy is placed between a client and a layer of services.",
    "Variants/2/Saga.png":
        "An atomically consistent saga rolls back changes after a failed write. An eventually consistent saga retries the failed write till it succeeds.",
    "Variants/2/Service-Based Architecture.png":
        "A sandwich-like topology with user interface, a layer of domain services, and a shared database.",
    "Variants/2/Service-Based to Layered Services.png":
        "A sandwich-like topology with shared user interface and database is gradually transformed into layered services.",
    "Variants/2/Shared Database - Event Log.png":
        "A service posts a message to a shared event log which both persists the message to a shared event store and forwards the message to other services.",
    "Variants/2/Shared Database.png":
        "Several services access a shared database and optionally communicate with each other directly.",
    "Variants/2/Shared files.png":
        "An algorithm processes a batch of input files and writes output files. Its output becomes an input for another algorithm. The algorithms make a pipeline.",
    "Variants/2/Shared memory.png":
        "Areas of shared memory (ring buffers) between two processes make a pair of event channels.",
    "Variants/2/Sidecars.png":
        "A proxy between a service and its client; one between a service and a middleware; an extension aside of a service; a utility layer below a service.",
    "Variants/2/Stamp Coupling.png":
        "A message collects pieces of data while passing through a pipeline.",
    "Variants/2/User Interface.png":
        "A user interface stands between a human and software. It receives mouse input and produces output on a display.",
    "Variants/2/Vertical Slice Architecture - Basic.png":
        "Each screen is connected to several backend slices, all of which share a database.",
    "Variants/2/Vertical Slice Architecture - Real.png":
        "In complex systems slices are grouped into features which are further composed into services. Each feature or service is encapsulated with an API. There are shared components.",
    "Variants/3/BFF - API gateways.png":
        "Each API gateway in the backends for frontends layer both adapts its client's protocol and orchestrates the services of the domain layer.",
    "Variants/3/BFF - Event mediators.png":
        "Each event mediator in the backends for frontends layer orchestrates the services of the domain layer.",
    "Variants/3/BFF - Gateways + Orchestrators.png":
        "In each pair in the backends for frontends layer the gateway adapts its client's protocol while the orchestrator calls the services of the domain layer.",
    "Variants/3/BFF - Gateways.png":
        "Each gateway in the backends for frontends layer adapts its client's protocol and calls the services of the domain layer.",
    "Variants/3/BFF - Orchestrators.png":
        "Each orchestrator in the backends for frontends layer calls the services of the domain layer.",
    "Variants/3/CQRS - pipeline view.png":
        "In CQRS data streams from the client to the write backend, then to the OLTP database, to the OLAP database, to the read backend and, finally, returns to the client.",
    "Variants/3/CQRS - subtypes.png":
        "In CQRS the OLAP databases receive data from the OLTP database or from events originating in the write backend. Alternatively, the read and write backends may share a database.",
    "Variants/3/CQRS.png":
        "Write requests from a client go to the write backend and OLTP database which feeds OLAP databases. Read requests go to the scaled read backend and the scaled OLAP database.",
    "Variants/3/Cache-Aside.png":
        "A cache hit only reads from the cache; a cache miss reads from the cache, reads from the database, and writes to the cache; a write writes to the database and to the cache.",
    "Variants/3/Cell-Based Architecture.png":
        "Cells of different kinds communicate with each other through cell gateways.",
    "Variants/3/DOMA.png":
        "There are five layers: segmented gateways, segmented presentation, segmented product made of cells, segmented business made of cells, and monolithic infrastructure.",
    "Variants/3/Distributed Monolith.png":
        "There are three segmented layers: tasks, services and infrastructure. Each component of a layer accesses multiple components in layers below it.",
    "Variants/3/Enterprise SOA.png":
        "An Enterprise Service Bus interconnects multilayered segmented subsystems each using its own protocol.",
    "Variants/3/Hierarchy - Bottom-up.png":
        "An integration middleware interconnects the middlewares of two systems.",
    "Variants/3/Hierarchy - Top-down.png":
        "A single component calls two components in the layer below it, each of which calls two or three lower-level leaf components.",
    "Variants/3/Historical Data.png":
        "A service works with an operational database. An archiver reads from the operational database and writes to an archive. An analyst reads from both the archive and operational database.",
    "Variants/3/Memory Image.png":
        "At startup a service reads from an event store and writes to a memory image. At runtime it reads from the memory image and updates both the memory image and event store.",
    "Variants/3/PAC.png":
        "Both Presentation-Abstraction-Control and Hierarchical Model-View-Controller are top-down hierarchies with three-component nodes, which share a database in the second pattern.",
    "Variants/3/PP - Derived Storage.png":
        "A derived database is fed data from the main database, from an indexer which scans the main database, from application events, or from events originating with another service.",
    "Variants/3/PP - File Storage.png":
        "A backend reads page templates while a frontend reads content from a content delivery network.",
    "Variants/3/PP - Private and Shared.png":
        "A subset of data shared between shards and between services.",
    "Variants/3/PP - Specialized.png":
        "A service which uses both SQL and NoSQL databases.",
    "Variants/3/Query Service.png":
        "Several services both stream updates and query data from a shared query service.",
    "Variants/3/Read-only Replica.png":
        "An instance of a backend writes to a leader database which streams updates to database replicas. Other backend instances read from the replicas.",
    "Variants/3/Reporting DB and CQRS View.png":
        "A service reads from a CQRS view which aggregates updates streamed by another service. An analyst queries a reporting database which aggregates a stream of events from the main database.",
    "Variants/3/SOA - AUTOSAR.png":
        "User applications run on top of a system-wide Virtual Functional Bus which communicates to various services that run on different chips in the system.",
    "Variants/3/Search Index.png":
        "An external index receives events from the main datastore. A service queries the external index to find ids of specific records which it later reads from the main database.",
    "Variants/3/Three-Layered Services.png":
        "In three-layered services the application layer of every service calls the domain layer of its service and the application layers of other services.",
    "Variants/3/Two-Layered Services.png":
        "The domain-level components of two-layered services participate in multiple pipelines and access their service's databases.",
    "Variants/4/AUTOSAR classic.png":
        "AUTOSAR Classic defines three segmented layers: applications, runtime environment with a shared Virtual Functional Bus, and basic software with generic and hardware-specific services.",
    "Variants/4/Actors.png":
        "Each actor reads from its message queue and writes to other actors' message queues.",
    "Variants/4/Addin.png":
        "An addin is hosted inside a system and implements a part of its control flow.",
    "Variants/4/Addon.png":
        "An addon is a layer between a system and its client. It translates a single client request into multiple calls to the underlying system.",
    "Variants/4/Ambassador Plugin.png":
        "An ambassador plugin is a part of one service hosted inside another service. When called, it may consult its origin service or make independent decisions.",
    "Variants/4/Cell - Basic - Evolutions.png":
        "A layered system transforms into a sandwich-based cell. A group of stand-alone services is aggregated into a cell behind a cell gateway.",
    "Variants/4/Cell - Basic - Subtypes.png":
        "A Cell with a sandwich, services, and a pipeline.",
    "Variants/4/Cell - Full-Featured - Plugins.png":
        "Injecting a part of a cell's business logic into another cell as an ambassador plugin improves performance by avoiding expensive intercell calls.",
    "Variants/4/Cell.png":
        "Several intercommunicating subservices are wrapped with a cell gateway that receives client requests, adapters for outgoing communication, and a plugin.",
    "Variants/4/Config file.png":
        "A configurator runs at a system's startup, reads a configuration file, and sets up a system of services.",
    "Variants/4/Extension.png":
        "An extension is called as a high-level part of a system's use case.",
    "Variants/4/Framework.png":
        "A framework is a facade between a user application and several lower-level components.",
    "Variants/4/Hexagonal - Adapters with Components.png":
        "Adapters co-located with external components translate a single message from the core into multiple calls to the adapted components.",
    "Variants/4/Hexagonal - Adapters with the Core.png":
        "Adapters for external services and a shared database are co-located with the core.",
    "Variants/4/Hexagonal - Driven.png":
        "The core uses adapters to call a database, a library, and an external service.",
    "Variants/4/Hexagonal - Driving and Driven.png":
        "The system's core is isolated with adapters for the following communication: data stream, REST, and SSH inputs; database and library access; publish/subscribe output stream.",
    "Variants/4/Hexagonal - Driving.png":
        "A component provides an API which is called by a GUI adapter for a system's user, a REST adapter for a web application, and a gRPC adapter for a software client.",
    "Variants/4/Hexagonal - Full Isolation.png":
        "A system with its core fully isolated by adapters from both inputs and outputs. The core depends only on its own interfaces.",
    "Variants/4/Interpreter.png":
        "Each script runs over its instance of an interprester. All the interpreters share a set of libraries.",
    "Variants/4/Layered Hexagonal.png":
        "Control flows for changing an entity in puristic Domain-Driven Design, pragmatic Domain-Driven Design, and Onion Architecture.",
    "Variants/4/Leaf-Spine.png":
        "Each server of a datacenter is connected to a leaf node. Each leaf communicates with every spine node.",
    "Variants/4/MVC - subtypes.png":
        "MVC with a dedicated view-controller pair for each widget, ADR and RMR where the action calls the responder, Model 2 with an orchestrating controller, and a game development engine.",
    "Variants/4/MVC.png":
        "The control flow in Model-View-Controller starts with mouse events handled by the controller which calls the model which calls the view which updates the display.",
    "Variants/4/MVP - subtypes.png":
        "MVP with a view-presenter pair for each screen, MVA with different adapters for different kinds of users, MVVM with data in ViewModel, and simple Document-View and Model 1.",
    "Variants/4/MVP.png":
        "The control flow of Model-View-Presenter is a loop that starts with an OS GUI, is handled by the view, passes to the presenter, then down to the model, and all the way back to the OS.",
    "Variants/4/Monolithic Hexagonal.png":
        "Adapters of the Hexagonal Architecture translate between the interfaces of its core and those of the adapted external components.",
    "Variants/4/OS.png":
        "Each application communicates with its runtime interfacing the shared operating system kernel which communicates with device drivers that adapt hardware components.",
    "Variants/4/P2P.png":
        "Each application is connected to a node of a mesh. The nodes find each other's addresses in a registry and then communicate directly.",
    "Variants/4/Pedestal.png":
        "A pedestal has a control layer mediating hardware drivers which wrap each hardware component. An operating system adds a kernel between the drivers and an application that uses them.",
    "Variants/4/Plugins.png":
        "Several low-level plugins are called by a use case running in a system.",
    "Variants/4/Saga engine.png":
        "A saga engine calls several services while executing multiple short-lived sagas.",
    "Variants/4/Service Mesh.png":
        "A service mesh comprises services each of which is connected to a sidecar connected to a mesh node. The mesh nodes communicate with a monitoring and control infrastructure.",
    "Variants/4/Space-Based Architecture.png":
        "Each processing unit is connected to a node of a data grid. The nodes directly exchange data updates and store them into a persistent database via a writer. There is also a reader to initiate nodes.",
    "Variants/4/Virtualizer.png":
        "A virtualizer stands between user applications and several instances of an operating system each running on a separate computer.",
    "Web/4Kinds.png":
        "Control, interactive, streaming, and computational systems.",
    "Web/About.png":
        "There are too many patterns!",
    "Web/Ambiguous.png":
        "Various systems called monoliths.",
    "Web/Backends for Frontends.png":
        "Backends for Frontends.",
    "Web/Choreography.png":
        "A client passing a request to a pipeline of three services and receiving a response from it.",
    "Web/Communication.png":
        "A client above three services with question marks between the components.",
    "Web/Comparison.png":
        "Services sharing a dataset, a pipeline, dependency inversion in an operating system with device drivers, and an adapter between a client and a service.",
    "Web/Complexity.png":
        "Three components each encapsulating a graph of nodes.",
    "Web/DI.png":
        "Polymorphic device drivers in an operating system.",
    "Web/Forces.png":
        "Mssaging in a three-layered system with the lower layer making multiple calls to hardware.",
    "Web/Heart.png":
        "The pain level of maintaining a project depends on the project's size, with different architectures being optimal for different project sizes.",
    "Web/Heart2.png":
        "Decoupling between internally cohesive services.",
    "Web/Heart3.png":
        "Layers, services, a hierarchy, and a pipeline.",
    "Web/Hexagonal Architecture.png":
        "Hexagonal Architecture with adapters between its core and input, output, database, and libraries.",
    "Web/Hierarchy.png":
        "A hierarchy with three layers. There is one component in the top layer, two components below it, and five components in the lowest layer.",
    "Web/Indirection.png":
        "A client accessing a service through an adapter.",
    "Web/Latency.png":
        "The first component of a pipeline immediately responds to the client.",
    "Web/Layered Services.png":
        "Three-layered services.",
    "Web/Layers.png":
        "A system with three layers: application, domain, and database.",
    "Web/Life cycle.png":
        "A cycle with the following architectures: monolith, layers, layered services, a sandwich cell interacting with orchestrated layered services, and layers with two databases.",
    "Web/Mesh.png":
        "Applications connected through a mesh.",
    "Web/Metapatterns.png":
        "Abstraction, subdomain, and sharding axes with the following text between them: your pattern here.",
    "Web/Microkernel.png":
        "Aplications running over a microkernel.",
    "Web/Middleware.png":
        "Services connected through a middleware.",
    "Web/Monolith.png":
        "A monolithic system that blends application, domain rules, generic code, and data in a single component.",
    "Web/Orchestration.png":
        "A client that calls an orchestrator which calls three services one by one.",
    "Web/Orchestrator.png":
        "Orchestrated services.",
    "Web/Pipeline.png":
        "A pipeline made from input, three processing steps, and output.",
    "Web/Pipelineliness.png":
        "A client passing data to a service, which passes it to its database, which passes it to another service's database, from which it goes to the other service, and back to the client.",
    "Web/Plugins.png":
        "Plugins Architecture.",
    "Web/Polyglot Persistence.png":
        "Polyglot Persistence.",
    "Web/Proxy.png":
        "A proxy between a client and services.",
    "Web/Read-write.png":
        "Read and write requests go to different databases.",
    "Web/Real-world.png":
        "Three services with queues of people and luggage above a transport layer with train stations and trains.",
    "Web/Sandwich.png":
        "Sandwich Architecture.",
    "Web/Service-Oriented Architecture.png":
        "Service-Oriented Architecture comprises layers of services.",
    "Web/Services.png":
        "Services Architecture.",
    "Web/Shards.png":
        "Interconnected shards.",
    "Web/Shared Repository.png":
        "Services accessing a shared repository.",
    "Web/Shared data.png":
        "A client communicating with a service which writes to a shared data layer, causing data processing by two other services.",
    "Web/Sharing.png":
        "Two services with private databases and one database shared by the services.",
    "Web/Topologies.png":
        "A monolith, layers, plugins, a hierarchy, and services in a system of coordinates that shows partitioning into layers and subdomains.",
}


if __name__ == "__main__":
    print()
    print("META DESCRIPTIONS AND LENGTHS (LIMIT 160):")
    for d in meta_descriptions.values():
        length = len(d)
        assert length <= 160, d
        print(f"{d}\t{length}")
    print()
    print("IMAGE ALTS:")
    for d in image_descriptions.values():
        print(d)
    print()