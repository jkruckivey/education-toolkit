---
description: Validate cohort course module structural consistency (element sequences, learning outcomes widgets, PAIRR methodology)
---

You are validating cohort course storyboards for structural consistency.

Use the **cohort-structure-checker** agent to verify that modules follow standardized structural patterns.

## What This Command Validates

The cohort-structure-checker agent checks:

### Module Structure
- ✅ Proper element sequencing (connecting text → learning outcomes widget → content → Final Project Connection → transition)
- ✅ Element numbering integrity (no skipped numbers, table matches content)
- ✅ Learning outcomes widgets placement (Element 2 in Modules 2-7)
- ✅ Module transitions (recap + preview pattern)

### PAIRR Methodology (Module 6)
- ✅ Peer feedback instructions present
- ✅ AI feedback instructions present
- ✅ Comparative reflection component (compare peer vs AI)
- ✅ Post-revision reflection component
- ✅ Bonus structure (5 points: 2+1+1+1)

### Content Quality
- ✅ Final Project Connection quality (specific, not generic)
- ✅ Case attachment flags (`🔗 ATTACH CASE HERE:`)
- ✅ AI roleplay timing references (should be removed)
- ✅ Standalone sections (content outside element structure)

### Module-Specific Requirements
- ✅ Module 1: Week-level learning outcomes (not module-level)
- ✅ Module 7: Wrap-up components, no new concepts

## When to Use This Command

### Pre-Build Validation
- After creating storyboards, before development begins
- Catches structural issues early (saves development rework)

### Quality Assurance
- Before sending storyboards to production team
- Ensures consistent structure across all weeks

### Compliance Checking
- Verify PAIRR methodology is properly implemented
- Ensure all learning outcomes widgets are embedded

### Issue Diagnosis
- "Why is Module 3 missing learning outcomes?"
- "Is PAIRR consistently applied across weeks?"

## Example Usage

```
/check-cohort-structure week1/storyboards/
/check-cohort-structure modules/week2/storyboards/modules/
/check-cohort-structure week1-5
```

## Expected Output

The agent provides a comprehensive validation report:

### Overall Assessment
- Compliance percentage (e.g., 95% compliant)
- Critical issues count
- Warning count
- Readiness rating (Ready / Needs Fixes / Major Rework)

### Module-by-Module Breakdown

**Module 1 Validation:**
- ✅ Element 1: Connecting text (Week 1 context)
- ✅ Element 4: Learning outcomes widget embedded
- ❌ Element 10: Final Project Connection too generic (needs specificity)

**Module 6 Validation:**
- ✅ Peer feedback instructions present
- ✅ AI feedback instructions present
- ❌ Comparative reflection missing (no "compare peer vs AI" questions)
- ⚠️ Bonus structure: 4 points instead of 5 (should be 2+1+1+1)

### Critical Issues
Issues that must be fixed before build:
- Line numbers with specific problems
- Corrected versions provided

### Warnings
Issues that should be fixed but don't block build:
- Minor formatting inconsistencies
- Suggestions for improvement

### Summary Statistics
- Modules validated: 7
- Total elements checked: 48
- Critical issues: 2
- Warnings: 5
- Pass rate: 95%

---

## Common Issues Found

### ❌ Missing Learning Outcomes Widgets
**Problem:** Module 2 Element 2 is an Infobox instead of learning outcomes widget

**Fix:** Replace with iframe embed:
```html
<iframe src="week2/widgets/learning-outcomes-module-2.html"></iframe>
```

### ❌ Incomplete PAIRR Methodology
**Problem:** Module 6 has peer review but no comparative reflection

**Fix:** Add comparative reflection questions:
- "Compare the peer feedback vs AI feedback you received. Which was more useful? Why?"
- "Did the AI feedback identify anything your peer missed?"
- "How confident are you in applying each type of feedback?"

### ❌ Generic Final Project Connections
**Problem:** "This week's content will help with your final project"

**Fix:** Specific connection with content references:
- "Element 4's revenue model framework (media, tickets, merch) directly applies to your capstone Section 3.2 revenue analysis..."

---

**When to Run This Check:**
1. After completing storyboards (before development)
2. Before peer review (catch issues early)
3. After revisions (verify fixes applied)
4. Pre-launch QA (final structure validation)

**Workflow Position:**
- Run AFTER `/build-storyboard` creates storyboards
- Run BEFORE `/peer-review` comprehensive QA
- Run WITH `/check-concept-threading` and `/check-terminology` for full validation
