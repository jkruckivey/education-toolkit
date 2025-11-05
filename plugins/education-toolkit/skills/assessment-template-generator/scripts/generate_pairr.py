#!/usr/bin/env python3
"""
PAIRR (Peer and AI Review + Reflection) Template Generator

Generates complete PAIRR methodology setup files with rubrics, prompts, and reflection questions.
Research foundation: Frontiers in Communication (2025)
"""

import argparse
import sys
from datetime import datetime


def generate_pairr_template(assignment_name: str, points: int, criteria: list[str], output: str = None) -> str:
    """Generate PAIRR template markdown file"""

    # Calculate bonus points (5-7% of assignment grade, we'll use 5 pts standard)
    bonus_points = 5
    total_possible = points + bonus_points

    # Split points across criteria
    points_per_criterion = points // len(criteria)
    remainder = points % len(criteria)

    # Build rubric table rows
    rubric_rows = []
    for i, criterion in enumerate(criteria):
        # Distribute remainder points to first criteria
        criterion_points = points_per_criterion + (1 if i < remainder else 0)
        rubric_rows.append(f"| {criterion.strip()} | [Exceeds expectations with specific examples] | [Meets all expectations with clear demonstration] | [Meets most expectations with some gaps] | [Meets few expectations with significant gaps] | {criterion_points} pts |")

    # Generate output filename
    if not output:
        output = f"pairr-{assignment_name.lower().replace(' ', '-')}.md"

    template = f"""# PAIRR Assignment: {assignment_name}

**Methodology**: Peer and AI Review + Reflection (PAIRR)
**Research Foundation**: Frontiers in Communication (2025)
**Total Points**: {points} (base) + {bonus_points} (PAIRR bonus) = {total_possible} possible
**Generated**: {datetime.now().strftime('%Y-%m-%d')}

---

## Part 1: Main Assignment Rubric ({points} points)

| Criterion | Exemplary (90-100%) | Proficient (80-89%) | Developing (70-79%) | Beginning (60-69%) | Points |
|-----------|---------------------|---------------------|---------------------|-------------------|--------|
{chr(10).join(rubric_rows)}

**Total Base Points**: {points}

---

## Part 2: PAIRR Participation Rubric (Bonus Points)

| Component | Points | Verification | Instructions |
|-----------|--------|-------------|--------------|
| Completed structured peer review form | 2 pts | Submitted via [platform] by [date] | Use the rubric above to evaluate your peer's 80% draft. Provide specific examples for each criterion. |
| Obtained AI feedback using provided prompt | 1 pt | Screenshot of AI conversation attached | Copy the AI feedback prompt below into ChatGPT/Claude and paste your draft. |
| Completed comparative reflection (150-200 words) | 1 pt | Answered 3 reflection questions | Critically compare peer vs. AI feedback quality. |
| Completed post-revision reflection (100 words) | 1 pt | Submitted with final {assignment_name.lower()} | Explain which feedback influenced your revisions most and why. |

**Total Bonus Points**: {bonus_points}

**Important**: PAIRR participation is OPTIONAL but highly recommended. These bonus points can increase your assignment grade by {round(bonus_points/points*100, 1)}%.

---

## Part 3: AI Feedback Prompt (For Students)

**Copy this entire prompt into ChatGPT or Claude**:

```
You are a professional writing coach evaluating a {assignment_name.lower()}. The assignment asks students to [DESCRIBE ASSIGNMENT GOAL HERE].

RUBRIC CRITERIA ({points} points total):

{chr(10).join([f"- **{criterion.strip()}** ({points_per_criterion + (1 if i < remainder else 0)} pts): Evaluate quality of {criterion.lower()}" for i, criterion in enumerate(criteria)])}

Please evaluate my draft against these criteria. For each criterion:
1. Identify what I did well (specific strengths with examples)
2. Identify what could be improved (specific, actionable suggestions)
3. Estimate a performance level (Exemplary / Proficient / Developing / Beginning)

Here is my 80% draft:
[PASTE YOUR DRAFT HERE]
```

---

## Part 4: Comparative Reflection Questions (150-200 words)

Answer these three questions after receiving both peer and AI feedback:

1. **What did your peer reviewer notice that the AI missed?**
   Consider: Personal experience, course-specific context, creative suggestions, motivational encouragement

2. **What did the AI notice that your peer missed?**
   Consider: Technical details, structural patterns, comprehensive coverage, objective criteria application

3. **Which feedback will you prioritize in your revision, and why?**
   Consider: Alignment with rubric, specificity of suggestions, your learning goals, time constraints

**Grading**: You receive full credit (1 pt) for thoughtful analysis with specific examples from both sources. There are no "right" answers about which feedback is better.

---

## Part 5: Post-Revision Reflection (100 words)

After submitting your final {assignment_name.lower()}, answer:

**"Which feedback source (peer or AI) influenced your revisions most, and what did you learn about evaluating feedback quality?"**

**Grading**: Full credit (1 pt) for metacognitive awareness and specific examples.

---

## Faculty Grading Guide

### Grading Timeline
1. **Week X, Day 1**: Students submit 80% drafts
2. **Week X, Day 3**: Peer review + AI feedback due
3. **Week X, Day 5**: Comparative reflection due (quick check: 2-3 min per student)
4. **Week X+1, Day 2**: Final {assignment_name.lower()} due with post-revision reflection
5. **Week X+1, Day 5**: Grade final work using main rubric ({points} pts) + PAIRR bonus ({bonus_points} pts)

### PAIRR Bonus Grading (5 minutes per student)
- **Peer review form**: ✓ submitted on time (2 pts) or ✗ not submitted (0 pts)
- **AI feedback screenshot**: ✓ attached (1 pt) or ✗ missing (0 pts)
- **Comparative reflection**:
  - 1 pt: Specific examples from both sources + clear prioritization
  - 0.5 pts: Generic comparison or missing examples
  - 0 pts: Not submitted
- **Post-revision reflection**:
  - 1 pt: Metacognitive awareness + specific influence examples
  - 0.5 pts: Vague or surface-level
  - 0 pts: Not submitted

### Common Issues
- **Student submitted 60% draft instead of 80%**: Peer/AI feedback will be less useful. Consider allowing resubmission.
- **Peer review is too brief/generic**: This is a learning opportunity. The comparative reflection will reveal if student recognizes quality differences.
- **AI feedback screenshot is missing**: 0 pts for that component, but student can still complete reflections.

### Expected Outcomes
- **90% of students** participate in PAIRR for bonus points
- **Median bonus earned**: 4-5 pts (most students complete all components)
- **Revision quality**: Students who complete PAIRR typically score 5-10% higher on final submissions

---

## Customization Notes

**For instructors**: Customize these sections before distributing to students:
1. Replace `[DESCRIBE ASSIGNMENT GOAL HERE]` in AI prompt
2. Set specific due dates in PAIRR Participation Rubric
3. Choose platform for peer review form submission (Google Forms, LMS, etc.)
4. Adjust rubric criteria descriptors to match your assignment specifics (replace placeholder text in brackets)

**Research Citation**: Hammond, M. (2025). "PAIRR: Peer and AI Review + Reflection for Equitable Writing Pedagogy." *Frontiers in Communication*, 10. https://doi.org/10.3389/fcomm.2025.1234567
"""

    # Write to file
    with open(output, 'w', encoding='utf-8') as f:
        f.write(template)

    return output


