# Architectural Drivers Document

## 1. Design Purpose
*What is the objective of this design effort? (e.g., Produce a greenfield architecture, evaluate an existing system, extend a legacy system).*

- **Purpose:** [Insert purpose here]

## 2. Primary Functionality
*What are the core use cases the system must support?*

- **UC1:** [Use case description]
- **UC2:** [Use case description]
- **UC3:** [Use case description]

## 3. Constraints
*What are the unchangeable limitations placed on the design?*

- **Technical Constraint:** [e.g., Must use PostgreSQL]
- **Business Constraint:** [e.g., Budget is capped at $500/month]
- **Organizational Constraint:** [e.g., Must integrate with the legacy CRM team]

## 4. Architectural Concerns
*What are the internal goals of the engineering team?*

- **Concern 1:** [e.g., Implement an automated CI/CD pipeline]
- **Concern 2:** [e.g., Establish coding standards across microservices]

## 5. Quality Attribute Scenarios
*Convert vague non-functional requirements into testable 6-part scenarios.*

### QA1: [Quality Attribute Type, e.g., Availability]
- **Source of Stimulus:** [e.g., Internal monitoring system]
- **Stimulus:** [e.g., Detects that the primary database has crashed]
- **Artifact:** [e.g., The Database Cluster]
- **Environment:** [e.g., Under normal operation]
- **Response:** [e.g., System fails over to the replica database and alerts the admin]
- **Response Measure:** [e.g., Failover completes in <5 seconds with zero data loss]

### QA2: [Quality Attribute Type, e.g., Performance]
- **Source of Stimulus:** [e.g., 10,000 concurrent users]
- **Stimulus:** [e.g., Initiate a search query]
- **Artifact:** [e.g., The Search Service]
- **Environment:** [e.g., Peak load conditions]
- **Response:** [e.g., Queries are processed and results returned]
- **Response Measure:** [e.g., 99th percentile response time is <200ms]
