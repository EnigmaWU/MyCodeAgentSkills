# Design Architecture Viewpoints

An agent skill for defining and documenting software architectures using **Viewpoints and Perspectives** from *Software Systems Architecture* by Nick Rozanski and Eóin Woods.

## What Is This

Developers often write architecture documentation solely from their own technical perspective, neglecting operators, maintainers, support staff, and business acquirers. This skill guides coding agents to design and verify architectures from diverse stakeholder views (Functional, Deployment, Operational, Concurrency, etc.) and apply cross-cutting quality perspectives (Security, Performance, Availability, Evolution).

## Directory Structure

```text
design-architecture-viewpoints/
  ├── SKILL.md                                 # Level-1: Main skill workflow (COMPLEX tier)
  ├── references/
  │   └── Software systems architecture.pdf    # Original textbook PDF (user-provided)
  └── details/                                 # New folder for structured references
      ├── viewpoints-and-perspectives-reference.md  # Level-2: Summary outline
      ├── functional-viewpoint-details.md      # Level-3: Detailed Ch 17 Functional Viewpoint guide
      ├── deployment-viewpoint-details.md      # Level-3: Detailed Ch 21 Deployment Viewpoint guide
      ├── security-perspective-details.md      # Level-3: Detailed Ch 25 Security Perspective guide
      └── performance-perspective-details.md   # Level-3: Detailed Ch 26 Performance Perspective guide
```

## Why This Method Matters

When scaling complex software systems, conflicts often arise between different architectural dimensions (e.g., code structure vs process threading vs VM topology). This skill helps coding agents resolve these issues through:
1. **Stakeholder & Scenario Discovery**: Defining who the stakeholders are (Acquirers, Developers, Operators, Users, etc.) and what scenarios (Use Case, Growth, Exploratory) matter to them.
2. **Multi-View Cataloging**: Drafting distinct views (e.g., deployment VPC layout, database concurrency locks, developer directory trees).
3. **Cross-Cutting Perspectives**: Layering security, performance, availability, and evolutionary checks on top of each view.
4. **Inter-View Consistency Checking**: Enforcing pairwise checks to guarantee that component mappings align perfectly across Functional, Development, Concurrency, and Deployment views.

## Usage

When structuring architecture documentation or performing system designs, invoke this skill using trigger phrases such as:
* *"document the viewpoints of this system"*
* *"create a deployment viewpoint diagram"*
* *"perform an inter-view consistency check on this architecture"*

The agent will read the viewpoint guides and checksheets in `details/` to build internally consistent, stakeholder-aligned architecture specs.
