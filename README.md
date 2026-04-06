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
