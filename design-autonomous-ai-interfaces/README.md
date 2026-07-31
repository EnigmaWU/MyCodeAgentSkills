# design-autonomous-ai-interfaces

## Overview

WHEN/WHERE/WHO: Product designers, UX researchers, architects, and AI agents should use this skill when asked to design an autonomous AI interface, agentic product UX, AI copilots that plan or act, human-in-the-loop controls, AI workflow checkpoints, or interfaces for creative and autonomous AI systems.

HOW: Use this COMPLEX SKILL to frame user intent and autonomy level, map capability and orchestration, design input/context capture, expose planning and permissions, manage progress/checkpoints/recovery, shape outputs for verification and onward action, and validate the design against shared-control criteria.

WHY: Autonomous AI products can become opaque, over-trusting, or over-controlling when input, computation, output, and agent action are not designed as one loop. This skill keeps users oriented, empowered, and able to verify or redirect the system.

## Usage

Use this skill for requests such as:

- Design an autonomous AI interface.
- Create an agentic UX flow with checkpoints and rollback.
- Design a human-in-the-loop copilot workflow.
- Add visible planning, permission prompts, and progress feedback to an AI agent.
- Evaluate whether an AI output experience is grounded, verifiable, and actionable.

Do not use it for backend-only agent implementation, prompt tuning alone, generic UI polish, or ordinary non-agentic chat copy unless the user-facing AI control model is part of the request.

## Structure

- [SKILL.md](./SKILL.md): Core workflow and validation gate.
- [details/principles.md](./details/principles.md): Core principles and control-loop model.
- [details/intent-capability-orchestration.md](./details/intent-capability-orchestration.md): Capability discovery and orchestration guidance.
- [details/input-patterns.md](./details/input-patterns.md): Intent capture patterns.
- [details/agentic-workflow-patterns.md](./details/agentic-workflow-patterns.md): Planning and delegation patterns.
- [details/progress-checkpoints-permissions.md](./details/progress-checkpoints-permissions.md): Latency, permissions, checkpoints, and rollback.
- [details/output-validation-and-recovery.md](./details/output-validation-and-recovery.md): Output, verification, and recovery guidance.
- [details/validation-checklist.md](./details/validation-checklist.md): Scenario review checklist.

## Source Shape

This skill condenses book-derived guidance on AI interface design into an executable workflow. The source material is not required during normal use because the operational rules are captured in the skill and detail files.
