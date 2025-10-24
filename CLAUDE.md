# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

**Education Toolkit** - Claude Code plugin providing 12 specialized agents, 10 slash commands, and automatic code review for educational developers, instructional designers, and course creators. Focus areas: accessibility (WCAG 2.2 AA), assessment design, UDL implementation, Quality Matters standards, AI-integrated pedagogy, multi-perspective peer design review, and fullstack code quality (FastAPI/Python + React/JSX).

**Version**: 2.5.0 (January 2025)
**Tech stack**: Markdown-based agent definitions, bundled knowledge base (464 KB), PostToolUse hooks for automatic code review
**Distribution**: Claude Code plugin marketplace (`/plugin marketplace add jameskruck/education-toolkit`)

## Architecture

### Plugin Structure

```
education-toolkit/
├── .claude-plugin/
│   ├── plugin.json          # Main plugin manifest
│   └── marketplace.json     # Marketplace configuration
├── hooks/                   # Automatic quality enforcement (5 hooks)
│   ├── hooks.json           # Hook configurations
│   ├── review-on-change.md  # PostToolUse: Fullstack code review (NEW v2.5.0)
│   └── scripts/
│       ├── validate-content.sh      # PostToolUse: Smart validator
│       ├── load-context.sh          # SessionStart: Context loader
│       ├── check-protected.sh       # PreToolUse: Content guardian
│       └── format-storyboard.py     # PostToolUse: Auto-formatter
├── agents/                  # 12 specialized agents
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
│   ├── backend-reviewer.md (12 KB, sonnet, FastAPI/Python expertise) # NEW v2.5.0
│   ├── frontend-reviewer.md (13 KB, sonnet, React/WCAG 2.2 AA) # NEW v2.5.0
│   └── assessment-knowledge/  # Bundled knowledge base
│       ├── frameworks/        # UDL, QM, Inclusive Teaching, Templates
│       └── research/          # AI assessment research (5 papers)
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
- Types: Smart validator, context loader, content guardian, auto-formatter

### Hooks System (NEW v2.4.1)

Hooks provide **deterministic automation** that runs at specific lifecycle events, transforming the plugin from reactive (user asks for validation) to proactive (automatic enforcement).

**Key Advantage**: Hooks use **zero API tokens** - they're pure bash/Python automation running on the user's local machine.

**4 Built-in Hooks**:

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

**Performance**: 1-3 seconds execution, 0 API tokens, 100% consistency

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
- **Version history** - Track methodology additions in README.md (v2.5.0 added Fullstack Code Review, v2.4.2 fixed peer review storyboard vs live content, v2.4.1 added Interactivity Analysis + Automatic Hooks, v2.4.0 added Executable Skills, v2.3.2 added Peer Design Review Simulator, v2.3.1 added storyboard validation enhancements, v2.0 added PAIRR, AI Roleplay, Diagnostic Rubrics)

## Version History & Changelog

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
- Marketplace installation: `/plugin marketplace add jameskruck/education-toolkit`
