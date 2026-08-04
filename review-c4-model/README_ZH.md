# review-c4-model

按照 Simon Brown《The C4 Model: Visualizing Software Architecture》中的 C4 模型规则，
审查软件架构图。

## 功能

识别图表类型（系统上下文、容器、组件、代码、动态、部署或系统全景），运行书中关于
通用/元素/关系的检查清单，并结合各图类型的作用域规则，输出结论（通过、有条件通过、
不通过），每条问题都对应具体的规则与修复建议。

## 目录结构

```text
review-c4-model/
  ├── SKILL.md                       # 主流程（COMPLICATED 层级）
  ├── README.md                      # 英文说明
  ├── README_ZH.md                   # 本说明
  ├── agents/openai.yaml             # UI 元数据
  └── details/
      ├── review-checklist.md        # 完整 PASS/FAIL 检查清单
      ├── notation-reference.md      # 第 10 章记法指南
      ├── common-anti-patterns.md    # 常见问题与反驳
      └── validation-log.md          # 层级选择与验证证据
```

## 触发词

- “review / critique / check this architecture diagram”
- “is this a valid or correct C4 diagram”
- “find problems in this diagram”
- “does this diagram follow the C4 model”

## 使用方法

提供一张或多张图（图片、PDF 页面、图表代码或粘贴的内容），可附带图表类型或目标受众。
技能会返回结构化的审查报告。如需保存为文件，请明确说明。

本技能基于 Simon Brown《The C4 Model: Visualizing Software Architecture》
(O'Reilly, 2026)，并使用 `create-skill-from-book` 流程创建。
