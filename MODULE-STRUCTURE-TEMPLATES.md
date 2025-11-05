# MODULE STRUCTURE TEMPLATES

## Critical: Course Format Determines Structure

**Before building storyboards, confirm course format:**

**COHORT COURSES:**
- Fixed start/end dates
- Weekly deadlines
- Synchronous peer interaction possible
- Can use PAIRR methodology (peer + AI feedback)
- Anchor Project with weekly milestones

**SELF-PACED COURSES:**
- Students work at own speed
- Asynchronous only
- NO peer interaction
- Individual assessments only (AI feedback OK, NO peer feedback)
- Final Project with checkpoint system

**ASK THE USER if format is unclear!** The templates below differ significantly.

---

## COHORT COURSE MODULE TEMPLATES

Use these templates when building cohort-based courses with fixed weekly deadlines and peer interaction.

### MODULE 0: Bridge/Hook (Optional)
**Purpose:** Teaser content to hook student interest

**Structure:**
- No prescribed element pattern (flexible content)
- Typically 2-4 elements
- No Final Project Connection required
- Short duration (5-10 minutes)

**Example Elements:**
- Video teaser
- Industry stat tiles
- "What you'll build" preview
- Course narrative setup

---

### MODULE 1: Welcome & Learning Outcomes
**Purpose:** Set weekly context and establish learning outcomes

**Required Element Sequence:**

| # | Element Type | Purpose | Content Specs |
|---|--------------|---------|---------------|
| 1 | **Text** | Welcome + connection from previous weeks | 100-150 words. Pattern: "Last week [recap], this week [preview]" |
| 2 | **Infobox (Callout)** | Week overview + time commitment | 75-100 words. State total hours, breakdown by activity type |
| 3 | **Text** | Full week learning outcomes (MLO X.1-X.4) | Each MLO needs: "What You'll Master", "Success Criteria", "Why This Matters" |
| 4 | **iFrame Widget** | Learning outcomes visualizer | File: `learning-outcomes-module-1.html` - shows ALL week's MLOs |
| 5 | **Text** | Anchor Project connection | How this week's outcomes support Anchor Project milestone |
| 6+ | **Various** | Additional content (optional) | Videos, infoboxes, etc. |
| N-1 | **Text** | 🎯 FINAL PROJECT CONNECTION | See template below |
| N | **Text** | Module 1 Complete - Transition | Preview Module 2 topic |

