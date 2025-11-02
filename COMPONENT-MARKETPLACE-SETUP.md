# Component Marketplace Setup Guide

This guide explains how to enable individual component installation for the education-toolkit (e.g., `/agent add widget-designer@education-toolkit`).

## What We Created

### 1. `generate_components_json.py`
Python script that scans `agents/`, `commands/`, and `skills/` directories and generates a catalog file (`docs/components.json`).

**What it does:**
- Reads all agent .md files, extracts frontmatter metadata
- Reads all command .md files
- Reads all skill SKILL.md files
- Categorizes components (widget-design, assessment, accessibility, etc.)
- Generates `docs/components.json` with full file content and metadata

**Run it:**
```bash
python generate_components_json.py
```

**Output:**
- `docs/components.json` (401 KB)
- Summary report with category breakdown

---

### 2. `docs/` Directory
Static website for component catalog, hosted via GitHub Pages.

**Files:**
- `docs/index.html` - Human-readable component browser
- `docs/components.json` - Machine-readable catalog (used by Claude Code marketplace)

---

## Setup Instructions

### Step 1: Enable GitHub Pages

1. **Push docs/ to GitHub:**
   ```bash
   cd C:\Users\james\OneDrive\Documents2\GitHub\education-toolkit
   git add docs/ generate_components_json.py COMPONENT-MARKETPLACE-SETUP.md
   git commit -m "Add component marketplace catalog"
   git push origin main
   ```

2. **Enable GitHub Pages:**
   - Go to: https://github.com/jkruckivey/education-toolkit/settings/pages
   - Source: Deploy from a branch
   - Branch: `main`
   - Folder: `/docs`
   - Click **Save**

3. **Wait 1-2 minutes for deployment**

4. **Verify it works:**
   - Visit: `https://jkruckivey.github.io/education-toolkit/`
   - Should see component catalog website
   - Visit: `https://jkruckivey.github.io/education-toolkit/components.json`
   - Should see JSON catalog

---

### Step 2: Update Marketplace Configuration

Once GitHub Pages is live, you'll need to tell the Claude Code marketplace where to find your component catalog.

**Add to `.claude-plugin/marketplace.json`:**

```json
{
  "$schema": "https://raw.githubusercontent.com/anthropics/claude-code/main/.claude-plugin/marketplace.schema.json",
  "name": "education-toolkit",
  "version": "2.8.0",
  "description": "...",
  "owner": {
    "name": "James Kruck",
    "email": "jkruck@ivey.ca",
    "github": "jkruckivey"
  },
  "componentsCatalog": {
    "url": "https://jkruckivey.github.io/education-toolkit/components.json"
  },
  "plugins": [
    {
      "name": "education-toolkit",
      "description": "...",
      "source": "./",
      "category": "education",
      "version": "2.8.0",
      "author": {
        "name": "James Kruck",
        "email": "jkruck@ivey.ca"
      }
    }
  ]
}
```

**Key addition:** `"componentsCatalog"` field with URL to your hosted `components.json`.

---

### Step 3: Test Individual Component Installation

Once GitHub Pages is live and marketplace.json is updated:

```bash
# Test installing individual agent
/agent add widget-designer@education-toolkit

# Test installing individual command
/command add design-assessment@education-toolkit

# Test installing individual skill
/skill add assessment-template-generator@education-toolkit
```

---

## Maintenance

### Updating the Catalog

Whenever you add/modify agents, commands, or skills:

1. **Regenerate catalog:**
   ```bash
   python generate_components_json.py
   ```

2. **Commit and push:**
   ```bash
   git add docs/components.json
   git commit -m "Update component catalog"
   git push origin main
   ```

3. **GitHub Pages auto-updates** (1-2 min delay)

---

## How It Works

### Installation Flow

When user runs `/agent add widget-designer@education-toolkit`:

1. Claude Code reads marketplace.json
2. Finds `componentsCatalog.url`
3. Fetches `components.json` from GitHub Pages
4. Searches for `widget-designer` in `agents` array
5. Extracts `content` field (full markdown)
6. Writes to user's `.claude/plugins/education-toolkit/agents/widget-designer.md`

### Category Structure

Components are auto-categorized by the script:

| Category | Agent Count | Command Count | Skill Count | Total |
|----------|-------------|---------------|-------------|-------|
| widget-design | 3 | 1 | 0 | 4 |
| assessment | 3 | 2 | 2 | 7 |
| accessibility | 2 | 0 | 1 | 3 |
| course-design | 2 | 2 | 0 | 4 |
| validation | 2 | 2 | 0 | 4 |
| review-testing | 3 | 3 | 0 | 6 |
| content | 2 | 0 | 0 | 2 |

**Total:** 17 agents, 10 commands, 3 skills = **30 components**

---

## Comparison: Bundle vs Individual

### Plugin Bundle Installation
```bash
/plugin install education-toolkit
```
- Installs all 30 components at once
- User gets entire toolkit
- Recommended for most users

### Individual Component Installation
```bash
/agent add widget-designer@education-toolkit
/command add design-assessment@education-toolkit
```
- Install only what's needed
- Smaller footprint
- Good for specific use cases

---

## Troubleshooting

### components.json not accessible
- **Check GitHub Pages status:** Settings > Pages
- **Verify URL:** https://jkruckivey.github.io/education-toolkit/components.json
- **Check file exists:** `docs/components.json` should be in repo

### Individual installation fails
- **Verify marketplace.json has `componentsCatalog` field**
- **Check component name matches catalog** (case-sensitive)
- **Ensure category/path is correct** in components.json

### Catalog out of date
- **Regenerate:** `python generate_components_json.py`
- **Push to GitHub:** `git push origin main`
- **Wait 1-2 min** for GitHub Pages to rebuild

---

## Next Steps

1. ✅ Generated `components.json` catalog
2. ✅ Created `docs/index.html` website
3. ⏳ Enable GitHub Pages (see Step 1)
4. ⏳ Update `.claude-plugin/marketplace.json` with `componentsCatalog` URL (see Step 2)
5. ⏳ Test individual component installation (see Step 3)

---

**Questions?**
- Check: https://github.com/anthropics/claude-code/discussions
- Reference: https://github.com/davila7/claude-code-templates (see their components.json structure)
