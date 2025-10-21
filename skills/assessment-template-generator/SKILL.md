---
name: "Assessment Template Generator"
description: "Generate structured assessment templates (PAIRR, AI Roleplay, Diagnostic Rubrics) using Python automation. Agents invoke this to quickly scaffold evidence-based assessment formats."
version: "1.0.0"
dependencies: "python>=3.8"
---

# Assessment Template Generator

Executable Python scripts that auto-generate assessment template files based on evidence-based methodologies.

## What This Skill Provides

### 1. PAIRR (Peer and AI Review + Reflection) Templates
- Complete PAIRR setup with rubric, AI prompt, reflection questions
- Bonus points structure (5-7% of assignment grade)
- Comparative reflection evaluation criteria
- Post-revision reflection prompts

### 2. AI Roleplay Exercise Configurations
- Uplimit-compatible AI roleplay scenarios
- Student instructions, AI character setup, system prompts
- Diagnostic, formative, or summative variants
- Rubric with appropriate performance levels

### 3. Diagnostic Rubric Structures
- 3-level pre-learning rubrics (Beginning → Developing → Proficient)
- Support flags for scaffolding triggers
- Faculty guidance with typical student responses
- Non-evaluative, formative-focused language

## How Agents Invoke This Skill

Agents use the Skill tool to run Python scripts that generate markdown template files:

```bash
# Generate PAIRR template
python scripts/generate_pairr.py --assignment-name "Week 3 Business Memo" --points 30 --criteria "Analysis quality, Evidence usage, Professional writing"

# Generate AI Roleplay configuration
python scripts/generate_ai_roleplay.py --scenario "Pitch to PE Partner" --type summative --learning-outcome "Defend investment using revenue ecosystem analysis"

# Generate Diagnostic Rubric
python scripts/generate_diagnostic_rubric.py --skill-area "Revenue Streams Knowledge" --week 1
```

## Script Reference

### generate_pairr.py
**Purpose**: Creates complete PAIRR methodology setup file

**Arguments**:
- `--assignment-name` (required): Name of the assignment (e.g., "Week 3 Memo")
- `--points` (required): Base assignment points (bonus will be calculated as 5-7%)
- `--criteria` (required): Comma-separated list of 3-5 rubric criteria
- `--output` (optional): Output filename (default: pairr-{assignment-name}.md)

**Output**: Markdown file containing:
- Main assignment rubric (30 points)
- PAIRR participation rubric (5 bonus points)
- AI feedback prompt template
- Comparative reflection questions
- Post-revision reflection questions
- Grading instructions for faculty

### generate_ai_roleplay.py
**Purpose**: Creates AI roleplay exercise configuration in Uplimit format

**Arguments**:
- `--scenario` (required): Scenario title (e.g., "Practice Sales Negotiation")
- `--type` (required): diagnostic | formative | summative
- `--learning-outcome` (required): The CLO/MLO being assessed
- `--ai-character-name` (optional): Name of AI role (default: auto-generated)
- `--ai-character-role` (optional): Role description (default: auto-generated from scenario)
- `--output` (optional): Output filename (default: ai-roleplay-{scenario}.md)

**Output**: Markdown file with Uplimit tabs:
- Learning Objective tab configuration
- Scenario tab (context, AI name/role, student role)
- Hidden Context tab (AI personality, behavioral guidelines, assessment goals)
- Criteria tab (rubric with appropriate levels based on type)

### generate_diagnostic_rubric.py
**Purpose**: Creates 3-level pre-learning assessment rubric

**Arguments**:
- `--skill-area` (required): Skill or knowledge area being diagnosed (e.g., "Revenue Streams Knowledge")
- `--week` (required): Week/module number for context
- `--criteria-count` (optional): Number of criteria (default: 3)
- `--output` (optional): Output filename (default: diagnostic-rubric-week{week}.md)

**Output**: Markdown file containing:
- 3-level rubric (Beginning | Developing | Proficient)
- Student-facing version with encouraging language
- Faculty version with support flags and typical responses
- Expected distribution (50% Beginning, 35% Developing, 15% Proficient)

## When to Use This Skill

**Assessment-designer agent should invoke when**:
- User asks to "create a PAIRR assignment"
- User requests "AI roleplay exercise"
- User needs "diagnostic assessment before Week X"
- User wants "pre-learning rubric"

**Rubric-generator agent should invoke when**:
- User specifies PAIRR methodology
- User requests diagnostic/formative rubric
- User mentions "pre-learning assessment"

## Example Invocations

### From assessment-designer agent:

```
User: "Help me create a PAIRR assignment for my Week 3 business memo"

Agent: I'll use the assessment-template-generator skill to create a complete PAIRR setup.

*Invokes Skill tool*:
Skill: assessment-template-generator
Command: python scripts/generate_pairr.py --assignment-name "Week 3 Business Memo" --points 30 --criteria "Strategic analysis, Evidence-based recommendations, Professional writing, Data visualization"
```

```
User: "Design a diagnostic AI roleplay to assess revenue knowledge before Week 1"

Agent: I'll generate a diagnostic AI roleplay configuration using the template generator.

*Invokes Skill tool*:
Skill: assessment-template-generator
Command: python scripts/generate_ai_roleplay.py --scenario "Explain Revenue Ecosystem" --type diagnostic --learning-outcome "Identify major revenue streams in sports business"
```

## Additional Resources

See `REFERENCE.md` for:
- Complete PAIRR methodology research citation (Frontiers in Communication 2025)
- AI roleplay design principles
- Diagnostic rubric best practices
- Customization examples
