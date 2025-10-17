# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

**Education Toolkit** - Claude Code plugin providing 10 specialized agents and 10 slash commands for educational developers, instructional designers, and course creators. Focus areas: accessibility (WCAG 2.2 AA), assessment design, UDL implementation, Quality Matters standards, AI-integrated pedagogy, and multi-perspective peer design review.

**Version**: 2.3.2 (October 2025)
**Tech stack**: Markdown-based agent definitions, bundled knowledge base (464 KB)
**Distribution**: Claude Code plugin marketplace (`/plugin marketplace add jameskruck/education-toolkit`)

## Architecture

### Plugin Structure

```
education-toolkit/
├── plugin.json              # Main plugin manifest
├── .claude-plugin/
│   └── marketplace.json     # Marketplace configuration
├── agents/                  # 10 specialized agents
│   ├── assessment-designer.md (27 KB, sonnet, 464 KB bundled knowledge)
│   ├── rubric-generator.md (11 KB, sonnet)
│   ├── accessibility-auditor.md (6 KB, sonnet, WebFetch)
│   ├── widget-tester.md (8 KB, sonnet, 3 personas)
│   ├── student-journey-simulator.md (6 KB, opus, 4 personas)
│   ├── consistency-checker.md (8 KB, opus)
│   ├── peer-review-simulator.md (15 KB, opus, 6 reviewer personas)
│   ├── branding-checker.md (10 KB, sonnet, Canvas/Uplimit)
│   ├── udl-content-generator.md (10 KB, sonnet)
│   ├── uplimit-storyboard-builder.md (26 KB, sonnet)
│   └── assessment-knowledge/  # Bundled knowledge base
│       ├── frameworks/        # UDL, QM, Inclusive Teaching, Templates
│       └── research/          # AI assessment research (5 papers)
└── commands/                  # 10 slash commands
    ├── audit-module.md
    ├── build-storyboard.md
    ├── check-branding.md
    ├── check-consistency.md
    ├── design-assessment.md
    ├── generate-rubric.md
    ├── peer-review.md
    ├── review-content.md
    ├── simulate-journey.md
    └── test-widget.md
```

### Agent vs Command Design Pattern

**Agents** (`.md` files in `agents/`):
- Autonomous subagents with specialized tools and model preferences
- YAML frontmatter: `name`, `description`, `tools`, `model`
- Invoked automatically by Claude Code when user requests match descriptions
- Self-contained prompt engineering with embedded knowledge

**Commands** (`.md` files in `commands/`):
- Quick-access slash commands for common workflows
- YAML frontmatter: `description` only
- Typically invoke agents with pre-configured parameters
- User-facing convenience layer over agent system

### Knowledge Base Bundling

The **assessment-designer** agent includes `assessment-knowledge/` directory with:
- **4 Framework Guides** (UDL, QM, Inclusive Teaching, Assessment Templates)
- **5 Research Papers** (AI Assessment Framework, Acceptable AI Use, Alternative Assessments, Academic Integrity, GenAI in Higher Ed)

**Access pattern**: Agents use relative paths from their installed location:
```bash
Read: assessment-knowledge/frameworks/udl-guide.md
Read: assessment-knowledge/research/acceptable-ai-use.md
```

## Key Concepts

### Evidence-Based Assessment Methodologies (v2.0)

**PAIRR (Peer and AI Review + Reflection)**:
- Dual-feedback methodology: students receive peer + AI feedback, then compare critically
- Research-backed (Frontiers in Communication, 2025)
- Develops AI literacy through structured comparison reflection
- Implementation: 80% draft → dual feedback → comparative reflection → revision → post-revision reflection

