# MyCodeAgentSkills - Skill Summary Directory

This document provides a comprehensive index of all the agent skills available in this repository.

---

## [UnitTesting-convert2CaTDD](./UnitTesting-convert2CaTDD/)

**English:** 

**中文:** 使用场景: 用户要求“转换为CaTDD”，“重构测试为CaTDD”，“应用CaTDD”，“使测试注释生效”，或要求使用US/AC/TC格式重构现有测试。有助于: 将遗留或无结构测试转换为带有结构化验证设计的CaTDD（注释驱动的测试驱动开发）格式。适用于: 任何缺少结构化US/AC/TC注释的现有测试文件。

---

## [activate-personal](./activate-personal/)

**English:** Use when: starting work with EnigmaWU''s skill set, the user says "activate my personal", asks to use their personal defaults, or declares durable expertise or preferences that should be reused later. Helps with: activating the user''s personal working profile and updating it for future sessions. Applies to: personal profile activation for AI-assisted work.

**中文:** 使用场景: 开始使用EnigmaWU技能集，用户要求“激活我的个人配置”，要求使用他们的个人默认设置，或者声明需要在日后重用的专业知识或偏好。有助于: 激活用户的个人工作配置并在未来的会话中更新它。适用于: AI辅助工作中的个人配置激活。

---

## [analyze-with-tactics-questionnaires](./analyze-with-tactics-questionnaires/)

**English:** This skill guides the agent to evaluate a software architecture design by applying Tactics-Based Questionnaires (from Chapter 8 / Appendix B of *Designing Software Architectures*). Instead of generic reviews, these questionnaires force a targeted review of specific Quality Attributes like Availability, Modifiability, or Security.

**中文:** 使用时间/地点/人员: 审查人员、架构师或代理人在分析建议或现有架构时。
方法: 使用此技能对照特定的质量属性问卷（例如，可用性，安全性）系统地评估设计。
原因: 在实施之前揭示隐藏的架构风险和缺失的策略。

---

## [apply-agile-testing-quadrants](./apply-agile-testing-quadrants/)

**English:** This skill guides the agent to apply the Agile Testing Quadrants (introduced by Brian Marick, popularized by Lisa Crispin and Janet Gregory in *Agile Testing*) to structure a comprehensive test strategy. It ensures that testing isn't just focused on automated developer tests (unit tests) or manual UI testing, but rather provides a balanced approach covering four distinct quadrants: Q1 (Technology/Support), Q2 (Business/Support), Q3 (Business/Critique), and Q4 (Technology/Critique).

**中文:** 使用场景: 为功能定义测试策略或规划测试时。有助于: 在业务/技术以及支持/评估维度上平衡测试覆盖率。适用于: 测试计划，功能审查，验收标准。

---

## [apply-architectural-tactics](./apply-architectural-tactics/)

**English:** 

**中文:** 使用场景: 设计系统架构，进行结构设计审查，或将质量目标映射到设计决策时。有助于: 定义架构重要需求（ASR），构建质量属性效用树，应用属性驱动设计（ADD）步骤，选择SAiP策略，并执行ATAM权衡分析。适用于: 架构设计文档，RFC和系统设计规范。

---

## [apply-attribute-driven-design](./apply-attribute-driven-design/)

**English:** This skill guides the agent to apply the **Attribute-Driven Design (ADD) 3.0** methodology, extracted from the *Designing Software Architectures* book. ADD is an iterative, 7-step process for making architectural decisions based heavily on Quality Attributes (like availability, modifiability, and performance) rather than just functional requirements.

**中文:** 使用时间/地点/人员: 软件架构师或核心开发人员设计新功能或全新系统时。
方法: 使用此技能系统地执行7步ADD 3.0方法，将驱动因素映射到设计模式。
原因: 确保架构处理所有约束和质量属性，而不仅仅是功能需求。

---

## [apply-oopsi-model](./apply-oopsi-model/)

**English:** This skill guides the agent to use the **OOPSI** model (Outcome, Outputs, Process, Scenarios, Inputs) created by Jenny Martin and Pete Buckney. OOPSI is a collaborative discovery practice that works backwards from the highest-value business outcome down to the granular data inputs needed to test it.

**中文:** 使用时间/地点/人员: 业务分析师、测试人员或代理人在探索用户旅程或数据工作流时。
方法: 使用此技能从业务结果(Outcome)倒推到有形输出(Outputs)、到过程(Process)、下至场景(Scenarios)和确切的输入(Inputs)。
原因: 从输入开始会模糊业务目标。从结果开始可以确保在编写精细测试之前达成一致。

