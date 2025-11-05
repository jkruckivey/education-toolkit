---
description: Validate concept threading across course weeks (track Week 1 concepts through later modules, identify orphaned concepts)
---

You are validating concept threading across a multi-week course to ensure Week 1 concepts appear and build throughout later weeks.

Use the **concept-threading-checker** agent to map concept introduction → usage → synthesis patterns.

## What This Command Validates

The concept-threading-checker agent tracks:

### Concept Introduction & Progression
- ✅ Identifies all concepts introduced in Week 1
- ✅ Tracks where each concept appears in later weeks
- ✅ Flags "orphaned concepts" (taught once, never revisited)
- ✅ Validates progressive complexity (simple → moderate → complex → synthesis)

### Callback References
- ✅ Checks for explicit callbacks ("Recall from Week 1...")
- ✅ Validates scaffolding language ("Building on your understanding of...")
- ✅ Identifies missing connection opportunities

### Concept Re-explanation
- ✅ Detects inappropriate re-teaching (concept re-defined in Week 4)
- ✅ Flags redundant explanations vs appropriate reminders

### Assessment Integration
- ✅ Validates assessments require cumulative knowledge
- ✅ Checks if Week 5 assessment tests Week 1 concepts (not just Week 5)
- ✅ Identifies siloed assessments (only test current week)

## When to Use This Command

### Course Design Validation
- After creating course outline (validate threading plan)
- After drafting all weeks (verify execution matches plan)

### Quality Assurance
- Diagnose "choppy" course flow (disconnected weeks)
- Ensure cohesive narrative arc across weeks

### Learning Progression
- Verify concepts build logically
- Catch premature introduction (advanced concept before foundation)

### Issue Diagnosis
- "Why don't Week 5 students remember Week 1 content?"
- "Are we re-teaching instead of building?"
- "Is our course cohesive or disconnected topics?"

## Example Usage

```
/check-concept-threading week1-5
/check-concept-threading modules/
/check-concept-threading storyboards/
```

## Expected Output

The agent provides a comprehensive threading analysis:

### Concept Map Overview

**Core Concepts Introduced in Week 1:**
1. Revenue Ecosystem Framework (media, tickets, merchandise)
2. Sponsorship Valuation Principles
3. Fan Engagement Metrics (CAC, CLV, retention)
4. Rights Holder Business Models

### Concept Threading Analysis

**Concept 1: Revenue Ecosystem Framework**
- ✅ **Week 1, Module 3**: Introduced with 3-category model
- ✅ **Week 2, Module 4**: Applied to media rights analysis
- ✅ **Week 3, Module 2**: Applied to merchandise strategy
- ✅ **Week 4, Module 5**: Applied to sponsorship packages
- ✅ **Week 5, Module 6**: Synthesized in capstone (all 3 categories)
- **Threading Score: 100%** (appears in all weeks, progressive complexity)
- **Callbacks: 4** (explicit "Recall Week 1 Revenue Ecosystem...")

**Concept 2: Fan Engagement Metrics**
- ✅ **Week 1, Module 4**: Introduced (CAC, CLV definitions)
- ❌ **Week 2**: Not mentioned
- ⚠️ **Week 3, Module 3**: Re-defined (instead of callback)
- ✅ **Week 4, Module 2**: Applied in retention strategy
- ❌ **Week 5**: Not in capstone assessment
- **Threading Score: 60%** (gaps in Weeks 2 & 5, re-explanation issue)
- **Callbacks: 1** (should have 3+)

**Concept 3: Rights Holder Business Models**
- ✅ **Week 1, Module 2**: Introduced
- ❌ **Week 2-5**: Never mentioned again
- **Threading Score: 20%** (ORPHANED CONCEPT)
- **Callbacks: 0**

### Progressive Complexity Validation

**Revenue Ecosystem Framework Progression:**
- Week 1: **Simple** - Define 3 categories
- Week 2: **Moderate** - Analyze one category (media)
- Week 3: **Moderate** - Analyze another category (merch)
- Week 4: **Complex** - Integrate sponsorship across categories
- Week 5: **Synthesis** - Optimize entire ecosystem in capstone

✅ **Appropriate scaffolding** - Each week builds on previous

**Fan Engagement Metrics Progression:**
- Week 1: **Simple** - Define CAC, CLV
- Week 3: **Simple** - Re-define same concepts ❌ (should be Moderate application)
- Week 4: **Moderate** - Apply to retention

⚠️ **Inappropriate re-teaching** - Week 3 should apply, not re-teach

### Assessment Threading

