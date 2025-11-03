# Education Toolkit - Claude Code Plugin

**Comprehensive toolkit for educational developers** with 17 specialized agents, 10 slash commands, and automatic code review. Includes cutting-edge assessment methodologies: PAIRR (Peer and AI Review + Reflection), AI Roleplay exercises, diagnostic rubrics, widget design system enforcement, multi-perspective peer design review simulation, strategic course outline creation, specialized consistency checkers (terminology, concept threading, assessment), cohort course structure validation, and fullstack code review with automatic quality checks.

> **🔧 FIXED in v2.8.5**: Repository restructured to single plugin format - agents now invokable without double-scoping (use `uplimit-storyboard-builder` instead of `uplimit-storyboard-builder:uplimit-storyboard-builder`)
>
> **✨ NEW in v2.8.0**: Widget design system enforcement agent (generate/audit HTML widgets) with automatic testing hook
>
> **🔧 FIXED in v2.8.0**: Slash commands now work properly (marketplace.json commands array added)
>
> **✨ NEW in v2.7.0**: Three specialized consistency checkers replace old monolithic checker - terminology validation, concept threading tracking, and assessment methodology consistency
>
> **✨ NEW in v2.6.3**: Cohort course structure checker validates module sequences, learning outcomes widgets, PAIRR methodology, and Final Project Connections
>
> **✨ NEW in v2.6.2**: Course outline and storyboard builders now ask about course format (cohort vs. self-paced) to inform design decisions
>
> **✨ NEW in v2.6.1**: Course design knowledge base with Ivey 6-phase development process, course outline examples, concept threading patterns, and varied content delivery principles
>
> **✨ NEW in v2.6.0**: Strategic course outline creator with CLOs, weekly structure, MLOs, assessment strategy, and concept threading
>
> **✨ NEW in v2.5.0**: Automatic code review hook for FastAPI/Python and React/JSX with PostToolUse triggers

## Installation

```bash
/plugin marketplace add jameskruck/education-toolkit
```

**Gets you:** All 17 agents + 10 commands + 3 skills + automatic hooks

Agents are invoked automatically when your request matches their description, or you can invoke them directly:
- `uplimit-storyboard-builder` (no double-scoping needed!)
- `widget-designer`
- `assessment-designer`
- etc.

---

**Migrating from claude-subagents NPM package?** This plugin replaces `@jameskruck/claude-subagents` with enhanced functionality (slash commands + same agents).

## What's Included

### 🤖 17 Specialized Agents

1. **accessibility-auditor** - WCAG 2.2 AA compliance checking with WebFetch capability
2. **assessment-consistency-checker** - **NEW in v2.7.0**: Validates PAIRR methodology consistency across weeks, rubric structures, grading distribution. Course-type aware (flags peer review in self-paced courses).
3. **assessment-designer** - Comprehensive assessment design with 464 KB bundled knowledge base. **NEW**: PAIRR methodology, AI Roleplay exercise design, Three-Tier AI permission model
4. **backend-reviewer** - FastAPI/Python code review for security, error handling, API design, and performance
5. **branding-checker** - Canvas LMS and Uplimit platform branding validation
6. **cohort-structure-checker** - **NEW in v2.6.3**: Validates cohort course module structures (sequences, learning outcomes widgets, PAIRR methodology, Final Project Connections)
7. **concept-threading-checker** - **NEW in v2.7.0**: Validates Week 1 concepts appear in later weeks with progressive complexity. Maps concept introduction→usage, flags orphaned concepts, checks callback references.
8. **consistency-checker-DEPRECATED** - ⚠️ DEPRECATED in v2.7.0. Use specialized checkers instead: terminology-consistency-checker, concept-threading-checker, assessment-consistency-checker
9. **course-outline-creator** - **NEW**: Strategic course planning with CLOs, weekly structure, MLOs, assessment strategy, and concept threading. Asks about course format (cohort vs. self-paced) to inform structure. References bundled course design knowledge base.
10. **frontend-reviewer** - React/JSX code review for accessibility (WCAG 2.2 AA), UX patterns, and performance
11. **peer-review-simulator** - Multi-perspective design review with 6 ID specialists (Emma-Content, Marcus-Accessibility, Priya-Visual, James-Technical, Sarah-Pedagogy, Alex-UX)
12. **rubric-generator** - QM-aligned rubric generation. **NEW**: Diagnostic rubrics (3-level), PAIRR bonus rubrics, AI feedback prompts
13. **student-journey-simulator** - 4-persona course experience testing (Sarah, Marcus, Priya, Alex)
14. **terminology-consistency-checker** - **NEW in v2.7.0**: Builds course glossary, validates term consistency across all weeks. Tracks variations, identifies undefined acronyms, checks capitalization, generates consistency scores.
15. **udl-content-generator** - Transform content into multimodal formats (audio, visual, interactive)
16. **uplimit-storyboard-builder** - Complete copy-paste-ready implementation guides for Uplimit courses. Asks about course format (cohort vs. self-paced) to inform pacing and deadlines. References bundled course design knowledge base.
17. **widget-designer** - **NEW in v2.8.0**: Generate new interactive widgets OR audit existing widgets for design system compliance. Enforces Geist typography, neutral gray palette (no gold/green), CSS variables (no hardcoded hex), NO EMOJIS policy, PDF exports (not JSON). Reports issues with line numbers and offers automatic fixes.
18. **widget-tester** - 3-persona widget testing (Sarah, James, Maria) for UX validation

