# Uplimit Content Design Guide
## Creating Engaging, UDL-Aligned Learning Modules

**Version:** 1.0
**Last Updated:** October 9, 2025
**Purpose:** Guide instructional designers through the process of creating varied, engaging content for Uplimit platform modules

---

## Table of Contents
1. [The Varied Content Delivery Principle](#the-varied-content-delivery-principle)
2. [When to Break Up Long Text Content](#when-to-break-up-long-text-content)
3. [Step-by-Step Process](#step-by-step-process)
4. [Uplimit Element Types](#uplimit-element-types)
5. [Content Planning Template](#content-planning-template)
6. [Best Practices](#best-practices)
7. [Case Study: Week 1 Module 3 Redesign](#case-study-week-1-module-3-redesign)

---

## The Varied Content Delivery Principle

### The Problem
Traditional online courses often present content in **monotonous formats**:
- Single long text documents (3,000+ words)
- 20+ minute continuous reading without breaks
- No visual variation or cognitive rest points
- Limited engagement for different learning styles

### The Solution
**Varied Content Delivery** breaks content into **multiple short elements** using different formats:
- 📝 Short text blocks (2-5 minutes each)
- 🎥 Videos (2-10 minutes)
- 📊 Tables and lists (scannable references)
- 🖼️ Images and diagrams (visual reinforcement)
- 💡 Infoboxes (key insights and callouts)
- 📂 Details accordions (optional depth)

### Key Insight
**Same content, same learning time, much higher engagement.**

Instead of one 20-minute text block, create a **learning journey**:
1. Read brief intro (2 min)
2. Watch overview video (2 min)
3. Scan visual reference (list/table)
4. Read focused deep dive (3-4 min)
5. See highlighted callout (infobox)
6. Continue pattern...

---

## When to Break Up Long Text Content

### Red Flags (Time to Redesign)
✅ Single text document exceeds **1,500 words** (10+ minute reading)
✅ Multiple concepts covered in **one long block** without visual breaks
✅ Students would benefit from **different learning modalities** (visual, auditory)
✅ Content feels **overwhelming** or **monotonous** when reviewing
✅ Complex information could be **simplified with visuals**

### When to Keep Long Text
❌ Content is a **case study narrative** that requires continuous reading
❌ Breaking it up would **disrupt the flow** or story
❌ Document is **intentionally comprehensive** (reference material)
❌ Reading is under **1,000 words** (6-7 minutes) and well-structured

---

## Step-by-Step Process

### Phase 1: Audit Existing Content

**Step 1: Identify the Problem**
- Word count: How long is the text block?
- Reading time: Calculate at ~175 words/minute
- Content coverage: How many distinct concepts are covered?

**Step 2: Map Concepts**
Break content into **logical sections**:
```
Example: "Understanding Revenue Streams" (3,500 words)

Concepts identified:
1. Introduction to 5 revenue streams (200 words)
2. Media rights deep dive (500 words)
3. Ticketing and live events (600 words)
4. Sponsorship partnerships (650 words)
5. Merchandising (300 words)
6. Betting and gaming (300 words)
7. Revenue interdependence (550 words)
```

---

### Phase 2: Design Varied Delivery

**Step 3: Choose Element Types**

For each concept section, ask:
- **Could this be visual?** → Create image/diagram
- **Is this a key insight?** → Use infobox
- **Should students scan this quickly?** → Use list or table
- **Is this optional depth?** → Use details accordion
- **Would narration help?** → Create video
- **Is this essential reading?** → Keep as short text (500-650 words max)

**Step 4: Plan the Learning Journey**

Create a **flow** that alternates formats every 2-4 elements:

| Order | Element Type | Content | Time |
|-------|-------------|---------|------|
| 1 | Text | Brief introduction | 2 min |
| 2 | Video | Overview concept | 2 min |
| 3 | List | Scannable reference | 1 min |
| 4 | Table | Comparison matrix | 1 min |
| 5 | Text | Deep dive #1 | 3-4 min |
| 6 | Infobox | Key insight | 1 min |
| 7 | Text | Deep dive #2 | 4-5 min |
| 8 | Image | Visual model | 2 min |
| 9 | Text | Deep dive #3 | 4-5 min |
| 10 | Details | Optional depth | Optional |
| 11 | Text | Synthesis/conclusion | 3-4 min |

**Total:** ~20 minutes (same as original), but with **visual breaks** and **varied engagement**

---

### Phase 3: Create Content

**Step 5: Write Short Text Files**

✅ **Do:**
- Keep each text block to **200-650 words**
- Focus on **one concept** per text element
- Use clear **headings and structure**
- Write in **markdown format** (.md files)
- Include **3-5 minute reading time** estimate

❌ **Don't:**
- Exceed 700 words in a single text element
- Cover multiple unrelated concepts in one block
- Write without visual breaks nearby

**Example Text File Structure:**
```markdown
# Sponsorship and Partnerships: Brand Alignment

Corporate sponsorship represents **15-25% of revenue** for most professional
teams, with higher percentages in markets with deep-pocketed corporations...

## Naming Rights: Geographic Brand Ownership

Stadium and arena naming rights are the most visible (and valuable)
sponsorship deals:

**Major Market Examples:**
- **Scotiabank Arena** (Toronto Maple Leafs/Raptors): ~$800 million...

[Continue for 650 words total]

---

**Word Count:** ~650 words
**Reading Time:** 4-5 minutes
**Usage:** Week 1 Module 3 - Sponsorship section
```

---

**Step 6: Design Visual Elements**

For **images and diagrams**, create specifications:

```markdown
### Image - Premium Seating Breakdown
**File:** `premium-seating-breakdown.png`
**Alt Text:** "Stadium seating diagram showing luxury suites, club seats,
and general admission with corresponding revenue percentages. Premium
seating (10-15% of capacity) generates 40-50% of total ticketing revenue."
**Caption:** "Premium Seating Economics: 10-15% of Capacity Generates
40-50% of Revenue"
**Size:** Optimized for web, max 800px width

**Visual to Create:**
- Stadium cross-section with three seating tiers
- Each tier labeled with:
  - % of total capacity
  - Average price per seat/season
  - % of total ticketing revenue
- Visual emphasis on premium tier generating disproportionate revenue
```

---

**Step 7: Write Infobox and Callout Content**

Use **infoboxes** to highlight critical insights:

✅ **Yellow Variant (Note):** Key concepts, critical definitions
✅ **Purple Variant (Insight):** Data highlights, statistics, "aha moments"
✅ **Blue Variant (Callout):** Instructions, learning objectives

**Example:**
```markdown
### Infobox (Note) - Appointment Viewing Insight
```
Title: Key Insight: "Appointment Viewing" in an On-Demand World 📺

Sports are the last true appointment viewing. You can't watch a game
"later" without risking spoilers from social media, friends, or news
alerts. This creates:

• Predictable, simultaneous audience (rare in 2024)
• Premium advertising rates (live = engaged = valuable)
• Subscription retention power (can't cancel during season)
• Cultural currency ("Did you see that play?")
```
```

---

**Step 8: Create Lists and Tables**

**Vertical Lists:** Use for **scannable summaries**
```markdown
**Item 1 - Title:** "Media Rights"
**Item 1 - Description:** "Broadcasting and streaming deals. Typically
40-60% of total revenue for major leagues. Predictable, long-term
contracts. Risk: Cord-cutting and audience fragmentation."
```

**Tables:** Use for **comparisons**
```markdown
| Revenue Stream | Typical % | Growth Trend | Risk Level |
|---------------|-----------|--------------|------------|
| Media Rights  | 40-60%    | Moderate     | Medium     |
| Ticketing     | 20-30%    | Stable       | Medium     |
```

---

**Step 9: Design Optional Depth (Details Accordions)**

Use **details accordions** for content that:
- Provides deeper understanding but isn't essential
- Would overwhelm some students if required
- Appeals to advanced learners

**Example:**
```markdown
### Details - Sponsorship ROI Measurement
```
Title: How Sponsors Measure Success

[Expand for deeper understanding of sponsorship evaluation]

Sophisticated sponsors don't just count logo impressions. They measure
three categories:

**1. Brand Awareness Metrics**
- Aided/unaided brand recall surveys
- Social media mentions and reach
[Continue with 200 words of optional depth]
```
```

---

### Phase 4: Update Storyboard Documentation

**Step 10: Document in Storyboard**

Update your `uplimit-weekX-storyboard.md` file with complete specifications:

```markdown
## MODULE 3: Core Reading & Revenue Stream Framework - UPDATED
**Purpose:** Provide foundational knowledge with VARIED delivery methods

| Order | Element | Content/Purpose | Source | Implementation Notes |
|-------|---------|----------------|--------|---------------------|
| 1 | **Text** 🔴 | Brief intro (200 words) | Import `intro.md` | Sets up concept |
| 2 | **Video** 🔴 | Overview (2 min) | Upload `video.mp4` | Visual intro |
| 3 | **List** 🔴 | Scannable reference | Type directly | Quick scan |
| 4 | **Table** 🔴 | Comparison matrix | Type directly | Analysis tool |
| 5 | **Text** 🔴 | Deep dive (500 words) | Import `deep-dive.md` | Focused reading |
| 6 | **Infobox** 🔴 | Key insight | Type directly | Highlight concept |
[Continue...]

**Content Summary:**
- Total text: ~2,600 words in 6 short readings (2-5 min each)
- Total video: 2 minutes
- Total time: ~20 minutes (same as original)

**Design Rationale:**
- Multiple means of representation (text, video, visual)
- Visual breaks every 2-4 elements
- Optional progressive disclosure
- No single element over 5 minutes
```

---

## Uplimit Element Types

### Text Elements
**Purpose:** Core reading content
**Best For:** Explanations, narratives, detailed information
**Length:** 200-650 words (2-5 minutes)
**Format:** Markdown (.md) files, import to Uplimit

**Priority Levels:**
- 🔴 **Required** - Essential content for learning outcomes
- 🟡 **Recommended** - Important but not critical
- 🟢 **Optional** - Supplemental depth

---

### Video Elements
**Purpose:** Visual/auditory learning, expert delivery
**Best For:** Overviews, complex concepts, expert interviews
**Length:** 2-10 minutes (2-min ideal for concept explainers)
**Format:** MP4 + VTT transcript (required for accessibility)

**Types:**
- **Instructional videos:** Narrated with animation (concept explainers)
- **Executive videos:** SME-led interviews (90 minutes)

---

### Visual Elements

**Tables**
- **Purpose:** Comparisons, structured data
- **Best For:** Side-by-side analysis, financial data
- **Format:** Type directly in Uplimit, markdown syntax

**Vertical Lists**
- **Purpose:** Scannable summaries, key points
- **Best For:** Quick reference, enumerated concepts
- **Format:** Numbered items with titles and descriptions

**Images**
- **Purpose:** Visual models, diagrams, infographics
- **Best For:** Complex processes, relationships, data visualization
- **Format:** PNG/JPG, optimized for web (max 800px), with alt text

---

### Interactive Elements

**Infoboxes**
- **Yellow (Note):** Key concepts, definitions
- **Purple (Insight):** Data highlights, statistics
- **Blue (Callout):** Instructions, activity setup
- **Format:** Type directly, supports markdown formatting

**Details Accordions**
- **Purpose:** Optional depth, progressive disclosure
- **Best For:** Advanced content, case studies, examples
- **Collapsed by default:** Students expand if interested

**iFrame Widgets**
- **Purpose:** Interactive simulations, tools
- **Best For:** Active learning, practice, exploration
- **Format:** Hosted HTML files, embedded via URL

**AI Chat Widgets**
- **Purpose:** On-demand support, Q&A, scaffolding
- **Best For:** Help during activities, concept clarification
- **Format:** Configure with system prompts in Uplimit

---

## Content Planning Template

Use this template when redesigning a module:

```markdown
# Module X Redesign Plan

## Original Content Analysis
- **Current format:** Single text document
- **Word count:** 3,500 words
- **Reading time:** 20+ minutes
- **Concepts covered:** 7 distinct topics
- **Problem:** Monotonous, text-heavy, low engagement

---

## Redesigned Structure

### Element Breakdown
| Order | Type | Content | Time | Source |
|-------|------|---------|------|--------|
| 1 | Text | Introduction | 2 min | intro.md |
| 2 | Video | Overview | 2 min | video1.mp4 |
| 3 | List | Reference | 1 min | Type direct |
| 4 | Table | Comparison | 1 min | Type direct |
| 5 | Text | Deep dive 1 | 3-4 min | topic1.md |
| 6 | Infobox | Key insight | 1 min | Type direct |
| 7 | Text | Deep dive 2 | 4-5 min | topic2.md |
| 8 | Image | Diagram | 2 min | diagram.png |
| 9 | Text | Deep dive 3 | 4-5 min | topic3.md |
| 10 | Details | Optional | Optional | Type direct |
| 11 | Text | Synthesis | 3-4 min | synthesis.md |

**Total Time:** ~20 minutes (same as original)
**Total Elements:** 11 (varied formats)

---

## Content to Create

### Text Files (Markdown)
- [ ] intro.md (200 words)
- [ ] topic1.md (500 words)
- [ ] topic2.md (600 words)
- [ ] topic3.md (650 words)
- [ ] synthesis.md (550 words)

### Videos
- [ ] video1.mp4 (2 min) - Script already written
- [ ] video1.vtt (captions)

### Visual Assets
- [ ] diagram.png (800x600px) - Specification written

### Direct Entry Content
- [ ] Vertical list (5 items)
- [ ] Table (5 rows)
- [ ] Infobox content (yellow variant)
- [ ] Details accordion content (200 words)

---

## UDL Principles Applied
- ✅ Multiple means of representation (text, video, visual)
- ✅ Strategic emphasis (infoboxes at key moments)
- ✅ Optional depth (details accordion)
- ✅ Digestible chunks (no element over 5 min)

---

## Student Experience Flow
1. Read brief intro (2 min) → Context established
2. Watch video (2 min) → Visual/auditory reinforcement
3. Scan list/table (2 min) → Quick reference created
4. Read deep dive (3-4 min) → Focused learning
5. See infobox callout (1 min) → Key insight highlighted
6. Continue pattern... → Sustained engagement

**Expected Impact:** Higher retention, reduced cognitive load,
better accommodation of diverse learning preferences
```

---

## Best Practices

### DO ✅
- **Break long text into 200-650 word chunks** (2-5 minutes each)
- **Alternate delivery formats** every 2-4 elements
- **Use infoboxes to highlight** critical concepts
- **Provide visual breaks** (images, tables, lists)
- **Offer optional depth** (details accordions)
- **Maintain same total learning time** as original
- **Create detailed specifications** for all visual assets
- **Write in markdown** for version control
- **Include reading time estimates** for all text elements

### DON'T ❌
- **Exceed 700 words** in a single text element
- **Place similar elements consecutively** (3 text blocks in a row)
- **Create videos over 10 minutes** without chunking
- **Forget alt text** for images
- **Skip content specifications** in storyboards
- **Mix unrelated concepts** in one element
- **Rely solely on one format** (all text or all video)

---

### Accessibility Checklist

Every element must meet WCAG 2.2 AA:
- [ ] **Videos have VTT captions** (required)
- [ ] **Images have descriptive alt text** (describe content, not "image of...")
- [ ] **Color contrast meets 4.5:1 ratio** (text on background)
- [ ] **Content is keyboard navigable** (no mouse-only interactions)
- [ ] **Headings use proper hierarchy** (H1 > H2 > H3, no skips)
- [ ] **Tables have proper headers** (`<th>` elements with scope)
- [ ] **Links are descriptive** (not "click here")

---

## Case Study: Week 1 Module 3 Redesign

### The Challenge
Module 3 originally had a **single 3,500-word text document** covering all 5 revenue streams. Reading time: 20+ minutes continuous.

**Student feedback (simulated personas):**
- **Sarah (Visual Learner):** "Text-heavy, no visual scaffolding" - 72/100 score
- **Marcus (Analytical Thinker):** "Need tables and structured comparisons" - 85/100
- **Priya (Collaborative):** "Felt isolated, no interaction" - 68/100

---

### The Solution
Broke content into **14 varied elements**:

| Order | Element | Content | Time | Format |
|-------|---------|---------|------|--------|
| 1 | Text | Brief intro | 2 min | intro.md |
| 2 | Video | 5 streams overview | 2 min | video.mp4 |
| 3 | Vertical List | 5 streams at a glance | 1 min | Type direct |
| 4 | Table | Comparison matrix | 1 min | Type direct |
| 5 | Text | Media rights deep dive | 3-4 min | media-rights.md |
| 6 | Infobox | Appointment viewing | 1 min | Type direct |
| 7 | Text | Ticketing deep dive | 4-5 min | ticketing.md |
| 8 | Image | Premium seating diagram | 2 min | seating.png |
| 9 | Text | Sponsorship deep dive | 4-5 min | sponsorship.md |
| 10 | Details | ROI measurement | Optional | Type direct |
| 11 | Text | Merchandising/betting | 4-5 min | merch-betting.md |
| 12 | Infobox | Betting growth stats | 1 min | Type direct |
| 13 | Text | Revenue interdependence | 3-4 min | interdependence.md |
| 14 | Image | Ecosystem diagram | 2 min | ecosystem.png |

**Total Time:** ~20 minutes (same as original)
**Elements Created:** 6 text files, 1 video, 2 images, 2 infoboxes, 1 list, 1 table, 1 details

---

### The Results

**UDL Principles Applied:**
- ✅ Multiple means of representation (text, video, visual, interactive)
- ✅ Strategic use of emphasis (infoboxes highlight key moments)
- ✅ Optional progressive disclosure (details accordion for interested students)
- ✅ Digestible chunks (no element exceeds 5 minutes)

**Student Experience Improvements:**
- **Visual breaks every 2-4 elements** prevent cognitive overload
- **Different delivery modes** maintain attention and engagement
- **Same total learning time** but much higher retention expected
- **Scaffolded progression:** intro → visual overview → focused deep dives → synthesis

**Expected Impact:**
- **Sarah (Visual Learner):** 72/100 → 85/100 target (visual content addresses needs)
- **Marcus (Analytical Thinker):** Already high, now has tables/comparisons
- **Priya (Collaborative):** 68/100 → 82/100 target (discussion prompts added separately)

---

### Files Created

**Text Content (`modules/text-content/`):**
```
week1-revenue-intro.md (200 words, 2 min)
week1-media-rights-deep-dive.md (500 words, 3-4 min)
week1-ticketing-deep-dive.md (600 words, 4-5 min)
week1-sponsorship-deep-dive.md (650 words, 4-5 min)
week1-merchandising-betting-deep-dive.md (600 words, 4-5 min)
week1-revenue-interdependence.md (550 words, 3-4 min)
```

**Storyboard Updated:**
- `modules/uplimit-week1-storyboard.md` - Module 3 section replaced (lines 206-332)
- Complete specifications for all 14 elements
- Design rationale documented
- Student experience flow mapped

---

## Next Steps After Redesign

### 1. Production Tasks
- [ ] Create video (if not already recorded)
- [ ] Design images/diagrams (Canva or professional designer)
- [ ] Write infobox content (type directly in Uplimit)
- [ ] Create list and table content (markdown format)
- [ ] Write details accordion content (optional depth)

### 2. Uplimit Implementation
- [ ] Import text .md files to Uplimit Text elements
- [ ] Upload video + VTT captions
- [ ] Upload images with alt text
- [ ] Type infobox content directly
- [ ] Type list and table content directly
- [ ] Configure details accordions
- [ ] Set priority badges (🔴 Required, 🟡 Recommended, 🟢 Optional)

### 3. Quality Assurance
- [ ] Review module as student (complete walkthrough)
- [ ] Test accessibility (WAVE, keyboard navigation)
- [ ] Check reading time estimates (175 words/min)
- [ ] Verify learning outcomes alignment
- [ ] Get peer review feedback
- [ ] Make final revisions

---

## Conclusion

Varied content delivery transforms monotonous text-heavy modules into **engaging learning journeys** that:
- Accommodate diverse learning preferences (UDL)
- Maintain attention with visual breaks
- Highlight critical concepts strategically
- Provide optional depth for advanced learners
- Maintain same total learning time but with **much higher retention**

**Key Takeaway:** It's not about adding more content or making modules longer. It's about **delivering the same content in varied, engaging ways** that respect how humans actually learn.

---

**Questions? Need help redesigning a module?**
Refer to this guide and the Week 1 Module 3 case study in `modules/uplimit-week1-storyboard.md` for a complete worked example.
