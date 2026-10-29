# Dishant Sharma - Verified Knowledge Base

Sources: Dishant's resume ("Dishant Sharma - Senior Software Engineer, Fullstack") and his LinkedIn profile export.
This is the only source of truth about Dishant. Do not state facts about him that are not in this document.

## Contact & Links

* Full name: Dishant Sharma
* LinkedIn: https://www.linkedin.com/in/dishant-sharma-849193158
* Email: dishantsharma0903@gmail.com
* Phone: +91-8283861390
* LeetCode: https://leetcode.com/u/no_cheating/
* Location: Vapi, Gujarat, India (resume). LinkedIn lists Gurugram, Haryana, India.

## Headline & Summary

* Resume title: Senior Full Stack Software Engineer
* LinkedIn headline: Software Engineer II | Full-Stack (React, Node, Java) | Elasticsearch Expert | Building Scalable Search Engines & High-Performance APIs for 50M+ Records

Resume summary: Senior Full Stack Software Engineer with 4.6+ years of experience designing and delivering scalable web applications, distributed backend systems, AI-powered platforms, and enterprise search solutions. Strong focus on backend architecture, authentication, API design, performance optimization, and cloud-native development. Engineered secure authentication systems, semantic search platforms supporting 50M+ indexed records, and AI-driven applications using Retrieval-Augmented Generation (RAG) and Sentence Transformers. Reduced API latency by over 80% and improved search performance by 40%.

LinkedIn summary: Full-Stack Software Engineer specializing in search infrastructure (Elasticsearch/OpenSearch) and scalable MERN/Java applications. Recently engineered a custom tokenizer that secured $10K+ in enterprise contracts and optimized APIs to handle 50M+ records.

## Skills

* Languages: Java (core Java only), JavaScript, TypeScript, Python, SQL
* Frontend: React.js, Next.js, Angular, Redux Toolkit, HTML5, CSS3, Tailwind CSS, Material UI
* Backend: Node.js, Express.js, FastAPI, Django, REST APIs
* AI / ML: RAG, Sentence Transformers, Vector Search, Semantic Search, LLM Applications, Prompt Engineering, Ollama
* Databases: PostgreSQL, MongoDB, Redis, Supabase
* Search: Elasticsearch, OpenSearch, Kibana
* Infrastructure & observability (from experience): Docker, Kubernetes, microservices, Jaeger, OpenTelemetry
* Security (from experience): JWT, CSRF protection, session management, role-based access control, refresh-token handling
* LinkedIn top skills: Front-End Development
* Java scope: Dishant's Java experience is core Java. When asked about Java, say only that he works with core Java. Do not list specific Java sub-topics, do not tie Java to any particular project, and do not mention Spring Boot, Spring Framework, Hibernate, or any other Java framework (not even to say he could learn them). If asked directly about a Java framework, say it is not part of his listed skill set.

## Certifications

* MongoDB - 100th percentile (LinkedIn)

## Experience

### Meril Life Sciences (Nuvo AI) - Software Engineer II (LinkedIn title: SDE)
December 2024 - Present | Vapi, Gujarat, India

Works on AI-driven healthcare and genomic research platforms.

* Engineered scalable backend services using FastAPI and Node.js for AI-driven healthcare applications with a modular service architecture.
* Designed and optimized Elasticsearch/OpenSearch indexing pipelines for 50M+ biomedical records, improving search performance by 40%.
* Implemented Redis caching, reducing average API latency from 1.2 seconds to about 200 ms.
* Architected a custom authentication and session platform using FastAPI, PostgreSQL, Supabase, JWT, CSRF validation, and Snowflake-based distributed session IDs.
* Built centralized auth APIs aggregating user, workspace, project, and role metadata into a single request.
* Designed authorization workflows with server-side session validation, token invalidation, and role-based access control.
* Led a 6-month migration of core auth and data access functions to microservices (Docker, Kubernetes, FastAPI), increasing release frequency by 60% across 8+ production services.
* Engineered high-availability user management modules with Ruby on Rails for enterprise authentication microservices.
* Launched a multi-tenant Help Centre platform in 4 months (FastAPI, PostgreSQL, Redis) serving 10K+ users monthly and cutting support tickets by 35%.
* Integrated Kibana dashboards with OpenSearch clusters to monitor production API health and error trends.
* Mentored junior developers through architecture discussions, code reviews, and onboarding (LinkedIn: improved onboarding efficiency by 50%).

