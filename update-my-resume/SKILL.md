---
name: update-my-resume
description: 'Use when: the user just solved a problem, completed a task, finished a debugging session, or says "update my resume", "add this to my resume", "what did I learn today", or "capture my growth". Helps with: analyzing what new skills or competencies the user demonstrated, then writing a structured resume entry in both English and Chinese that covers the problem, the step-by-step approach, and the verified outcome. Applies to: .resume in the project root or $HOME/.resume, both EN and ZH sections.'
---

# Update My Resume

## Who
Developers or learners who just solved a non-trivial problem or completed a meaningful task and want to capture the demonstrated competency as a verifiable, well-structured resume entry in both English and Chinese.

## What
Analyze the current conversation to extract a resume-worthy accomplishment, then write and append a structured entry to both the English and Chinese sections of the user's `.resume` file. Each entry follows the three-part narrative:
1. **WHAT problem** was met
2. **HOW** the user approached it step by step
3. **WHAT was gained** and evidence that it is useful and repeatable

## When
- The user says "update my resume", "add this to my resume", "capture my growth", or "what did I learn today".
- A conversation solved a non-trivial problem that required reasoning, debugging, architecture decisions, or learning a new tool.
- The conversation produced a working, verified solution that could be repeated.
- Do **not** use this for trivial lookups, one-liner fixes, or routine tasks that any junior developer would handle without thought.
- Do **not** fabricate accomplishments. Only write what the conversation actually shows.

## Where
- Source material: the current conversation and any code, commands, logs, or artifacts it produced.
- Resume file (English): `.resume` in the project root, or `$HOME/.resume` if no project-level file exists. Look for an `[EN]` or `[English]` section header.
- Resume file (Chinese): the same file, under a `[ZH]` or `[中文]` section header. If the file has no ZH section yet, create one at the end.
- If neither location exists, create `$HOME/.resume` with the minimal structure shown in the **Resources** section.

## Why
- Solving hard problems is valuable, but the value disappears if it is never recorded.
- A resume entry written immediately after the fact is more accurate and more specific than one written from memory weeks later.
- Structured entries (problem → approach → verified outcome) are more convincing to reviewers than vague bullet points.
- Maintaining both EN and ZH versions keeps the record accessible for opportunities in any language context.
- The repeatable-and-useful test forces honest reflection: if the skill cannot be applied again, it may not belong on a resume yet.

## Inputs
- The full current conversation (required).
- Code, commands, logs, config snippets, or test results produced during the conversation (optional but strengthens the entry).
- Explicit user feedback on what they consider the most important takeaway (optional).
- Target resume file path override from the user (optional; defaults to project `.resume` then `$HOME/.resume`).

## Output
- A structured resume entry appended to the English section of the `.resume` file.
- The same entry, translated and culturally adapted, appended to the Chinese section of the `.resume` file.
- A brief summary shown to the user: what was appended, where, and why it qualifies.
- A recommendation to skip the update when the conversation does not meet the bar, with a clear reason.

## Constraints
- Only record what the conversation actually demonstrates. Do not inflate scope.
- Each entry must include all three parts: the problem, the step-by-step approach, and the verified outcome.
- Keep each entry concise — aim for 3–6 lines per part, enough to be credible but not a narrative essay.
- The Chinese entry is a translation and cultural adaptation, not a separate story. Keep the facts identical.
- Do not overwrite existing resume entries. Always append.
- If the resume file does not exist, create it with the minimal skeleton first, then append.
- Do not share or transmit the resume file contents to any external service.

## One More Thing
If anything is unclear, missing, or conflicting — especially which problem to highlight, what the actual verified outcome was, or where the resume file lives — stop and ask the user before writing anything.

## How

### Phase 1: Locate the Resume File
1. Check for `.resume` in the current project root.
2. If not found, check `$HOME/.resume`.
3. If neither exists, ask the user whether to create `$HOME/.resume` with the minimal skeleton (see **Resources**).
4. Note the file path and remember it for Phases 4 and 5.

### Phase 2: Assess Whether the Conversation Qualifies
1. Review the conversation for evidence of a non-trivial problem that was actually solved.
2. Ask:
   - Was there a clear problem or goal that required more than a one-step answer?
   - Did the solution require reasoning, iteration, or domain knowledge?
   - Is there evidence that the outcome works (test passing, output verified, build succeeding)?
   - Could a similar approach be applied to a future problem?
3. If the answer to any of these is "no" or "unclear", say so and stop:

   > "This conversation doesn't clearly meet the bar for a resume entry because [reason]. Consider running this skill again after you have a verified, repeatable outcome."

### Phase 3: Extract the Three-Part Narrative
Build the narrative from the conversation:

**Part 1 — The Problem (WHAT)**
- State the problem or goal concisely. Include the domain, the specific challenge, and why it was non-trivial.
- Example: "Diagnosed a race condition in a Go service where concurrent map writes caused intermittent panics under load."

**Part 2 — The Approach (HOW)**
- Describe the step-by-step reasoning and actions taken. Include tools, commands, and pivots.
- Keep it ordered: what was tried first, what failed, what worked, and why.
- Example: "Added `-race` flag to reproduce the panic reproducibly → identified the shared map with `go tool pprof` → replaced with `sync.Map` → re-ran load test to confirm zero panics."

**Part 3 — The Outcome (WHAT I GOT)**
- State what was gained: the fix, the skill, the understanding.
- Include verification evidence: test results, metrics, code diff, or peer review.
- State why it is repeatable: the same pattern applies to [similar future scenario].
- Example: "Eliminated all race-condition panics under 10× normal load. Pattern is reusable for any shared-state concurrent Go service."

### Phase 4: Write the English Entry
Format the entry as follows and append it to the English section of the resume file:

```
--- [YYYY-MM-DD] ---
Problem:  <one-sentence problem statement>
Approach: <ordered steps, separated by " → ">
Outcome:  <result + verification evidence>
Reuse:    <why this skill applies to future situations>
```

### Phase 5: Write the Chinese Entry
Translate and culturally adapt the English entry. Append it to the Chinese (`[ZH]` / `[中文]`) section:

```
--- [YYYY-MM-DD] ---
问题：  <一句话描述问题>
过程：  <有序步骤，用" → "分隔>
收获：  <结果 + 验证证据>
复用性：<为何此技能可应用于未来类似场景>
```

Keep the facts identical to the English entry. Adapt phrasing to feel natural in Chinese rather than literally translated.

### Phase 6: Verify and Report
1. Read back the appended entries to the user.
2. Confirm the file path where they were written.
3. Ask: "Does this accurately capture what you accomplished? Would you like to adjust any part before we finish?"
4. Apply any requested adjustments.

## Resources
- Minimal `.resume` skeleton to create if no file exists:

```
[EN]
# My Resume

## Experience & Growth Log


[ZH]
# 我的简历

## 成长与经历记录

```

- Related skills:
  - `save-as-skill` — if the conversation also produced a reusable workflow worth preserving as a skill
  - `improve-existing-skill` — if an earlier resume entry needs correction after new evidence

## Validation
1. Verify the resume file exists and was written to the correct path.
2. Verify the English entry contains all four fields: `Problem`, `Approach`, `Outcome`, `Reuse`.
3. Verify the Chinese entry contains all four fields: `问题`, `过程`, `收获`, `复用性`.
4. Verify no existing entries were modified or removed.
5. Verify the facts in both entries are identical (same problem, same steps, same outcome).
6. Verify the conversation actually supports the claims in the entry — no inflation.
