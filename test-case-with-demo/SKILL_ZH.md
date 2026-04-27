---
name: test-case-with-demo
description: '使用场景：当用户要求创建 demo 测试用例、示例测试、UserGuide 演示、UserStories 演示、手动演示、带 SETUP 脚本的测试用例，或明确调用 test-case-with-demo 时使用。帮助解决：构建一个端到端演示测试包，用来展示如何按照 UserGuide 使用某个功能，并证明它满足 UserStories/验收标准；同时包含 SETUP 脚本、ManualInstruction.md、夹具数据、期望输出和可追踪关系。适用于：CLI、API、工具、工作流、仓库级 UserGuide 和用户故事规格的文档型 P4 Demo/Example 测试。'
---

# 带 Demo 的测试用例

## Who

需要用可验证 demo 来说明真实用户工作流的开发人员、QA 工程师、文档维护者或智能体。

## What

为一个 UserGuide 工作流及其匹配的 UserStories/验收标准创建自包含的 demo 测试包。该包应展示用户如何准备输入、运行功能、观察期望输出，并在最后清理环境。它应包含 setup/run/cleanup 脚本、`ManualInstruction.md`、回溯到 UserGuide、UserStories 和验收标准的 traceability、夹具数据、期望产物，并在项目有测试框架时包含至少一个可运行检查。

Demo 测试属于 P4 Addons：用于文档、上手和工作流验证。它补充 P1/P2/P3 自动化测试，但不能替代那些证明单个验收标准的聚焦测试。

## When

- 用户提出“demo test case”、“example test”、“manual demo”、“UserGuide demo”、“test-case-with-demo”或“setup script plus ManualInstruction”。
- 一个功能已经有 UserGuide 或 README 工作流，需要一个可运行示例展示如何使用。
- CLI、API 或工作流仅靠单元测试不容易理解，需要端到端演示。
- 某个 fork 或示例实现需要轻量证明它满足可见的 UserGuide 路径以及相关 UserStories/AC 场景。
- 不要把该技能用于没有用户可见工作流的窄单元测试；这种情况使用 `test-case-with-readme` 或常规 TDD。

## Where

- 从面向用户的文档开始，尤其是 `README_UserGuide.md`、`README_UserStories.md`、API 文档、CLI 文档或等价文件。当 UserGuide 和 UserStories 同时存在时，将二者视为成对来源。
- 将生成的 demo 包放在项目既有的 demo/test/example 目录中。如果没有惯例，使用 `tests/demo/<demo-name>/`。
- 使用本技能 `assets/` 目录中的模板作为起点，并根据目标项目和语言调整。

## Why

- Demo 测试让 UserGuide 变得足够可执行，使后续维护者能验证它仍然有效。
- SETUP 脚本消除隐藏前置条件，让工作流可重复。
- 手动说明帮助人在自动化失败或上手培训时复现相同行为。
- Traceability 避免示例逐渐偏离 UserGuide 行为、用户故事和验收标准。

## Inputs

- 必需：要演示的 UserGuide 或工作流文档。
- 当存在时必需：该工作流匹配的 UserStories 和验收标准。
- 必需：功能、命令、API 或工作流名称。
- 建议：相关用户故事或验收标准。
- 建议：既有测试框架、夹具惯例和项目设置命令。
- 可选：目标 demo 名称、输出目录、平台限制，以及 demo 应完全自动化还是以手动为主。

## Output

- 一个 demo 包，通常结构如下：

  ```text
  tests/demo/<demo-name>/
    README.md
    ManualInstruction.md
    SETUP.sh
    RUN.sh
    CLEANUP.sh
    demo_manifest.json
    fixtures/
    expected/
    outputs/        # 生成内容，按需忽略或清理
    test_<demo_name>.<ext>
  ```

- 一个 traceability 区块，链接到 UserGuide 章节、User Story ID 和可用的 AC ID。
- 可幂等执行的 setup/run/cleanup 脚本，可从干净 checkout 运行。
- 手动说明，包含前置条件、设置、运行、期望结果、故障排查、清理和证据采集。
- 验证证据，说明执行了哪些脚本或测试。

## Constraints

- 不要编造 CLI 参数、文件、输出或产品行为。写 demo 之前先阅读 UserGuide、UserStories 和现有实现。
- 当 UserStories/AC 存在时，不要把仅覆盖 UserGuide 的用法示例视为充分；demo 必须同时展示如何使用该工作流，以及它满足哪条用户可见需求。
- Demo 应小而确定。优先使用本地夹具仓库、样例 JSON、临时目录和生成输出，避免网络依赖。
- 脚本必须幂等、快速失败，并避免破坏 demo 目录或显式配置临时目录之外的内容。
- `ManualInstruction.md` 必须让没有读过对话的人也能理解。
- 除非是有意提交的 expected fixture，否则不要把生成输出纳入版本控制。
- 如果功能尚未实现，创建 planned demo 包，并将可执行测试标记为 RED 或 blocked，而不是假装已通过。