---

## [apply-screenplay-pattern](./apply-screenplay-pattern/)

**English:** This skill guides the agent to design and implement automated tests using the **Screenplay Pattern**, an advanced architectural pattern for test automation. Traditional Page Objects become brittle and bloated at scale, mixing test execution logic with page locators. The Screenplay Pattern resolves this by modeling tests from the perspective of an Actor interacting with the system to accomplish a Task.

**中文:** 使用时间/地点/人员: SDET，开发人员或代理人在编写或重构自动化验收测试时。
方法: 使用此技能围绕参与者(Actors)，任务(Tasks)，交互(Interactions)，能力(Abilities)和问题(Questions)来组织测试代码，而不是使用页面对象(Page Objects)。
原因: 页面对象会膨胀成包含脆弱定位器和混合关注点的庞大“上帝类”。Screenplay将SOLID原则应用于测试代码，使其在规模化时具备可重用性、可读性和高度可维护性。

---

## [blog-topic-discover](./blog-topic-discover/)

**English:** Use when: a task is completed, a goal is met, or the user asks to review recent work for blog ideas. Helps with: extracting insights, mistakes, new methods, and topics from recent git commits and chat logs to brainstorm blog posts. Applies to: post-task reflection and developer branding.

**中文:** 使用场景: 任务完成、目标达成或用户要求回顾最近工作以寻找博客灵感时。有助于: 从最近的git提交和聊天记录中提取见解、错误、新方法和主题，以集思广益博客文章。适用于: 任务后反思和开发者个人品牌建设。

---

## [build-business-objectives-model](./build-business-objectives-model/)

**English:** This skill guides the agent to extract and construct a **Business Objectives Model (BOM)** as defined in *Visual Models for Software Requirements*. The BOM sits at the very top of the Requirements Modeling Language (RML) hierarchy. It ensures that before any features are designed, the team agrees on the exact Business Problems, the quantifiable Business Objectives, and the overarching Product Concept.

**中文:** 使用时间/地点/人员: 产品负责人或代理人在分析项目启动文档或愿景陈述时。
方法: 使用此技能将主观的业务问题映射到可量化的业务目标，并推导出产品概念。
原因: 避免构建无人需要的功能的陷阱。如果功能无法追溯到BOM目标，则不应构建它。

---

## [build-data-dictionary](./build-data-dictionary/)

**English:** This skill guides the agent to extract and define data elements from functional requirements, generating a **Data Dictionary** as described in *Software Requirements (3rd Edition)*. A Data Dictionary provides a common vocabulary for the project, ensuring that when developers and stakeholders say "Customer ID," they mean the exact same data type and format.

**中文:** 使用时间/地点/人员: 数据库设计师，业务分析师或代理人在分析表单，报告或数据密集型需求时。
方法: 使用此技能从文本中提取领域名词，并将其映射到严格的数据字典（元素名称，数据类型，长度，允许的值）中。
原因: 模棱两可的数据定义会导致集成失败。

---

## [build-feature-tree](./build-feature-tree/)

**English:** This skill guides the agent to organize a flat list of product features into a hierarchical **Feature Tree** (L1, L2, L3 features), as defined in *Visual Models for Software Requirements*. A Feature Tree allows stakeholders to view the entire scope of a system on a single page, making it easy to identify missing functional areas or redundant requirements.

**中文:** 使用时间/地点/人员: 分析师或代理人在审查扁平的产品待办列表或冗长的PRD时。
方法: 使用此技能将非结构化的需求分组为分层功能树（L1，L2，L3），并渲染为思维导图。
原因: 扁平列表隐藏了缺失的功能。可视化层次结构暴露了差距。

---

## [comment-alive-test-driven-development](./comment-alive-test-driven-development/)

**English:** 

**中文:** 使用场景: 从头开始编写新测试，为新功能或模块设计验证，应用CaTDD，以及通过注释驱动设计启动新测试文件。有助于: 使用CaTDD方法创建结构化的测试文件，包含US/AC/TC设计，基于优先级的测试分类，以及适合LLM的验证注释。适用于: 任何语言中针对单元测试、系统测试和用户测试的新测试文件。

---

## [create-ecosystem-map](./create-ecosystem-map/)

**English:** This skill guides the agent to map out the boundaries of a system using an **Ecosystem Map** (from the *Visual Models for Software Requirements* methodology). Systems do not exist in a vacuum; they interact with users, legacy databases, third-party APIs, and downstream services. An Ecosystem Map visualizes these dependencies to prevent "out of scope" surprises.

