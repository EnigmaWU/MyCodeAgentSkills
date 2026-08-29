---
name: select-ai-pm-toolkit
description: >
  WHEN/WHERE/WHO: AI project managers and agents who must choose tools and
  platforms for managing and implementing AI projects.
  HOW: Survey the PM tool trifecta (tracking, knowledge documentation, technical
  management), AI productivity tools, and the technology stack; run the tooling
  checklist and vendor analysis template; recommend a curated toolkit.
  WHY: Tool choice affects team adoption, reproducibility, cost, and ROI; a
  structured evaluation prevents duplication and lock-in.
---

# Select AI PM Toolkit

## Who
AI project managers, tech leads, and agents selecting tools for AI teams.

## What
Produce a recommended AI PM toolkit:

- project tracking (boards/backlogs);
- knowledge documentation and experiment tracking;
- code/model/data repositories;
- AI-enabled productivity tools (task management, meetings, ideation);
- technology stack awareness (infrastructure, platforms, dev suites, libraries,
  governance);
- vendor analysis for any candidate tool.

## When
Trigger when the user asks to: "which AI PM tools should we use", "build an AI
project toolkit", "choose project tracking tools", "compare AI tool vendors",
or "what tools do we need for the AI project".

## Where
Works from the organization's context: team preferences, budget, existing
stack, and project type. Output is a toolkit recommendation.

## Why
The book defines the PM tool trifecta (visibility, structure, traceability) and
provides a tooling checklist plus vendor analysis template; the right toolkit
removes friction and keeps AI work auditable.

## Inputs
- **Project/organization context** (required): team size, AI maturity, budget,
  existing tools, project type.
- **Candidate tools** (optional): tools to evaluate.

## Output (Logical Evidence)
- Toolkit recommendation covering the trifecta categories, AI productivity
  tools, and technology stack notes.
- Vendor analysis table for any tool under evaluation.

## Optimization Readiness
- **Failure Signals**: Recommendation ignores team preferences; no vendor
  evaluation; duplicates existing tools; toolkit too heavy for the team's
  maturity; no cost/ROI reasoning.
- **Evidence To Collect**: User feedback; adoption issues; vendor changes.
- **Safe Mutation Boundaries**: Tool lists, checklist wording, and analysis
  template may change. The trifecta structure and evaluation criteria must
  remain.
- **Acceptance Criteria**: A revision must produce a toolkit covering all
  categories with rationale for each choice.
- **Rejected Revision Handling**: Record rejected tool mappings in the
  umbrella's validation log.
- **Transfer Check**: Must work for startups and enterprises, ML and GenAI
  projects.
- **Stop Rule**: If the context (team, budget, existing stack) is missing, stop
  and ask.

## Constraints (Logical Boundaries)
- Recommend only real, standard tools; never hallucinate products.
- Prioritize team adoption over PM preference.
- Cover governance/compliance tools for responsible AI.
- Include cost and vendor risk in evaluations.
- **Anti-Pattern Mapping**:
  - MUST NOT recommend a tool without checking fit with team skills.
  - MUST NOT ignore data/model versioning in the technical stack.
  - MUST NOT skip the vendor analysis for paid tools.

## One More Thing
If the organization context is missing, stop and ask before recommending tools.

## How (Structural Workflow)

### Phase 1: Survey the trifecta
1. Project tracking: choose board/backlog tools (e.g., Jira/Linear/Azure DevOps,
   Trello/Asana, Notion, ClickUp) that the team will actually use.
2. Knowledge documentation: choose wikis (Confluence/Notion/GitBook) and
   experiment tracking (MLflow, Weights & Biases, Unity Catalog).
3. Technical management: choose code repositories (GitHub/GitLab/Bitbucket),
   dataset versioning (DVC/lakeFS), and model hubs (Hugging Face Hub).

### Phase 2: Add AI productivity tools
1. Task management and drafting (autoprioritization, user stories).
2. Meeting summarization and semantic search (Slack AI, Otter, Teams Copilot).
3. Ideation/prototyping (Miro/Figma, Lovable/Replit, presentation generators).

### Phase 3: Map the technology stack
1. Infrastructure: CPU/GPU, on-prem vs. cloud (CAPEX/OPEX), PTUs/TPUs.
2. Platforms: AI studios (SageMaker, Vertex AI, Foundry), containerization
   (Docker/Kubernetes), data lakehouses (Databricks/Snowflake/Fabric).
3. Development suites: notebooks (JupyterLab), IDEs (VS Code), code assistants.
4. Libraries: Scikit-learn/TensorFlow/PyTorch/XGBoost; GenAI frameworks
   (LangChain, LlamaIndex, Haystack), protocols (MCP, A2A).
5. Governance: Purview/watsonx.governance, model monitoring (Fiddler/Arize),
   RAI toolkits (Fairlearn, AIF360, SHAP).

### Phase 4: Run the vendor analysis (for candidate tools)
Evaluate: vendor profile/reputation/pace of innovation/geography; tool scope
(environment, features, model types, AI knowledge); compliance/security; usage
(technical level, interoperability, customization, service, pricing); key
questions (fit, lock-in, cost-value, ROI).

### Phase 5: Validate
1. Confirm all categories are covered.
2. Confirm each recommendation includes a reason and adoption risk.
3. Deliver the toolkit.

## Validation (Verifiable Rewards)
1. Toolkit covers tracking, documentation, technical management, productivity,
   and technology stack.
2. Each recommended tool is real and standard.
3. Vendor analysis includes cost, compliance, and lock-in for paid tools.
4. Recommendations account for team skills and adoption.
