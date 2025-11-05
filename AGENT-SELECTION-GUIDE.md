# Agent Selection Guide

**Quick Reference**: Which agent to use when

---

## 🎯 Task-Based Agent Selection

### 📝 COURSE PLANNING & DESIGN

| Task | Use This Agent | NOT This Agent | Why |
|------|---------------|----------------|-----|
| Create new course outline from scratch | **course-outline-creator** | uplimit-storyboard-builder | Outline creator does strategic CLOs/MLOs/assessment strategy first |
| Build detailed storyboards after outline exists | **uplimit-storyboard-builder** | course-outline-creator | Storyboard builder creates copy-paste-ready module designs |
| Audit existing storyboards for platform compliance | **uplimit-storyboard-builder** (AUDIT mode) | branding-checker | Storyboard builder includes branding + interactivity + structure |
| Check ONLY branding symbols (no other issues) | **branding-checker** | uplimit-storyboard-builder | Faster for branding-only checks |

**Sequential Workflow:**
1. **course-outline-creator** → Create strategic outline (CLOs, weekly themes, assessment strategy)
2. **uplimit-storyboard-builder** → Design detailed storyboards (elements, widgets, copy)
3. **peer-review-simulator** → Get comprehensive QA before build

---

### ✅ VALIDATION & CONSISTENCY

| Task | Use This Agent | NOT This Agent | Why |
|------|---------------|----------------|-----|
| Check terminology consistency (glossary building) | **terminology-consistency-checker** | concept-threading-checker | Terminology checker finds term variations/acronyms |
| Check Week 1 concepts appear in later weeks | **concept-threading-checker** | terminology-consistency-checker | Concept threading tracks concept progression |
| Check PAIRR methodology consistency across weeks | **assessment-consistency-checker** | cohort-structure-checker | Assessment checker validates methodology consistency |
| Check module structural patterns (element sequences) | **cohort-structure-checker** | assessment-consistency-checker | Structure checker validates storyboard architecture |
| Validate rubric point totals, grading distribution | **assessment-consistency-checker** | rubric-generator | Assessment checker audits existing assessments |

**When to Run Multiple Checkers:**
- **Comprehensive Course Audit**: Run all 4 checkers (terminology + concept + assessment + cohort-structure)
- **Pre-Launch QA**: Run cohort-structure-checker + assessment-consistency-checker minimum

---

### 📊 ASSESSMENT DESIGN

| Task | Use This Agent | NOT This Agent | Why |
|------|---------------|----------------|-----|
| Design complete assessment (instructions + rubric + AI policy) | **assessment-designer** | rubric-generator | Assessment designer does full design with research-backed methodologies |
| Generate ONLY a rubric quickly | **rubric-generator** | assessment-designer | Faster for rubric-only needs |
| Create PAIRR assessment | **assessment-designer** | rubric-generator | PAIRR requires dual-feedback design (research knowledge needed) |
| Create AI Roleplay exercise | **assessment-designer** | rubric-generator | AI roleplay requires character config + system prompts |
| Create diagnostic rubric (3-level, formative) | **assessment-designer** | rubric-generator | Diagnostic rubrics need specialized structure |

**Decision Logic:**
- **Need full assessment?** → assessment-designer
- **Already have instructions, just need rubric?** → rubric-generator
- **AI integration required?** → assessment-designer (has 464 KB knowledge base)

---

### 🎨 WIDGET DESIGN & TESTING

| Task | Use This Agent | NOT This Agent | Why |
|------|---------------|----------------|-----|
| Generate new widget from scratch | **widget-designer** (GENERATE mode) | widget-tester | Designer creates widget code with design system |
| Audit existing widget for design system compliance | **widget-designer** (AUDIT mode) | widget-tester | Designer checks Geist fonts, CSS variables, emojis |
| Test widget UX with student personas | **widget-tester** | widget-designer | Tester simulates 3 student personas (Quick/Methodical/Struggling) |
| Fix design system violations (hardcoded colors, emojis) | **widget-designer** (AUDIT mode) | widget-tester | Designer offers auto-fix for violations |

