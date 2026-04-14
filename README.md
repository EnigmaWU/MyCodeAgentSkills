# MyCodeAgentSkills

## Use as SubModule

You can integrate **MyCodeAgentSkills** into your own project as a Git submodule, making the skills available to your code agent under `.github/skills`.

### Add the submodule

Run the following command from the root of your repository:

```bash
git submodule add https://github.com/EnigmaWU/MyCodeAgentSkills.git .github/skills
```

This will clone `MyCodeAgentSkills` into the `.github/skills` directory of your project and register it as a submodule in `.gitmodules`.

### Initialize and update

When cloning a project that already includes this submodule, use:

```bash
git clone --recurse-submodules <your-repo-url>
```

Or, if you have already cloned the project without `--recurse-submodules`:

```bash
git submodule update --init --recursive
```

### Keep the submodule up to date

To pull the latest changes from `MyCodeAgentSkills`:

```bash
git submodule update --remote .github/skills
```

Then commit the updated submodule reference in your repository:

```bash
git add .github/skills
git commit -m "chore: update MyCodeAgentSkills submodule"
```

## 📦 Custom Skills Directory (VS Code Agent Mode)

By default, Copilot agent mode discovers skills in the following locations:

| Scope | Path |
|-------|------|
| Repository | `.github/skills/` |
| Repository | `.claude/skills/` |
| Repository | `.agents/skills/` |
| User | `~/.copilot/skills/` |

### Adding a custom skills directory

To load skills from an additional directory (for example `MySkills/`), add the `chat.agentSkillsLocations` setting to your `.vscode/settings.json` or VS Code user settings.

> **Note:** This setting **replaces** the default search paths, so include every directory you want Copilot to scan.

```jsonc
{
  "chat.agentSkillsLocations": [
    "${workspaceFolder}/.github/skills",
    "${workspaceFolder}/MySkills",
    "~/.copilot/skills"
  ]
}
```

Copilot will load skills from all listed directories when running in agent mode.

### Further reading

- [VS Code — Agent mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode)
- [GitHub Copilot documentation](https://docs.github.com/en/copilot)
