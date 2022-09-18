# CSC-370: Database Systems

## Course Overview
This course provides an overview of a relational database management system (RDBMS), from modelling the world and designing a database to querying the data and optimising performance in a manner that maintains the critical ACID properties of a database. The course will include elements of software engineering, theoretical computer science, programming, and computer systems.

## Topics
The course will consist of four modules, which each depend on the prior module. The list of modules and associated topics include:

    1. Logical Database Design with the Relational Data Model
        • The Relational Data Model
        • Basic Relational Algebra
        • Data Dependencies and Constraints
        • Normalisation
    2. Conceptual Database Design with the Entity-Relationship Model
        • Entity-Relationship Diagrams (ERD's)
        • Principles of good design
        • Mapping between ERD's and the relational data model
    3. Interacting with relational databases
        • Mathematically expressing the logic of complex queries (using a logic-based programming language called Datalog)
        • Writing queries in SQL (the de-facto standard declarative language for relational databases) to create databases, manipulate content, and perform data analysis
        • ACID properties, including transactions and isolation levels to support concurrency
        • Interfacing with relational databases using connectors like JDBC [optional content subject to the course's pace]
    4. Query Processing & Storage
        • The I/O Computational Model
        • Algorithms and data structures for efficiently computing query results
        • Physical and logical query plans expressed with relational algebra parse trees
        • Query cost estimation and query plan optimisation
        • Recovery, logging, redundancy, and resilience
        
## Course Objectives And Learning Outcomes
    • Database design: how can we describe the world in terms of data?
    • Data analysis: how can we answer questions about the world in terms of questions on such data?
    • Concurrency and robustness: how does the database management system (DBMS) allow multiple users to query and modify the same data? What happens when there is a system failure?
    • Efficiency and scalability: how does the DBMS store large amounts of data and process them efficiently?

