# Bug Fix Summary: Agent Registration Issue (CORRECTED)

## Problem Report

User reported that Education Toolkit agents were not being recognized by Claude Code:

```
Error: Agent type 'uplimit-storyboard-builder' not found.
Available agents: general-purpose, statusline-setup, Explore, Plan,
project-management-suite:product-strategist, project-management-suite:business-analyst
```

## Root Cause Analysis (CORRECTED)

**Initial diagnosis was PARTIALLY WRONG.** The actual issue was more nuanced:

### What Was Wrong

The repository had:
```
education-toolkit/
├── .claude-plugin/
│   └── marketplace.json (source: "./plugins/education-toolkit")
└── plugins/
    └── education-toolkit/
        ├── .claude-plugin/plugin.json
        ├── agents/
        └── commands/
```

**Problem**: The `marketplace.json` pointed to `./plugins/education-toolkit`, but Claude Code was having issues with this nested structure.

### What I Initially Did Wrong

I initially **deleted marketplace.json entirely**, thinking single plugins don't need it. This was **incorrect**.

### The Actual Requirement

Per [Claude Code documentation](https://docs.claude.com/en/docs/claude-code/plugin-marketplaces):

> **Even single plugins require marketplace.json** when distributed via `/plugin add owner/repo`

The correct structure for a single plugin is:

```
education-toolkit/
├── .claude-plugin/
│   ├── marketplace.json  ← REQUIRED (source: "./")
│   └── plugin.json       ← REQUIRED
├── agents/               ← At root (not nested)
├── commands/
└── hooks/
```

## The Correct Solution

### 1. Flatten Directory Structure ✅ (This part was correct)

Moved from nested `plugins/education-toolkit/*` to root:
- `agents/` at root
- `commands/` at root
- `hooks/` at root
- `skills/` at root

### 2. Keep BOTH Configuration Files ✅ (Corrected)

**marketplace.json** - Required for `/plugin add` to find the plugin:
```json
{
  "name": "education-toolkit",
  "plugins": [
    {
      "name": "education-toolkit",
      "source": "./",  ← Points to root (where plugin.json is)
      "strict": true
    }
  ]
}
```

**plugin.json** - Defines what the plugin contains:
```json
{
  "name": "education-toolkit",
  "version": "2.8.5",
  "agents": "./agents",
  "commands": "./commands",
  "hooks": "./hooks/hooks.json",
  "skills": "./skills"
}
```

## How It Works

When users run `/plugin add jameskruck/education-toolkit`:

1. Claude Code fetches the repository
2. Looks for `.claude-plugin/marketplace.json`
3. Reads the `plugins` array
4. Finds entry with `source: "./"`
5. Looks in root directory for `.claude-plugin/plugin.json` (because `strict: true`)
6. Reads `plugin.json` to discover agents, commands, hooks, skills
7. Installs to `~/.claude/plugins/education-toolkit/`
8. Registers all 17 agents

## Key Insights

### Marketplace vs Single Plugin Confusion

- **Marketplace** = JSON file listing available plugins (can have 1+ entries)
- **Single plugin** = Still needs marketplace.json, just with ONE entry
- **Source field options**:
  - `"source": "./"` = Plugin at repository root
  - `"source": "./plugins/name"` = Plugin in subdirectory
  - `"source": { "source": "github", "repo": "..." }` = External repo

### Why Both Files?

- **marketplace.json** = Distribution layer ("where is the plugin?")
- **plugin.json** = Definition layer ("what does the plugin contain?")

Even for a single plugin, you need both files when distributing via `/plugin add`.

## Files Changed (Corrected)

### Initial Fix (Commits 245c312, fd67c5e, b30b6fa)
- ✅ Moved agents, commands, hooks, skills to root
- ❌ Deleted marketplace.json (WRONG - needed to restore it)
- ✅ Moved plugin.json to root
- ✅ Updated documentation

### Corrected Fix (This commit)
- ✅ **Restored marketplace.json** with `source: "./"`
- ✅ Both marketplace.json and plugin.json at `.claude-plugin/`
- ✅ Flattened structure (agents/ at root)

## The Correct Repository Structure

```
education-toolkit/                    # Single plugin repository
├── .claude-plugin/
│   ├── marketplace.json             # Distribution config (source: "./")
│   └── plugin.json                  # Plugin definition
├── agents/                          # 17 agents at root
│   ├── uplimit-storyboard-builder.md
│   ├── widget-designer.md
│   └── ... (15 more)
├── commands/                        # 14 commands at root
│   ├── build-storyboard.md
│   ├── design-widget.md
│   └── ... (12 more)
├── hooks/                           # 5 hooks at root
│   ├── hooks.json
│   └── scripts/
├── skills/                          # 3 skills at root
│   ├── assessment-template-generator/
│   ├── accessibility-audit-tools/
│   └── qm-validator/
├── assessment-knowledge/            # Bundled research
└── course-design-knowledge/         # Bundled guides
```

## Installation Now Works

```bash
# Single command installs everything
/plugin add jameskruck/education-toolkit

# Claude Code:
# 1. Fetches repo
# 2. Reads .claude-plugin/marketplace.json
# 3. Finds plugin at source: "./"
# 4. Reads .claude-plugin/plugin.json
# 5. Installs agents, commands, hooks, skills
# 6. All 17 agents registered ✓
```

## For Users with Old Installation

```bash
# Remove old installation (if exists)
# Windows:
rd /s /q "%USERPROFILE%\.claude\plugins\marketplaces\education-toolkit-marketplace"
rd /s /q "%USERPROFILE%\.claude\plugins\education-toolkit"

# macOS/Linux:
rm -rf ~/.claude/plugins/marketplaces/education-toolkit-marketplace
rm -rf ~/.claude/plugins/education-toolkit

# Install fresh with corrected structure
/plugin add jameskruck/education-toolkit

# Test
# Try: "Use uplimit-storyboard-builder to audit this storyboard"
```

## Lessons Learned

### Don't Skip marketplace.json

Even for single plugins distributed via `/plugin add owner/repo`, you need:
1. `.claude-plugin/marketplace.json` (distribution config)
2. `.claude-plugin/plugin.json` (plugin definition)

### When You DON'T Need marketplace.json

Only if installing via direct path:
```bash
/plugin add ./local/path/to/plugin
```

In this case, Claude Code looks directly for `plugin.json` at that path.

### When You DO Need marketplace.json

When distributing via:
- GitHub: `/plugin add owner/repo`
- Git: `/plugin add https://gitlab.com/repo.git`
- URL: `/plugin add https://url.of/marketplace.json`

## References

- [Plugin marketplaces documentation](https://docs.claude.com/en/docs/claude-code/plugin-marketplaces)
- [Plugin manifest schema](https://docs.claude.com/en/docs/claude-code/plugins-reference)

---

**Fixed by**: Claude Code (Sonnet 4.5)
**Date**: 2025-11-05
**Branch**: `claude/debug-repo-issues-011CUpz7MTkHrP8Jgwbm7zmC`
**Corrected**: After reviewing official documentation