**MLO Format Requirements:**
- Use single action verbs (Analyze, Evaluate, Design - NOT compound verbs)
- Format: MLO X.1, X.2, X.3, X.4 (where X = week number)
- Each MLO needs three subsections:
  - "What You'll Master:" (skill/capability)
  - "Success Criteria:" (how students know they've mastered it)
  - "Why This Matters:" (real-world application)

**Element 5 Special Note (Anchor Project):**
- Module 1's Anchor Project connection explains **Week 5 final capstone**, not just current week
- Sets up the big picture (what students will build by end of course)
- Explains how each week builds toward capstone

---

### MODULES 2-5: Standard Content Modules
**Purpose:** Deliver weekly content with clear learning progression

**Required Element Sequence:**

| # | Element Type | Purpose | Content Specs |
|---|--------------|---------|---------------|
| 1 | **Text** | Connecting intro | 100-150 words. Pattern: "You've just [previous module] → Now you'll [current module]". NO repeated learning objectives! |
| 2 | **iFrame Widget** | Learning outcomes widget | File: `learning-outcomes-module-{N}.html` - shows SUBSET of week's MLOs relevant to THIS module |
| 3+ | **Various** | Content delivery | Videos, text, widgets, infoboxes, tiles, tables, accordions - follow V3 Interactive-First |
| N-1 | **Text** | 🎯 FINAL PROJECT CONNECTION | See template below |
| N | **Text** | Module X Complete - Transition | Recap insights, preview next module |

**Element 1 Validation (Connecting Text):**
- ✅ CORRECT: "You now understand the four learning outcomes (Module 1). Before exploring frameworks, hear from practitioners..."
- ❌ WRONG: Repeating learning objectives verbatim (those belong in Module 1 only)
- ❌ WRONG: Generic intro without connection to previous module

**Element 2 Widget Specs:**
- Widget shows **subset** of week's MLOs practiced in THIS specific module
- NOT all MLOs repeated (Module 1 showed all MLOs already)
- Example: Module 3 might practice MLO 2.2 and 2.4 (not all 2.1-2.4)

**Content Elements (3+):**
- Follow V3 Interactive-First principles
- Text blocks: 100-150 words max
- Widget every 2-3 elements
- Varied element types (not all text)

---

### MODULE 6: Assessment (Special Requirements)
**Purpose:** Summative assessment for the week

**Required Element Sequence:** Same as Modules 2-5 PLUS:

**PAIRR Methodology Components (REQUIRED for Cohort Courses):**

PAIRR (Peer and AI Review + Reflection) must include these 4 components:

**1. Dual Feedback Phase:**
```markdown
## Feedback Instructions

### Peer Feedback
- Submit your draft to peer review platform by [deadline]
- Use rubric provided (Section 4.1) to evaluate classmate's work
- Provide constructive feedback on 3 areas: [list criteria]

### AI Feedback
- Paste your draft into ChatGPT with this prompt:
  "You are an executive coach reviewing a strategic business memo.
   Evaluate this memo on clarity, strategic thinking, and evidence use.
   Provide specific suggestions for improvement."
- Save AI feedback responses for comparative reflection
```

**2. Comparative Reflection Questions:**
```markdown
## Comparative Reflection (1 bonus point)

After receiving both peer and AI feedback, answer:

1. **Feedback Quality:** Which feedback source (peer or AI) was more useful? Why?
2. **Specific Insights:** What did your peer notice that AI missed? What did AI notice that your peer missed?
3. **Trust & Confidence:** How confident are you in applying each type of feedback?
4. **Synthesis:** How will you combine both feedback sources for your revision?
```

**3. Post-Revision Reflection:**
```markdown
## Post-Revision Reflection (1 bonus point)

After revising your work, answer:

1. **Feedback Integration:** Which pieces of feedback did you incorporate? Which did you reject? Why?
2. **Learning from Comparison:** What did comparing peer vs AI feedback teach you about using AI in your work?
3. **Future Use:** How will this experience inform how you use AI feedback in future work?
```

**4. Bonus Structure (5 points total):**
- 2 pts: Complete peer review for classmate (using rubric)
- 1 pt: Generate and submit AI feedback on own draft
- 1 pt: Complete comparative reflection
- 1 pt: Complete post-revision reflection

**Common PAIRR Errors to Avoid:**
- ❌ Only peer review (missing AI component)
- ❌ AI feedback present but no comparative reflection
- ❌ Missing post-revision reflection after incorporating feedback
- ❌ Generic "get feedback" instructions without PAIRR framework
- ❌ Bonus points don't total 5 or breakdown is different

---

### MODULE 7: Wrap-Up & Reflection
**Purpose:** Consolidate learning and prepare for next week

**Required Components:**

**1. Week Journey Recap:**
```markdown
## Your Journey This Week

You've completed a comprehensive week exploring [topic]. Here's your path:

- **Module 0:** [Hook content summary]
- **Module 1:** [Learning outcomes established]
- **Module 2:** [Practitioners' perspectives]
- **Module 3:** [Frameworks & analysis]
- **Module 4:** [Hands-on simulation]
- **Module 5:** [Case study application]
- **Module 6:** [Strategic assessment + PAIRR]
- **Module 7:** [Synthesis & reflection]
```

**2. Reflection Prompts:**
- 3-5 questions for students to process learning
- Connection to big picture/course narrative
- "What surprised you?" "How does this change your thinking?" type questions

**3. Anchor Project Milestone Reminder:**
```markdown
## ⏰ Anchor Project Milestone Due: [Date]

This week's Milestone [X]: [Deliverable name]

**What's Due:**
- [Specific deliverable 1]
- [Specific deliverable 2]

**How This Week Supports Your Milestone:**
[Paragraph connecting week's learning to milestone completion]
```

**4. Next Week Preview:**
- Build anticipation for Week X+1
- Show how learning progression continues
- Tease next week's hook/case/simulation

**5. Final Project Connection:**
- How this week's frameworks apply to Week 5 capstone
- What students can start incorporating now

---

### FINAL PROJECT CONNECTION TEMPLATE (All Modules)

Every module must have this section (second-to-last or third-to-last element):

```markdown
## 🎯 FINAL PROJECT CONNECTION

**How Module [X] Supports Your Final Strategic Vision:**

[1-2 sentences connecting module content to Week 5 capstone deliverable]

**What You Learned:**
- [Specific capability 1 from this module]
- [Specific capability 2 from this module]
- [Specific capability 3 from this module]
- [Specific capability 4 from this module]

**How to Apply This to Your Final Project:**

[Paragraph explaining application strategy with specific references to module content]

- **[Specific Application 1]:** [Detailed example referencing widget/framework/case from module]
- **[Specific Application 2]:** [Detailed example with quote or specific technique]
- **[Specific Application 3]:** [Detailed example showing integration]

**Real-World Application:** [One sentence about how professionals use these skills]
```

**Quality Criteria:**
- ✅ **Specific:** References actual module content (widgets used, frameworks taught, cases analyzed)
- ✅ **Actionable:** Clear guidance on HOW to apply learning
- ✅ **Connected:** Ties module learning to capstone deliverable structure
- ❌ **Generic:** "This module helps your final project" (TOO VAGUE)
- ❌ **Disconnected:** No references to actual module elements

---

## SELF-PACED COURSE MODULE TEMPLATES

Use these templates when building self-paced courses with asynchronous individual work only.

**KEY DIFFERENCES FROM COHORT:**
- ❌ NO PAIRR methodology (requires peer feedback)
- ❌ NO peer review activities
- ❌ NO "Anchor Project milestones" (use "Final Project checkpoints")
- ❌ NO fixed deadlines (use "recommended pacing")
- ❌ NO synchronous elements
- ✅ Individual assessments with AI feedback only
- ✅ Checkpoint-based progress tracking

### MODULE 0: Bridge/Hook (Optional)
**Same as cohort template** - No structural changes needed

---

### MODULE 1: Welcome & Learning Outcomes (Self-Paced)
**Purpose:** Set course context and establish learning outcomes

**Required Element Sequence:**

| # | Element Type | Purpose | Content Specs |
|---|--------------|---------|---------------|
| 1 | **Text** | Welcome + course overview | 100-150 words. Pattern: "Welcome to [course]. You'll complete [X] modules at your own pace." |
| 2 | **Infobox (Callout)** | Module overview + estimated time | 75-100 words. State estimated hours, suggest pacing (e.g., "Most students complete this in 2-3 days") |
| 3 | **Text** | Full course learning outcomes (CLO 1-5) | Each CLO needs: "What You'll Master", "Success Criteria", "Why This Matters" |
| 4 | **iFrame Widget** | Learning outcomes visualizer | File: `learning-outcomes-module-1.html` - shows ALL course CLOs |
| 5 | **Text** | Final Project Overview | Explain final project, checkpoints, what students will build |
| 6+ | **Various** | Additional content (optional) | Videos, infoboxes, etc. |
| N-1 | **Text** | 🎯 FINAL PROJECT CONNECTION | See self-paced template below |
| N | **Text** | Module 1 Complete - Transition | Preview Module 2, suggest next steps |

**Changes from Cohort:**
- Element 1: "Welcome to the course" (not "Last week recap")
- Element 2: "Estimated time" (not fixed deadlines)
- Element 5: "Final Project Overview" (not "Anchor Project milestone")
- Remove all deadline language
- Use "recommended pacing" instead of "due dates"

---

### MODULES 2-5: Standard Content Modules (Self-Paced)
**Purpose:** Deliver content with clear learning progression

**Required Element Sequence:** Same as cohort EXCEPT:

| # | Element Type | Purpose | Content Specs |
|---|--------------|---------|---------------|
| 1 | **Text** | Connecting intro | "You've just completed [previous module]. Now you'll [current module]" - use completion language, not time references |
| 2 | **iFrame Widget** | Learning outcomes widget | Same as cohort |
| 3+ | **Various** | Content delivery | Same as cohort - V3 Interactive-First |
| N-1 | **Text** | 🎯 FINAL PROJECT CONNECTION | See self-paced template below |
| N | **Text** | Checkpoint reminder + transition | "Ready to move on? Complete Checkpoint [X] to track your progress" |

**Pacing Language:**
- ✅ "Most students spend 2-3 hours on this module"
- ✅ "Recommended: Complete before moving to Module X"
- ✅ "Checkpoint [X]: Submit your draft when ready"
- ❌ "Due Friday by 11:59 PM"
- ❌ "Week 3 Milestone"
- ❌ "Submit by [date]"

---

### MODULE 6: Assessment (Self-Paced - NO PAIRR)
**Purpose:** Individual summative assessment

**Required Element Sequence:** Same as Modules 2-5 PLUS:

**Individual Assessment with AI Feedback (NO Peer Component):**

```markdown
## Assessment Instructions

### Your Task
[Assignment instructions - memo, analysis, project proposal, etc.]

### AI Feedback Tool (Optional)
Want feedback before final submission? Use this AI feedback prompt:

**Prompt to use in ChatGPT:**
"You are an executive coach reviewing a strategic business memo.
 Evaluate this memo on clarity, strategic thinking, and evidence use.
 Provide specific suggestions for improvement."

**How to Use AI Feedback:**
1. Paste your draft into ChatGPT with the prompt above
2. Review AI suggestions critically
3. Revise based on feedback you find valuable
4. Submit final version when ready

### Rubric
[Standard rubric - no PAIRR bonus structure]

**Total Points:** [X] points
```

**What's DIFFERENT from Cohort:**
- ❌ NO peer review component
- ❌ NO comparative reflection (only one feedback source)
- ❌ NO post-revision reflection comparing peer vs AI
- ❌ NO bonus structure for PAIRR participation
- ✅ AI feedback is OPTIONAL (students choose to use it)
- ✅ Standard rubric (no extra PAIRR bonus points)

**Common Self-Paced Assessment Errors:**
- ❌ Including peer review (impossible without cohort)
- ❌ Including PAIRR methodology
- ❌ Fixed deadlines for submission
- ❌ Required peer feedback exchange

---

### MODULE 7: Wrap-Up & Reflection (Self-Paced)
**Purpose:** Consolidate learning and prepare for next module or final project

**Required Components:**

**1. Course Journey Recap** (if final module) OR **Module Recap** (if mid-course):
```markdown
## Your Progress

You've completed [Module/Course] exploring [topic]. Here's what you've accomplished:

- **Module 1:** [Established learning outcomes]
- **Module 2:** [Learned frameworks]
- **Module 3:** [Applied analysis]
- **Module 4:** [Hands-on practice]
- **Module 5:** [Case study]
- **Module 6:** [Strategic assessment]
- **Module 7:** [Synthesis]
```

**2. Reflection Prompts:**
- Same as cohort (3-5 processing questions)

**3. Final Project Checkpoint Reminder:**
```markdown
## ✅ Checkpoint [X]: Ready for Final Project?

Before moving forward, ensure you've completed:
- [ ] [Checkpoint task 1]
- [ ] [Checkpoint task 2]
- [ ] [Checkpoint task 3]

**How This Module Supports Your Final Project:**
[Paragraph connecting module learning to final project completion]
```

**4. Next Steps:**
- If mid-course: Preview next module
- If final module: Final project submission instructions

**5. Final Project Connection:**
- How to integrate this module's learning
- Specific sections of final project where learning applies

**Changes from Cohort:**
- "Checkpoint [X]" (not "Milestone due [date]")
- "When ready" language (not fixed deadlines)
- Self-directed progress tracking
- Optional vs required pacing

---

### FINAL PROJECT CONNECTION TEMPLATE (Self-Paced)

```markdown
## 🎯 FINAL PROJECT CONNECTION

**How Module [X] Supports Your Final [Project Name]:**

[1-2 sentences connecting module content to final project deliverable]

**What You Learned:**
- [Specific capability 1 from this module]
- [Specific capability 2 from this module]
- [Specific capability 3 from this module]
- [Specific capability 4 from this module]

**How to Apply This to Your Final Project:**

[Paragraph explaining application strategy]

- **[Specific Application 1]:** [Detailed example - "Use the framework from Element 3 in your Section 2.1..."]
- **[Specific Application 2]:** [Detailed example with specific technique]
- **[Specific Application 3]:** [Detailed example showing integration]

**Checkpoint Suggestion:** [Optional guidance - "Consider drafting Section [X] of your final project now while these concepts are fresh"]

**Real-World Application:** [One sentence about professional use]
```

**Changes from Cohort:**
- Remove "Week 5 capstone" language (use "final project")
- Add optional "Checkpoint Suggestion"
- Use self-directed language ("Consider drafting..." not "You must complete...")

---

## KEY DIFFERENCES SUMMARY

| Aspect | Cohort Courses | Self-Paced Courses |
|--------|---------------|-------------------|
| **Assessment (Module 6)** | PAIRR methodology (peer + AI + comparative reflection) | Individual assessment with optional AI feedback only |
| **Bonus Points** | 5-point PAIRR bonus structure | No bonus (standard rubric) |
| **Project Structure** | Anchor Project with weekly milestones | Final Project with flexible checkpoints |
| **Deadlines** | Fixed dates ("Due Friday 11:59 PM") | Recommended pacing ("Most spend 2-3 hours") |
| **Module 1 Element 5** | Anchor Project milestone connection | Final Project overview |
| **Module 7** | Milestone reminder with due date | Checkpoint reminder ("when ready") |
| **Pacing Language** | "Week X", "This week", "Next week" | "Module X", "This module", "Next module" |
| **Peer Activities** | Allowed (peer review, discussions) | NOT allowed (asynchronous individual only) |

---

## COMMON STRUCTURAL ELEMENTS (Both Course Types)

These requirements apply to BOTH cohort and self-paced courses:

### Element Numbering Integrity
- Element table "Order" column must match content section numbers
- No skipped numbers (1, 2, 3... no gaps)
- Element types in table must match content headings

### Learning Outcomes Widgets
- Module 1 Element 4: Shows ALL week/course learning outcomes
- Modules 2-7 Element 2: Shows SUBSET of outcomes practiced in THIS module
- Exception: Self-paced might not have Modules 2-7 if shorter course

### Module Transitions
- Every module ends with transition text
- Pattern: "Module [X] Complete - [transition message]"
- Preview next module topic
- Use encouraging, forward-looking language

### Case Attachment Flags
- When modules include cases, use: `🔗 ATTACH CASE HERE: [Specific file/instructions]`
- Makes attachment points unmistakable for implementation team

### AI Roleplay Specifications
- NO timing references in Hidden Context ("5 questions over 10-15 min" → "5 questions")
- Both course types can use AI Roleplay exercises
- Always third-person format in tabs

### Widget Introduction Format
- All interactive widgets need: Activity header + MLO connection + 100-150 word introduction
- Exception: Learning outcomes widgets (no introduction needed)
- Both course types follow same format

---

## WHEN TO APPLY THESE TEMPLATES

**BUILD MODE:**
1. **Ask user about course format** if not already specified (cohort vs self-paced)
2. **Select appropriate template** based on answer
3. **Follow template structure** when generating module storyboards
4. **Apply course-type-specific language** throughout (deadlines vs checkpoints, PAIRR vs individual)

**AUDIT MODE:**
1. **Detect course format** from content (look for PAIRR, deadlines, Anchor Project = cohort)
2. **Validate against appropriate template**
3. **Flag course-type violations** (e.g., peer review in self-paced course)
4. **Provide course-type-appropriate corrections**

---