**中文:** 使用时间/地点/人员: 系统架构师，分析师或代理人在定义新项目范围时。
方法: 使用此技能从文本中提取所有上游和下游系统，并将它们渲染为Mermaid.js图。
原因: 早期未识别集成点会导致后期大量的架构返工。生态系统图定义了确切的边界。

---

## [create-living-documentation](./create-living-documentation/)

**English:** 

**中文:** 使用场景: 自动化规范，提取领域词汇表，生成PlantUML/Graphviz架构图，或创建BDD核对测试时。有助于: 建立单一事实来源，避免文档漂移，通过AST/注解提取代码元数据，并通过单元测试验证文档。适用于: 工作区中的代码库架构、词汇表生成器、API模式和构建验证脚本。

---

## [create-skill-from-book](./create-skill-from-book/)

**English:** 

**中文:** 使用场景: 将技术教科书、工程标准或参考手册整理为可重用的代理技能时。有助于: 提取程序化工作流、设计约束和检查表；将它们结构化为简单、复杂或极其复杂的技能模板。适用于: 工作区中的技能目录、参考指南和设计检查表。

---

## [define-architectural-drivers](./define-architectural-drivers/)

**English:** This skill guides the agent to extract and formalize **Architectural Drivers** from unstructured product requirements (PRDs, User Stories, or transcripts). It ensures that before any design happens (via ADD 3.0), the four types of drivers are clearly defined: Design Purpose, Quality Attributes, Primary Functionality, and Constraints/Concerns.

**中文:** 使用时间/地点/人员: 系统分析师或架构师在设计开始前分析原始产品需求时。
方法: 使用此技能提取非结构化需求并将其形式化为四种类型的架构驱动因素。
原因: 没有明确的约束和优先级的质量属性场景，就无法设计架构。

---

## [design-agents-using-patterns](./design-agents-using-patterns/)

**English:** 

**中文:** 使用场景: 设计多代理系统，创建路由逻辑，构建自校正提示链，或添加工具使用和规划能力时。有助于: 选择适当的代理模式，构建协调员-专家团队，实现异常处理，并防止失控的LLM循环。适用于: 工作区中的编排脚本、代理系统设计和提示链配置。

---

## [design-architecture-viewpoints](./design-architecture-viewpoints/)

**English:** 

**中文:** 使用场景: 定义系统的结构视图，记录系统架构，或调整利益相关者的期望时。有助于: 识别利益相关者和场景，选择视角，起草视图（上下文，功能，信息，并发，开发，部署，操作）。适用于: 软件架构说明、系统设计文档和RFC。

---

## [doc-with-usage-example](./doc-with-usage-example/)

**English:** Use when: the user asks to create or update documentation. Helps with: producing docs that always include 5W1H context and a copy-exec Usage Example. Applies to: markdown documents, READMEs, guides, and runbooks.

**中文:** 使用场景: 用户要求创建或更新文档时。有助于: 生成始终包含5W1H上下文和可复制执行的使用示例的文档。适用于: markdown文档、README、指南和操作手册。

---

## [document-architectural-decisions](./document-architectural-decisions/)

**English:** 

**中文:** 使用场景: 在做出关键设计选择，解决架构设计权衡，或用户要求“记录此决定”或“编写ADR”时。有助于: 编写结构化的12字段决策记录（ADR），创建替代方案比较矩阵，并通过Kruchten本体对选择进行分类。适用于: 工作区中的架构记录、设计建议、RFC和决策文件夹。

---

## [document-legacy-codebase](./document-legacy-codebase/)

**English:** 

**中文:** 使用场景: 对棕地系统进行逆向工程，映射遗留代码结构，建立气泡上下文边界，或应用绞杀者迁移模式时。有助于: 提取化石化的知识，通过边车/装饰器叠加元数据结构。适用于: 工作区中的遗留库、棕地代码库、边界接口和迁移配置。

---

## [draft-srs-document](./draft-srs-document/)

**English:** This skill guides the agent to compile scattered requirements into a formal **Software Requirements Specification (SRS)** document, using the industry-standard template provided in *Software Requirements (3rd Edition)*. The SRS serves as the ultimate agreement between the customer and the development team.

