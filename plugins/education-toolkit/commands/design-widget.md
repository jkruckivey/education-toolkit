---
description: Generate new interactive widgets with standardized design system OR audit existing widgets for compliance
---

You are creating or auditing interactive educational widgets.

Use the **widget-designer** agent to generate new widgets with standardized design system OR audit existing widgets for design consistency.

## What This Command Does

The widget-designer agent operates in two modes:

### GENERATE Mode (Default)
Creates new interactive widgets from scratch with:
- **Geist font family** (400, 500, 600, 700 weights)
- **Neutral gray color palette** (CSS variables, no hardcoded hex)
- **NO EMOJIS policy** (use text labels or symbols like → • ▼)
- **Standardized button patterns** (neutral-900 active, neutral-700 completed, neutral-100 default)
- **Built-in accessibility** (ARIA labels, keyboard nav, focus states)
- **PDF export format** (using jsPDF, not JSON)

### AUDIT Mode
Validates existing widgets for design system compliance:
- Color system (flags hardcoded hex colors)
- Typography (Geist font loaded?)
- Button patterns (match standard states?)
- Spacing (8px scale?)
- Border-radius (8px containers, 4px small elements?)
- Accessibility (ARIA, keyboard nav, lang attribute?)
- Emoji violations (flags all instances)

## When to Use This Command

### Generate New Widgets
- Creating quiz interactions
- Building decision simulators
- Designing concept maps
- Developing calculation tools
- Creating progress trackers

### Audit Existing Widgets
- Before launching course (design system compliance check)
- After designer handoff (validate implementation)
- Bulk widget cleanup (standardize legacy widgets)
- Pre-production QA (catch visual inconsistencies)

## Example Usage

### Generate Mode
```
/design-widget
/design-widget quiz "Revenue Models"
/design-widget simulator "Sponsorship Valuation Calculator"
/design-widget decision-tree "Marketing Mix Selection"
/design-widget concept-map "Fan Engagement Ecosystem"
```

### Audit Mode
```
/design-widget audit week2/widgets/revenue-quiz.html
/design-widget audit modules/week3/widgets/*.html
```

## Expected Output

### GENERATE Mode Output

The agent will ask clarifying questions:
1. **Widget Type**: Quiz, simulator, decision tree, concept map, progress tracker, other?
2. **Interactivity**: What actions can students take? (click, drag, input, calculate?)
3. **Primary Color**: Stick with neutral gray or need accent color? (avoid gold/green)
4. **Data Structure**: What data needs to be tracked? (score, selections, calculations?)
5. **Features**: Need PDF export? Feedback messages? Progress saving?

