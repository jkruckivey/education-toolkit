# GitHub Repository Setup Instructions

## Step 1: Create GitHub Repository

1. Go to: https://github.com/new
2. Fill in the form:
   - **Repository name**: `education-toolkit`
   - **Description**: `Claude Code plugin with 7 specialized agents and 6 slash commands for course developers: accessibility auditing, widget testing, assessment design, student journey simulation, consistency checking, and UDL content generation`
   - **Visibility**: ✅ Public
   - **DO NOT** initialize with README, .gitignore, or license (we already have these)
3. Click "Create repository"

## Step 2: Push Local Repository to GitHub

After creating the repository, run these commands:

```bash
cd "C:/Users/jkruck/Ivey Business School/EdTech Lab - Documents/Github/education-toolkit"

# Add GitHub as remote origin
git remote add origin https://github.com/jameskruck/education-toolkit.git

# Push to GitHub
git push -u origin main
```

## Step 3: Verify Repository

1. Visit https://github.com/jameskruck/education-toolkit
2. Verify these files are visible:
   - README.md with complete documentation
   - .claude-plugin/plugin.json
   - agents/ directory with 8 agents (7 .md files + assessment-knowledge folder)
   - commands/ directory with 6 slash commands
   - LICENSE file

## Step 4: Create Marketplace Configuration (Optional)

If you want to add this plugin to the official Claude Code marketplace:

1. Create `.claude-plugin/marketplace.json` at the root of the repository:

```json
{
  "$schema": "https://raw.githubusercontent.com/anthropics/claude-code/main/.claude-plugin/marketplace.schema.json",
  "name": "education-toolkit",
  "version": "1.0.0",
  "description": "Comprehensive toolkit for course developers with 7 specialized agents and 6 slash commands",
  "owner": {
    "name": "James Kruck",
    "email": "jkruck@ivey.ca",
    "github": "jameskruck"
  },
  "plugins": [
    {
      "name": "education-toolkit",
      "description": "7 agents + 6 commands for accessibility, assessment design, widget testing, and course QA",
      "source": "./",
      "category": "education",
      "version": "1.0.0",
      "author": "James Kruck"
    }
  ]
}
```

2. Commit and push:

```bash
git add .claude-plugin/marketplace.json
git commit -m "Add marketplace configuration"
git push
```

## Step 5: Test Installation

After pushing to GitHub, test the plugin installation:

```bash
/plugin marketplace add jameskruck/education-toolkit
/plugin install education-toolkit
```

Verify installation:
- Check that slash commands appear in command palette
- Try invoking agents with natural language
- Test a few commands like `/audit-module` or `/test-widget`

## Repository URLs

- **Repository**: https://github.com/jameskruck/education-toolkit
- **Issues**: https://github.com/jameskruck/education-toolkit/issues
- **Clone URL**: https://github.com/jameskruck/education-toolkit.git

## Adding Topics/Tags (Recommended)

On the GitHub repository page, click "Add topics" and add:
- `claude-code`
- `claude-code-plugin`
- `education`
- `accessibility`
- `wcag`
- `udl`
- `quality-matters`
- `assessment-design`
- `course-development`
- `pedagogical-qa`

This makes the plugin more discoverable!
