# scaffold-cmake-cxx-sanitize-gtest-env

## 概述 (Overview)
WHEN/WHERE/WHO: [Scheduling: 当AI智能体需要使用稳健的测试和安全护栏来引导C/C++项目时使用。]
HOW: [Structural: 使用此技能注入标准化的CMakeLists.txt（自动发现Google Tests并支持Clang/GCC Sanitizers），并生成构建指南。]
WHY: [Scheduling: 确保所有C/C++项目都具有统一、安全且易于测试的基线环境，而无需手动配置。]

## 使用方法 (Usage)
触发此技能以执行定义的工作流。有关特定的触发器和输入，请参见 `SKILL.md`。

## 结构 (Structure)
- [SKILL.md](./SKILL.md): 技能的核心工作流和定义。
- [details/cmake-template.md](./details/cmake-template.md): 稳健的CMake配置模板。
- [details/readme-build-run-test-template.md](./details/readme-build-run-test-template.md): 开发人员指南的模板。
- [details/vscode-settings-template.md](./details/vscode-settings-template.md): VSCode CMake和Clangd集成的模板。