**Week 5 Capstone Assessment:**
- ✅ Tests Week 1: Revenue Ecosystem (yes)
- ✅ Tests Week 2: Media rights (yes)
- ✅ Tests Week 3: Merchandise (yes)
- ✅ Tests Week 4: Sponsorship (yes)
- ❌ Tests Week 1: Fan Engagement Metrics (no)

⚠️ **Partial cumulative assessment** - Fan Engagement Metrics missing

### Orphaned Concepts

**1. Rights Holder Business Models**
- Introduced: Week 1, Module 2
- Last mention: Week 1, Module 2 (same place!)
- **Problem:** Never applied, analyzed, or assessed
- **Impact:** Students forget, perceive as "filler content"
- **Fix Options:**
  1. Apply in Week 3 merchandise strategy
  2. Apply in Week 4 sponsorship negotiation
  3. Remove from Week 1 (if not essential)

### Missing Callbacks

**Fan Engagement Metrics (Week 3, Module 3):**
- Current: "CAC (Customer Acquisition Cost) is the cost to acquire one new fan..."
- Should be: "Recall from Week 1: CAC is the cost to acquire one new fan. Now let's apply this metric to your retention strategy..."

**Recommendation:** Add 3 explicit callbacks throughout Week 3-5

### Recommended Actions

**Priority 1: Fix Orphaned Concepts**
1. Apply Rights Holder Business Models in Week 3-4 OR remove from Week 1
2. Add Fan Engagement Metrics to Week 5 capstone

**Priority 2: Improve Callbacks**
1. Week 3, Module 3: Add Revenue Ecosystem callback
2. Week 4, Module 2: Add Fan Engagement Metrics callback
3. Week 5, Module 1: Add comprehensive Week 1 recap

**Priority 3: Fix Re-teaching**
1. Week 3, Module 3: Change Fan Engagement Metrics from "re-definition" to "application"

---

## Threading Patterns (Reference)

The agent references 4 research-backed threading patterns:

### 1. Foundation → Application → Synthesis
- Week 1: Teach concept
- Weeks 2-4: Apply to different contexts
- Week 5: Synthesize across contexts

### 2. Progressive Layering
- Week 1: Layer 1 (basic concept)
- Week 2: Layer 2 (add complexity)
- Week 3: Layer 3 (add nuance)
- Week 5: Full model

### 3. Spiral Curriculum
- Week 1: Introduce concept
- Week 2: Revisit with more depth
- Week 3: Revisit with application
- Week 5: Mastery level

### 4. Tool Accumulation
- Week 1: Tool A
- Week 2: Tool B (using Tool A)
- Week 3: Tool C (using Tools A+B)
- Week 5: All tools integrated

---

## Common Issues Found

### ❌ Orphaned Concepts
**Problem:** "Competitive analysis framework" taught in Week 1, never used again

**Impact:** Students forget, perceive course as disjointed

**Fix:** Either thread through Weeks 2-5 OR remove from Week 1

### ❌ Inappropriate Re-teaching
**Problem:** Week 4 re-defines "revenue model" (already taught Week 1)

**Impact:** Wastes time, insults student intelligence, prevents deeper learning

**Fix:** Change to application: "Using the revenue model from Week 1, analyze this scenario..."

### ❌ Siloed Assessments
**Problem:** Week 3 assessment only tests Week 3 content

**Impact:** Students forget Week 1-2, no cumulative learning

**Fix:** Add Week 1-2 concepts to Week 3 assessment

---

## Threading Checklist

The agent validates against this checklist:

**Planning Phase:**
- [ ] 3-5 core concepts identified
- [ ] Each core concept appears in ≥3 weeks
- [ ] Progressive complexity planned
- [ ] Callback language planned

**Week-by-Week Design:**
- [ ] Week 1 introduces all core concepts
- [ ] Week 2-4 apply/build on Week 1 concepts
- [ ] Week 5 synthesizes all concepts
- [ ] Each week has ≥1 explicit callback to Week 1

**Assessment Alignment:**
- [ ] Week 2-5 assessments test Week 1 concepts
- [ ] Capstone requires cumulative knowledge
- [ ] No siloed assessments (current week only)

---

**When to Run This Check:**
1. After course outline created (validate threading plan)
2. After drafting all weeks (verify execution)
3. Before peer review (catch threading gaps early)
4. After revisions (verify threading fixes)

**Workflow Position:**
- Run AFTER `/create-outline` validates threading plan
- Run WITH `/check-terminology` (concepts need consistent terms)
- Run BEFORE `/peer-review` (threading affects pedagogical design score)
