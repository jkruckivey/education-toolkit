---
name: "QM Validator"
description: "Quality Matters (QM) compliance validation for rubrics and assessments. Python scripts check outcome-criteria alignment, rubric math, measurable language (Bloom's taxonomy), and QM standards. Agents invoke for fast quality assurance."
version: "1.0.0"
dependencies: "python>=3.8"
---

# QM Validator

Executable Python scripts that validate Quality Matters (QM) standards compliance for educational assessments and rubrics.

## What This Skill Provides

### 1. Outcome-Criteria Alignment Checker
- Validates every rubric criterion maps to at least one learning outcome
- Ensures every learning outcome is assessed by at least one criterion
- Detects orphaned criteria (no outcome alignment)
- Checks Bloom's taxonomy level consistency

### 2. Rubric Math Validator
- Verifies point totals add up correctly
- Checks for point distribution balance (no single criterion >50% of grade)
- Validates performance level percentages (90-100%, 80-89%, etc.)
- Detects missing or duplicate point values

### 3. Measurable Language Analyzer
- Scans learning outcomes for measurable Bloom's verbs
- Flags vague language ("understand", "know", "learn about")
- Validates verb-outcome alignment (Analyze → analytical criteria)
- Suggests specific alternatives for unmeasurable language

### 4. QM Standards Compliance Report
- Checks against QM Standard 3 (Assessment and Measurement)
- Validates clear instructions (Standard 5)
- Ensures accessibility considerations (Standard 6)
- Generates compliance matrix with gaps

## How Agents Invoke This Skill

Agents use the Skill tool to run Python scripts on rubric/assessment files:

```bash
# Check outcome-criteria alignment
python scripts/check_alignment.py --rubric rubric.md --outcomes outcomes.txt

# Validate rubric math
python scripts/check_rubric_math.py --file rubric.md

# Analyze measurable language
python scripts/check_measurable_language.py --outcomes outcomes.txt --strict

# Generate QM compliance report
python scripts/check_qm_compliance.py --assessment-dir week3/ --report html
```

## Script Reference

### check_alignment.py
**Purpose**: Validates outcome-rubric criteria alignment

**Arguments**:
- `--rubric` (required): Rubric markdown file
- `--outcomes` (required): Learning outcomes file (text or markdown)
- `--verbose` (optional): Show detailed mapping

**Output**: Alignment report with:
- Outcome → Criteria mapping matrix
- Orphaned criteria (no outcome link)
- Untested outcomes (no criteria assess them)
- Bloom's level mismatches
- Recommendations for fixes

**QM Standard Addressed**: Standard 3.1 - "Assessments measure stated learning objectives"

### check_rubric_math.py
**Purpose**: Validates rubric point calculations

**Arguments**:
- `--file` (required): Rubric markdown file
- `--tolerance` (optional): Allowed point variance (default: 0)

**Output**: Math validation report with:
- Total points stated vs. actual sum
- Per-criterion point allocation
- Balance analysis (flagging if one criterion >50%)
- Performance level percentages validation
- Missing point values

**Common Issues Detected**:
- Total points = 30 but criteria sum to 28 (ERROR)
- Single criterion worth 20/30 pts (WARNING: over-weighted)
- Performance level "Proficient (80-89%)" but points say "24-27/30" = 80-90% (MISMATCH)

### check_measurable_language.py
**Purpose**: Validates learning outcomes use measurable Bloom's taxonomy verbs

**Arguments**:
- `--outcomes` (required): Learning outcomes file
- `--strict` (optional): Flag even borderline cases
- `--suggest` (optional): Provide alternative wording suggestions

**Output**: Measurability audit with:
- Outcomes using measurable verbs (PASS)
- Outcomes using vague language (FAIL)
- Bloom's taxonomy level for each outcome
- Suggested rewording for unmeasurable outcomes

**Bloom's Taxonomy Reference**:
- **Remember**: Define, List, Recall, Identify, Name
- **Understand**: Explain, Describe, Summarize, Interpret
- **Apply**: Apply, Demonstrate, Use, Solve, Calculate
- **Analyze**: Analyze, Compare, Contrast, Differentiate, Examine
- **Evaluate**: Evaluate, Justify, Critique, Assess, Defend
- **Create**: Create, Design, Develop, Formulate, Construct

**Vague Language to Avoid**:
- ❌ "Understand the concept of..." → ✅ "Explain the concept of..."
- ❌ "Know about revenue streams" → ✅ "Identify five major revenue streams"
- ❌ "Be familiar with..." → ✅ "Describe the characteristics of..."
- ❌ "Appreciate the importance of..." → ✅ "Evaluate the impact of..."

### check_qm_compliance.py
**Purpose**: Generates comprehensive QM Standards compliance report

