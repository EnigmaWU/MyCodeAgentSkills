# update-my-resume

## 概述 (Overview)
使用场景: 用户刚解决了一个问题，完成了一项任务，结束了调试会话，或要求“更新我的简历”时。有助于: 分析用户展示的新技能，然后编写包含问题、步骤和结果的结构化中英文简历条目。适用于: 根目录或$HOME下的 .resume 文件。

## 使用方法 (Usage)
触发此技能以执行定义的工作流。有关特定的触发条件和输入，请参阅 `SKILL.md`。

## 结构 (Structure)
- [SKILL.md](./SKILL.md): 技能的核心工作流和定义。
- [scripts/validate_resume_entry.py](./scripts/validate_resume_entry.py): 确定性校验脚本，检查条目日期、字段完整性与顺序、EN/ZH 双区段配对，校验通过（exit 0）才可交付。
