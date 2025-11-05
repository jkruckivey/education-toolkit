# Slash Command Analysis

**Question:** Why are there 17 agents but only 9 slash commands?

---

## 📊 Current State

### Agents WITH Slash Commands (9)

| Agent | Slash Command | Rationale |
|-------|--------------|-----------|
| accessibility-auditor | `/audit-module` | Common workflow: audit HTML files for WCAG |
| accessibility-auditor | `/review-content` | Alternative entry point for content review |
| assessment-designer | `/design-assessment` | Common workflow: create assessments |
| branding-checker | `/check-branding` | Common workflow: quick branding validation |
| peer-review-simulator | `/peer-review` | Common workflow: comprehensive QA |
| rubric-generator | `/generate-rubric` | Common workflow: quick rubric creation |
| student-journey-simulator | `/simulate-journey` | Common workflow: test course flow |
| uplimit-storyboard-builder | `/build-storyboard` | Common workflow: create storyboards |
| widget-tester | `/test-widget` | Common workflow: test widgets |

**Total:** 9 commands for 8 agents (accessibility-auditor has 2 commands)

---

### Agents WITHOUT Slash Commands (9)

| Agent | Why No Command? | Should It Have One? |
|-------|----------------|---------------------|
| **assessment-consistency-checker** | Specialized validator, better invoked by name | ⚠️ MAYBE - /check-assessment-consistency |
| **backend-reviewer** | Automatic (PostToolUse hook triggers it) | ❌ NO - hook handles it |
| **cohort-structure-checker** | Specialized validator, newer agent (v2.6.3) | ⚠️ MAYBE - /check-cohort-structure |
| **concept-threading-checker** | Specialized validator, newer agent (v2.7.0) | ⚠️ MAYBE - /check-concept-threading |
| **course-outline-creator** | Newer agent (v2.6.0), complex workflow | ⚠️ MAYBE - /create-outline |
| **frontend-reviewer** | Automatic (PostToolUse hook triggers it) | ❌ NO - hook handles it |
| **terminology-consistency-checker** | Specialized validator, newer agent (v2.7.0) | ⚠️ MAYBE - /check-terminology |
| **udl-content-generator** | Specialized content creation, less common | ⚠️ MAYBE - /generate-udl-alternatives |
| **widget-designer** | Newer agent (v2.8.0), dual-mode (GENERATE/AUDIT) | ⚠️ MAYBE - /design-widget or /audit-widget |

---

## 🔍 README Error Found

**README.md claims 10 slash commands:**
> 4. **/check-consistency** - Check consistency across modules (terminology, threading, narrative)

**Reality:** This command file doesn't exist!

**Explanation:**
- The old `consistency-checker` agent (deprecated v2.7.0) likely had a `/check-consistency` command
- In v2.7.0, consistency-checker was replaced by 3 specialized agents:
  - `terminology-consistency-checker`
  - `concept-threading-checker`
  - `assessment-consistency-checker`
- The slash command was removed but README wasn't updated
- **Actual count: 9 slash commands, not 10**

---

## 🧠 Design Philosophy: Why Not All Agents Have Commands?

### Principle 1: Common Workflows Only
**Slash commands are for frequent, simple invocations.**

✅ **Good candidates:**
- `/build-storyboard` - Very common workflow
- `/design-assessment` - Frequent task
- `/test-widget` - Quick testing

❌ **Bad candidates:**
- Agents that require complex context or parameters
- Specialized validators that are better invoked with natural language
- Agents triggered automatically by hooks

---

### Principle 2: Automatic Triggers Don't Need Commands
**Code reviewers (backend-reviewer, frontend-reviewer) are triggered by PostToolUse hooks.**

**Why no command?**
- Users don't manually request code reviews
- Hooks automatically run after Edit/Write on .py/.jsx files
- Command would be redundant

---

### Principle 3: Natural Language Invocation Works Well
**Some agents are better invoked by description matching.**

**Example:**
```
User: "Check terminology consistency across Week 1-5"
Claude: [Automatically invokes terminology-consistency-checker]
```

**Why this works:**
- Agent description is clear and specific
- Natural language is more flexible than rigid command syntax
- Users don't need to memorize command names

---

### Principle 4: Newer Agents Haven't Been Prioritized Yet
**Agents added in v2.6.0+ don't have commands yet.**

**Timeline:**
- **v2.6.0**: course-outline-creator (no command)
- **v2.6.3**: cohort-structure-checker (no command)
- **v2.7.0**: 3 consistency checkers (no commands)
- **v2.8.0**: widget-designer (no command)

**Why?**
- Focus was on agent functionality first
- Slash commands can be added later based on user feedback
- Natural invocation works fine for now

---

## 💡 Recommendations

### Option A: Keep Current State (Minimal Commands)
**Rationale:** Natural language invocation works well, don't over-complicate

**Pros:**
- Less to maintain
- Natural language is more flexible
- Hooks handle automatic triggers

**Cons:**
- Users need to remember agent names
- No quick shortcuts for newer agents

---

### Option B: Add Commands for Top 5 Missing Agents
**Recommended additions:**

1. **`/create-outline`** → course-outline-creator
   - **Why:** Common starting point for new courses
   - **Usage:** `/create-outline 5-week MBA Marketing`