**Sequential Workflow:**
1. **widget-designer** (GENERATE) → Create widget with design system
2. **widget-designer** (AUDIT) → Verify design compliance
3. **widget-tester** → Test UX with personas
4. **accessibility-auditor** → Deep WCAG audit (if widget is complex)

**Automatic Testing:**
- PostToolUse hook auto-runs widget testing after Write operations

---

### ♿ ACCESSIBILITY

| Task | Use This Agent | NOT This Agent | Why |
|------|---------------|----------------|-----|
| Audit HTML/CSS for WCAG 2.2 AA compliance | **accessibility-auditor** | frontend-reviewer | Accessibility auditor specializes in WCAG with automated tools |
| Review React/JSX code (accessibility + best practices) | **frontend-reviewer** | accessibility-auditor | Frontend reviewer does holistic code review |
| Audit static HTML widgets | **accessibility-auditor** | frontend-reviewer | Accessibility auditor has contrast/alt text automation |
| Review React learning platform code | **frontend-reviewer** | accessibility-auditor | Frontend reviewer understands React patterns |

**Decision Logic:**
- **Static HTML/CSS files?** → accessibility-auditor
- **React components?** → frontend-reviewer (includes accessibility + React patterns + UX + performance)
- **Need both?** → Run accessibility-auditor first (detailed WCAG), then frontend-reviewer (code quality)

---

### 💻 CODE REVIEW

| Task | Use This Agent | Why |
|------|---------------|-----|
| Review FastAPI/Python backend code | **backend-reviewer** | Specializes in security, error handling, API design |
| Review React/JSX frontend code | **frontend-reviewer** | Specializes in React patterns, accessibility, UX, performance |

**Automatic Review:**
- PostToolUse hook auto-reviews Python/JSX files after Edit/Write

**NO OVERLAP**: These agents target different languages.

---

### 🎭 SIMULATION & TESTING

| Task | Use This Agent | NOT This Agent | Why |
|------|---------------|----------------|-----|
| Comprehensive design review (6 specialists) | **peer-review-simulator** | student-journey-simulator | Peer review simulates ID team (Content/Accessibility/Visual/Technical/Pedagogical/UX) |
| Test course flow across multiple weeks | **student-journey-simulator** | peer-review-simulator | Journey simulator tests 4 student personas through full course |
| Test single widget with student personas | **widget-tester** | student-journey-simulator | Widget tester focuses on 3 personas (Quick/Methodical/Struggling) for one widget |
| Pre-launch QA (storyboards) | **peer-review-simulator** | student-journey-simulator | Peer review scores readiness (0-100) with prioritized fixes |
| Validate learning progression, cognitive load | **student-journey-simulator** | peer-review-simulator | Journey simulator tracks week-by-week student experience |

**Decision Logic:**
- **Review storyboards before build?** → peer-review-simulator
- **Test implemented course flow?** → student-journey-simulator
- **Test single widget?** → widget-tester

---

### 🎓 CONTENT CREATION

| Task | Use This Agent | Why |
|------|---------------|-----|
| Create UDL alternatives (audio scripts, infographics) | **udl-content-generator** | Transforms content for diverse learners |

**NO OVERLAP**: This agent is unique.

---

## 🔍 OVERLAP ANALYSIS

### Overlap #1: Accessibility Checking

**accessibility-auditor** vs **frontend-reviewer**

| Dimension | accessibility-auditor | frontend-reviewer |
|-----------|----------------------|-------------------|
| **File Type** | HTML/CSS | React/JSX |
| **Focus** | WCAG 2.2 AA compliance | Code quality + accessibility |
| **Depth** | Deep WCAG audit (every criterion) | Accessibility is 1 of 5 areas |
| **Tools** | Automated contrast/alt text checkers | Manual code review |
| **Output** | Line-by-line fixes with WCAG citations | Strengths/suggestions/critical issues |

