# improve-existing-skill

## 概述 (Overview)

使用场景: 已应用现有技能但未完全解决问题，用户在对话中进一步迭代以达到有效解决方案，并要求“改进此技能”时。有助于: 使用对话中学到的、超出原始技能涵盖范围的经验教训更新现有的SKILL.md。适用于: .github/skills/ 等目录中的现有技能包。

该工作流本身是一个 **COMPLEX** 元技能：它会识别有证据支撑的缺口、判断更新范围、保持原技能身份不变，并通过独立验收门验证修订结果，而不是把“文件被改了”当作成功。

## 使用方法 (Usage)

触发此技能以执行定义的工作流。有关特定的触发条件和输入，请参阅 `SKILL.md`。

常见触发语句包括：

- “improve this skill”
- “update the skill”
- “the skill needs fixing”
- “make this skill better”
- “this skill didn't work”

## 结构 (Structure)

- [SKILL.md](./SKILL.md): 技能的核心工作流和定义。

## 为什么以前不容易被激活

- 关键触发语句原本主要写在 `## When`，而不是 frontmatter `description`。
- 自动激活通常更依赖 frontmatter 的发现面，所以过于抽象的描述会削弱路由效果。
- 现在的修订把精确触发语句和 near-miss 边界放进了 frontmatter，使模型更容易把这项技能选出来。
