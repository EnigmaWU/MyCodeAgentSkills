# Intent, Capability, and Orchestration

## Capability Mapping

Create a simple map before designing screens:

| User need | AI capability | Required context | Tool or data source | User-visible control | Limit or fallback |
| --- | --- | --- | --- | --- | --- |
| What the user wants done | What the system can actually do | What the system must know | What it must access | How the user sees or changes it | What happens when it cannot work |

Remove capabilities that do not serve the user job. Surface limits where they matter instead of hiding them in help text.

## Discovery Rules

- Use task-specific starter prompts, templates, examples, buttons, and mode labels.
- Prefer examples that show the actual domain, data, and output shape.
- Avoid generic empty states such as "Ask me anything" when the product has a defined job.
- Let the interface teach what is possible through available actions, disabled states, previews, and concrete examples.

## Orchestration Rules

Orchestration is the layer that connects users to models, agents, tools, permissions, data, and memory.

- **Intentional**: Ask for choices at meaningful moments, not as setup clutter.
- **Transparent**: Show how capabilities change when the model, tool, permission, data source, or mode changes.
- **Recognizable**: Preserve stable labels, icons, placement, examples, and configuration views so users can reorient later.

## Configuration Checklist

- Which model or agent is active?
- Which tools can it call?
- Which files, databases, apps, or memories can it use?
- What can it change, send, publish, delete, buy, or commit?
- How does the user inspect and revoke access?
- What changes visibly when any of the above change?