2. **`/check-cohort-structure`** → cohort-structure-checker
   - **Why:** Important pre-launch validation
   - **Usage:** `/check-cohort-structure week1-5`

3. **`/check-terminology`** → terminology-consistency-checker
   - **Why:** Frequently needed consistency check
   - **Usage:** `/check-terminology week1-5`

4. **`/check-concept-threading`** → concept-threading-checker
   - **Why:** Critical for course cohesion
   - **Usage:** `/check-concept-threading week1-5`

5. **`/design-widget`** → widget-designer (GENERATE mode)
   - **Why:** Common workflow for interactive content
   - **Usage:** `/design-widget quiz Revenue Models`

**Result:** 14 total slash commands (9 existing + 5 new)

---

### Option C: Add Commands for ALL Non-Automatic Agents
**Add commands for 7 agents** (exclude backend-reviewer, frontend-reviewer which are automatic)

**Additional commands beyond Option B:**
6. **`/check-assessment-consistency`** → assessment-consistency-checker
7. **`/generate-udl-alternatives`** → udl-content-generator

**Result:** 16 total slash commands (9 existing + 7 new)

---

## 🎯 My Recommendation: Option B

**Add 5 strategic slash commands for frequently-used newer agents.**

**Rationale:**
- **course-outline-creator** is a natural starting point (high value)
- **3 consistency checkers** are frequently needed for QA
- **widget-designer** is a common workflow for interactive content
- Keeps command list manageable (14 total)
- Leaves UDL generator and assessment consistency checker for natural invocation (less frequent)

**What to do:**
1. Create 5 new command files in `/commands/`
2. Update README.md to reflect actual count (9 → 14)
3. Remove `/check-consistency` from README (doesn't exist)
4. Update plugin.json description if needed

---

## 📋 Command Implementation Template

### Example: `/create-outline`

**File:** `commands/create-outline.md`

```markdown
---
description: Create strategic course outline with CLOs, weekly structure, MLOs, and assessment strategy
---

You are helping create a comprehensive course outline from scratch.

Use the **course-outline-creator** agent to guide the instructor through:

1. Discovery interview (subject area, level, duration, format)
2. CLO definition (QM-compliant, single action verbs)
3. Weekly structure planning
4. MLO creation per week
5. Assessment strategy design
6. Concept threading map
7. Case study & practitioner plan

Output a complete course outline ready for storyboarding.

# Example Usage

```
/create-outline
/create-outline 5-week MBA Marketing
/create-outline "Executive Ed Finance 3-week cohort"
```

# Expected Output

## Course Outline: [Title]
- Course Learning Outcomes (CLOs)
- Course Structure (weekly breakdown)
- Assessment Summary
- Concept Threading Map
- Case Study & Practitioner Plan
```

---

## 🔧 Quick Fixes Needed

### Fix #1: Update README.md Slash Command Count
**Current (WRONG):**
> ### ⚡ 10 Quick Slash Commands

**Should be:**
> ### ⚡ 9 Quick Slash Commands

---

### Fix #2: Remove Non-Existent Command from README
**Current (WRONG):**
> 4. **/check-consistency** - Check consistency across modules (terminology, threading, narrative)

**Should be:** Remove this line (command doesn't exist)

**Alternative:** Add note explaining deprecation:
> 4. ~~**/check-consistency**~~ - **DEPRECATED in v2.7.0**. Use specialized agents instead: `terminology-consistency-checker`, `concept-threading-checker`, `assessment-consistency-checker`

---

## 📊 Summary

| Category | Count | Details |
|----------|-------|---------|
| **Total Agents** | 17 | All functional |
| **Agents with Commands** | 8 | accessibility-auditor (2 commands), 7 others (1 each) |
| **Total Commands** | 9 | Not 10 as README claims |
| **Automatic Agents** | 2 | backend-reviewer, frontend-reviewer (hooks) |
| **Candidates for New Commands** | 7 | 5 high-priority (Option B), 7 total (Option C) |

**Current mismatch:** README claims 10, reality is 9 commands.

**Reason for gap:** Newer agents (v2.6.0+) and specialized validators don't have commands yet. Code reviewers don't need commands (automatic).

**Recommendation:** Add 5 high-value commands (Option B) to reach 14 total.

---

## ✅ Action Items

### Immediate (Fix README Errors)
- [ ] Change "10 Quick Slash Commands" → "9 Quick Slash Commands"
- [ ] Remove or mark deprecated `/check-consistency` line
- [ ] Add note explaining why code reviewers don't have commands

### Optional (Add New Commands - Option B)
- [ ] Create `/create-outline` → course-outline-creator
- [ ] Create `/check-cohort-structure` → cohort-structure-checker
- [ ] Create `/check-terminology` → terminology-consistency-checker
- [ ] Create `/check-concept-threading` → concept-threading-checker
- [ ] Create `/design-widget` → widget-designer
- [ ] Update README count: "9 Quick Slash Commands" → "14 Quick Slash Commands"

---

**Decision:** Should we:
1. Just fix the README errors (9 commands, not 10)?
2. Add 5 strategic commands (Option B - total 14)?
3. Add all 7 possible commands (Option C - total 16)?
