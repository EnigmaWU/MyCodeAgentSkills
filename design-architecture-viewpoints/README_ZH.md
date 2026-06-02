# 设计架构视点 (Design Architecture Viewpoints)

用于应用 Nick Rozanski 和 Eóin Woods 所著《软件系统架构：使用视点和视角与利益相关者合作》(Software Systems Architecture: Working with Stakeholders using Viewpoints and Perspectives) 中多视图架构定义与分析方法的 Agent 技能。

## 什么是 design-architecture-viewpoints

开发人员在编写架构文档时，往往只从自身的开发技术视角出发，而忽略了运维人员、维护人员、支持团队和业务收购方的诉求。该技能指导 AI 编码 Agent 从多元利益相关者视点（功能视点、部署视点、运行视点、并发视点等）设计并核算架构，并应用横切质量视角（安全、性能、可用性、演化）进行检验。

## 目录结构

```text
design-architecture-viewpoints/
  ├── SKILL.md                                 # Level-1: 主技能工作流 (COMPLEX 层级)
  ├── references/
  │   └── Software systems architecture.pdf    # 原始教材 PDF (用户自行拷贝)
  └── details/                                 # 结构化参考资料
      ├── viewpoints-and-perspectives-reference.md  # Level-2: 视点与视角总览与一致性检查矩阵
      ├── functional-viewpoint-details.md      # Level-3: Ch 17 功能视点 (Functional Viewpoint) 详细指南
      ├── deployment-viewpoint-details.md      # Level-3: Ch 21 部署视点 (Deployment Viewpoint) 详细指南
      ├── security-perspective-details.md      # Level-3: Ch 25 安全视角 (Security Perspective) 详细检查清单
      └── performance-perspective-details.md   # Level-3: Ch 26 性能与可伸缩性视角 详细检查清单
```

## 为什么这一方法至关重要

在扩展复杂软件系统时，各个架构维度之间经常会出现冲突（例如：代码组织结构与进程线程模型冲突，或者与物理虚机拓扑冲突）。此技能协助 Agent 通过以下步骤解决这些问题：
1. **利益相关者与场景识别**：定义系统相关利益者（收购方、开发方、运维方、用户等）以及对其至关重要的场景（用例场景、增长场景、探索场景）。
2. **多视图目录定义**：草拟不同视图（如部署 VPC 网络拓扑、数据库并发锁模型、开发包目录结构等）。
3. **横切视角应用**：在每个视图之上叠加安全、性能、可用性与演化能力的检查。
4. **视图间一致性检查**：执行两两对齐检查，确保功能视图、开发视图、并发视图以及部署视图中的组件映射关系完全一致，无冲突漏洞。

## 使用方法

在编写系统架构文档或设计复杂系统架构时，可通过以下触发词唤醒此技能：
* *“记录该系统的架构视点和视图”*
* *“为该系统创建部署视点图”*
* *“对该架构执行视图间一致性检查”*

Agent 将读取 `details/` 目录下的视点指南与检查表，确保输出的架构说明书在内部各视图完全对齐，符合全部利益相关者的核心利益。
