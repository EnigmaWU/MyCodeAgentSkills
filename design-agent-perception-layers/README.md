# design-agent-perception-layers

## Overview
WHEN/WHERE/WHO: [Scheduling: Use when designing the context-gathering tools (Abilities) for an autonomous agent, especially when mixing fast APIs and slow UI interactions.]
HOW: [Structural: Use this SKILL to separate "Fast Thinking" (API queries) from "Slow Thinking" (UI vision tools), forcing the agent to use the fastest possible method for perception.]
WHY: [Scheduling: Agents interacting with UIs are slow, expensive, and brittle. Blended perception layers optimize token usage and execution speed by relying on underlying APIs for context.]

## Usage
Trigger this skill to execute the defined workflow. See `SKILL.md` for specific triggers and inputs.

## Structure
- [SKILL.md](./SKILL.md): The core workflow and definition of the skill.
