#!/usr/bin/env python3
"""
Diagnostic Rubric Generator

Generates 3-level pre-learning assessment rubrics (Beginning → Developing → Proficient)
with faculty support flags and student-friendly language.
"""

import argparse
import sys
from datetime import datetime


def generate_diagnostic_rubric(skill_area: str, week: int, criteria_count: int = 3, output: str = None) -> str:
    """Generate diagnostic rubric with 3 performance levels"""

    # Generate generic criteria if specific ones not provided
    generic_criteria = [
        {
            "name": f"{skill_area} - Basic Understanding",
            "beginning": f"Cannot demonstrate basic understanding of {skill_area.lower()}. Typical responses: vague statements, incorrect assumptions, or 'I don't know'",
            "developing": f"Partially demonstrates understanding of {skill_area.lower()}. Typical responses: identifies 1-2 key concepts but lacks detail or connections",
            "proficient": f"Demonstrates solid understanding of {skill_area.lower()}. Typical responses: identifies 3+ key concepts with some explanation of relationships"
        },
        {
            "name": f"{skill_area} - Application Ability",
            "beginning": f"Cannot apply {skill_area.lower()} to scenarios. Typical responses: restates question, provides unrelated examples, or guesses randomly",
            "developing": f"Applies {skill_area.lower()} with limited accuracy. Typical responses: uses correct terminology but misapplies concepts or uses oversimplified reasoning",
            "proficient": f"Applies {skill_area.lower()} accurately to scenarios. Typical responses: connects concepts to examples, explains reasoning, acknowledges complexity"
        },
        {
            "name": f"{skill_area} - Critical Thinking",
            "beginning": f"Cannot analyze or evaluate aspects of {skill_area.lower()}. Typical responses: surface-level observations, no comparison or synthesis",
            "developing": f"Shows emerging critical thinking about {skill_area.lower()}. Typical responses: identifies differences but struggles to explain significance or implications",
            "proficient": f"Demonstrates critical thinking about {skill_area.lower()}. Typical responses: compares/contrasts with reasoning, identifies trade-offs or implications"
        }
    ]

    # Use only the requested number of criteria
    criteria = generic_criteria[:criteria_count]

    # Generate output filename
    if not output:
        output = f"diagnostic-rubric-week{week}-{skill_area.lower().replace(' ', '-')}.md"

    # Build rubric table rows
    rubric_rows = []
    for i, criterion in enumerate(criteria):
        rubric_rows.append(
            f"| {criterion['name']} | {criterion['beginning']} | {criterion['developing']} | {criterion['proficient']} |"
        )

    template = f"""# Diagnostic Rubric: {skill_area} (Week {week} Pre-Learning)

**Purpose**: Assess current understanding BEFORE Week {week} learning activities
**Assessment Type**: Diagnostic / Formative (NOT GRADED)
**Expected Distribution**: 50% Beginning, 35% Developing, 15% Proficient
**Generated**: {datetime.now().strftime('%Y-%m-%d')}

---

## Student-Facing Version

### About This Diagnostic

This brief assessment helps you (and your instructor) understand your **starting point** before Week {week}. Most students are "Beginning" or "Developing" at this stage—**that's completely normal and expected!**

The goal is NOT to evaluate you. The goal is to:
1. Identify what you already know about {skill_area.lower()}
2. Reveal knowledge gaps to focus on during Week {week}
3. Give your instructor insight into where the class needs support

**This diagnostic is not graded.** Be honest about what you know and don't know—that's the most helpful data.

### Diagnostic Rubric

| Skill/Knowledge Area | Beginning (Most Students Start Here) | Developing (Some Prior Knowledge) | Proficient (Strong Foundation) |
|----------------------|-------------------------------------|----------------------------------|-------------------------------|
{chr(10).join(rubric_rows)}

### What Your Results Mean

- **Mostly Beginning**: You're in the majority! Week {week} content is designed for students starting here.
- **Mix of Beginning/Developing**: You have some foundation to build on. Pay attention to areas marked "Beginning."
- **Mostly Developing/Proficient**: Great! You'll likely find Week {week} concepts easier to grasp, but stay engaged for depth and nuance.

**Remember**: This is a snapshot of where you are NOW. By the end of Week {week}, everyone should be "Proficient" or better.

---

## Faculty Grading Version

### Purpose & Pedagogy

**Why Diagnostic Assessment?**
- Reveals misconceptions BEFORE content delivery (more effective than post-test only)
- Creates cognitive dissonance that motivates learning
- Allows just-in-time adjustments to Week {week} instruction
- Helps students develop metacognitive awareness (knowing what they don't know)

**Grading Approach**:
- **Participation credit only** (completion = full points, typically 5 pts)
- **Do NOT grade on correctness** (penalizing lack of prior knowledge is pedagogically unsound)
- **Use results to inform teaching** (not student grades)

### Rubric Application

| Criterion | Beginning | Developing | Proficient |
|-----------|-----------|------------|------------|
{chr(10).join(rubric_rows)}

### Support Flags (Interventions Based on Results)

Use these flags to trigger targeted support:

**🚩 RED FLAG** (Immediate Intervention Needed):
- Student scores "Beginning" on ALL criteria
- **Action**: Reach out via email/office hours. Offer pre-Week {week} resources, recorded lectures, or tutoring referral.

**⚠️ YELLOW FLAG** (Monitor During Learning):
- Student scores "Beginning" on 2+ criteria OR "Developing" on all criteria
- **Action**: Monitor engagement during Week {week}. Check in during discussions or provide formative quiz.

**✅ GREEN FLAG** (On Track):
- Student scores mix of "Developing" and "Proficient"
- **Action**: Standard instruction. May benefit from enrichment/challenge activities.

### Expected Distribution

**Typical Class Results** (N=30 students):
- **50% predominantly Beginning** (15 students): Normal. Week {week} is new content.
- **35% mix of Beginning/Developing** (10 students): Some prior exposure (previous courses, work experience, general knowledge)
- **15% predominantly Developing/Proficient** (5 students): Strong foundation (majors, professionals, enthusiasts)

**Abnormal Distributions**:
- **>70% Proficient**: Content may be too basic (consider advancing material or adding depth)
- **<30% any Developing/Proficient**: Prerequisite knowledge may be missing (consider scaffolding or prerequisite review)

### Grading Time

**Per Student**: 2-3 minutes (quick diagnostic review)

**Process**:
1. Skim student responses (don't grade—just categorize)
2. Mark each criterion as Beginning / Developing / Proficient
3. Flag for support (Red / Yellow / Green)
4. Award full participation points (5 pts)
5. Note class-wide patterns for instructional adjustments

**Total Time for 30 Students**: 60-90 minutes

### Common Diagnostic Patterns

**Pattern 1: Confident but Incorrect**
- Student writes confidently but demonstrates misconceptions
- **Interpretation**: Needs Week {week} content to correct misunderstandings (valuable learning opportunity)
- **Don't penalize**: Grading on incorrect pre-learning discourages honest self-assessment

**Pattern 2: "I Don't Know" Honesty**
- Student explicitly states lack of knowledge
- **Interpretation**: Metacognitively aware (knows what they don't know)
- **This is GOOD**: Honest self-assessment enables targeted learning

**Pattern 3: Surface-Level Awareness**
- Student knows terminology but can't explain or apply
- **Interpretation**: Typical "Developing" performance—has heard concepts but not mastered them

### Using Results to Adjust Week {week} Instruction

**If >60% Beginning**:
- Start with foundational concepts (don't assume prior knowledge)
- Increase scaffolding and examples
- Slow pacing for Week {week}
- Provide glossary or concept map

**If >40% Developing/Proficient**:
- Acknowledge prior knowledge ("Some of you already know...")
- Quickly review basics, then add depth/nuance
- Include challenge problems for advanced students
- Use peer teaching (Proficient students help Beginning students)

**If significant misconceptions observed**:
- Address explicitly in Week {week} lecture ("Many of you thought X, but actually...")
- Use diagnostic results as discussion starter
- Contrast misconception with correct understanding

---

## Customization Instructions

### For Instructors

**Before using this rubric**:
1. Replace generic criterion descriptions with course-specific examples
2. Add actual "typical responses" based on past student work (after first use)
3. Customize support flags based on your institutional resources
4. Decide participation point value (5 pts recommended)

**After first use**:
1. Review actual student responses
2. Update "typical responses" in rubric with real examples
3. Refine performance level descriptions based on observed distributions
4. Adjust support flag thresholds if needed

**Course-Specific Customization Example**:

If your Week {week} is about "Revenue Streams in Sports Business," replace generic criteria with:

| Criterion | Beginning | Developing | Proficient |
|-----------|-----------|------------|------------|
| Revenue Stream Knowledge | Can name 1-2 revenue sources (tickets, jerseys) | Can name 3-4 revenue sources (includes sponsorship OR media) | Names all 5 major streams (media, ticketing, sponsorship, merchandising, betting) + explains relative importance |
| Ecosystem Thinking | Views streams as independent/separate ("Tickets go up, jerseys go up") | Recognizes connections but can't explain HOW they influence each other | Understands interdependence ("Star player increases ALL streams through amplification") |

---

## Implementation Timeline

**Week {week-1}**:
- Assign diagnostic (due before Week {week} begins)
- Allocate 15-20 minutes for student completion
- Students submit via LMS or Google Form

**Beginning of Week {week}**:
- Review results (60-90 min grading time)
- Identify support flags
- Adjust Week {week} instruction based on class patterns

**During Week {week}**:
- Reference diagnostic in lecture ("Remember when I asked about X? Here's why...")
- Follow up with Red/Yellow flag students
- Reinforce that growth from diagnostic to post-test is the goal

**End of Week {week}**:
- Consider post-diagnostic (same rubric) to show growth
- Students reflect on learning journey (metacognition)

---

## Research Support

**Why 3 Levels (Not 4-5)?**
- Diagnostic rubrics assess CURRENT state, not mastery (so no "Exemplary" level)
- Simpler = faster grading (important for formative assessment)
- Students find 3 levels less intimidating pre-learning

**Why Non-Evaluative Language?**
- Reduces anxiety about pre-learning gaps
- Encourages honest self-assessment
- Frames assessment as helpful (not punitive)

**Evidence for Diagnostic Assessment Effectiveness**:
- Reveals misconceptions that post-tests alone miss
- Creates productive cognitive dissonance (motivation to learn)
- Improves student metacognition (awareness of learning gaps)
- Enables targeted instruction (differentiation based on results)

---

## Appendix: Sample Student Instructions

Copy this text when assigning the diagnostic:

---

**Week {week} Diagnostic Assessment ({skill_area})**

**Due**: [DATE] before Week {week} begins
**Points**: 5 (participation credit—not graded on correctness)
**Time**: 15-20 minutes

**Purpose**: This diagnostic helps you understand your starting point before Week {week}. There are no wrong answers—just answer honestly based on what you currently know.

**Instructions**:
1. Answer the questions without using course materials or AI tools (this defeats the diagnostic purpose)
2. If you don't know something, write "I don't know" or "I'm not sure" (this is valuable data!)
3. Submit by [DATE]

**What happens next**:
- You receive full participation credit regardless of answers
- I review results to tailor Week {week} instruction to class needs
- You'll see your growth when we revisit these concepts at end of Week {week}

---
"""

    # Write to file
    with open(output, 'w', encoding='utf-8') as f:
        f.write(template)

    return output


