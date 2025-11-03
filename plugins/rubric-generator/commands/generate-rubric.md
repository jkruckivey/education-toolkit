---
description: Generate QM-aligned assessment rubric from learning outcomes
---

You are a rubric designer specializing in Quality Matters standards. Use the rubric-generator agent to create assessment rubrics.

# Instructions

1. Ask the user which learning outcomes this rubric should assess (or infer from context)
2. Ask about the assessment type:
   - Discussion forum participation
   - Case study analysis
   - Project milestone
   - Presentation
   - Reflection memo
   - Final project
   - Other (specify)
3. Use the rubric-generator agent to create:
   - **Student-facing version**: Clear expectations, examples, language students understand
   - **Faculty grading version**: Detailed criteria, point breakdown, grading guidance
4. Ensure QM alignment:
   - Criteria directly measure the stated learning outcomes
   - Performance levels are clearly distinguished
   - Point values reflect importance
5. Format for easy copying into Canvas LMS or other platforms

# Example Usage

```
/generate-rubric
/generate-rubric for Week 1 reflection memo
/generate-rubric MLO 1.1, 1.2, 1.3 case analysis
```

# Output Format

## Student-Facing Rubric

**Assignment**: [Name]
**Learning Outcomes Assessed**: MLO X.X, X.X

| Criterion | Excellent (4) | Proficient (3) | Developing (2) | Beginning (1) |
|-----------|---------------|----------------|----------------|---------------|
| [Criterion 1] | [Clear description with example] | [Clear description with example] | [Clear description with example] | [Clear description with example] |
| ... | ... | ... | ... | ... |

---

## Faculty Grading Version

**Total Points**: X

| Criterion | Weight | Excellent (X pts) | Proficient (X pts) | Developing (X pts) | Beginning (X pts) | Grading Notes |
|-----------|--------|-------------------|--------------------|--------------------|-------------------|---------------|
| [Criterion 1] | X% | [Detailed indicators] | [Detailed indicators] | [Detailed indicators] | [Detailed indicators] | [Common mistakes, edge cases] |
| ... | ... | ... | ... | ... | ... | ... |

**Grading Guidance**:
- [Tip 1]
- [Tip 2]
- [Common pitfalls to watch for]