**When to Use Both:**
1. **frontend-reviewer** → Holistic React code review
2. **accessibility-auditor** → Deep WCAG audit of HTML output

---

### Overlap #2: PAIRR Checking

**cohort-structure-checker** vs **assessment-consistency-checker**

| Dimension | cohort-structure-checker | assessment-consistency-checker |
|-----------|-------------------------|-------------------------------|
| **What it checks** | PAIRR components PRESENT in Module 6 | PAIRR used CONSISTENTLY across weeks |
| **Scope** | Single week structural validation | Cross-week methodology consistency |
| **Focus** | "Does Module 6 have all 4 PAIRR parts?" | "Do Weeks 1-5 all use same methodology?" |
| **Output** | Structural violations (missing element) | Consistency violations (Week 1 has PAIRR, Week 3 doesn't) |

**When to Use Both:**
- Run **cohort-structure-checker** per week (validate structure)
- Run **assessment-consistency-checker** across all weeks (validate consistency)

---

### Overlap #3: Rubric Creation

**assessment-designer** vs **rubric-generator**

| Dimension | assessment-designer | rubric-generator |
|-----------|--------------------|--------------------|
| **Output** | Complete assessment (instructions + rubric + AI policy) | Rubric only |
| **Time** | 10-15 minutes | 2-3 minutes |
| **Knowledge Base** | 464 KB research (PAIRR, AI Roleplay, etc.) | QM standards only |
| **Use Case** | New assessment design | Quick rubric scaffolding |

**Decision Logic:**
- **Quick rubric for existing assignment?** → rubric-generator
- **Design new assessment from scratch?** → assessment-designer

---

### Overlap #4: Simulation Agents

**peer-review-simulator** vs **student-journey-simulator** vs **widget-tester**

| Dimension | peer-review-simulator | student-journey-simulator | widget-tester |
|-----------|----------------------|--------------------------|---------------|
| **Perspective** | 6 ID specialists | 4 student personas | 3 student personas |
| **Scope** | Any content (storyboards/live) | Multi-week course flow | Single widget |
| **Focus** | Design quality (comprehensive QA) | Learning progression, cognitive load | UX, accessibility, usability |
| **Model** | Opus (slower, deeper) | Sonnet (faster) | Sonnet (faster) |
| **Output** | Readiness score + prioritized fixes | Week-by-week persona journeys | UX issues per persona |

**When to Use Which:**
- **Pre-launch QA for storyboards?** → peer-review-simulator
- **Test course flow across weeks?** → student-journey-simulator
- **Test single widget?** → widget-tester

---

### Overlap #5: Branding Checks

**uplimit-storyboard-builder** (AUDIT) vs **branding-checker**

| Dimension | uplimit-storyboard-builder | branding-checker |
|-----------|---------------------------|------------------|
| **Checks** | Platform compliance + branding + interactivity + structure | Branding only (symbols, conventions) |
| **Platforms** | Uplimit only | Canvas LMS + Uplimit |
| **Speed** | 2-5 minutes (comprehensive) | 30 seconds (branding only) |
| **Use Case** | Full storyboard audit | Quick branding-only check |

**Decision Logic:**
- **Need full storyboard audit?** → uplimit-storyboard-builder (AUDIT)
- **Only check emoji/symbol compliance?** → branding-checker

---

## 🚀 RECOMMENDED WORKFLOWS

### Workflow 1: New Course Design (Start to Finish)

```
1. course-outline-creator
   ↓ (Strategic outline: CLOs, MLOs, weekly themes, assessment strategy)
2. uplimit-storyboard-builder (BUILD MODE)
   ↓ (Detailed storyboards: elements, widgets, copy)
3. terminology-consistency-checker
   ↓ (Validate term consistency, build glossary)
4. concept-threading-checker
   ↓ (Ensure Week 1 concepts thread through later weeks)
5. assessment-consistency-checker
   ↓ (Validate PAIRR/rubric consistency)
6. cohort-structure-checker
   ↓ (Validate structural patterns per module)
7. peer-review-simulator
   ↓ (Comprehensive QA with 6 specialists)
8. student-journey-simulator
   ↓ (Test course flow with 4 personas)
9. BUILD COURSE
10. accessibility-auditor (HTML widgets)
11. frontend-reviewer (React components)
```

**Time estimate:** 3-5 hours for full pipeline

---

### Workflow 2: Audit Existing Course

```
1. uplimit-storyboard-builder (AUDIT MODE)
   ↓ (Platform compliance, interactivity, branding)
2. cohort-structure-checker
   ↓ (Structural validation)
3. assessment-consistency-checker
   ↓ (Methodology consistency)
4. terminology-consistency-checker
   ↓ (Term variations, glossary)
5. concept-threading-checker
   ↓ (Concept progression)
6. peer-review-simulator
   ↓ (Comprehensive QA)
7. accessibility-auditor (widgets)
8. frontend-reviewer (code)
```

**Time estimate:** 2-4 hours for full audit

---

### Workflow 3: Quick Widget Creation

```
1. widget-designer (GENERATE MODE)
   ↓ (Create widget with design system)
2. widget-designer (AUDIT MODE)
   ↓ (Verify design compliance)
3. widget-tester
   ↓ (Test UX with 3 personas)
4. accessibility-auditor
   ↓ (Deep WCAG audit)
```

**Time estimate:** 15-30 minutes

**Note:** PostToolUse hook auto-runs step 3 after widget creation.

---

### Workflow 4: Assessment Design

**Option A: Full Assessment (PAIRR/AI Roleplay)**
```
1. assessment-designer
   ↓ (Instructions + rubric + AI policy + methodology)
2. assessment-consistency-checker
   ↓ (Validate consistency with other weeks)
```

**Option B: Quick Rubric Only**
```
1. rubric-generator
   ↓ (QM-aligned rubric only)
```

---

## 📋 AGENT QUICK REFERENCE

| Agent | Primary Use | Time | Model |
|-------|-------------|------|-------|
| **accessibility-auditor** | WCAG 2.2 AA audit (HTML/CSS) | 2-5 min | sonnet |
| **assessment-consistency-checker** | Cross-week assessment consistency | 3-5 min | sonnet |
| **assessment-designer** | Full assessment design (PAIRR, AI roleplay) | 10-15 min | sonnet |
| **backend-reviewer** | FastAPI/Python code review | 2-5 min | sonnet |
| **branding-checker** | Canvas/Uplimit branding validation | 30 sec | sonnet |
| **cohort-structure-checker** | Module structure validation | 5-10 min | sonnet |
| **concept-threading-checker** | Week 1 → later weeks concept tracking | 3-5 min | sonnet |
| **course-outline-creator** | Strategic course outline (CLOs/MLOs) | 10-20 min | sonnet |
| **frontend-reviewer** | React/JSX code review + accessibility | 2-5 min | sonnet |
| **peer-review-simulator** | 6-specialist comprehensive QA | 10-20 min | opus |
| **rubric-generator** | Quick QM-aligned rubric | 2-3 min | sonnet |
| **student-journey-simulator** | Multi-week course flow testing | 8-15 min | sonnet |
| **terminology-consistency-checker** | Term consistency, glossary building | 3-5 min | sonnet |
| **udl-content-generator** | UDL alternatives (audio, infographics) | 5-10 min | sonnet |
| **uplimit-storyboard-builder** | Create/audit storyboards | 5-20 min | sonnet |
| **widget-designer** | Generate/audit widgets (design system) | 5-10 min | sonnet |
| **widget-tester** | Test widgets with 3 personas | 3-5 min | sonnet |

---

## 🎯 DECISION TREES

### "I need to check accessibility"

```
START
  ↓
Is it React/JSX code?
  YES → frontend-reviewer (includes accessibility + React patterns + UX)
  NO → Is it static HTML/CSS?
        YES → accessibility-auditor (deep WCAG audit)
        NO → Ask: What file type?
```

### "I need to validate consistency"

```
START
  ↓
What type of consistency?
  ├─ Terminology (term variations, acronyms) → terminology-consistency-checker
  ├─ Concepts (Week 1 in later weeks) → concept-threading-checker
  ├─ Assessment methodology (PAIRR, rubrics) → assessment-consistency-checker
  └─ Structure (element sequences, PAIRR presence) → cohort-structure-checker
```

### "I need to design an assessment"

```
START
  ↓
Do you need complete assessment (instructions + rubric + AI policy)?
  YES → assessment-designer
  NO → Do you just need a rubric?
        YES → rubric-generator
        NO → What do you need?
```

### "I need to test/review content"

```
START
  ↓
What scope?
  ├─ Single widget → widget-tester (3 personas, UX focus)
  ├─ Multi-week course flow → student-journey-simulator (4 personas, learning progression)
  └─ Pre-launch QA (any content) → peer-review-simulator (6 specialists, comprehensive)
```

---

## ⚠️ COMMON MISTAKES

### ❌ Using the Wrong Agent

| Wrong | Right | Why |
|-------|-------|-----|
| Using rubric-generator for PAIRR | assessment-designer | PAIRR needs dual-feedback design |
| Using frontend-reviewer for HTML widgets | accessibility-auditor | HTML audit needs specialized tools |
| Using cohort-structure-checker for cross-week consistency | assessment-consistency-checker | Structure checker validates per-week, not across weeks |
| Using branding-checker for full storyboard audit | uplimit-storyboard-builder (AUDIT) | Branding checker only checks symbols |
| Using widget-tester to create widgets | widget-designer | Tester tests UX, doesn't generate code |

### ❌ Skipping Agents in Sequence

| Skipping | Result |
|----------|--------|
| Skipping course-outline-creator, going straight to storyboarding | No strategic foundation (CLOs, threading plan, assessment strategy) |
| Skipping consistency checkers before launch | Inconsistent terminology, orphaned concepts, PAIRR gaps |
| Skipping peer-review-simulator before build | Launch with design flaws that 6 specialists would catch |

### ❌ Using Multiple Overlapping Agents Unnecessarily

| Redundant | Efficient |
|-----------|-----------|
| Running branding-checker + uplimit-storyboard-builder AUDIT | Just run uplimit-storyboard-builder AUDIT (includes branding) |
| Running rubric-generator + assessment-designer for same assessment | Pick one: assessment-designer for full design, rubric-generator for quick rubric |

---

## 📞 AGENT INVOCATION EXAMPLES

### Correct Invocation
```
uplimit-storyboard-builder
widget-designer
assessment-designer
peer-review-simulator
```

### ❌ OLD Invocation (v2.8.4 and earlier - NO LONGER NEEDED)
```
uplimit-storyboard-builder:uplimit-storyboard-builder
widget-designer:widget-designer
```

**v2.8.5 fix:** Agents now invokable without double-scoping!

---

## 🔄 VERSION HISTORY

**v2.8.5** (2025-01-03):
- Fixed double-scoping issue (agents now invokable without namespace collision)
- Repository restructured to single plugin format

**v2.8.0** (2025-01-31):
- Added widget-designer agent (generate/audit widgets)
- Added widget auto-tester hook (PostToolUse)

**v2.7.0** (2025-01-31):
- Added 3 specialized consistency checkers (terminology, concept-threading, assessment)
- Deprecated monolithic consistency-checker agent

**v2.6.3** (2025-01-31):
- Added cohort-structure-checker agent

**v2.6.0** (2025-01-28):
- Added course-outline-creator agent

**v2.5.0** (2025-01-23):
- Added backend-reviewer and frontend-reviewer agents
- Added automatic code review hook (PostToolUse)

---

**Questions?** Check the main README.md or CLAUDE.md for detailed agent documentation.