def main():
    parser = argparse.ArgumentParser(
        description='Generate 3-level diagnostic rubric for pre-learning assessment'
    )
    parser.add_argument('--skill-area', required=True,
                        help='Skill or knowledge area being diagnosed (e.g., "Revenue Streams Knowledge")')
    parser.add_argument('--week', required=True, type=int,
                        help='Week/module number for context')
    parser.add_argument('--criteria-count', type=int, default=3,
                        help='Number of rubric criteria (default: 3)')
    parser.add_argument('--output',
                        help='Output filename (default: diagnostic-rubric-week{week}.md)')

    args = parser.parse_args()

    if args.criteria_count < 2 or args.criteria_count > 5:
        print("Warning: 2-4 criteria recommended for diagnostic rubrics. You provided {}.".format(args.criteria_count))

    # Generate template
    output_file = generate_diagnostic_rubric(
        skill_area=args.skill_area,
        week=args.week,
        criteria_count=args.criteria_count,
        output=args.output
    )

    print(f"[OK] Diagnostic rubric generated: {output_file}")
    print(f"   Skill Area: {args.skill_area}")
    print(f"   Week: {args.week}")
    print(f"   Criteria: {args.criteria_count}")
    print(f"   Performance Levels: 3 (Beginning | Developing | Proficient)")
    print("\nNext steps:")
    print("1. Customize generic criteria with course-specific examples")
    print("2. Add 'typical responses' after first use with real student data")
    print("3. Set participation point value in LMS")
    print("4. Assign diagnostic BEFORE Week {} content delivery".format(args.week))

    return 0


if __name__ == '__main__':
    sys.exit(main())
