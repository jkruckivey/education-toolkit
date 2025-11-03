---
description: Create strategic course outline with CLOs, weekly structure, MLOs, and assessment strategy
---

You are helping create a comprehensive course outline from scratch.

Use the **course-outline-creator** agent to guide the instructor through strategic course planning.

## What This Command Does

The course-outline-creator agent will:
1. Conduct a discovery interview (subject area, level, duration, course format)
2. Define Quality Matters-compliant Course Learning Outcomes (CLOs)
3. Plan weekly structure and themes
4. Create Module Learning Outcomes (MLOs) for each week
5. Design assessment strategy (formative/summative balance, PAIRR methodology)
6. Map concept threading (ensure Week 1 concepts appear in later weeks)
7. Identify case studies and practitioner perspectives
8. Consider UDL principles and accessibility

## When to Use This Command

- Starting a brand new course from scratch
- Restructuring an existing course to meet QM standards
- Converting subject matter expertise into pedagogical structure
- Planning assessment strategy before diving into detailed module design

## Workflow Position

**Use BEFORE uplimit-storyboard-builder:**
1. `/create-outline` → Strategic planning (CLOs, assessment strategy)
2. `/build-storyboard` → Detailed module design (elements, widgets, copy)

## Example Usage

```
/create-outline
/create-outline 5-week MBA Marketing
/create-outline "Executive Education Finance 3-week cohort"
/create-outline self-paced undergrad psychology
```

## Expected Output

The agent will produce a complete course outline document with:

### Course Learning Outcomes (CLOs)
- 3-5 measurable outcomes using single action verbs (Analyze, Evaluate, Design)
- Bloom's taxonomy levels indicated
- Context provided for each outcome

### Course Structure
- Weekly breakdown with themes
- Module Learning Outcomes (MLOs) per week
- Suggested case studies
- Practitioner perspectives
- Assessment touchpoints

### Assessment Summary
- Assessment alignment matrix (which CLOs assessed when)
- Formative vs summative balance
- Point distribution across weeks
- PAIRR methodology opportunities (cohort courses)

### Concept Threading Map
- Core concepts introduced in Week 1
- How concepts build across weeks
- Callbacks and reinforcement strategy

### Implementation Notes
- Course format considerations (cohort vs self-paced)
- UDL implementation opportunities
- Accessibility considerations
- Estimated development timeline

---

**Next Steps After Outline:**
1. Review outline with stakeholders
2. Use `/build-storyboard` to create detailed module storyboards
3. Use `/check-concept-threading` to validate threading plan
4. Use `/design-assessment` for specific assessment design
