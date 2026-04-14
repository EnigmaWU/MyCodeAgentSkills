# improve-existing-skill

Update an existing skill when a conversation reveals that the original skill is incomplete, outdated, or wrong. This is the companion to `save-as-skill`: where `save-as-skill` creates a brand-new skill from a conversation, `improve-existing-skill` folds conversation learnings back into an existing skill.

## What Is This

When you apply a saved skill and it does not fully work — you need extra steps, workarounds, or corrections — the improvements typically stay in your chat and never reach the skill file. This skill captures those improvements and merges them back into the original `SKILL.md`, keeping the skill accurate over time.

## When to Use This vs save-as-skill

| Situation | Skill to use |
| --------- | ------------ |
| Conversation solved a new problem, no prior skill exists | `save-as-skill` |
| Applied an existing skill, had to iterate further | `improve-existing-skill` |
| Skill is completely wrong and needs a rewrite | `save-as-skill` (create a replacement) |
| Skill needs a cosmetic or formatting fix | Edit the file directly |

## Porting to Other Agents

The core content is identical across agents. Only the file location and frontmatter differ.

### Layer 1: Manual Trigger

The user explicitly asks to improve a skill (slash command or keyword).

**Copilot** — create `.github/prompts/improve-existing-skill.prompt.md`:

```markdown
---
mode: agent
description: 'Improve an existing skill based on what this conversation learned.'
---

Follow the instructions in .github/skills/improve-existing-skill/SKILL.md
```

User types `/improve-existing-skill`.

**Cline** — add to `.clinerules`:

```text
# .clinerules
When the user asks to "improve this skill", "update the skill", "the skill needs fixing",
or "make this skill better",
read and follow .github/skills/improve-existing-skill/SKILL.md
```

**Continue** — create `.continue/prompts/improve-existing-skill.prompt`:

```yaml
---
name: improve-existing-skill
description: "Improve an existing skill based on what this conversation learned."
invokable: true
---
```

Then paste the body of `SKILL.md` (everything below the frontmatter) into the file.

**Claude Code** — create `.claude/commands/improve-existing-skill.md`:

```markdown
Improve an existing skill based on what this conversation learned.
Follow the instructions in .claude/skills/improve-existing-skill/SKILL.md
```

User types `/improve-existing-skill` in Claude Code's prompt.

### Layer 2: Auto-Invocable

The model detects a conversation where an existing skill was applied and improved upon.

**Copilot** — place `SKILL.md` in `.github/skills/improve-existing-skill/SKILL.md`. The `description` field in frontmatter controls when the model triggers it.

**Cline** — copy or symlink the skill:

```bash
mkdir -p .cline/skills/improve-existing-skill
cp .github/skills/improve-existing-skill/SKILL.md .cline/skills/improve-existing-skill/
```

**Continue** — Continue uses the same `.continue/prompts/improve-existing-skill.prompt` file for both manual and auto-invocation.

**Claude Code** — copy the skill directory:

```bash
mkdir -p .claude/skills/improve-existing-skill
cp .github/skills/improve-existing-skill/SKILL.md .claude/skills/improve-existing-skill/
```

### Layer 3: Always-On Nudge

At the end of qualifying conversations, the agent suggests improving the skill that was applied.

**Copilot** — create `.github/instructions/improve-existing-skill-nudge.instructions.md`:

```markdown
---
applyTo: "**"
---

At the end of a conversation, if ALL of these are true:
1. An existing skill was applied during the conversation
2. The conversation required steps or corrections beyond what the skill prescribed
3. The improvements are non-trivial (not just typos or formatting)
4. The skill would benefit from the new knowledge

Then suggest: "This conversation improved on an existing skill. Want to update the skill with what we learned? Type /improve-existing-skill."
```

**Cline** — append to `.clinerules`:

```text
# Skill-improvement nudge
At the end of a conversation, if an existing skill was applied and the conversation
required non-trivial corrections or extra steps beyond what the skill prescribed,
suggest: "This conversation improved on an existing skill. Want to update it?"
```

**Continue** — add to `.continue/config.yaml` system message:

```yaml
systemMessage: |
  At the end of conversations where an existing skill was applied but required
  non-trivial corrections, suggest improving the skill by typing /improve-existing-skill.
```

**Claude Code** — add to `CLAUDE.md` in the project root:

```markdown
## Skill-Improvement Nudge

At the end of conversations where an existing skill was applied but required
non-trivial corrections or extra steps, suggest: "Want to improve the skill
with what we learned?" Then follow .claude/skills/improve-existing-skill/SKILL.md
```

## Usage

### In Copilot Chat

```text
/improve-existing-skill
```

The agent compares what the original skill prescribed with what the conversation actually needed, then updates the skill.

### Validate the Updated Skill

```bash
python .github/skills/save-as-skill/scripts/validate_skill.py \
  .github/skills/my-skill/SKILL.md \
  --tier complicated
```

Use the tier of the original skill. If unsure, use `--tier auto`.
