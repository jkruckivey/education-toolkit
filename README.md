# Education Toolkit - Claude Code Plugin

Comprehensive toolkit for course developers with 7 specialized agents and 6 slash commands for accessibility auditing, widget testing, branding validation, assessment design, student journey simulation, consistency checking, and UDL content generation.

## Installation

```bash
/plugin marketplace add jameskruck/education-toolkit
/plugin install education-toolkit
```

## What's Included

### 🤖 7 Specialized Agents

1. **accessibility-auditor** - WCAG 2.2 AA compliance checking with WebFetch capability
2. **widget-tester** - 3-persona widget testing (Sarah, James, Maria) for UX validation
3. **branding-checker** - Canvas LMS and Uplimit platform branding validation
4. **rubric-generator** - Quick rubric generation from learning outcomes (QM-aligned)
5. **student-journey-simulator** - 4-persona course experience testing (Sarah, Marcus, Priya, Alex)
6. **consistency-checker** - Cross-module terminology, concept threading, outcome alignment
7. **assessment-designer** - Comprehensive assessment design with 464 KB bundled knowledge base (AI integration, UDL/QM compliance, research-backed guidance)

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

- **1.0.0** (2025-10-10): Initial release with 7 agents, 6 commands, 464 KB knowledge base
