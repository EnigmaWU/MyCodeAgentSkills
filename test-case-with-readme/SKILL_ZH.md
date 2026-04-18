---
name: test-case-with-readme
description: '使用场景：当用户创建一个新的测试用例、打算编写一个测试、或者要求为已有的测试生成 readme 文档时使用。帮助解决：为测试文件规划并记录结构化的目的、状态、覆盖范围和手动执行步骤。适用于：任何测试创建工作流或现有的测试文件（如 .py、.cxx 等）。'
---

# 附带Readme的测试用例

## Who
需要以一致的结构来记录单个测试用例的开发人员、QA 工程师或智能体（Agents）。

## What
为给定的测试用例文件生成一个配套的 markdown readme 文档。对于名为 `test_something.ext`（例如 `test_user_story.py`）的测试文件，它会创建相应的 `test_something_readme.md`（例如 `test_user_story_readme.md`）。该 readme 包含特定的结构化部分：目的（Purpose）、状态（Status）、覆盖范围（Covered）和手动测试步骤（Manual）。该技能既可防御性地用于记录已有测试，也可主动作为一种规划工具，在编写测试代码之前设计测试的边界。

## When
- 用户或智能体创建了一个新的测试用例文件。
- 用户正在规划或准备编写一个新的测试用例，触发“readme 先行”的规划方法。
- 用户要求“为一个测试用例创建 readme”。
- 用户提供了一个现有的测试文件并要求为其编写文档。
- 用户明确调用 `test-case-with-readme` 技能。

## Where
- 默认情况下，生成的 readme 文件应与目标测试文件存放在同一目录，除非用户另有指定。

## Why
- 通过在实现之前规范测试意图和范围，促进测试规划和测试驱动开发（TDD）。
- 在不同的语言和框架中保持测试文档的一致性。
- 帮助跟踪单个测试的状态、范围和覆盖率。
- 如果需要手动执行步骤或环境设置要求，可以有一个清晰的地方来记录它们。

## Inputs
- **测试用例文件**（必填）：测试文件的路径或内容（例如 `test_user_story.py`）。
- **附加背景信息**（选填）：用户希望包含的关于目的、状态、覆盖范围或手动步骤的任何具体细节。

## Output
一个名为 `<不带扩展名的测试文件名>_readme.md`（例如 `test_user_story_readme.md`）的 markdown 文件，具有以下结构：

```markdown
# Test Case: <测试名称>

## Purpose
<描述此测试用例正在验证什么，以及它针对的业务逻辑或边缘情况。>

## Status
<测试的当前状态：例如 规划中 (Planned)、草稿 (Draft)、已实现 (Implemented)、通过 (Passing)、失败 (Failing)、不稳定 (Flaky)>

## Covered
<此测试明确覆盖的需求、用户故事、函数或特定代码路径的列表。>

## Manual
<手动运行或重现此测试所需的步骤，包括任何必要的手动设置或清理工作。>
```

## Example

### Target Test File
`test_payment_gateway.py`（尚未编写代码，处于规划阶段）

### Output (`test_payment_gateway_readme.md`)
```markdown
# Test Case: test_payment_gateway

## Purpose
该测试验证支付网关与 Stripe API 的集成，重点核对成功扣款和信用卡被拒绝时的优雅错误处理。

## Status
Planned / Draft

## Covered
- 通过 `StripeClient.charge()` 实现的成功扣款流程。
- 对于 `card_declined` API 异常的错误处理。
- 用户故事："使用信用卡结账"。

## Manual
1. 确保已导出环境变量 `STRIPE_TEST_KEY`。
2. 提供一个模拟的信用卡号。
3. 使用 `pytest test_payment_gateway.py -v` 运行测试。
```

## Constraints
- 请勿修改原始的测试代码文件。
- 确保生成的文件使用测试文件的准确基本名称，并附加 `_readme.md`（例如 `test_login.cxx` -> `test_login_readme.md`）。
- 分析测试代码以推断各部分的内容。如果某些细节无法推断，请使用占位符或明确向用户提问。

## One More Thing
如果有任何不清楚、缺失或冲突的地方，请在继续执行之前停止并向用户询问。

## How
1. **识别文件与意图**：确定目标测试文件名，并判断测试是已编写完成，还是正在规划/新建的阶段。
2. **确定输出文件名**：去掉文件扩展名并附加 `_readme.md`（例如 `test_user_story.py` 变为 `test_user_story_readme.md`）。
3. **分析或规划测试上下文**：
   - 如果测试代码尚不存在（规划阶段），推断或询问用户该测试的“目的（Purpose）”和“覆盖范围（Covered）”应该是什么。
   - 如果测试已存在，审查提供的测试代码以提取这些信息。
4. **生成 Markdown 文档**：按照确切的输出格式要求起草内容。如果测试尚未编写，请将“状态（Status）”标记为“Draft（草稿）”或“Planned（规划中）”。
5. **写入文件**：将生成的文档保存到目标 `.md` 文件（与被记录的测试用例存放于同级目录）中。
