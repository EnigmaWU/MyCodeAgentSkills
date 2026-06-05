---
name: activate-personal
description: 'Use when: starting work with EnigmaWU''s skill set, the user says "activate my personal", asks to use their personal defaults, or declares durable expertise or preferences that should be reused later. Helps with: activating the user''s personal working profile and updating it for future sessions. Applies to: personal profile activation for AI-assisted work.'
---

# Activate Personal

## Who
Agents or maintainers using EnigmaWU's skill set who need to apply the user's durable expertise, working style, and personal defaults consistently across sessions.

## What
Activate the user's personal working profile before doing the main task, then keep that profile up to date when the user declares new durable expertise, preferences, or corrections. The deliverable is an explicit activation summary for the current task plus a minimal update to the stored personal profile when new durable information appears.

## When
- The user says "activate my personal", "use my personal defaults", "load my profile", or similar.
- A session starts with EnigmaWU's skill set and the agent should apply the user's known personal context before proceeding.
- The user says "I am good at...", "my expertise is...", "remember that I prefer...", "next time use...", or otherwise declares durable expertise or preferences.
- The user corrects previously used personal context and wants the correction reused in future sessions.
- Do **not** use this skill for one-off task instructions that apply only to the current request.
- Do **not** use this skill to change repository-wide conventions for everyone. Use repository instructions or documentation instead.

## Where
- The current conversation and any already-available user-scoped memory.
- The deployed skill folder, especially `activate-personal/personal-profile.md` when that file exists and is intended to hold reusable profile details such as expertise, teamwork defaults, terminology mappings, and engineering preferences.
- The companion template at `activate-personal/references/personal-profile-template.md` when a profile file needs to be created or restructured.

## Why
- The user wants their personal context activated automatically instead of being re-explained in every session.
- Durable expertise and preferences are easy to lose if they stay only in chat.
- Separating reusable personal profile data from one-off task instructions keeps future sessions faster and more accurate.
- A lightweight activation step reduces drift: the agent starts from the user's known strengths and preferences, but still adapts to the current task.

## Inputs
- The user's current request.
- Existing personal profile data from memory or `activate-personal/personal-profile.md` when available.
- New expertise, preferences, teamwork defaults, terminology mappings, corrections, or boundaries declared during the conversation.
- Optional confirmation from the user when a statement might be temporary, private, or ambiguous.

## Output
- A concise activation summary describing which personal expertise or preferences are being applied to the current task.
- A minimal update to the stored personal profile when the user provides new durable information.
- A short note explaining what was added, changed, or left unchanged for future sessions.

## Constraints
- Only store durable user-provided information that is safe and appropriate to reuse. Do not invent expertise or preferences.
- Do not treat temporary instructions such as "for this task" or "for now" as profile updates.
- Do not store secrets, credentials, sensitive personal data, or anything the user would not expect to persist.
- Personal defaults must not override explicit instructions in the current task.
- If it is unclear whether a statement is durable, personal, or safe to save, stop and ask before updating the profile.

## One More Thing
If anything is unclear, missing, or conflicting, stop and ask the user before proceeding.

## How

### Phase 1: Find the Current Personal Profile
1. Look for reusable personal context in this order:
   - user-scoped memory that is already available to the agent,
   - `activate-personal/personal-profile.md` beside the deployed skill,
   - explicit profile details stated earlier in the current conversation.
2. If no reusable profile exists, activate only what the current conversation clearly supports and ask whether the user wants a reusable profile created for future sessions.
3. Ignore statements that are clearly task-specific, temporary, or unrelated to how the user works.

### Phase 2: Activate It for the Current Task
1. Extract only the profile items that matter for the current request, such as:
   - durable expertise,
   - preferred problem-solving method,
   - preferred teamwork framing or virtual team roles,
   - preferred working style,
   - preferred output style,
   - terminology mappings or translation rules,
   - recurring boundaries or defaults.
2. State the activation briefly before continuing, for example:

   ```text
   Activated personal profile:
   - Expertise: ...
   - Teamwork: ...
   - Preferences: ...
   - Terminology: ...
   - Boundaries: ...
   ```

3. Apply the activated profile while doing the task, but let explicit task instructions win if they conflict.

### Phase 3: Update the Profile for Next Time
1. Watch for durable declarations such as:
   - "I am an expert in ..."
   - "My expertise is ..."
   - "Treat Agent as ..."
   - "Use this term as ..."
   - "Remember that I prefer ..."
   - "Next time, use ..."
2. Rewrite the declaration into a short, reusable fact without changing its meaning.
3. If the declaration might be temporary, private, or unclear, ask the user whether it should be saved for future sessions.
4. Save the update in the best durable location available:
   - use user-scoped memory when the agent supports persistent memory,
   - otherwise update `activate-personal/personal-profile.md`,
   - if that file does not exist, create it from `activate-personal/references/personal-profile-template.md` with the user's approval.
5. Re-activate the updated profile and tell the user what changed.

### Phase 4: Keep the Profile Clean
1. Merge duplicates and corrections instead of appending contradictory facts.
2. Remove or rewrite outdated items when the user explicitly supersedes them.
3. Keep the profile focused on reusable working context, not a transcript of the conversation.
4. If no durable profile change occurred, say so instead of forcing an update.

## Resources
- `activate-personal/personal-profile.md` — a concrete personal profile that can be activated directly when deployed with this skill set.
- `activate-personal/references/personal-profile-template.md` — starter structure for a reusable personal profile file.
- `save-as-skill/SKILL.md` — use when the conversation produced a brand-new reusable workflow instead of a personal profile update.
- `improve-existing-skill/SKILL.md` — use when another existing skill needs to absorb lessons learned from the conversation.

## Validation
1. Verify the frontmatter `name` matches the folder name.
2. Verify the section layout matches the COMPLEX template.
3. Verify the workflow both activates existing personal context and updates it when the user declares new durable expertise, terminology, or preferences.
4. Verify the skill tells the agent to stop and ask when profile updates are ambiguous or unsafe.
5. Run:

   ```bash
   python save-as-skill/scripts/validate_skill.py activate-personal/SKILL.md --tier complex
   ```
