---
description: Validate terminology consistency across course weeks (build glossary, flag variations, identify undefined acronyms)
---

You are validating terminology consistency across a multi-week course.

Use the **terminology-consistency-checker** agent to build a comprehensive course glossary and identify term variations.

## What This Command Validates

The terminology-consistency-checker agent checks:

### Term Consistency
- ✅ Tracks all technical terms across weeks
- ✅ Flags term variations (e.g., "revenue streams" vs "revenue sources" vs "monetization channels")
- ✅ Identifies inconsistent usage of the same concept
- ✅ Generates consistency scores per term (100 = perfect)

### Acronym Management
- ✅ Detects undefined acronyms (first use without expansion)
- ✅ Tracks acronym consistency (IRR vs I.R.R. vs internal rate of return)
- ✅ Identifies acronyms that should be expanded for clarity

### Capitalization Patterns
- ✅ Checks for inconsistent capitalization ("Anchor Project" vs "anchor project")
- ✅ Validates proper noun treatment
- ✅ Flags mixed case usage (IoT vs IOT vs iot)

### Technical Jargon
- ✅ Identifies jargon that needs definition
- ✅ Checks if terms defined before use
- ✅ Suggests glossary candidates

### Learning Outcome Terminology
- ✅ Validates CLO/MLO format consistency
- ✅ Checks action verb consistency
- ✅ Ensures outcome numbering follows pattern

## When to Use This Command

### Course Development
- After drafting all weeks' content
- Before sending to production (catch inconsistencies early)

### Quality Assurance
- Part of pre-launch QA checklist
- After multiple authors contribute (ensures unified voice)

### Glossary Building
- Generate comprehensive course glossary
- Identify terms that need student-facing definitions

### Issue Diagnosis
- "Why do students ask about terminology inconsistencies?"
- "What terms need better definition?"
- "Is our technical vocabulary consistent?"

## Example Usage

```
/check-terminology week1-5
/check-terminology modules/
/check-terminology storyboards/
```

## Expected Output

The agent provides a comprehensive terminology report:

### Overall Consistency Score
- Score: 85/100
- Major inconsistencies: 3
- Minor variations: 12
- Undefined acronyms: 5

### Course Glossary

**Core Terms (Consistent):**
- **Revenue Model** (37 occurrences, 100% consistent)
  - First mention: Week 1, Module 2, Element 3
  - Definition provided: Yes (Week 1)
  - Student-facing: Yes

**Inconsistent Terms:**
- **Revenue Streams** (15x) vs **Revenue Sources** (8x) vs **Monetization Channels** (4x)
  - Consistency Score: 55/100
  - Recommendation: Standardize to "Revenue Streams" (most common)
  - Occurrences:
    - Week 1, Module 3: "revenue sources"
    - Week 2, Module 4: "monetization channels"
    - Week 3, Module 2: "revenue streams"

### Undefined Acronyms

**IRR (Internal Rate of Return)**
- First use: Week 2, Module 4, Element 6 (no expansion)
- Total uses: 12
- Recommendation: Expand on first use: "Internal Rate of Return (IRR)"

**CLV (Customer Lifetime Value)**
- First use: Week 3, Module 2, Element 4 (no expansion)
- Total uses: 8
- Recommendation: Add to glossary

### Capitalization Issues

**"Anchor Project" vs "anchor project"**
- Uppercase: 24 occurrences
- Lowercase: 7 occurrences
- Recommendation: Standardize to "Anchor Project" (proper noun treatment)
- Fix locations:
  - Week 2, Module 1, Element 5: change to uppercase
  - Week 4, Module 7, Element 3: change to uppercase

### Technical Jargon Needing Definition

**CAC (Customer Acquisition Cost)**
- Used without definition: Week 2, Module 3
- Student confusion likely: High
- Recommendation: Add definition or link to glossary

### Learning Outcome Format

**MLO Format Consistency:**
- ✅ Consistent: MLO 1.1, 1.2, 1.3, 1.4 (Week 1)
- ✅ Consistent: MLO 2.1, 2.2, 2.3, 2.4 (Week 2)
- ❌ Inconsistent: "Learning Outcome 3-1" instead of "MLO 3.1" (Week 3)

### Recommended Actions

**Priority 1: Critical Fixes (Do Before Launch)**
1. Define IRR on first use (Week 2, Module 4, Element 6)
2. Standardize "Anchor Project" capitalization (7 instances)
3. Fix MLO 3.1 format inconsistency

**Priority 2: Consistency Improvements**
1. Standardize "revenue streams" terminology (12 variations)
2. Expand CLV acronym on first use
3. Add CAC definition

**Priority 3: Glossary Additions**
1. Create student-facing glossary with 15 core terms
2. Link glossary from Week 1 overview
3. Consider hover definitions for key terms

---

## Common Issues Found

### ❌ Term Variations Causing Confusion
**Problem:** "Revenue model" (Week 1) vs "business model" (Week 3) vs "monetization strategy" (Week 5)

**Impact:** Students unsure if these are same concept or different

**Fix:** Choose one primary term, use consistently. Add glossary note: "Revenue Model (also called business model or monetization strategy)"

### ❌ Undefined Acronyms
**Problem:** "Calculate the NPV using 10% discount rate..."

**Impact:** Students without finance background confused

**Fix:** First use: "Net Present Value (NPV)"

### ❌ Capitalization Inconsistency
**Problem:** "final project" vs "Final Project" vs "Capstone Project"

**Impact:** Students unsure if referring to same assignment

**Fix:** Standardize to "Final Project" (capitalize as proper noun)

---

## Glossary Export

The agent can generate:
- **Student-facing glossary** (markdown table, alphabetical)
- **Instructor reference** (includes consistency scores, recommendations)
- **Quick fix list** (file paths + line numbers for bulk editing)

---

**When to Run This Check:**
1. After drafting all weeks (build initial glossary)
2. Before peer review (catch inconsistencies early)
3. After revisions (verify terminology fixes)
4. Pre-launch QA (final consistency check)

**Workflow Position:**
- Run AFTER all content drafted
- Run WITH `/check-concept-threading` (concepts need consistent terminology)
- Run BEFORE `/peer-review` (terminology consistency affects content quality score)