Then generates:
- Complete HTML file with inline CSS and JavaScript
- Geist font loaded from CDN
- CSS variables for all colors (no hardcoded hex)
- ARIA labels and keyboard navigation
- Focus states (2px solid #3182ce)
- Screen reader support
- Responsive design (mobile-friendly)
- PDF export functionality (if requested)

**Pre-flight Checklist (Automated):**
- ✅ All colors use CSS variables
- ✅ No emojis in UI
- ✅ Focus states present
- ✅ Keyboard navigation works
- ✅ Responsive breakpoints set

---

### AUDIT Mode Output

The agent generates a compliance report:

### Overall Score: 75/100

**Color System: 60/100**
- ❌ Line 45: Hardcoded `#3b82f6` → Should use `var(--color-info)`
- ❌ Line 67: Hardcoded `#22c55e` → Should use `var(--color-success)`
- ❌ Line 89: Hardcoded `#171717` → Should use `var(--color-neutral-900)`
- ✅ Line 120: Correctly uses `var(--color-primary)`

**Typography: 90/100**
- ✅ Geist font loaded via CDN
- ✅ Font weights used: 400, 500, 600
- ⚠️ Line 234: Font size 0.9rem not in standard scale (use 0.875rem)

**Buttons: 80/100**
- ✅ Active state: neutral-900 (correct)
- ❌ Line 156: Completed state uses green (#22c55e) → Should use neutral-700
- ✅ Default state: neutral-100 (correct)

**Accessibility: 70/100**
- ✅ ARIA labels present on buttons
- ✅ Keyboard navigation works (Enter/Space)
- ❌ Line 12: Missing `lang="en"` attribute on `<html>`
- ❌ Line 78: Focus indicator has 1px border (should be 2px solid #3182ce)

**Emoji Violations: FAIL**
- ❌ Line 201: "🎯 Correct!" → Change to "✓ Correct!" or "Correct"
- ❌ Line 215: "🔴 Try again" → Change to "✗ Try again" or "Incorrect"

**Spacing: 100/100**
- ✅ All spacing uses 8px scale

**Border-Radius: 100/100**
- ✅ Containers: 8px
- ✅ Small elements: 4px

---

### Quick Fixes Offered

**Option 1: Auto-fix** (Agent applies all fixes automatically)
- Replace 3 hardcoded colors with CSS variables
- Remove 2 emojis
- Add lang attribute
- Fix focus indicator
- Adjust button completed state

**Option 2: Manual fix guide** (Line-by-line instructions)

**Option 3: Partial fixes** (Fix critical issues only, leave warnings)

---

## Design System Standards

The agent enforces these standards:

### Color System
```css
--color-neutral-50: #fafafa;
--color-neutral-100: #f5f5f5;
--color-neutral-200: #e5e5e5;
--color-neutral-300: #d4d4d4;
--color-neutral-400: #a3a3a3;
--color-neutral-500: #737373;
--color-neutral-600: #525252;
--color-neutral-700: #404040;
--color-neutral-800: #262626;
--color-neutral-900: #171717;

--color-success: #22c55e;
--color-error: #ef4444;
--color-warning: #f59e0b;
--color-info: #3b82f6;
```

### Typography Scale
- h1: 1.8rem
- h2: 1.5rem
- h3: 1.2rem
- body: 1rem
- labels: 0.875rem

### Button States
- **Active**: `background: var(--color-neutral-900); color: white;`
- **Completed**: `background: var(--color-neutral-700); color: white;`
- **Default**: `background: var(--color-neutral-100); color: var(--color-neutral-900);`

### Spacing Scale
- `--spacing-1: 8px`
- `--spacing-2: 16px`
- `--spacing-3: 24px`
- `--spacing-4: 32px`

### NO EMOJIS Policy
Use these instead:
- ✓ or "Correct" (not 🎯)
- ✗ or "Incorrect" (not ❌ 🔴)
- → (not 👉)
- • (not 🔘)
- ▼ (not ⬇️)

---

## Common Widget Types

### Quiz Widget
- Multiple choice or true/false
- Instant feedback
- Score tracking
- Progress indicator
- PDF export of results

### Simulator Widget
- Sliders or input fields
- Real-time calculations
- Visual charts (Chart.js)
- Scenario comparison
- Export results

### Decision Tree Widget
- Branching logic
- Path visualization
- Outcome display
- Retry functionality

### Concept Map Widget
- Interactive nodes
- Connection visualization
- Hover definitions
- Zoom/pan controls

---

## Automatic Testing

After generation, the widget-tester hook automatically:
- Tests keyboard navigation
- Checks focus indicators
- Validates ARIA labels
- Tests screen reader compatibility
- Generates accessibility report

---

## Widget Introduction Format

When embedding widgets in storyboards, use standardized introduction:

```markdown
### ⚙ Interactive Activity: [Widget Name]

**Practice: MLO X.X ([brief description])**

[100-150 word contextual introduction with:]
- Readiness statement ("You're now ready to...")
- What they'll do (specific interaction description)
- Why it matters (real-world relevance/industry connection)
- What they'll gain (learning outcome and application)

<iframe src="week2/widgets/revenue-quiz.html" width="100%" height="600px"></iframe>
```

---

**When to Use This Command:**

**GENERATE:**
1. Starting new widget from scratch
2. Need standardized design system applied
3. Want accessibility built-in from start

**AUDIT:**
1. Before launching course (compliance check)
2. After designer handoff (validate implementation)
3. Bulk widget cleanup (standardize visual consistency)

**Workflow Position:**
- Run AFTER storyboards identify widget needs
- Run BEFORE `/test-widget` (test UX after design compliance)
- Run WITH `/audit-module` (accessibility deep-dive)
