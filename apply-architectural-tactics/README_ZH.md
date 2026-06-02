# 应用架构战术 (Apply Architectural Tactics)

用于应用 Len Bass、Paul Clements 和 Rick Kazman 所著《软件架构实践》(Software Architecture in Practice, SAiP) 中系统化软件架构设计方法的 Agent 技能。

## 什么是 apply-architectural-tactics

该技能指导 AI 编码 Agent 执行以**质量属性**（非功能性需求）为驱动的结构化架构设计与分析，而非随意凭直觉选择技术。它能有效防止 Agent 在未分析系统可用性、可修改性、性能、安全性和可测试性目标之前，就直接引入具体的中间件或库。

## 目录结构

```text
apply-architectural-tactics/
  ├── SKILL.md                                 # Level-1: 主技能工作流 (COMPLEX 层级)
  ├── references/
  │   └── Software Architecture in Practice.pdf # 原始教材 PDF (用户自行拷贝)
  └── details/                                 # 结构化参考资料
      ├── quality-attribute-tactics-and-checklists.md  # Level-2: 架构战术总览与设计清单
      ├── availability-checklist-details.md    # Level-3: Ch 5 可用性 (Availability) 详细设计清单
      ├── performance-checklist-details.md     # Level-3: Ch 8 性能 (Performance) 详细设计清单
      ├── security-checklist-details.md        # Level-3: Ch 9 安全性 (Security) 详细设计清单
      └── modifiability-checklist-details.md   # Level-3: Ch 7 可修改性 (Modifiability) 详细设计清单
```

## 为什么这一方法至关重要

LLM Agent 在设计软件架构时经常会过度倾向于某种特定技术或给出虚假的配置参数。此技能强制 Agent 遵循 **属性驱动设计 (ADD)** 方法：
1. **效用树与 QAS (质量属性场景)**：将模糊的口号（如“快速响应”）量化为包含六要素（源、刺激、制品、环境、响应、响应度量）的可衡量场景。
2. **战术目录 (Tactics)**：在挑选具体技术前，先从书中选择经过验证的架构战术（如主动冗余、缓存、封装等）。
3. **ATAM (架构权衡分析方法)**：进行权衡分析，识别出敏感点（如数据库复制因子）和风险点。
4. **CBAM (成本效益分析方法)**：引入经济考量，计算设计选择的投资回报率 (ROI)。

## 使用方法

在设计或审查系统架构时，可通过以下触发词唤醒此技能：
* *“应用软件架构战术对该系统进行设计”*
* *“使用 SAiP 战术为 [需求] 设计系统”*
* *“评估该架构的质量属性场景”*

Agent 将加载 `details/` 目录中的摘要和详细设计清单，自动生成结构化、高可信度的架构设计文件。