**中文:** 使用时间/地点/人员: 业务分析师、系统工程师或代理人将需求汇编成最终规范时。
方法: 使用此技能将分散的用户故事、约束和UI注释映射到正式的IEEE风格SRS模板中。
原因: 非结构化文档会导致上下文缺失。SRS强迫团队明确声明功能旁边的依赖关系、外部接口和质量属性。

---

## [elicit-requirements-models](./elicit-requirements-models/)

**English:** This skill guides the agent to convert flat, text-based software requirements into structured visual models (using Mermaid.js). According to *Software Requirements Essentials*, creating requirements models (like state transition diagrams or data flow diagrams) is one of the most effective ways to expose missing requirements, logical dead ends, and edge cases that are invisible in raw text.

**中文:** 使用时间/地点/人员: 业务分析师，代理人或开发人员在审查复杂的用户故事或PRD时。
方法: 使用此技能将文本需求解析为Mermaid.js可视化模型（状态/流程图），以识别缺失的逻辑。
原因: 纯文本掩盖了缺失的边缘情况和逻辑死胡同。可视化建模可以在编写代码之前暴露这些差距。

---

## [extract-business-rules](./extract-business-rules/)

**English:** This skill guides the agent to extract and classify Business Rules from unstructured requirements text, as defined in *Software Requirements (3rd Edition)*. Business rules (policies, laws, regulations, and industry standards) dictate how a system must behave, but they are often incorrectly documented as software features. By extracting them, teams can manage the rules independently of the software implementation.

**中文:** 使用时间/地点/人员: 业务分析师或代理人在审查包含嵌入式业务逻辑的用户故事或PRD时。
方法: 使用此技能从文本中提取策略、法律和计算，并将其分类为严格的业务规则分类。
原因: 业务规则的变化比软件更频繁。将规则硬编码为“功能”会产生遗留债务。

---

## [facilitate-example-mapping](./facilitate-example-mapping/)

**English:** This skill guides the agent to facilitate an **Example Mapping** workshop. Example Mapping is a fast, structured, low-tech way to explore a User Story before development starts. It forces the team to identify the Business Rules, concrete Examples that prove those rules, and open Questions that block progress.

**中文:** 使用时间/地点/人员: 业务分析师、产品负责人或代理人领导待办事项梳理或“Three Amigos”会议时。
方法: 使用此技能将用户故事分解为业务规则（蓝色），具体示例（绿色）和未决问题（粉色）。
原因: 非结构化的对话会漫无目的并遗漏边缘情况。Example Mapping提供了一个视觉上的广度优先约束。

---

## [improve-existing-skill](./improve-existing-skill/)

**English:** 

**中文:** 使用场景: 已应用现有技能但未完全解决问题，用户在对话中进一步迭代以达到有效解决方案，并要求“改进此技能”时。有助于: 使用对话中学到的、超出原始技能涵盖范围的经验教训更新现有的SKILL.md。适用于: .github/skills/ 等目录中的现有技能包。

---

## [improve-user-story](./improve-user-story/)

**English:** This skill guides the agent to proactively detect when a conversation introduces a new improvement, edge case, or feature change, and updates the relevant existing user story to reflect it using strict BDD formatting.

**中文:** 使用时间/地点/人员: 开发人员、产品负责人、QA工程师或需要更新现有BDD风格用户故事的代理人。
方法: 使用此技能主动检测对话中引入的新边缘情况或更改，并安全地使用新的Given/When/Then场景更新相关的用户故事。
原因: 需求在讨论期间演变，文档往往会变得陈旧。

---

## [prioritize-requirements](./prioritize-requirements/)

**English:** This skill guides the agent to systematically prioritize a backlog of requirements, user stories, or features. As noted in *Software Requirements Essentials*, simply tagging items as "High/Medium/Low" is subjective and often fails. This skill implements an analytical matrix to rank requirements based on weighted business value, user value, cost, and risk.

**中文:** 使用时间/地点/人员: 产品负责人或代理人梳理功能或用户故事积压时。
方法: 使用此技能通过分析矩阵对价值、成本和风险项目进行评分，得出严格的排序。
原因: 主观的“高/中/低”标签会导致所有内容都被标记为“高”。数学评分强制进行客观的权衡。

---

## [save-as-skill](./save-as-skill/)

**English:** 

**中文:** 使用场景: 经过长时间对话解决了一个难题，调试会话产生了一个可重用的工作流，或者用户要求“保存为技能”时。有助于: 提取可重用的SKILL.md，保留对话中的推理和工件。适用于: 当前对话，生成的技能包以及AI助手的技能交接。

---

## [task-commit-trigger](./task-commit-trigger/)

