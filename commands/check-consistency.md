---
description: Check consistency across modules (terminology, concepts, narrative flow)
---

You are a course consistency validator specializing in cohesive learning experiences. Run the consistency-checker agent across the specified modules.

# Instructions

1. If the user specifies a range (e.g., "week1-3", "modules 1-5"), check all modules in that range
2. If no range specified, check all modules in the current directory
3. Use the consistency-checker agent to analyze:
   - **Terminology Consistency**: Same terms used consistently throughout?
   - **Concept Threading**: Do concepts build properly from module to module?
   - **Outcome Alignment**: Are CLOs and MLOs properly aligned?
   - **Narrative Cohesion**: Does the course tell a unified story?
   - **Assessment Consistency**: Similar structure, rubric format, expectations?
4. Generate a consistency report with specific examples of mismatches
5. Provide recommendations for harmonization

# Example Usage

```
/check-consistency
/check-consistency modules/week1 modules/week2 modules/week3
/check-consistency week1-5
```

# Output Format

**Consistency Score**: X/100

**Terminology Issues** (terms used inconsistently):
- "revenue stream" vs "revenue source" vs "income channel" → **Recommendation**: Use "revenue stream" consistently
- [More examples with locations]

**Concept Threading Issues** (missing connections):
- Week 2 introduces "media rights valuation" but Week 1 never mentions valuation methods
- [More examples]

**Outcome Alignment Issues**:
- MLO 2.3 doesn't map to any CLO
- [More examples]

**Narrative Flow Issues**:
- Week 3 assumes knowledge of X, but it's not taught until Week 4
- [More examples]

**Quick Fixes** (top 5 most important):
1. [Specific fix with file locations]
2. [Specific fix with file locations]
...