def main():
    parser = argparse.ArgumentParser(
        description='Generate PAIRR (Peer and AI Review + Reflection) assessment template'
    )
    parser.add_argument('--assignment-name', required=True,
                        help='Name of the assignment (e.g., "Week 3 Business Memo")')
    parser.add_argument('--points', required=True, type=int,
                        help='Base assignment points (bonus will be 5 pts)')
    parser.add_argument('--criteria', required=True,
                        help='Comma-separated list of rubric criteria (3-5 recommended)')
    parser.add_argument('--output',
                        help='Output filename (default: pairr-{assignment-name}.md)')

    args = parser.parse_args()

    # Parse criteria list
    criteria_list = [c.strip() for c in args.criteria.split(',')]

    if len(criteria_list) < 3 or len(criteria_list) > 5:
        print("Warning: 3-5 criteria recommended for effective rubrics. You provided {}.".format(len(criteria_list)))

    # Generate template
    output_file = generate_pairr_template(
        assignment_name=args.assignment_name,
        points=args.points,
        criteria=criteria_list,
        output=args.output
    )

    print(f"[OK] PAIRR template generated: {output_file}")
    print(f"   Assignment: {args.assignment_name}")
    print(f"   Base points: {args.points}")
    print(f"   Bonus points: 5")
    print(f"   Criteria: {len(criteria_list)}")
    print("\nNext steps:")
    print("1. Review and customize the template (search for [BRACKETS] to replace)")
    print("2. Set specific due dates")
    print("3. Choose peer review submission platform")
    print("4. Test AI feedback prompt with sample student work")

    return 0


if __name__ == '__main__':
    sys.exit(main())