**AI Roleplay Exercises**:
- Conversational assessments with AI character roleplaying stakeholder/expert
- Three types: Diagnostic (pre-learning), Formative (practice), Summative (graded)
- Tests application/synthesis (higher Bloom's levels)
- Design components: Student instructions, AI character config, system prompt, rubric

**Diagnostic Rubrics (3-Level)**:
- Formative pre-learning rubrics: Beginning → Developing → Proficient
- No "Exemplary" (mastery not expected before learning)
- Support flags for scaffolding triggers
- Non-evaluative tone for formative use

### Persona-Based Testing

**Widget Tester (3 personas)**:
- Sarah (Quick Learner) - tech-savvy, skims instructions
- James (Methodical Analyst) - tests edge cases
- Maria (Struggling Student) - needs guidance, frustrated easily

**Student Journey Simulator (4 personas)**:
- Sarah (Visual Learner) - diagrams > text
- Marcus (Analytical Thinker) - wants data/sources
- Priya (Collaborative Leader) - thrives in groups
- Alex (Time-Constrained Professional) - needs efficiency

### Multi-Perspective Peer Design Review (v2.3)

**Peer Review Simulator (6 ID specialist reviewers)**:
- Emma (Content & Writing) - Grammar, clarity, inclusive language, readability
- Marcus (Accessibility & Inclusion) - WCAG 2.2 AA, UDL, assistive tech, cultural sensitivity
- Priya (Visual Design & UI) - Typography, layout, visual hierarchy, consistency
- James (Technical & Functionality) - Browser compatibility, performance, security, broken links
- Sarah (Pedagogical Design) - Learning alignment, Bloom's accuracy, scaffolding, assessment design
- Alex (UX & Navigation) - Information architecture, wayfinding, usability, mobile UX

**Key Features**:
- Comprehensive review: Every element analyzed by all 6 specialists
- Cross-reviewer themes: Issues flagged by 3+ reviewers = top priority
- Scoring system: Each reviewer scores 0-100, overall readiness calculated
- Prioritized action plan: Critical (block launch) → High → Medium → Low
- Fix time estimates: Helps prioritize based on effort

### AI Assessment Framework (Three-Tier Model)

Embedded in assessment-designer agent:
- **Tier 1: AI Prohibited** - High-stakes, individual competency verification
- **Tier 2: AI Permitted with Documentation** - Learning process, must document use
- **Tier 3: AI Required** - AI literacy development, critique AI outputs

**Design Principles** (AI-resistant tasks):
1. Highly contextualized (course-specific materials)
2. Process-oriented (multiple checkpoints)
3. Unique and personal (lived experience)
4. Metacognitive (explain thinking)
5. Synthesis across sources (compare specific readings)

## Development Guidelines

### Creating New Agents

1. **Agent file** (`agents/new-agent.md`):
```yaml
---
name: agent-name
description: Use this subagent for [specific use case]. Example requests include "..." or "...".
tools: Read, Glob, Grep  # Available: Read, Write, Edit, Glob, Grep, WebFetch
model: sonnet  # or opus
---

[Agent system prompt with embedded knowledge and workflows]
```

2. **Update plugin.json** - No action needed (agents auto-discovered)

3. **Test invocation**: Natural language matching description triggers agent

### Creating New Commands

1. **Command file** (`commands/new-command.md`):
```yaml
---
description: Brief description of command action
---

[Prompt for Claude Code to execute when command invoked]
[Typically invokes agent: "Run the [agent-name] agent on..."]
```

2. **Test**: `/new-command [arguments]`

### Version Management

**Marketplace publishing**:
1. Update `plugin.json` version
2. Update `.claude-plugin/marketplace.json` version
3. Update `README.md` version history
4. Commit and push to GitHub
5. Users run `/plugin marketplace update` to fetch latest

**Deprecation**: This plugin replaces `@jameskruck/claude-subagents` NPM package (now deprecated)

## Common Workflows

### Testing Plugin Changes Locally

```bash
# After editing agent or command files
cd ~/.claude/plugins/education-toolkit  # or wherever plugin installed
# Files are read at invocation time - no restart needed
# Test by invoking agent or command
```

### Adding Research to Knowledge Base

```bash
# Add new .md file to agents/assessment-knowledge/research/
# Update assessment-designer.md to reference new file
# Increase knowledge base size in descriptions (currently 464 KB)
```

### Quality Assurance Checklist

Before version releases:
- [ ] All agent descriptions match current capabilities
- [ ] Command invocations work with latest agent changes
- [ ] README.md examples reflect actual behavior
- [ ] Version numbers synchronized (plugin.json, marketplace.json, README.md)
- [ ] Knowledge base file paths correct (relative to agent location)
- [ ] YAML frontmatter valid in all agents/commands

## Accessibility & Standards Compliance

**This repository emphasizes**:
- WCAG 2.2 AA compliance (accessibility-auditor agent)
- Universal Design for Learning (UDL) principles
- Quality Matters (QM) standards for educational tools
- Inclusive teaching practices
- AI-integrated pedagogy with clear boundaries

**When editing agents**: Maintain research-backed methodologies and cite sources where applicable (e.g., PAIRR from Frontiers in Communication 2025).

## Plugin Marketplace Context

**Installation command**: `/plugin marketplace add jameskruck/education-toolkit`
**Category**: education
**Target users**: Educational developers, instructional designers, course creators, faculty developers
**Competitive positioning**: Only Claude Code plugin with bundled assessment research and evidence-based AI integration methodologies

## Important Notes

- **No build process** - Pure markdown configuration, no compilation
- **Agent autonomy** - Agents read their own knowledge base files, don't require user file paths
- **Model selection** - Use `sonnet` for speed (2-5 min), `opus` for depth (5-12 min for peer-review-simulator)
- **WebFetch capability** - Only accessibility-auditor and assessment-designer have WebFetch access
- **Version history** - Track methodology additions in README.md (v2.3.2 added Peer Design Review Simulator, v2.3.1 added storyboard validation enhancements, v2.0 added PAIRR, AI Roleplay, Diagnostic Rubrics)

## Version History & Changelog

### v2.3.2 (2025-10-17) - Peer Design Review Simulator

**New Agent**:
- **peer-review-simulator.md** (15 KB, Opus) - Multi-perspective design review with 6 ID specialists
  - Emma (Content & Writing): Grammar, clarity, inclusive language
  - Marcus (Accessibility & Inclusion): WCAG 2.2 AA, UDL, assistive tech
  - Priya (Visual Design & UI): Typography, layout, visual hierarchy
  - James (Technical & Functionality): Browser compatibility, performance, security
  - Sarah (Pedagogical Design): Learning alignment, Bloom's accuracy, scaffolding
  - Alex (UX & Navigation): Information architecture, wayfinding, usability

**New Command**:
- **/peer-review** - Quick access to comprehensive design review panel

**Key Features**:
- Comprehensive review: Every element analyzed by all 6 specialists
- Cross-reviewer themes: Issues flagged by 3+ reviewers = top priority
- Scoring system: Each reviewer scores 0-100, overall readiness calculated
- Prioritized action plan: Critical (block launch) → High → Medium → Low
- Fix time estimates for each issue

**Use Cases**:
- Pre-launch quality assurance for entire week/unit
- Identify systemic issues (flagged by multiple reviewers)
- Get specialist feedback without assembling actual review team
- Simulate real design review meeting with diverse expertise

### v2.3.1 (2025-10-16) - Enhanced Storyboard Validation

**Agent Enhancements**:

**consistency-checker.md**:
- **Section 6: Storyboard Structure Patterns** - Comprehensive validation of storyboard formatting
  - Module intro text blocks (Modules 2-6): Validates connecting narrative between modules
  - Case attachment flags: Checks for `🔗 ATTACH CASE HERE:` pattern to make attachment points unmistakable
  - AI roleplay timing references: Detects and flags timing references (should be removed - roleplays are student-paced)
  - Element numbering integrity: Ensures element table matches content sections (no skipped numbers)
  - Standalone sections: Flags content outside element structure (should be consolidated)
- **Section 7: PAIRR Methodology Consistency** - Cross-week PAIRR validation
  - Checks if PAIRR methodology is consistently applied across all weeks
  - Flags inconsistencies (Week 1 has PAIRR, Week 3 has basic peer review only)
  - Validates all PAIRR components: dual feedback, comparative reflection, post-revision reflection, bonus structure

**branding-checker.md**:
- **Uplimit Storyboard Symbol Validation** - Accessibility-first symbol checking
  - Priority badges: Validates black symbols (⬤ ◐ ○) vs colored emoji (🔴 🟡 🟢)
  - Infobox icons: Validates black symbols (◉ ▶ ▪ ■ ◆ ▸) vs colored emoji (🎯 📺 📊 🏟️ 💡 🎮)
  - Rationale: Ensures accessibility and neutral design consistency
  - Reporting: Provides line numbers of deprecated emoji usage with replacement guidance

**Use Cases**:
- After implementing PAIRR in Week 1, run consistency-checker to ensure all weeks use same methodology
- After converting colored emoji to black symbols, run branding-checker to verify complete conversion
- During storyboard creation, run both agents to catch structural and branding issues early

**Impact**:
- Catches PAIRR consistency issues that affect learning experience (students expect consistent feedback structure)
- Prevents accessibility regressions (colored emoji → black symbols conversion)
- Validates storyboard integrity (element numbering, attachment flags, timing references)

### v2.3.0 (2025-10-15) - PAIRR Methodology Validation

**Agent Additions**:
- Added PAIRR (Peer and AI Review + Reflection) methodology validation to consistency-checker
- Research-backed dual feedback approach (Frontiers in Communication, 2025)
- Develops AI literacy through critical comparison of peer vs AI feedback

### v2.0.0 (2025-10-10) - Initial Plugin Release

**Major Launch**:
- Converted from NPM package (@jameskruck/claude-subagents) to Claude Code plugin format
- 9 specialized agents + 6 slash commands
- 464 KB bundled knowledge base (frameworks + research)
- Marketplace installation: `/plugin marketplace add jameskruck/education-toolkit`