## One More Thing

如果有任何不清楚、缺失或冲突的地方，请在继续执行之前停止并向用户询问。Stop and ask the user before proceeding.

## How

### Phase 1: 阅读用户工作流

1. 阅读相关 UserGuide、README 和 UserStories，直到足以理解目标工作流和需求意图。
2. 从 UserGuide 中提取精确的用户可见命令、API 调用、输入文件、输出文件和成功标准。
3. 从 UserStories 中提取匹配的 AS A / I WANT / SO THAT 用户故事以及 GIVEN / WHEN / THEN 验收标准。
4. 找到能同时证明工作流和匹配故事/AC 的最小 demo 场景。先优先 happy path，只有 UserGuide 或 UserStories 要求时再增加边界 demo。
5. 记录 traceability：UserGuide 章节名、用户故事 ID、AC ID，以及涉及的协议或契约文件。

### Phase 2: 设计 Demo 包

1. 选择清晰的 demo 名称，例如 `aggregate-core-metrics-demo` 或 `cli-basic-usage-demo`。
2. 遵循项目既有测试或示例布局。若不存在惯例，创建 `tests/demo/<demo-name>/`。
3. 复制或改写这些内置模板：
   - `assets/README.template.md` -> `README.md`。
   - `assets/ManualInstruction.template.md` -> `ManualInstruction.md`。
   - `assets/SETUP.template.sh` -> `SETUP.sh`。
   - `assets/RUN.template.sh` -> `RUN.sh`。
   - `assets/CLEANUP.template.sh` -> `CLEANUP.sh`。
   - `assets/demo_manifest.template.json` -> `demo_manifest.json`。
   - `assets/test_case.template.md` 作为自动化 demo 测试的设计来源。
4. 创建 `fixtures/` 保存 demo 输入，创建 `expected/` 保存期望输出或对比数据。

### Phase 3: 构建可重复脚本

1. 让 `SETUP.sh` 将 demo 所需的一切创建或复制到本地工作目录。
2. 让 `RUN.sh` 精确执行 UserGuide 描述的用户可见工作流。
3. 让 `CLEANUP.sh` 删除临时工作内容，但不删除已提交的 fixtures 或 expected 结果。
4. 使用 `set -euo pipefail`，从脚本位置推导路径，并输出简短状态消息。
5. 避免硬编码绝对路径。如果需要工具路径，通过环境变量传入，并在 `ManualInstruction.md` 中记录。

### Phase 4: 编写 Demo 测试

1. 优先使用仓库既有测试框架和语言。
2. 按 SETUP -> BEHAVIOR -> VERIFY -> CLEANUP 组织测试。
3. 验证用户可见输出，而不是私有实现细节。
4. Demo 应广而浅：从用户角度证明工作流，而不是穷尽每个分支。
5. 如果不适合自动化，清楚写出测试规格和手动验证路径，并将状态标记为 manual-only。

### Phase 5: 验证并报告

1. 在可行时运行 `SETUP.sh`、`RUN.sh` 和 demo 测试。
2. 当生成了 demo 目录时，运行本技能的校验器：

   ```bash
    python3 .github/skills/test-case-with-demo/scripts/check_demo_case.py tests/demo/<demo-name>
   ```

3. 将实际输出与 `expected/`、UserGuide 输出契约以及链接的 UserStories/AC 期望结果比较。
4. 更新 `README.md`、`ManualInstruction.md` 和 `demo_manifest.json` 中的 demo 状态。
5. 报告创建了什么、它演示了哪条 UserGuide 路径和哪些 UserStories/AC，以及运行了哪些命令/测试。

## Resources

- `assets/README.template.md` - demo 包 README 模板。
- `assets/ManualInstruction.template.md` - 手动运行手册模板。
- `assets/SETUP.template.sh` - setup 脚本模板。
- `assets/RUN.template.sh` - run 脚本模板。
- `assets/CLEANUP.template.sh` - cleanup 脚本模板。
- `assets/demo_manifest.template.json` - traceability manifest 模板。
- `assets/test_case.template.md` - demo 测试设计模板。
- `scripts/check_demo_case.py` - 生成 demo 包的轻量校验器。

## Validation

1. 确认技能 frontmatter 包含 `name: test-case-with-demo`，并且 `description` 已加引号。
2. 确认生成的 demo 包包含 `README.md`、`ManualInstruction.md`、`SETUP.sh`、`RUN.sh`、`CLEANUP.sh` 和 `demo_manifest.json`。
3. 确认 `ManualInstruction.md` 包含 Purpose、Prerequisites、Setup、Run、Expected Result、Troubleshooting、Cleanup 和 Evidence 章节。
4. 确认 demo 映射到真实 UserGuide 章节、User Story ID 和可用 AC ID。
5. 在可行时运行生成脚本和自动化测试；如果不可行，准确记录阻塞原因。
