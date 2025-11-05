# Agent Registration Troubleshooting Guide

## Problem
Agents aren't getting registered correctly - Claude Code sees the plugin and can find the agent directory when path is pasted, but agents can't be "deployed" or invoked.

## Fixes Applied (Commits 8ae263b, 441226d)

### 1. Changed Agent Discovery from Directory to Explicit Array

**Before** (directory-based discovery):
```json
// plugin.json & marketplace.json
"agents": "./agents"
```

**After** (explicit file listing):
```json
// Both files now have:
"agents": [
  "./agents/accessibility-auditor.md",
  "./agents/assessment-consistency-checker.md",
  // ... (all 17 agents listed explicitly)
]
```

### 2. Validated All Agent YAML Frontmatter

✅ **All 17 agents have valid YAML frontmatter** with required fields:
- `name` (kebab-case, matches filename)
- `description` (clear, actionable)
- `tools` (Read, Write, Edit, Glob, Grep, WebFetch, Bash, Skill)
- `model` (sonnet or opus)

## Current Repository Structure

```
education-toolkit/
├── .claude-plugin/
│   ├── marketplace.json  (explicit agents array)
│   └── plugin.json       (explicit agents array)
├── agents/               (17 .md files, all valid YAML)
│   ├── accessibility-auditor.md
│   ├── assessment-consistency-checker.md
│   ├── assessment-designer.md
│   ├── backend-reviewer.md
│   ├── branding-checker.md
│   ├── cohort-structure-checker.md
│   ├── concept-threading-checker.md
│   ├── course-outline-creator.md
│   ├── frontend-reviewer.md
│   ├── peer-review-simulator.md
│   ├── rubric-generator.md
│   ├── student-journey-simulator.md
│   ├── terminology-consistency-checker.md
│   ├── udl-content-generator.md
│   ├── uplimit-storyboard-builder.md
│   ├── widget-designer.md
│   └── widget-tester.md
├── commands/             (14 .md files)
├── hooks/                (5 hook scripts)
└── skills/               (3 skill directories)
```

## Testing Instructions

### 1. Remove Old Installation

```bash
# Windows
rd /s /q "%USERPROFILE%\.claude\plugins\education-toolkit"
rd /s /q "%USERPROFILE%\.claude\plugins\marketplaces\education-toolkit-marketplace"

# macOS/Linux
rm -rf ~/.claude/plugins/education-toolkit
rm -rf ~/.claude/plugins/marketplaces/education-toolkit-marketplace
```

### 2. Install Fresh from GitHub

```bash
/plugin add jameskruck/education-toolkit
```

### 3. Verify Installation

**Check installed files**:
```bash
# Windows
dir "%USERPROFILE%\.claude\plugins\education-toolkit"

# macOS/Linux
ls -la ~/.claude/plugins/education-toolkit/
```

**Should see**:
- `.claude-plugin/marketplace.json`
- `.claude-plugin/plugin.json`
- `agents/` (17 .md files)
- `commands/` (14 .md files)
- `hooks/`
- `skills/`

### 4. Test Agent Invocation

**Method 1: Natural language**
```
Use uplimit-storyboard-builder to audit this storyboard
```

**Method 2: Direct invocation** (if natural language fails)
```
Run the widget-designer agent to create a new quiz widget
```

**Method 3: Check available agents**
```
What agents are available to you?
```

## Expected Behavior vs Current Issue

### Expected ✅
- Agents automatically registered when plugin installed
- Agents appear in available agents list
- Natural language invocation works
- Direct agent names work

### Current Issue ❌
- Plugin installs successfully
- Agent files visible when path pasted
- But agents can't be "deployed" - **why?**

## Possible Remaining Issues

### 1. Path Resolution Problem
- Maybe Claude Code can't resolve `./agents/...` paths correctly?
- **Test**: Try absolute paths in marketplace.json/plugin.json?

### 2. Agent Name Conflicts
- Maybe agent names conflict with built-in agents?
- **Check**: Do any agent names match system agents?

### 3. YAML Parsing Runtime Issue
- Frontmatter validates locally but fails in Claude Code?
- **Test**: Try simplifying one agent's frontmatter to minimal fields

### 4. Marketplace vs Plugin Conflict
- Having agents in both files causing issues?
- **Test**: Try removing agents from marketplace.json, keep only in plugin.json?

### 5. Strict Mode Issue
- `strict: true` might require something we're missing?
- **Test**: Try `strict: false` in marketplace.json?

## Diagnostic Commands

**If you can access the installed plugin directory**:

```bash
# Check plugin.json was installed correctly
cat ~/.claude/plugins/education-toolkit/.claude-plugin/plugin.json | grep -A 5 "agents"

# Count agent files
ls ~/.claude/plugins/education-toolkit/agents/*.md | wc -l

# Check first agent's frontmatter
head -7 ~/.claude/plugins/education-toolkit/agents/accessibility-auditor.md

# Check for any permission issues
ls -la ~/.claude/plugins/education-toolkit/agents/
```

## Next Steps to Try

### Option 1: Simplify to Test One Agent

Temporarily modify marketplace.json/plugin.json to include ONLY one agent:

```json
"agents": ["./agents/accessibility-auditor.md"]
```

If this works, it narrows down the issue (maybe too many agents at once?).

### Option 2: Try strict: false

Change marketplace.json:
```json
"strict": false
```

This makes plugin.json optional and uses marketplace.json as the complete manifest.

### Option 3: Remove marketplace agents field

Try letting plugin.json handle agents entirely:

```json
// marketplace.json - remove agents field
{
  "plugins": [{
    "name": "education-toolkit",
    "source": "./",
    "strict": true
    // NO agents field here
  }]
}

// plugin.json - keeps agents array
{
  "agents": [...array of 17 agents...]
}
```

## Contact Points

If issue persists:
- **GitHub Issues**: https://github.com/jkruckivey/education-toolkit/issues
- **Claude Code Docs**: https://docs.claude.com/en/docs/claude-code/plugins
- **Error messages**: Please share exact error text when agents "can't be deployed"

## Current Branch Status

- **Branch**: `claude/debug-repo-issues-011CUpz7MTkHrP8Jgwbm7zmC`
- **Latest commits**:
  - `441226d` - Explicit agents array in plugin.json
  - `8ae263b` - Explicit agents array in marketplace.json
  - `1d47f0c` - Restored marketplace.json
  - `245c312` - Restructured to root-level

Ready to merge and test!