### ⚡ 10 Quick Slash Commands

1. **/audit-module** - Audit module for WCAG 2.2 AA accessibility compliance
2. **/build-storyboard** - Build comprehensive Uplimit storyboard with copy-paste-ready content
3. **/check-branding** - Validate Canvas LMS or Uplimit platform branding consistency
4. **/check-consistency** - Check consistency across modules (terminology, threading, narrative)
5. **/design-assessment** - Design comprehensive assessment with AI integration and UDL/QM compliance
6. **/generate-rubric** - Generate QM-aligned assessment rubric (quick rubric-only tasks)
7. **/peer-review** - **NEW**: Simulate design review panel with 6 ID specialists
8. **/review-content** - Quick content review for educational quality
9. **/simulate-journey** - Simulate student journey through modules with 4 personas
10. **/test-widget** - Test interactive widget with 3 student personas

### 📚 Bundled Knowledge Base (~614 KB)

**Assessment Research Knowledge (464 KB)** - Used by assessment-designer agent:
- **4 Framework Guides**: UDL, Quality Matters, Inclusive Teaching, Assessment Templates
- **5 Research Papers**: AI Assessment Framework, Acceptable AI Use, Alternative Assessments, Academic Integrity, GenAI in Higher Ed
- **AI Assessment Principles**: Three-Tier Permission Model, Social Boundary Theory, AI-Resistant Design

**Course Design Knowledge (~150 KB)** - **NEW in v2.6.1** - Used by course-outline-creator and uplimit-storyboard-builder agents:
- **Ivey 6-Phase Development Process**: Planning → Design → Production → Build → Quality → Launch, cohort/self-paced models, team roles
- **Course Outline Examples**: Anonymized 5-week MBA course templates with CLOs, MLOs, assessment scaffolding, concept threading
- **Concept Threading Guide**: 4 threading patterns (Foundation→Application→Synthesis, Progressive Layering, Spiral Curriculum, Tool Accumulation), best practices, checklists
- **Varied Content Delivery Guide**: Break text-heavy content into interactive elements, engagement metrics, transformation opportunities

### ✨ NEW: Evidence-Based Assessment Methodologies

#### PAIRR (Peer and AI Review + Reflection)
**Research-backed dual-feedback methodology** where students receive feedback from both a peer and AI, then critically compare both sources through structured reflection.

**Benefits:**
- Develops critical AI literacy (students evaluate AI output quality)
- Multiple perspectives improve writing quality
- Students maintain writerly agency (choose which feedback to apply)
- Prepares for AI-integrated workplaces

**Implementation:**
1. Student submits 80% draft
2. Gets peer review (rubric-aligned) + AI feedback (same rubric)
3. Completes comparative reflection (150-200 words)
4. Revises based on critical evaluation
5. Post-revision reflection on which feedback influenced most