**Arguments**:
- `--assessment-dir` (required): Directory containing assessment materials
- `--report` (optional): Output format: text | json | html (default: text)
- `--standards` (optional): Which standards to check: 3 | 5 | 6 | all (default: all)

**Output**: QM compliance matrix with:
- Standard 3 (Assessment): Objectives measured, appropriate strategies, clear criteria, sufficient feedback
- Standard 5 (Instruction): Clear instructions, appropriate workload
- Standard 6 (Accessibility): Accessible content, assistive tech compatibility
- Compliance score per standard (0-100%)
- Specific gaps with line/file references
- Recommendations for achieving compliance

**QM Standards Checked**:

**Standard 3: Assessment and Measurement**
- 3.1: Assessments measure stated learning objectives ✓
- 3.2: Assessment strategies appropriate for objectives ✓
- 3.3: Criteria and standards clearly stated ✓
- 3.4: Sufficient feedback provided ✓

**Standard 5: Learner Support & Instructional Materials**
- 5.1: Clear instructions on assignment requirements ✓
- 5.2: Examples or models provided ✓
- 5.3: Workload appropriate for credit hours ✓

**Standard 6: Accessibility & Usability**
- 6.1: Content accessible to students with disabilities ✓
- 6.2: Compatible with assistive technologies ✓
- 6.3: Readability and comprehension appropriate ✓

## When to Use This Skill

**Rubric-generator agent should invoke when**:
- After generating rubric (quality assurance check)
- User requests "validate rubric" or "check QM compliance"
- Before finalizing rubric for distribution

**Assessment-designer agent should invoke when**:
- User asks "does this meet QM standards?"
- Creating new assessment (proactive validation)
- User provides learning outcomes and asks for aligned rubric

**Consistency-checker agent should invoke when**:
- Checking consistency across multiple rubrics
- Ensuring all module assessments use measurable outcomes

## Example Invocations

### From rubric-generator agent:

```
User: "Generate a rubric for Week 3 memo and make sure it's QM compliant"

Agent: I'll generate the rubric then validate QM compliance.

*Generates rubric first*

*Then invokes Skill tool*:
Skill: qm-validator

Commands (run in sequence):
1. python scripts/check_alignment.py --rubric week3-rubric.md --outcomes week3-outcomes.txt
2. python scripts/check_rubric_math.py --file week3-rubric.md
3. python scripts/check_qm_compliance.py --assessment-dir week3/ --report text

*If issues found*:
Agent: Found 2 QM compliance issues:
1. Learning outcome "Analyze revenue streams" not assessed by any rubric criterion
   → Add criterion: "Revenue Stream Analysis (10 pts)"
2. Rubric points total 28 but states "Total: 30 points"
   → Adjust criterion weights or update total

*Fixes issues and regenerates rubric*
```

### From assessment-designer agent:

```
User: "Check if my case study assignment meets Quality Matters standards"

Agent: I'll run a comprehensive QM compliance check.

*Invokes Skill tool*:
Skill: qm-validator
Command: python scripts/check_qm_compliance.py --assessment-dir case-study/ --report html --output qm-report.html

*Analyzes results*:
Agent: QM Compliance Summary:
- Standard 3 (Assessment): 85% compliant (3.4 needs improvement - insufficient feedback detail)
- Standard 5 (Instructions): 100% compliant ✅
- Standard 6 (Accessibility): 70% compliant (missing alt text on 3 images, contrast issues on rubric)

Priority fixes:
1. Add specific feedback examples to rubric (addresses 3.4)
2. Add alt text to images (addresses 6.1, 6.2)
3. Fix color contrast on rubric table (addresses 6.1)
```

## Integration with Other Skills

**Works well with**:
- **assessment-template-generator**: Validate generated PAIRR/AI roleplay rubrics for QM compliance
- **accessibility-audit-tools**: QM validator checks Standard 6 (accessibility), but accessibility-audit-tools provides deeper WCAG validation

**Typical Workflow**:
1. Generate rubric (assessment-template-generator or rubric-generator agent)
2. Validate QM compliance (qm-validator)
3. Fix identified issues
4. Check accessibility (accessibility-audit-tools)
5. Finalize and distribute

## Limitations

**What This Tool CAN Do**:
- Detect missing outcome-criteria alignments
- Calculate point total errors
- Flag unmeasurable language patterns
- Check for presence of QM-required elements

**What This Tool CANNOT Do**:
- Judge pedagogical soundness (requires human expertise)
- Assess criterion quality/specificity (pattern matching only)
- Determine if feedback is "sufficient" (subjective)
- Evaluate assessment appropriateness for course level

**Recommendation**: Use as first-pass validation, then review results with instructional design expertise.

## Additional Resources

See `REFERENCE.md` for:
- Complete QM Standards 3, 5, 6 rubrics
- Bloom's taxonomy verb lists by level
- Measurable vs. unmeasurable language examples
- Case studies of common QM compliance issues
- Alignment matrix templates