### Indian Institute of Technology, Kanpur - Full Stack Engineer
February 2025 - March 2025 | Kanpur, Uttar Pradesh, India

* Worked for Meril on an internal project from the IIT Kanpur office.

### Grazitti Interactive - Software Development Engineer / Full Stack Engineer
Total tenure 2 years 10 months | Panchkula, Haryana, India
LinkedIn roles: Software Engineer (October 2021 - July 2024) and Full Stack Engineer (April 2022 - July 2024)

* Built reusable React.js and TypeScript component libraries that standardized UI development across multiple enterprise applications.
* Developed workflow-driven applications with React, Redux, and REST APIs; developed and maintained MERN stack applications for enterprise clients.
* Designed Elasticsearch queries, custom analyzers for biomedical terminology, and indexing strategies, improving search accuracy by 30%.
* Refactored frontend architecture (code splitting, lazy loading, asset optimization), reducing page load time by 20%.
* Migrated data pipelines from R to Python/FastAPI, cutting processing time by 35%.
* Improved asynchronous request handling, increasing application throughput by 35%.
* Integrated backend APIs using Node.js and Express and designed API contracts with backend engineers.
* Built reusable form engines, validation utilities, and shared UI modules used across projects.
* Implemented distributed tracing with Jaeger and OpenTelemetry across 15+ Node.js microservices over 12 months, reducing incident resolution time by 25%.
* Conducted security and penetration testing to identify vulnerabilities.
* Worked in Agile sprints with product managers, UX designers, and QA; took part in code reviews and production debugging.

### Freelance React Developer (Independent Client Projects)
April 2020 - September 2021

* Built single-page applications with React.js (Hooks), JavaScript, HTML5, and CSS3.
* Built UI components, client dashboards, authentication flows, and REST API integrations.
* Optimized rendering with memoization, efficient state management, and lazy loading.
* Worked directly with clients on requirements, performance, and UX improvements, and maintained production deployments.

### Earlier Roles (LinkedIn)

* Webomaze Technologies Private Limited - Search Engine Optimization Analyst (March 2020 - May 2020), Panchkula, Haryana
* Click Labs - Unity Game Development (July 2019 - March 2020)
* Click Labs - Digital Marketing Intern (August 2019 - February 2020), Panchkula: managed a SaaS product, ran online marketing campaigns, social media, landing page design, competitor analysis, client case studies, and product articles
* Dialabank.com - Web Content Writer (June 2019 - July 2019), Chandigarh Area
* Freelance tech and non-tech Content Writer (March 2017 - March 2021)
* Lionbridge - Crowd sourcing (2018 - March 2020) and Social Media Evaluator (2017 - March 2020)
* Ethical Hacker, online (January 2012 - June 2019): bug bounties and finding vulnerabilities

## Projects

### AI Resume Intelligence Platform (this portfolio assistant)

* Full-stack RAG pipeline using Next.js, FastAPI, and Sentence Transformers for semantic retrieval over resume content.
* Vector similarity search with configurable confidence thresholds to reduce hallucinations.
* Guardrails restricting the LLM to retrieved resume context.
* Modular ingestion, embedding, retrieval, and response orchestration; embedding caching for low latency.
* React chat interface with streaming responses and conversation history.

### Custom Authentication & Session Engine

* Custom auth layer on Supabase GoTrue and PostgREST using FastAPI, bypassing SDK limitations.
* Server-side session management with Snowflake-generated IDs beyond stateless JWT.
* JWT validation, CSRF protection, refresh-token handling, and server-side token invalidation.
* Centralized /me endpoint aggregating auth, workspace, project, and role metadata in one query.
* Containerized with Docker.

### Enterprise Search Infrastructure

* Elasticsearch/OpenSearch indexing pipelines for 50M+ records across biomedical repositories.
* Tuned analyzers, mappings, and scoring, increasing search accuracy by 30%.
* Redis caching for frequent searches, reducing latency by over 80%.
* Optimized query composition, pagination, and aggregations for concurrent workloads.

## Achievements

* Custom tokenizer that secured $10K+ in enterprise contracts (LinkedIn).
* Search systems handling 50M+ records.
* API latency reduced from 1.2s to ~200ms with Redis.

## Education

* Sri Guru Gobind Singh College, Sector-26 - Bachelor of Science, Computer Science (2016 - 2019)
* Chitkara University - Bachelor of Engineering (BE), Computer Science (2015 - 2016)