**English:** Use when: a task is just completed. Helps with: auto triggering or noticing developer "shall we commit just completed work?", and generating a structured WHAT/HOW/WHY commit message. Applies to: git repositories and conversation context.

**中文:** 使用场景: 任务刚完成时。有助于: 自动触发或提醒开发人员提交刚完成的工作，并生成结构化的WHAT/HOW/WHY提交消息。适用于: git存储库和对话上下文。

---

## [test-case-with-demo](./test-case-with-demo/)

**English:** Use when: the user asks to create a demo test case, example test, UserGuide demo, UserStories demo, manual demo, setup-backed test case, or explicitly invokes test-case-with-demo. Helps with: building an end-to-end demonstration test package that shows how to use a feature according to the UserGuide and how it satisfies UserStories/acceptance criteria, including setup scripts, manual instructions, fixtures, expected outputs, and traceability. Applies to: documentation-oriented P4 demo/example tests for CLIs, APIs, tools, workflows, repository user guides, and user story specifications.

**中文:** 使用场景: 用户要求创建演示测试用例，示例测试，手册演示，或显式调用 test-case-with-demo 时。有助于: 构建端到端演示测试包，以展示如何使用功能并满足用户故事，包含设置脚本和可追溯性。适用于: 面向文档的P4演示/示例测试。

---

## [test-case-with-readme](./test-case-with-readme/)

**English:** Use when: the user creates a new test case, plans to write a test, or asks to generate a readme for an existing test. Helps with: planning and documenting test files with structured purpose, status, coverage, and manual steps. Applies to: any test creation workflow or existing test files like .py, .cxx, etc.

**中文:** 使用场景: 用户创建新测试用例、计划编写测试，或要求为现有测试生成自述文件时。有助于: 使用结构化的目的、状态、覆盖范围和手动步骤来计划和记录测试文件。适用于: 任何测试创建工作流或现有的测试文件。

---

## [test-driven-development](./test-driven-development/)

**English:** Use when implementing any feature or bugfix, before writing implementation code

**中文:** 在实现任何功能或错误修复时，在编写实现代码之前使用。

---

## [update-my-resume](./update-my-resume/)

**English:** 

**中文:** 使用场景: 用户刚解决了一个问题，完成了一项任务，结束了调试会话，或要求“更新我的简历”时。有助于: 分析用户展示的新技能，然后编写包含问题、步骤和结果的结构化中英文简历条目。适用于: 根目录或$HOME下的 .resume 文件。

---

## [update-spec-context](./update-spec-context/)

**English:** Use when: a vibe-coding or AI-assisted coding conversation changes requirements, design decisions, plans, task status, or implementation context. Helps with: updating spec-driven-development context files before the details are lost. Applies to: GitHub Spec Kit-style specs, plans, tasks, constitutions, and repository planning docs.

**中文:** 使用场景: AI辅助编码对话改变了需求、设计决策、计划、任务状态或实现上下文时。有助于: 在细节丢失之前更新规范驱动开发的上下文文件。适用于: GitHub Spec Kit 风格的规范、计划、任务、章程和存储库规划文档。

---

## [validate-requirements-criteria](./validate-requirements-criteria/)

**English:** This skill guides the agent to review and test requirements *before* any code is written, a core practice emphasized in *Software Requirements Essentials*. It hunts for ambiguous adjectives (e.g., "fast," "user-friendly," "robust"), identifies missing edge cases, and outputs strict, testable Acceptance Criteria using Behavior-Driven Development (BDD) syntax.

**中文:** 使用时间/地点/人员: QA工程师，代理人或业务分析师在开发前审查起草的需求时。
方法: 使用此技能寻找模棱两可的词语，识别边缘情况，并将文本翻译成严格的BDD验收标准。
原因: 模棱两可的需求会导致错误。在分析阶段修复需求缺陷是成本最低的。

---

## [write-user-story](./write-user-story/)

**English:** This skill guides the agent to produce well-structured User Stories with BDD-style acceptance criteria. It ensures that requirements are broken down into testable, unambiguous executable specifications while maintaining a strong focus on business value.

**中文:** 使用时间/地点/人员: 开发人员，产品负责人或代理人将需求形式化为待办事项时。
方法: 使用此技能以标准的“作为...我想要...”格式编写用户故事，并以BDD“给定/当/那么”可执行规范为后盾。
原因: 模糊的故事会导致误解和错误。BDD风格的验收标准使预期行为明确、可测试和清晰。

---

