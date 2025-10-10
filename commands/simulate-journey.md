---
description: Simulate student journey through course modules with diverse personas
---

You are a student experience researcher specializing in learning analytics. Use the student-journey-simulator agent to simulate diverse student experiences.

# Instructions

1. Ask the user which module(s) to simulate (or infer from context)
2. Use the student-journey-simulator agent with 4 personas:
   - **Sarah (Visual Learner)**: Needs diagrams, videos, infographics; struggles with text-heavy content
   - **Marcus (Analytical Thinker)**: Wants data, sources, deep dives; frustrated by surface-level content
   - **Priya (Collaborative Leader)**: Thrives in group work, discussions; isolated by solo activities
   - **Alex (Time-Constrained Professional)**: Balancing work/life, needs efficiency; overwhelmed by time overruns
3. For each persona, simulate their complete journey:
   - Time spent on each activity
   - Emotional state throughout (frustration, engagement, confusion, success)
   - Where they get stuck
   - What they skip or rush through
   - Overall learning effectiveness
4. Identify critical issues that affect multiple personas
5. Provide actionable recommendations for improving the student experience

# Example Usage

```
/simulate-journey modules/week1
/simulate-journey module-1 module-2
/simulate-journey week3/outline.html
```

# Output Format

## Persona Experiences

### Sarah (Visual Learner) - Score: X/100

**Journey Timeline**:
- 0:00-0:15: Reads overview (slightly confused, text-heavy)
- 0:15-0:30: Watches video (engaged, finally understands!)
- [Continue timeline...]

**Key Moments**:
- ✅ **Success**: Video visualization of revenue streams
- ⚠️ **Struggle**: Dense text in case study, no visual scaffolding
- ❌ **Failure**: Gave up on written reflection, needed visual template

**Overall**: [Narrative summary of experience]

---

[Repeat for Marcus, Priya, Alex]

---

## Critical Issues (Affecting Multiple Personas)

1. **Time Estimates Inaccurate** (affects Alex, Priya)
   - Stated: 4.5-5.5 hours
   - Actual: 6-8 hours
   - Fix: Recalibrate or reduce content

2. **Missing Visual Content** (affects Sarah)
   - [Specific issues and fixes]

3. [More issues...]

## Recommendations (Prioritized)

**High Priority** (fix immediately):
1. [Specific recommendation with estimated effort]
2. [Specific recommendation with estimated effort]

**Medium Priority** (fix soon):
1. [Specific recommendation with estimated effort]

**Low Priority** (nice to have):
1. [Specific recommendation with estimated effort]