**Ask agents:** "Design a PAIRR workflow for my reflection memo" or "Generate a PAIRR rubric with bonus points"

#### AI Roleplay Exercises
**Conversational assessments** where students engage with AI character roleplaying as stakeholder, expert, or decision-maker.

**Three Types:**
1. **Diagnostic** (pre-learning): Reveals gaps before content delivery
2. **Formative** (during learning): Practice before summative assessment
3. **Summative** (after learning): Demonstrates mastery through conversation

**Benefits:**
- Tests application & synthesis (higher Bloom's levels)
- Authentic communication practice
- Immediate conversational feedback
- Accessibility: Oral assessment alternative

**Ask agents:** "Design an AI Roleplay for practicing [skill]" or "Create a diagnostic roleplay exercise"

#### Diagnostic Rubrics (3-Level)
**Formative pre-learning rubrics** with Beginning → Developing → Proficient levels (no "Exemplary" since mastery not expected).

**Key Features:**
- Typical student responses at each level
- Support flags (when to provide scaffolding)
- Non-evaluative tone ("This helps you identify what to focus on")
- 2-3 minute grading time per student

**Ask agents:** "Generate a diagnostic rubric for pre-assessment" or "Create a 3-level formative rubric"

### 🚀 NEW: Executable Skills (Python Automation)

**Agents now invoke executable Python skills for automated template generation and validation.**

#### assessment-template-generator
**Automated PAIRR, AI Roleplay, and Diagnostic Rubric generation**
- Generates complete PAIRR assignment templates (rubric + AI prompt + reflections + faculty guide)
- Creates Uplimit AI Roleplay configurations (diagnostic/formative/summative types)
- Builds 3-level diagnostic rubrics with support flags
- **Agents invoke automatically** when you request these assessment types

**Example**: "Create a PAIRR assignment for my marketing memo" → Agent runs Python script → Complete template generated

#### accessibility-audit-tools
**Automated WCAG 2.2 AA compliance checking**
- Color contrast validator (calculates ratios, suggests fix colors)
- Alt text checker (presence + quality patterns)
- Heading hierarchy validator
- ARIA compliance scanner
- **Agents invoke for first-pass automation**, then manual review

**Example**: "Check accessibility compliance" → Agent runs automated tests → Detailed report with line numbers and fixes

#### qm-validator
**Quality Matters standards validation**
- Outcome-criteria alignment checker (detects orphaned criteria)
- Rubric math validator (point totals, distribution balance)
- Measurable language analyzer (Bloom's taxonomy verbs)
- **Agents invoke proactively** after generating rubrics

**Example**: Agent generates rubric → Auto-validates QM compliance → Fixes issues before presenting to you

**Why Skills Matter**: These executable tools save 10-15 minutes per assessment by automating repetitive structure generation and validation, letting agents focus on customization and design advice.

**Distribution Options:**
- **Bundled** (default): Skills included with plugin, zero config
- **Standalone**: Download ZIPs from [releases](https://github.com/jkruckivey/education-toolkit/releases) for use with other plugins

📖 **[Skills Installation Guide](SKILLS-INSTALLATION.md)** - Detailed setup instructions, requirements, and troubleshooting

### 🔄 NEW: Automatic Quality Enforcement (Hooks)

**Built-in automation that runs quality checks automatically - zero API tokens, zero manual effort.**

This plugin includes 5 automatic hooks that enforce quality standards in real-time (plus 1 new in v2.8.0):

#### Hook 1: Smart Content Validator (PostToolUse)
**Runs after every file edit** - Instant feedback on quality issues

✓ **HTML files**: WCAG 2.2 AA checks (contrast, alt text, headings, buttons, tables)
✓ **Markdown files**: Learning outcomes (Bloom's verbs), rubric math, PAIRR components, WCAG version
✓ **Storyboards**: Colored emoji detection, terminology consistency

**Example output:**
```
📋 Auto-validation found 2 issue(s):
  ⚠️  Found 3 instance(s) of vague learning outcome language
     Avoid: understand, know, learn about
     Use: explain, identify, analyze, evaluate

  ⚠️  Missing alt text on 1 image(s)
     All images need alt="description" or alt="" (if decorative)
```

**Token savings**: ~10,000 tokens per validation × 20 edits/day = 200,000 tokens/day saved

#### Hook 2: Educational Context Loader (SessionStart)
**Runs once at session start** - Sets educational standards context automatically

✓ Loads WCAG 2.2 AA, QM 6th Edition, Bloom's Taxonomy, UDL standards
✓ Displays available quick commands (/design-assessment, /peer-review, etc.)
✓ Shows course-specific config (if `.education-toolkit-config.json` exists)
✓ Reminds you of automatic quality checks active

**No more forgetting** which WCAG version to use or which commands are available.

#### Hook 3: Protected Content Guardian (PreToolUse)
**Runs before editing published content** - Prevents accidental changes to student-facing materials

✓ Blocks edits to `published/`, `production/`, `final/`, `student-facing/`, `graded/` paths
✓ Shows warning with risks (fairness, academic integrity, student trust)
✓ Recommends creating draft version first
✓ Requires explicit approval to proceed

**Protects against**: Changing rubrics after students submit, modifying published assessments mid-term

#### Hook 4: Storyboard Auto-Formatter (PostToolUse)
**Runs after editing storyboards** - Ensures consistent platform conventions

✓ Converts colored emoji → black symbols (🔴→⬤ 🟡→◐ 🟢→○)
✓ Standardizes priority badges, element headings, MLO references
✓ Fixes table spacing, heading spacing, time estimates
✓ Removes trailing spaces, normalizes blank lines

**Example output:**
```
✨ Auto-formatted storyboard:
  • Converted 8× 🔴 → ⬤
  • Converted 5× 📺 → ▶
  • Standardized element heading format (dash → colon)
  • Fixed table spacing
```

#### Hook 5: Fullstack Code Reviewer (PostToolUse)
**Runs after editing Python or React code** - Automatic code review for educational technology projects

✓ **Backend (Python/FastAPI)**: Security, input validation, error handling, API design, async/await
✓ **Frontend (React/JSX)**: Accessibility (WCAG 2.2 AA), state management, UX patterns, performance
✓ **Smart routing**: Detects file type → launches specialized agent (backend-reviewer or frontend-reviewer)
✓ **Skips non-code**: Config files, package.json, small formatting changes

**Review criteria:**
- **Security**: Authentication, input sanitization, secret management
- **Accessibility**: ARIA labels, semantic HTML, keyboard navigation, color contrast
- **Best practices**: React hooks, error handling, loading states, user feedback
- **Performance**: Database queries, re-renders, bundle size

**Example output:**
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

**When to use manually**: Invoke `backend-reviewer` or `frontend-reviewer` agents directly for comprehensive file review without waiting for edits

#### Hook 6: Widget Auto-Tester (PostToolUse) - **NEW in v2.8.0**
**Runs after creating new widgets** - Automatic accessibility testing and optional browser preview

✓ **Auto-detects widget creation**: Triggers only on new `.html` files in `widget` directories
✓ **Accessibility tests**: Runs webapp-testing skill (keyboard nav, focus indicators, ARIA, touch targets)
✓ **JSON results**: Generates `*_accessibility_results.json` with violations and recommendations
✓ **Optional browser preview**: Auto-opens widget in browser (enable with `.auto-open-widgets` file)
✓ **Cross-platform**: macOS (open), Linux (xdg-open), Windows (start)

**Example output:**
```
🧪 AUTO-TESTING NEW WIDGET: quiz.html
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Running accessibility tests...
✓ Accessibility test complete: quiz_accessibility_results.json
  • Found 3 accessibility issue(s)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Enable auto-open in browser:**
```bash
# macOS/Linux
touch ~/.claude/plugins/education-toolkit/.auto-open-widgets

# Windows (PowerShell)
New-Item -ItemType File -Path "$env:USERPROFILE\.claude\plugins\education-toolkit\.auto-open-widgets"
```

**Token savings**: ~5,000 tokens per manual test × 10 widgets/week = 50,000 tokens/week saved

#### Performance & Cost

| Metric | Value |
|--------|-------|
| **Execution time** | 1-8 seconds (runs locally, widget tests take longer) |
| **API tokens used** | 0 tokens (pure bash/Python automation) |
| **Token savings** | ~250,000+ tokens/day for active users |
| **Accuracy** | 100% consistent (deterministic, not LLM-based) |

#### Configuration (Optional)

Create `.education-toolkit-config.json` in your project root for custom settings:

```json
{
  "courseName": "Business of Sports Marketing",
  "institution": "Ivey Business School",
  "platform": "Uplimit",
  "conventions": {
    "learningOutcomePrefix": "MLO",
    "wcagVersion": "2.2"
  },
  "protectedPaths": [
    "published/*",
    "custom/protected/path/*"
  ]
}
```

See `.education-toolkit-config.example.json` for full configuration options.

**Hooks are always active when plugin is enabled** - no setup required. Disable individual hooks by editing `hooks/hooks.json` if needed.

## Usage Examples

### Quick Accessibility Check
```bash
/audit-module modules/week1
```

### Test a Widget
```bash
/test-widget widgets/revenue-empire-builder.html
```

### Review Content Quality
```bash
/review-content modules/week2/outline.html
```

### Generate Assessment Rubric
```bash
/generate-rubric for Week 1 case analysis
```

### Simulate Student Experience
```bash
/simulate-journey modules/week1 modules/week2
```

### Check Course Consistency
```bash
/check-consistency week1-5
```

### Peer Design Review
```bash
/peer-review Week 1
```

## Natural Language Invocation

After installation, you can also invoke agents with natural language:

- "Audit modules/module-1/index.html for accessibility"
- "Test the fan engagement lab widget"
- "Check if this matches Canvas LMS branding"
- "Generate a rubric for this reflection memo"
- "Simulate a student going through Week 1"
- "Check terminology consistency across all modules"

## Use Cases

### Course Development Teams
- Standardize QA workflows across team members
- Ensure consistent accessibility and branding compliance
- Validate pedagogical quality before publishing

### Solo Course Developers
- Get instant feedback on content quality
- Test widgets with multiple student perspectives
- Generate professional rubrics quickly

### Instructional Designers
- Audit courses for WCAG 2.2 AA compliance
- Validate UDL principles implementation
- Check Quality Matters standards alignment

### Educational Technologists
- Test interactive learning tools thoroughly
- Ensure platform branding consistency
- Validate assessment design best practices

## Agent Details

### accessibility-auditor
**Tools**: Read, Glob, Grep, WebFetch
**Speed**: 2-5 minutes (Sonnet)
**Best for**: WCAG 2.2 AA audits, Canvas LMS content, HTML/CSS validation

### widget-tester
**Tools**: Read, Glob
**Speed**: 2-5 minutes (Sonnet)
**Best for**: Interactive widgets, simulations, learning games
**Personas**:
- Sarah (Quick Learner) - tech-savvy, skims instructions
- James (Methodical Analyst) - tests edge cases, explores deeply
- Maria (Struggling Student) - needs clear guidance, frustrated easily

### branding-checker
**Tools**: Read, Glob
**Speed**: 2-5 minutes (Sonnet)
**Best for**: Canvas LMS courses, Uplimit platform content
**Detects**: Uplimit Geist font, neutral grays, NO colored labels/badges

### rubric-generator
**Tools**: Read, Glob, Grep
**Speed**: 2-5 minutes (Sonnet)
**Best for**: QUICK rubric-only tasks
**Note**: For comprehensive assessment design, use assessment-designer instead

### student-journey-simulator
**Tools**: Read, Glob, Grep
**Speed**: 5-8 minutes (Opus)
**Best for**: Multi-week course experience testing
**Personas**:
- Sarah (Visual Learner) - needs diagrams, struggles with text
- Marcus (Analytical Thinker) - wants data and sources
- Priya (Collaborative Leader) - thrives in group work
- Alex (Time-Constrained Professional) - needs efficiency

### consistency-checker
**Tools**: Read, Glob, Grep
**Speed**: 5-8 minutes (Opus)
**Best for**: Cross-module narrative flow, concept threading, terminology audits

### peer-review-simulator
**Tools**: Read, Glob, Grep
**Speed**: 8-12 minutes (Opus)
**Best for**: Comprehensive multi-perspective design review before launch
**Review Panel**:
- Emma (Content & Writing) - Grammar, clarity, inclusive language
- Marcus (Accessibility & Inclusion) - WCAG 2.2 AA, UDL, cultural sensitivity
- Priya (Visual Design & UI) - Typography, layout, visual consistency
- James (Technical & Functionality) - Browser compatibility, performance, security
- Sarah (Pedagogical Design) - Learning alignment, Bloom's accuracy, scaffolding
- Alex (UX & Navigation) - Information architecture, wayfinding, usability
**Output**: Cross-reviewer themes prioritized, individual specialist feedback, fix time estimates

### assessment-designer
**Tools**: Read, Glob, Grep, WebFetch
**Speed**: 3-6 minutes (Sonnet)
**Best for**: Strategic assessment design, AI integration, UDL/QM compliance
**Knowledge Base**: 464 KB (9 files) - frameworks and AI assessment research

## Contributing

Found a bug or have a feature request? Open an issue at:
https://github.com/jameskruck/education-toolkit/issues

## License

MIT License - See LICENSE file for details

## Author

**James Kruck**
Email: jkruck@ivey.ca
GitHub: [@jameskruck](https://github.com/jameskruck)

## Version History

- **2.7.0** (2025-01-29): Specialized consistency checkers
  - Replaced monolithic consistency-checker with 3 specialized agents for better precision
  - Added **terminology-consistency-checker** (18 KB): Builds course glossary, validates term consistency, tracks variations, identifies undefined acronyms
  - Added **concept-threading-checker** (22 KB): Maps concept introduction→usage across weeks, flags orphaned concepts, validates progressive complexity, checks callback references
  - Added **assessment-consistency-checker** (20 KB): Validates PAIRR methodology consistency, rubric structures, grading distribution, course-type aware (flags peer review in self-paced courses)
  - Deprecated old consistency-checker (renamed to consistency-checker-DEPRECATED.md with migration guide)
  - **Why the change?** Old checker tried to do too much (7 dimensions), leading to missed issues. New specialized agents have narrow scope, are faster, and catch more problems.
  - 16 agents total (up from 14)
- **2.6.3** (2025-01-28): Cohort course structure validation
  - Added **cohort-structure-checker** agent (25 KB, sonnet)
  - Validates cohort course module structures against standardized templates
  - Checks module sequences (0→1→2→...→7), element patterns, learning outcomes widgets (module-specific MLOs→CLOs)
  - Validates PAIRR methodology presence in Module 6, Final Project Connections quality, element numbering integrity
  - Identifies inconsistencies: missing widgets, wrong element types, generic project connections
  - Course-type aware: Different validation rules for cohort vs self-paced courses
  - 15 agents total (up from 14)
- **2.6.2** (2025-01-28): Course format discovery
  - Updated course-outline-creator agent to ask about course format (cohort vs. self-paced) as first discovery question
  - Updated uplimit-storyboard-builder agent to request course format in initial context gathering
  - Added course format to Required Input section with detailed explanations (cohort: fixed dates, synchronous elements; self-paced: own speed, asynchronous only)
  - Course format informs critical design decisions: weekly structure vs modules, deadlines, peer review feasibility, synchronous elements
- **2.6.1** (2025-01-28): Added course design knowledge base
  - Added ~150 KB bundled course design knowledge base (4 files)
  - **ivey-course-development-process.md**: 6-phase process, cohort/self-paced models, team roles
  - **course-outline-examples.md**: Anonymized 5-week MBA course templates with full CLO/MLO structure
  - **concept-threading-guide.md**: 4 threading patterns, best practices, checklists to prevent orphaned concepts
  - **uplimit-content-design-guide.md**: Varied content delivery principles, engagement metrics, transformation opportunities
  - Updated course-outline-creator agent to reference all 4 knowledge files
  - Updated uplimit-storyboard-builder agent to reference content design guide
  - Total bundled knowledge: ~614 KB (course design 150 KB + assessment research 464 KB)
  - Fixed WCAG 2.1 → 2.2 in 3 knowledge base files (inclusive-teaching.md, qm-standards.md, udl-guide.md)
  - Added YAML frontmatter to backend-reviewer, frontend-reviewer, uplimit-storyboard-builder agents
- **2.6.0** (2025-01-28): Added strategic course outline creator
  - Added course-outline-creator agent (14 KB, sonnet, WebFetch)
  - Strategic curriculum design expert for comprehensive course outlines
  - Guides instructors through: CLO definition (QM-compliant), weekly structure planning, MLO creation, assessment strategy design, concept threading, case/practitioner identification
  - Discovery interview process for gathering requirements
  - Assessment alignment matrix ensures all CLOs covered proportionally
  - Concept threading prevents orphaned topics (introduced Week 1, applied Weeks 2-5)
  - Workflow position: SME expertise → course-outline-creator → uplimit-storyboard-builder → build in platform
  - 13 agents total (up from 12)
- **2.5.0** (2025-01-23): Added automatic fullstack code review
  - Added backend-reviewer agent (FastAPI/Python expertise)
  - Added frontend-reviewer agent (React/JSX + WCAG 2.2 AA)
  - Added Hook 5: review-on-change.md (PostToolUse automatic code review)
  - Smart routing: Detects file type → launches specialized agent
  - Intelligent skipping: Config files, small formatting changes, comment-only edits
  - Review criteria: Security, accessibility, best practices, performance
  - 12 agents total, 5 hooks
- **2.4.2** (2025-10-21): Fixed peer-review-simulator to distinguish storyboards vs live content
  - Added critical content type detection (storyboard design specs vs implemented courses)
  - Updated all 6 reviewers with dual modes: STORYBOARD REVIEW vs LIVE CONTENT REVIEW
  - Storyboard mode: Reviews design quality, specifications clarity, feasibility, accessibility planning
  - Live content mode: Tests actual functionality, measures compliance, validates implementation
  - Fixed edge cases: Unbuilt widgets in storyboards = EXPECTED, in live content = CRITICAL
  - Updated report format to clearly indicate review mode and content type
  - Added example invocations showing when to use each mode
  - Prevents confusion: No longer tests browser compatibility on markdown design documents
- **2.4.1** (2025-10-20): Added automatic quality enforcement hooks
  - 4 new hooks: Smart content validator, educational context loader, protected content guardian, storyboard auto-formatter
  - Zero API tokens consumed (pure bash/Python automation)
  - Automatic WCAG/QM/Bloom's validation after every edit (1-3 seconds)
  - Session startup loads educational standards context automatically
  - Protects published content from accidental edits
  - Auto-formats storyboards for platform branding compliance
  - Added .education-toolkit-config.json support for course-specific settings
- **2.4.0** (2025-10-17): Added executable skills for automation
  - 3 new skills: assessment-template-generator, accessibility-audit-tools, qm-validator
  - Python automation for PAIRR templates, AI roleplay configs, diagnostic rubrics
  - Automated WCAG 2.2 AA accessibility testing (color contrast, alt text, headings, ARIA)
  - Quality Matters validation (outcome-criteria alignment, rubric math, measurable language)
  - Agents proactively invoke skills for template generation and validation
  - Dual distribution: bundled with plugin (default) + standalone ZIPs for reusability
  - Saves 10-15 minutes per assessment through automation
  - Added SKILLS-INSTALLATION.md with comprehensive setup guide
- **2.3.0** (2025-10-17): Added peer design review simulation
  - Added peer-review-simulator agent with 6 ID specialists (Emma, Marcus, Priya, James, Sarah, Alex)
  - Added /peer-review slash command
  - Multi-perspective comprehensive review with cross-reviewer theme prioritization
  - 10 agents total, 10 slash commands
- **2.0.0** (2025-10-11): Major update with evidence-based assessment methodologies
  - Added PAIRR (Peer and AI Review + Reflection) methodology to assessment-designer
  - Added AI Roleplay exercise design guidance (diagnostic, formative, summative)
  - Added diagnostic rubrics (3-level) to rubric-generator
  - Added uplimit-storyboard-builder agent (9 agents total, up from 7)
  - Consolidated from claude-subagents NPM package (deprecated)
- **1.0.0** (2025-10-10): Initial release with 7 agents, 6 commands, 464 KB knowledge base
