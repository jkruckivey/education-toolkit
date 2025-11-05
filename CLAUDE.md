# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

**Education Toolkit** - Claude Code plugin providing 17 specialized agents, 14 slash commands, and automatic code review for educational developers, instructional designers, and course creators. Focus areas: widget design system enforcement, strategic course planning (CLOs, weekly structure, assessment strategy), specialized consistency validation (terminology, concept threading, assessment methodology), cohort course structure validation, accessibility (WCAG 2.2 AA), assessment design, UDL implementation, Quality Matters standards, AI-integrated pedagogy, multi-perspective peer design review, and fullstack code quality (FastAPI/Python + React/JSX).

**Version**: 2.8.5 (January 2025)
**Tech stack**: Markdown-based agent definitions, bundled knowledge base (course design knowledge + 464 KB assessment research), PostToolUse hooks for automatic code review
**Distribution**: Claude Code plugin (`/plugin add jameskruck/education-toolkit`)
**Structure**: Single plugin with marketplace.json (source: "./") - all components at repository root
**Note**: Requires both marketplace.json (distribution config) and plugin.json (plugin definition) per Claude Code requirements

## Architecture

### Plugin Structure

```
education-toolkit/
├── .claude-plugin/
│   ├── marketplace.json     # Distribution config (required for /plugin add)
│   └── plugin.json          # Plugin manifest
├── hooks/                   # Automatic quality enforcement (5 hooks)
│   ├── hooks.json           # Hook configurations
│   ├── review-on-change.md  # PostToolUse: Fullstack code review (NEW v2.5.0)
│   └── scripts/
│       ├── validate-content.sh      # PostToolUse: Smart validator
│       ├── load-context.sh          # SessionStart: Context loader
│       ├── check-protected.sh       # PreToolUse: Content guardian
│       ├── format-storyboard.py     # PostToolUse: Auto-formatter
│       └── test-widget.sh           # PostToolUse: Widget auto-tester (NEW v2.8.0)
├── agents/                  # 17 specialized agents
│   ├── course-outline-creator.md (14 KB, sonnet, WebFetch) # Strategic course planning
│   ├── cohort-structure-checker.md (25 KB, sonnet) # Validates cohort course module structures
│   ├── terminology-consistency-checker.md (18 KB, sonnet) # NEW v2.7.0 - Term consistency & glossary building
│   ├── concept-threading-checker.md (22 KB, sonnet) # NEW v2.7.0 - Week 1 concepts in later weeks
│   ├── assessment-consistency-checker.md (20 KB, sonnet) # NEW v2.7.0 - PAIRR, rubrics, grading
│   ├── assessment-designer.md (27 KB, sonnet, 464 KB bundled knowledge)
│   ├── rubric-generator.md (11 KB, sonnet)
│   ├── accessibility-auditor.md (6 KB, sonnet, WebFetch)
│   ├── widget-tester.md (8 KB, sonnet, 3 personas)
│   ├── widget-designer.md (16 KB, sonnet) # NEW v2.8.0 - Generate/audit HTML widgets with design system
│   ├── student-journey-simulator.md (6 KB, opus, 4 personas)
│   ├── peer-review-simulator.md (15 KB, opus, 6 reviewer personas)
│   ├── branding-checker.md (10 KB, sonnet, Canvas/Uplimit)
│   ├── udl-content-generator.md (10 KB, sonnet)
│   ├── uplimit-storyboard-builder.md (26 KB, sonnet)
│   ├── backend-reviewer.md (12 KB, sonnet, FastAPI/Python expertise)
│   ├── frontend-reviewer.md (13 KB, sonnet, React/WCAG 2.2 AA)
├── course-design-knowledge/  # Bundled course design knowledge (NEW v2.6.1)
│   ├── ivey-course-development-process.md  # 6-phase process, cohort/self-paced models
│   ├── course-outline-examples.md          # Anonymized course structure templates
│   ├── concept-threading-guide.md          # Threading patterns and best practices
│   └── uplimit-content-design-guide.md     # Varied content delivery principles
├── assessment-knowledge/  # Bundled assessment research knowledge
│   ├── frameworks/        # UDL, QM, Inclusive Teaching, Templates
│   └── research/          # AI assessment research (5 papers)
├── commands/                  # 10 slash commands
│   ├── audit-module.md
│   ├── build-storyboard.md
│   ├── check-branding.md
│   ├── check-consistency.md
│   ├── design-assessment.md
│   ├── generate-rubric.md
│   ├── peer-review.md
│   ├── review-content.md
│   ├── simulate-journey.md
│   └── test-widget.md
└── skills/                    # NEW: 3 executable skills (Python automation)
    ├── assessment-template-generator/
    │   ├── SKILL.md           # Skill manifest and documentation
    │   ├── REFERENCE.md       # Research foundations and customization
    │   └── scripts/
    │       ├── generate_pairr.py            # PAIRR template generator
    │       ├── generate_ai_roleplay.py      # AI roleplay config generator
    │       └── generate_diagnostic_rubric.py # Diagnostic rubric generator
    ├── accessibility-audit-tools/
    │   ├── SKILL.md
    │   └── scripts/
    │       ├── check_contrast.py   # WCAG 2.2 AA color contrast validator
    │       └── check_alt_text.py   # Alt text presence/quality checker
    └── qm-validator/
        ├── SKILL.md
        └── scripts/
            ├── check_alignment.py       # Outcome-criteria alignment checker
            └── check_rubric_math.py     # Rubric point total validator
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

**Skills** (`.md` files in `skills/*/SKILL.md`) - **NEW**:
- Executable Python automation invoked by agents
- YAML frontmatter: `name`, `description`, `version`, `dependencies`
- Agents use Skill tool to run Python scripts
- Automate repetitive tasks: template generation, validation, compliance checking

### Agent → Skill Invocation Pattern

**How Agents Use Skills**:
1. Agent recognizes user request matches skill capability (e.g., "create PAIRR assignment")
2. Agent invokes: `Skill: assessment-template-generator`
3. Agent runs: `python scripts/generate_pairr.py --assignment-name "..." --points 30 --criteria "..."`
4. Skill generates markdown template file
5. Agent reads generated file
6. Agent customizes template with course-specific details
7. Agent presents finalized content to user

**Example Workflow**:
```
User: "Create a PAIRR assignment for my marketing memo"

assessment-designer agent:
1. Asks clarifying questions (learning outcomes, points, criteria)
2. Invokes skill: Skill: assessment-template-generator
3. Runs: python scripts/generate_pairr.py --assignment-name "Marketing Memo" --points 30 --criteria "Analysis, Strategy, Writing, Budget"
4. Reads generated template (pairr-marketing-memo.md)
5. Customizes AI prompt, rubric descriptors, due dates
6. Invokes qm-validator to check compliance
7. Fixes any issues found
8. Presents complete PAIRR assignment to user
```

**Skills Empower Agents**:
- Save 10-15 min per assessment (automation vs. manual writing)
- Ensure structural consistency (templates follow research-backed patterns)
- Proactive quality assurance (QM validation catches errors before user sees them)
- Let agents focus on design advice (automation handles repetitive structure)

**Hooks** (`hooks/hooks.json` + bash/Python scripts) - **NEW v2.4.1**:
- Automatic quality enforcement at lifecycle events (PostToolUse, PreToolUse, SessionStart)
- Zero API tokens consumed (runs locally on user's machine)
- Deterministic validation (not LLM-dependent, 100% consistent)
- Types: Smart validator, context loader, content guardian, auto-formatter, widget auto-tester

### Hooks System (NEW v2.4.1)

Hooks provide **deterministic automation** that runs at specific lifecycle events, transforming the plugin from reactive (user asks for validation) to proactive (automatic enforcement).

**Key Advantage**: Hooks use **zero API tokens** - they're pure bash/Python automation running on the user's local machine.

**5 Built-in Hooks**:

1. **Smart Content Validator** (PostToolUse on Edit/Write)
   - HTML files: WCAG 2.2 AA checks (contrast, alt text, headings, tables)
   - Markdown files: Bloom's verbs, rubric math, PAIRR components, colored emoji
   - Execution time: 1-3 seconds
   - Token savings: ~10,000 tokens per manual validation avoided

2. **Educational Context Loader** (SessionStart)
   - Loads WCAG 2.2 AA, QM 6th Edition, Bloom's Taxonomy, UDL standards
   - Displays available commands and active methodologies
   - Reads course-specific config from `.education-toolkit-config.json`
   - One-time execution per session

3. **Protected Content Guardian** (PreToolUse on Edit/Write)
   - Blocks edits to `published/`, `production/`, `final/`, `student-facing/` paths
   - Shows warning with risks (fairness, academic integrity, student trust)
   - Requires explicit approval to proceed
   - Prevents accidental rubric changes after student submissions

4. **Storyboard Auto-Formatter** (PostToolUse on Edit/Write)
   - Converts colored emoji → black symbols (🔴→⬤ 🟡→◐ 🟢→○)
   - Standardizes element headings, priority badges, MLO references
   - Fixes table/heading spacing, removes trailing spaces
   - Ensures platform branding compliance automatically

5. **Widget Auto-Tester** (PostToolUse on Write) - **NEW v2.8.0**
   - Automatically tests new widgets after creation (detects `*.html` files in `widget` directories)
   - Runs accessibility tests via webapp-testing skill (keyboard nav, focus indicators, ARIA)
   - Generates test results JSON with violations and recommendations
   - Optionally auto-opens widgets in browser (create `.auto-open-widgets` file to enable)
   - Execution time: 3-8 seconds (depends on widget complexity)
   - Token savings: ~5,000 tokens per manual test avoided

**Configuration**:
```json
// .education-toolkit-config.json (optional)
{
  "courseName": "Business of Marketing in Sport",
  "institution": "Ivey Business School",
  "platform": "Uplimit",
  "conventions": {
    "learningOutcomePrefix": "MLO",
    "wcagVersion": "2.2"
  },
  "protectedPaths": [
    "published/*",
    "custom/path/*"
  ]
}
```

**Enable Auto-Open Widgets in Browser** (optional):
```bash
# macOS/Linux
touch ~/.claude/plugins/education-toolkit/.auto-open-widgets

# Windows (Git Bash/PowerShell)
New-Item -ItemType File -Path "$env:USERPROFILE\.claude\plugins\education-toolkit\.auto-open-widgets"
```

**Performance**: 1-8 seconds execution, 0 API tokens, 100% consistency

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

**Plugin publishing**:
1. Update version in BOTH files:
   - `.claude-plugin/marketplace.json` (top-level version and plugins[0].version)
   - `.claude-plugin/plugin.json` version
2. Update `README.md` version history
3. Commit and push to GitHub
4. Users run `/plugin update education-toolkit` to fetch latest

**Migration Note**:
- v2.8.5: Restructured from nested plugin (plugins/education-toolkit/) to root-level (source: "./")
- Both marketplace.json and plugin.json are required for distribution via `/plugin add`
- This plugin replaces `@jameskruck/claude-subagents` NPM package (now deprecated)
- If you have the old installation, reinstall with `/plugin add jameskruck/education-toolkit`

## Common Workflows

### Testing Plugin Changes Locally

```bash
# After editing agent or command files locally
cd /path/to/education-toolkit  # your local repo
# Make changes to agents/*.md, commands/*.md, etc.
# Files are read at invocation time - no restart needed
# Test by invoking agent or command in Claude Code

# To test installed plugin changes:
cd ~/.claude/plugins/education-toolkit  # installed plugin location
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

## Plugin Distribution

**Installation command**: `/plugin add jameskruck/education-toolkit`
**Update command**: `/plugin update education-toolkit`
**Category**: education
**Format**: Single plugin (not a marketplace)
**Target users**: Educational developers, instructional designers, course creators, faculty developers
**Competitive positioning**: Only Claude Code plugin with bundled assessment research and evidence-based AI integration methodologies

## Important Notes

- **No build process** - Pure markdown configuration, no compilation
- **Agent autonomy** - Agents read their own knowledge base files, don't require user file paths
- **Model selection** - Use `sonnet` for speed (2-5 min), `opus` for depth (5-12 min for peer-review-simulator)
- **WebFetch capability** - Only course-outline-creator, accessibility-auditor, and assessment-designer have WebFetch access
- **Version history** - Track methodology additions in README.md (v2.8.1 added Widget Introduction Format Enforcement, v2.8.0 added Widget Design System Enforcement, v2.7.0 added Specialized Consistency Checkers, v2.6.3 added Cohort Structure Checker, v2.6.2 added Course Format Discovery, v2.6.1 added Course Design Knowledge Base, v2.6.0 added Course Outline Creator, v2.5.0 added Fullstack Code Review, v2.4.2 fixed peer review storyboard vs live content, v2.4.1 added Interactivity Analysis + Automatic Hooks, v2.4.0 added Executable Skills, v2.3.2 added Peer Design Review Simulator, v2.3.1 added storyboard validation enhancements, v2.0 added PAIRR, AI Roleplay, Diagnostic Rubrics)

## Version History & Changelog

### v2.8.1 (2025-02-01) - Widget Introduction Format Enforcement

**Agent Updates**:

**uplimit-storyboard-builder.md**:
- **Required Widget Introduction Format**: All interactive widgets (except learning outcomes displays) must now include standardized introductory text before iframe embed
- **Three Required Components**:
  1. **Activity Header**: `### ⚙ Interactive Activity: [Widget Name]`
  2. **MLO Practice Connection**: `**Practice: MLO X.X ([brief description])**`
  3. **Contextual Introduction Paragraph** (100-150 words) with four elements:
     - Readiness statement ("You're now ready to...")
     - What they'll do (specific interaction description)
     - Why it matters (real-world relevance/industry connection)
     - What they'll gain (learning outcome and application)
- **BUILD MODE Enhancement**: Generates properly formatted widget introductions automatically when creating storyboards
- **AUDIT MODE Enhancement**: Validates widget introduction format and flags violations:
  - ❌ Missing activity header or MLO connection
  - ❌ Generic introductions without context
  - ❌ Jumping straight to iframe without setup
  - ❌ Introductions too brief (<50 words) or too long (>200 words)
- **Complete Example Added**: Sponsorship Valuation Calculator with 147-word contextual introduction showing all four required elements
- **Anti-Patterns Documentation**: Clear examples of what NOT to do (generic introductions, missing MLO connections, no context)
- **Audit Scenario Added**: Scenario 5 demonstrates correcting a widget lacking proper introduction (Revenue Mix Slider example with before/after)

**Why This Format**:
- **Engagement**: Readiness statements connect to prior learning and signal progression
- **Motivation**: Role immersion ("Step into the role of...") and industry relevance establish real-world value
- **Clarity**: Students understand exactly what they'll do and what they'll gain before interacting
- **Learning Alignment**: Explicit MLO practice connections ensure widgets target specific learning outcomes

**Exception**: Learning outcomes widgets (Module 1 Element 2 in cohort courses) display CLOs/MLOs visually and do NOT require introductory narrative.

**Updated Files**:
- `uplimit-storyboard-builder.md`: Lines 312-421 (BUILD MODE widget section), Lines 1243-1264 (AUDIT MODE widget section), Lines 1523-1567 (Audit Scenario 5)
- `plugin.json`: Version 2.8.1, description updated to mention "required widget introduction format"
- `marketplace.json`: Version 2.8.1 (both top-level and plugin-level), description updated
- `CLAUDE.md`: Added v2.8.1 to version history

**Impact**:
- Ensures consistent, engaging widget introductions across all courses (no more "Use this calculator" generic text)
- Improves student motivation through clear real-world connections and role immersion
- Saves 5-10 minutes per widget by providing clear format template
- Audit mode catches missing introductions before storyboards go to production

---

### v2.8.0 (2025-01-31) - Widget Design System Enforcement

**New Agent**:

**widget-designer.md** (16 KB, sonnet):
- Dual-mode agent: GENERATE new widgets OR AUDIT existing widgets for design system compliance
- Enforces standardized design system extracted from Business of Marketing in Sport widgets
- **Typography**: Geist font family (400, 500, 600, 700 weights), standardized size scale (1.8rem h1, 1.5rem h2, 0.95rem subtitle, 0.875rem labels)
- **Color System**: Neutral gray palette (neutral-50 through neutral-900), CSS variables required (no hardcoded hex)
- **Content Guidelines**: NO EMOJIS policy (use text labels or symbols like → • ▼ instead)
- **Button Standards**: Neutral gray states (neutral-900 active, neutral-700 completed, neutral-100 default), font-weight 500, border-radius 8px
- **Accessibility Requirements**: ARIA labels, keyboard nav (Enter/Space), focus states (2px solid #3182ce), screen reader support
- **Export Formats**: PDF generation (not JSON) using jsPDF library for student submissions

**GENERATE Mode**:
- Scaffolds new interactive widgets with standardized design system
- Asks clarifying questions (widget type, interactivity, primary color, data structure, features)
- Generates base template with Geist font, CSS variables, accessibility built-in
- Adds widget-specific components (quiz, simulator, decision tree, concept map patterns)
- Pre-flight checklist: All colors use variables, no emojis, focus states, keyboard nav, responsive

**AUDIT Mode**:
- Validates existing widgets against design system standards
- Systematic checks: Color system (flags hardcoded hex), typography (Geist loaded?), buttons (pattern compliance), spacing (8px scale), border-radius (8px containers, 4px small), accessibility (ARIA, keyboard, lang attribute), emojis (flags all instances)
- Generates comprehensive audit report with line numbers, critical issues, warnings, passing standards, quick fix recommendations
- Offers to automatically fix issues (replace hardcoded colors, add Geist font, remove emojis, standardize border-radius)

**Design System Standards** (extracted from 4 sample widgets):
- **Neutral Color Scale**: `--color-neutral-50` (#fafafa) through `--color-neutral-900` (#171717)
- **Semantic Colors**: `--color-success` (#22c55e), `--color-error` (#ef4444), `--color-warning` (#f59e0b), `--color-info` (#3b82f6)
- **Primary Color**: `--color-primary` (#171717 dark gray default, configurable per widget)
- **Typography Scale**: h1 (1.8rem) → h2 (1.5rem) → h3 (1.2rem) → body (1rem) → labels (0.875rem)
- **Spacing Scale**: 8px base (`--spacing-1: 8px`, `--spacing-2: 16px`, etc.)
- **Border**: `--border-radius: 8px`, `--border-radius-sm: 4px`

**Use Cases**:
- "Create a quiz widget with progress tracker" → Generates standardized HTML
- "Audit this widget for design system compliance" → Reports hardcoded colors, missing Geist, emoji usage
- "Generate a decision simulator" → Scaffolds with sliders, buttons, charts, all using CSS variables
- "Check color variable usage in my widget" → Lists every hardcoded hex with line numbers

**Impact**:
- Ensures visual consistency across all course widgets (same font, colors, spacing)
- Saves 15-20 minutes per widget audit (automated find-replace for hardcoded colors)
- Prevents accessibility regressions (automatic checks for ARIA, keyboard nav, emojis)
- Professional educational tone (no emojis policy enforced)
- Submission-ready exports (PDF format, not JSON)

**New Hook**:

**Widget Auto-Tester** (PostToolUse on Write):
- Automatically runs accessibility tests after widget creation
- Detects `*.html` files in `widget` directories (only triggers on Write, not Edit)
- Invokes webapp-testing skill to test keyboard nav, focus indicators, ARIA
- Generates `*_accessibility_results.json` with violations and recommendations
- Optionally auto-opens widgets in browser (enable with `.auto-open-widgets` file)
- Cross-platform: macOS (open), Linux (xdg-open), Windows (start)
- Execution time: 3-8 seconds (depends on widget complexity)
- Token savings: ~5,000 tokens per manual test avoided

**Updated Files**:
- `plugin.json`: Version 2.8.0, description updated (17 agents), added keywords "widget-design", "design-system"
- `marketplace.json`: Version 2.8.0, description highlights widget design system enforcement
- `CLAUDE.md`: Added widget-designer to architecture, widget auto-tester hook, updated version history
- `hooks/hooks.json`: Added test-widget.sh hook (PostToolUse on Write)
- `hooks/scripts/test-widget.sh`: New bash script for automated widget testing

---

### v2.7.0 (2025-01-31) - Specialized Consistency Checkers

**New Agents (3 specialized checkers):**

**terminology-consistency-checker.md** (18 KB, sonnet):
- Builds comprehensive course glossary across all weeks/modules
- Flags term variations (e.g., "revenue streams" vs "revenue sources" vs "monetization channels")
- Identifies undefined terms and acronyms (e.g., "IRR" used without expansion)
- Validates capitalization consistency (e.g., "Anchor Project" vs "anchor project")
- Checks technical jargon appropriateness
- Validates learning outcome terminology alignment (CLO/MLO format consistency)
- Generates consistency scores per term (100 = perfect, deductions for variations)

**concept-threading-checker.md** (22 KB, sonnet):
- Validates Week 1 concepts appear in later weeks (prevents orphaned concepts)
- Tracks concept usage across all weeks with line numbers
- Checks for callback references ("Recall from Week 1...")
- Validates progressive complexity (simple → moderate → complex → synthesis)
- Flags re-explanations (same concept defined multiple times)
- Validates assessments require cumulative knowledge (not siloed)
- References bundled concept-threading-guide.md for patterns

**assessment-consistency-checker.md** (20 KB, sonnet):
- Validates PAIRR methodology consistency across weeks (cohort courses only)
- Checks rubric point totals and category consistency
- Validates learning outcome alignment with assessments
- Analyzes formative vs. summative balance
- Checks grading distribution consistency
- Validates assessment timing and pacing (no deadline clustering)
- **Course-type aware**: Flags peer review in self-paced courses (not allowed)

**Deprecated Agent:**
- `consistency-checker.md` → `consistency-checker-DEPRECATED.md`
- Renamed with deprecation notice pointing to 3 specialized replacements
- Kept for reference only, will be removed in future version

**Why the Change:**
The old consistency-checker tried to validate 7 dimensions at once (terminology, threading, outcomes, assessment, narrative, structure, PAIRR), leading to:
- Missed issues due to large scope
- Slower performance (large context per check)
- Users couldn't target specific concerns

The new specialized agents:
- Have narrow scope (catch more issues)
- Run faster (smaller context per agent)
- Can run independently or together
- Target specific validation needs

**Updated Files:**
- `plugin.json`: Version 2.7.0, description updated (16 agents)
- `marketplace.json`: Version 2.7.0, description updated
- `CLAUDE.md`: Added 3 new agents, marked old consistency-checker as deprecated

**Use Cases:**
- **terminology-consistency-checker**: "Check terminology consistency across Weeks 1-5", "Build course glossary", "Flag undefined acronyms"
- **concept-threading-checker**: "Validate concept threading Week 1-5", "Check for orphaned concepts", "Ensure Week 1 concepts appear later"
- **assessment-consistency-checker**: "Check PAIRR consistency", "Validate rubric points", "Check if assessments are cumulative"

**Impact:**
- Targeted validation (run specific checker for specific concern)
- Faster execution (smaller scope per agent)
- Better issue detection (proven by cohort-structure-checker catching issues old checker missed)
- Course-type awareness (assessment-consistency-checker flags peer review in self-paced courses)

---

### v2.6.3 (2025-01-31) - Cohort Course Structure Validation

**New Agent**:

**cohort-structure-checker.md** (25 KB, sonnet):
- Validates cohort course module structures against standardized templates
- Checks module sequences (0→1→2→...→7), element patterns (connecting text, learning outcomes widgets, Final Project Connections)
- Validates PAIRR methodology in Module 6 (peer feedback, AI feedback, comparative reflection, post-revision reflection, bonus structure)
- Checks learning outcomes widgets are embedded in all modules (Element 2 for Modules 2-7)
- Validates Final Project Connection quality (specificity, content match, application examples)
- Cross-module consistency: Element numbering integrity, case attachment flags, AI roleplay timing references
- Module-specific requirements: Module 1 (week-level outcomes), Module 7 (wrap-up components)

**Use Cases**:
- Validate storyboards follow cohort course template before development
- Identify missing PAIRR components in assessment modules
- Check Final Project Connection sections for quality and specificity
- Ensure learning outcomes widgets are properly embedded
- Catch element numbering mismatches between tables and content

**Impact**:
- Prevents structural inconsistencies across course weeks
- Ensures PAIRR methodology is consistently applied (critical for AI literacy development)
- Validates Final Project Connections are specific and actionable (not generic)
- Catches missing learning outcomes widgets (students need visual CLO/MLO mapping)
- Provides comprehensive validation report with line numbers and fix recommendations

**Updated Files**:
- `plugin.json`: Version 2.6.3, description updated (14 agents)
- `marketplace.json`: Version 2.6.3, description updated (14 agents)
- `CLAUDE.md`: Added cohort-structure-checker to architecture, updated agent count

**Example Issues Detected**:
- ❌ Module 6: PAIRR methodology completely missing (no comparative reflection)
- ❌ Module 2: Element 2 should be learning outcomes widget, found Infobox instead
- ❌ Module 1: Learning outcomes widget described but iframe code not embedded
- ⚠️ Module 3: Final Project Connection too generic (needs specific content references)

---

### v2.6.2 (2025-01-28) - Course Format Discovery

**Agent Updates**:

**course-outline-creator.md**:
- Added course format (cohort vs. self-paced) to Required Input section (item #4)
- Added detailed explanations: Cohort (fixed start/end dates, synchronous elements, weekly deadlines) vs. Self-paced (own speed, asynchronous only, checkpoint-based)
- Made course format the first question in Discovery Interview process
- Course format informs critical design decisions: weekly structure vs modules, firm deadlines vs flexible pacing, peer review feasibility, synchronous session planning

**uplimit-storyboard-builder.md**:
- Added course format to Required Context section (line 144)
- Added course format as first confirmation question in BUILD MODE initial response
- Course format affects: pacing recommendations, deadline language, synchronous element inclusion, module vs weekly structure

**Rationale**:
- Course format is a fundamental structural decision that affects every design choice downstream
- Cohort courses can include synchronous peer review, live sessions, anchor projects with milestones
- Self-paced courses require fully asynchronous design, checkpoint tasks instead of deadlines, individual work only
- Asking upfront prevents costly redesign when format assumptions are incorrect

**Updated Files**:
- `course-outline-creator.md`: Lines 88-90 (Required Input), line 102 (Discovery Interview)
- `uplimit-storyboard-builder.md`: Line 144 (Required Context), line 1494 (BUILD MODE)
- `plugin.json`: Version 2.6.2
- `marketplace.json`: Version 2.6.2 (both locations)
- `README.md`: Added v2.6.2 callout, updated agent descriptions for course-outline-creator and uplimit-storyboard-builder

**Impact**:
- Agents now gather course format at start of every outline/storyboard creation
- Design recommendations appropriately match course delivery model
- Prevents assumptions that lead to incompatible design choices (e.g., peer review in self-paced course)

### v2.5.0 (2025-01-23) - Automatic Fullstack Code Review

**New Agents**:

**backend-reviewer.md** (12 KB, sonnet):
- Expert FastAPI/Python code reviewer with focus on educational technology projects
- Review criteria: Security (auth, input validation, secrets), Error handling (try/except, user feedback), API design (REST conventions, response structure), Performance (async/await, database queries)
- Context-aware: Understands adaptive learning platforms, OpenAI integration patterns, learner state management
- Output format: Strengths, suggestions, critical issues with specific line numbers

**frontend-reviewer.md** (13 KB, sonnet):
- Expert React/JSX code reviewer with WCAG 2.2 AA accessibility specialization
- Review criteria: Accessibility (ARIA labels, semantic HTML, keyboard nav, color contrast), React best practices (hooks, state management), UX (loading states, error messages), Performance (re-renders, bundle size)
- Context-aware: Understands educational platforms, student-facing UX requirements, error recovery patterns
- Output format: Strengths, suggestions, critical issues with specific line numbers

**New Hook**:

**review-on-change.md** (PostToolUse hook):
- Automatic code review after Write/Edit operations on .py, .jsx, .js files
- Smart routing: Detects file type → launches specialized agent (backend-reviewer or frontend-reviewer)
- Intelligent skipping: Config files, package.json, single-line formatting changes, comment-only edits
- Event trigger: PostToolUse with matcher "Write|Edit"
- Decision logic: >10 lines OR new functions → Agent review; <10 lines → Quick inline or skip

**Updated Files**:
- `plugin.json`: Version 2.5.0, description updated (12 agents, 5 hooks)
- `README.md`: Added Hook 5 documentation with examples, updated agent count, added code review keywords

**Use Cases**:
- Automatically review backend endpoints for security and validation issues
- Check frontend components for accessibility compliance after edits
- Enforce best practices (async/await, React hooks, error handling) proactively
- Educational: Learn code quality principles through instant feedback with explanations

**Example Output**:
```
📝 Frontend Review: App.jsx:236-267

✅ STRENGTHS:
  • Line 236-248: Excellent assessment-result pattern
  • Line 245-246: Smart use of _next_content to preload

⚠️ SUGGESTIONS:
  • Line 194-206: getCalibrationMessage could be memoized
  • Line 249: Consider functional update: setContentIndex(i => i + 1)

🔴 CRITICAL ISSUES:
  • None found
```

### v2.6.0 (2025-01-28) - Strategic Course Outline Creation

**New Agent**:

**course-outline-creator.md** (14 KB, sonnet, WebFetch):
- Strategic curriculum design expert for creating comprehensive course outlines
- Guides instructors through: CLO definition (QM-compliant), weekly structure planning, MLO creation, assessment strategy design, concept threading, case/practitioner identification
- **Workflow Position**: Comes BEFORE uplimit-storyboard-builder (strategic planning → detailed module design)
- **Discovery Interview**: Asks clarifying questions about subject area, level, duration, target audience, course goals
- **CLO Standards**: Single action verbs (Analyze, Evaluate, Design), observable performance, context provided, NO compound verbs
- **Assessment Alignment Matrix**: Plans what gets assessed when, ensures all CLOs covered proportionally
- **Concept Threading**: Ensures Week 1 concepts are built upon in Weeks 2-5 (no orphaned topics)
- **Output Format**: Complete course outline with CLOs, weekly themes, MLOs, assessment summary, threading map, case/practitioner plan, UDL considerations

**Use Cases**:
- Create new course from scratch (5-week MBA, 3-week executive ed, 10-week undergrad)
- Restructure existing course to meet QM standards
- Convert subject matter expertise into strategic course blueprint
- Plan assessment strategy before diving into detailed module design

**Example Output Structure**:
```
# Course Outline: [Title]

## Course Learning Outcomes (CLOs)
- CLO 1: [Action Verb] [Domain] (Bloom's Level)
- CLO 2-5: [etc.]

## Course Structure
- Week 1: [Theme] (CLOs, MLOs, case, practitioner, assessment)
- Week 2-5: [etc.]

## Assessment Summary (table)
## Concept Threading Map
## Case Study & Practitioner Plan
```

**Integration**:
- Use **course-outline-creator** first → Create strategic blueprint
- Pass outline to **uplimit-storyboard-builder** → Design detailed modules
- Use **peer-review-simulator** → Quality check before build

**Updated Files**:
- `plugin.json`: Version 2.6.0, description updated (13 agents)
- `marketplace.json`: Version 2.6.0, description updated
- `CLAUDE.md`: Added course-outline-creator to architecture, updated version

**Impact**:
- Fills critical workflow gap (SME expertise → strategic outline → detailed storyboard)
- Ensures QM compliance from start (single action verbs, measurable outcomes, aligned assessments)
- Prevents "orphaned concepts" through explicit threading map
- Saves 3-5 hours of outline creation with guided interview process
- Produces consistent, high-quality course structures ready for storyboarding

### v2.6.1 (2025-01-28) - Course Design Knowledge Base

**New Knowledge Base**:

**agents/course-design-knowledge/** (4 files, ~150 KB total):
- Bundled Ivey-specific course design principles and templates for internal team use
- Provides concrete examples and institutional context for agents to reference

**ivey-course-development-process.md** (~9,500 words):
- **Source**: Converted from 9-page PDF "IveyOnline Process and Learning Models"
- **Content**: 6-phase development process (Planning → Design → Production → Build → Quality → Launch)
- **Cohort Course Model**: 5-week structure with anchor projects, Learning Manager touchpoints, Ivey cases, AI integration (chatbot activities, interactive avatars, ABIEL)
- **Self-Paced Course Model**: 2-5 modules with checkpoint tasks, auto-graded activities, flexible pacing
- **Team Roles**: SME (Subject Matter Expert), LED (Learning Experience Designer), LES (Learning Experience Specialist), LEC (Learning Experience Coordinator), AD (Assistant Director), CTS (Campus Technology Services)
- **Use When**: course-outline-creator and uplimit-storyboard-builder reference when explaining Ivey's development timeline, team responsibilities, or learning model expectations

**course-outline-examples.md** (~20,000 words):
- **Source**: Anonymized from business-of-marketing-in-sport course (5-week MBA cohort)
- **Example 1**: Complete 5-week course with CLOs (5 outcomes), MLOs (4-5 per week), assessment scaffolding (formative → summative), concept threading (Revenue Ecosystem Framework introduced Week 1, applied Weeks 2-5), real cases (NHL/NBA/EPL/UFC), practitioner perspectives
- **Example 2**: 3-week executive education self-paced course with condensed structure
- **Key Patterns**: CLO design (single action verbs, Bloom's levels), MLO laddering (1.1-1.4 for Week 1), assessment alignment matrix, concept threading demonstrations
- **Use When**: course-outline-creator provides concrete templates when instructor says "show me an example" or needs inspiration for structure

**concept-threading-guide.md** (~12,500 words):
- **Purpose**: Prevent "orphaned concepts" (taught once, never revisited)
- **4 Threading Patterns**: Foundation→Application→Synthesis, Progressive Layering, Spiral Curriculum, Tool Accumulation
- **How-To Guide**: Step 1 (Identify core concepts), Step 2 (Introduce in Week 1), Step 3 (Apply in Weeks 2-4), Step 4 (Synthesize in Week 5), Step 5 (Make threads explicit with callbacks)
- **Common Mistakes**: Orphaned concepts, too many new concepts each week, implicit threading, linear topics instead of threaded concepts, assessment misalignment
- **Threading Checklist**: Planning phase (3-5 core concepts, Week 1 introduces all, minimum 3 appearances per concept), week-by-week design, language scaffolding, assessment alignment
- **Use When**: course-outline-creator guides instructor on course cohesion, uplimit-storyboard-builder validates threading across modules

**uplimit-content-design-guide.md** (~16,000 words):
- **Source**: Copied from business-of-marketing-in-sport Project Knowledge
- **Varied Content Delivery Principle**: Break text >1,500 words into multiple short elements using varied formats (text, video, infobox, widget, accordion)
- **Step-by-Step Process**: Phase 1 (Audit existing content for red flags), Phase 2 (Design varied delivery with format selection guide)
- **Case Study**: Week 1 Module 3 redesign (3,500 words → 1,000 words, 5% active → 75% active engagement through 8 widgets)
- **Uplimit Element Types**: Comprehensive guide to choosing appropriate formats (when to use video vs widget vs accordion)
- **Use When**: uplimit-storyboard-builder applies varied content delivery principles, transforms text-heavy content, selects appropriate element types

**Agent Updates**:

**course-outline-creator.md** (lines 50-79):
- Added "Bundled Knowledge Base" section referencing all 4 course-design-knowledge files
- References Ivey 6-phase process when instructor asks about timeline or team roles
- References course outline examples when instructor needs templates or inspiration
- References concept threading guide when instructor asks about course cohesion or week connections

**uplimit-storyboard-builder.md** (lines 72-116):
- Added "Bundled Knowledge Base" section referencing uplimit-content-design-guide.md
- References guide when creating storyboards (apply varied content delivery principles)
- References guide when auditing for interactivity (engagement metrics, passive/active ratios)
- References guide when transforming text-heavy content into interactive elements

**Updated Files**:
- `plugin.json`: Version 2.6.1, description mentions "bundled course design knowledge base"
- `marketplace.json`: Version 2.6.1, description updated similarly
- `CLAUDE.md`: Architecture diagram includes course-design-knowledge/ directory, version history updated

**Use Cases**:
- Internal Ivey team developing new courses: Agents reference institutional process and proven patterns
- Course outline creation: Concrete examples show what "good" looks like (CLO/MLO structure, threading, assessment alignment)
- Storyboard design: Varied content delivery guide prevents text-heavy modules
- Concept threading: Explicit patterns and checklists ensure cohesive course narratives

**Impact**:
- Agents provide Ivey-specific guidance (not generic instructional design advice)
- Concrete examples reduce "blank page" paralysis when starting new course
- Proven patterns from real courses (business-of-marketing-in-sport) ensure quality
- 4 knowledge files (~150 KB) complement existing assessment-knowledge/ (464 KB)
- Total bundled knowledge: ~614 KB (course design + assessment research)

### v2.4.2 (2025-10-21) - Peer Review Agent Storyboard vs Live Content Fix

**Agent Fixes**:

**peer-review-simulator.md**:
- **Critical Content Type Detection** - Agent now determines if reviewing storyboards (design specs) vs live content (implementations) FIRST
- **Dual-Mode Reviewer Profiles** - All 6 reviewers (Emma, Marcus, Priya, James, Sarah, Alex) now have two distinct modes:
  - **STORYBOARD REVIEW**: Reviews design quality, specifications clarity, feasibility, accessibility planning
    - Emma: Reviews learning objectives quality, element descriptions, tone specs
    - Marcus: Checks if accessibility is PLANNED (captions mentioned? keyboard nav specified?)
    - Priya: Reviews design system specs, visual descriptions clarity
    - James: Reviews widget specs for feasibility ("can this be built? is behavior clear?")
    - Sarah: Reviews learning design plans (alignment, sequencing, cognitive load planning)
    - Alex: Reviews navigation plans, information architecture design
  - **LIVE CONTENT REVIEW**: Tests actual implementation, measures compliance, validates functionality
    - Emma: Tests actual grammar, conciseness, readability
    - Marcus: Measures actual WCAG 2.2 AA compliance (contrast ratios, screen reader testing)
    - Priya: Tests actual typography, spacing, layout implementation
    - James: Tests actual functionality (browsers, links, performance, security)
    - Sarah: Reviews actual implementation (tests alignment, measures cognitive load)
    - Alex: Tests actual navigation, findability, usability
- **Fixed Edge Cases**:
  - Storyboards with unbuilt widgets = EXPECTED (specs describe future builds)
  - Live content with unbuilt widgets = CRITICAL PROBLEM (students see broken experience)
- **Updated Report Format**:
  - Clearly indicates review mode (STORYBOARD REVIEW vs LIVE CONTENT REVIEW)
  - Specifies content type (Storyboards .md vs Live Course Content .html)
  - Readiness criteria adapted: "Ready to build" vs "Launch-ready"
- **Updated Process**:
  - Step 0: DETERMINE CONTENT TYPE (check .md with element tables = storyboard, .html = live)
  - Step 2: Comprehensive analysis adapted based on content type
  - Updated checklists: Separate STORYBOARD vs LIVE CONTENT checklists
- **Example Invocations Updated**: Shows clear examples of both modes and when to use each

**Impact**:
- Prevents confusion: No longer tests browser compatibility on markdown design documents
- Enables preventative review: Catch spec issues before building (saves development time)
- Proper QA mode: Live content gets actual testing (links, contrast, functionality)
- Clear user guidance: Agent asks for clarification when content type unclear

**Bug Fixed**: Agent was reviewing storyboards (markdown design documents) as if they were live courses, trying to test links, measure contrast, and check browser compatibility on text files describing what WILL be built.

### v2.4.1 (2025-10-20) - Interactivity Analysis

**Agent Enhancements**:

**uplimit-storyboard-builder.md**:
- **Interactivity Analysis (New Audit Capability)** - Analyzes passive/active engagement ratios in course content
  - **Text Density Analysis**: Counts static text vs interactive elements, targets 30/70 passive/active ratio
  - **Knowledge Check Frequency**: Assesses formative assessment density (target: every 3-5 minutes)
  - **Transformation Opportunities**: Identifies text that should become widgets, videos, or hands-on activities
  - **AI Chat Placement**: Checks for contextual AI assistance throughout (not just at end)
  - **Video/Multimedia Balance**: Flags modules with zero video content
  - **Hands-On Practice**: Detects "tell-only" content that needs "do-it-yourself" activities
  - **Engagement Metrics Table**: Provides scorecard with 7 metrics (text words, passive/active ratio, knowledge checks, widgets, videos, hands-on activities, AI touchpoints)

**Use Cases**:
- Converting Canvas LMS content to Uplimit (identify text-heavy sections)
- Auditing existing storyboards for engagement quality (not just platform compliance)
- Diagnosing low completion rates (likely too much passive reading)
- Transforming traditional lecture content into interactive learning experiences

**Impact**:
- Identifies specific line ranges that should be transformed (e.g., "Lines 34-66: 3 pillars → animated timeline widget")
- Provides before/after element flow comparisons (e.g., "Current: 18 min, 80% passive → Recommended: 25 min, 70% active")
- Recommends specific widget types for each transformation (decision tree, scenario explorer, sandbox)
- Targets research-backed 30/70 passive/active ratio for optimal engagement

**Trigger Conditions**:
- User explicitly requests "interactivity analysis" or "engagement audit"
- User says content is "too text-heavy" or "needs more interaction"
- Audit reveals very long text blocks (>500 words per element)
- User is converting from traditional course format to Uplimit

### v2.4.0 (2025-10-17) - Executable Skills for Automation

**New Features**:
- **3 Executable Skills** - Python automation for template generation and validation
  - `assessment-template-generator` - PAIRR, AI roleplay, diagnostic rubric generators
  - `accessibility-audit-tools` - WCAG 2.2 AA automated testing (contrast, alt text, headings, ARIA)
  - `qm-validator` - Quality Matters validation (alignment, rubric math, measurable language)

**Agent Updates**:
- Updated `assessment-designer.md` - Invokes skills for PAIRR/AI roleplay generation + QM validation
- Updated `rubric-generator.md` - Invokes skills for diagnostic rubrics + proactive QM validation
- Updated `accessibility-auditor.md` - Invokes skills for automated first-pass testing

**Documentation**:
- Added `SKILLS-INSTALLATION.md` - Comprehensive installation guide with troubleshooting
- Updated `README.md` - Skills section with distribution options and examples
- Updated `CLAUDE.md` - Agent → Skill invocation pattern documentation

**Distribution**:
- **Bundled** (default): Skills included with plugin, zero configuration
- **Standalone**: ZIP files for reusability across plugins (24 KB, 9.6 KB, 11 KB)

**Impact**:
- Saves 10-15 minutes per assessment through automation
- Proactive quality assurance (catches errors before user sees them)
- Enables agents to focus on design advice vs. repetitive structure writing
- 152 KB total skill size (Python scripts + documentation)

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
- Direct installation: `/plugin add jameskruck/education-toolkit`
