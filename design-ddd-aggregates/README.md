# design-ddd-aggregates

## Overview
WHEN/WHERE/WHO: Developers, database designers, or agents designing the object-oriented domain layer of a system.
HOW: Use this SKILL to strictly apply Vaughn Vernon's 4 Rules of Aggregate Design to shape entities and value objects.
WHY: Most developers build massive "God Objects" (e.g., an Order object containing all OrderItems, Customer details, and Shipping history). This causes concurrency conflicts and unscalable database transactions. Designing small aggregates referenced by ID ensures transactional safety and high performance.

## Usage
Trigger this skill to execute the defined workflow. See `SKILL.md` for specific triggers and inputs.

## Structure
- [SKILL.md](./SKILL.md): The core workflow and definition of the skill.
