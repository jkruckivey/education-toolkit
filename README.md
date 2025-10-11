# Education Toolkit - Claude Code Plugin

**Comprehensive toolkit for educational developers** with 9 specialized agents and 6 slash commands. Includes cutting-edge assessment methodologies: PAIRR (Peer and AI Review + Reflection), AI Roleplay exercises, and diagnostic rubrics for pre-learning assessment.

> **✨ NEW in v2.0**: PAIRR assessment methodology, AI Roleplay exercise design, and diagnostic rubric generation for formative assessment.

## Installation

```bash
/plugin marketplace add jameskruck/education-toolkit
/plugin install education-toolkit
```

**Migrating from claude-subagents NPM package?** This plugin replaces `@jameskruck/claude-subagents` with enhanced functionality (slash commands + same agents).

## What's Included

### 🤖 9 Specialized Agents

1. **accessibility-auditor** - WCAG 2.2 AA compliance checking with WebFetch capability
2. **assessment-designer** - Comprehensive assessment design with 464 KB bundled knowledge base. **NEW**: PAIRR methodology, AI Roleplay exercise design, Three-Tier AI permission model
3. **branding-checker** - Canvas LMS and Uplimit platform branding validation
4. **consistency-checker** - Cross-module terminology, concept threading, outcome alignment
5. **rubric-generator** - QM-aligned rubric generation. **NEW**: Diagnostic rubrics (3-level), PAIRR bonus rubrics, AI feedback prompts
6. **student-journey-simulator** - 4-persona course experience testing (Sarah, Marcus, Priya, Alex)
7. **udl-content-generator** - Transform content into multimodal formats (audio, visual, interactive)
8. **uplimit-storyboard-builder** - Complete copy-paste-ready implementation guides for Uplimit courses
9. **widget-tester** - 3-persona widget testing (Sarah, James, Maria) for UX validation

### ⚡ 6 Quick Slash Commands

1. **/audit-module** - Audit module for WCAG 2.2 AA accessibility compliance
2. **/test-widget** - Test interactive widget with 3 student personas
3. **/review-content** - Quick content review for educational quality
4. **/check-consistency** - Check consistency across modules
5. **/generate-rubric** - Generate QM-aligned assessment rubric
6. **/simulate-journey** - Simulate student journey through modules

### 📚 Bundled Knowledge Base (464 KB)

The **assessment-designer** agent includes:
- **4 Framework Guides**: UDL, Quality Matters, Inclusive Teaching, Assessment Templates
- **5 Research Papers**: AI Assessment Framework, Acceptable AI Use, Alternative Assessments, Academic Integrity, GenAI in Higher Ed
- **AI Assessment Principles**: Three-Tier Permission Model, Social Boundary Theory, AI-Resistant Design

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

- **2.0.0** (2025-10-11): Major update with evidence-based assessment methodologies
  - Added PAIRR (Peer and AI Review + Reflection) methodology to assessment-designer
  - Added AI Roleplay exercise design guidance (diagnostic, formative, summative)
  - Added diagnostic rubrics (3-level) to rubric-generator
  - Added uplimit-storyboard-builder agent (9 agents total, up from 7)
  - Consolidated from claude-subagents NPM package (deprecated)
- **1.0.0** (2025-10-10): Initial release with 7 agents, 6 commands, 464 KB knowledge base
