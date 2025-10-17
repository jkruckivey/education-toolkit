---
name: "Accessibility Audit Tools"
description: "Automated WCAG 2.2 AA compliance checking for educational content. Python scripts test color contrast, heading hierarchy, alt text, and ARIA attributes. Agents invoke for fast accessibility validation."
version: "1.0.0"
dependencies: "python>=3.8, beautifulsoup4, lxml"
---

# Accessibility Audit Tools

Executable Python scripts that automate WCAG 2.2 AA accessibility compliance checks for HTML/CSS educational content.

## What This Skill Provides

### 1. Color Contrast Checker
- Tests text/background color combinations against WCAG 2.2 AA standards
- Minimum 4.5:1 for normal text, 3:1 for large text (>24px)
- New WCAG 2.2: Focus appearance 3:1 contrast
- Generates pass/fail report with specific fixes

### 2. Heading Hierarchy Validator
- Checks for proper semantic structure (h1 → h2 → h3, no skips)
- Identifies missing h1 or multiple h1s
- Detects heading level jumps (h2 → h4)
- Provides fix recommendations

### 3. Alt Text Checker
- Scans all `<img>` tags for alt attribute presence
- Identifies decorative images without `alt=""`
- Flags informative images missing alt text
- Checks for placeholder text like "image" or "untitled"

### 4. ARIA Compliance Scanner
- Validates ARIA labels on interactive elements (buttons, links, form inputs)
- Checks landmark regions (header, nav, main, footer)
- Detects missing labels on form inputs
- Identifies improper ARIA usage (decorative elements without `aria-hidden="true"`)

## How Agents Invoke This Skill

Agents use the Skill tool to run Python scripts on HTML/CSS files:

```bash
# Check color contrast for a file
python scripts/check_contrast.py --file module1.html --report json

# Validate heading hierarchy
python scripts/check_headings.py --file module1.html

# Check alt text on all images
python scripts/check_alt_text.py --directory modules/ --recursive

# Run full ARIA compliance scan
python scripts/check_aria.py --file module1.html --verbose
```

## Script Reference

### check_contrast.py
**Purpose**: Validates color contrast ratios against WCAG 2.2 AA standards

**Arguments**:
- `--file` (required): HTML/CSS file to analyze
- `--report` (optional): Output format: text | json | html (default: text)
- `--threshold` (optional): Contrast threshold: AA | AAA (default: AA)
- `--output` (optional): Save report to file

**Output**: List of contrast violations with:
- Element location (line number, selector)
- Current colors (hex codes)
- Current contrast ratio
- Required ratio (4.5:1 or 3:1)
- Suggested fix colors

**WCAG 2.2 Standards**:
- Normal text (<24px): 4.5:1 minimum
- Large text (≥24px): 3:1 minimum
- Focus indicators (2.4.13): 3:1 minimum, 2px perimeter

### check_headings.py
**Purpose**: Validates semantic heading structure

**Arguments**:
- `--file` (required): HTML file to analyze
- `--strict` (optional): Enable strict mode (fails on warnings)

**Output**: Heading structure analysis with:
- Heading outline visualization
- Missing h1 warnings
- Multiple h1 warnings
- Heading level skips (errors)
- Recommendations for fixes

**Common Issues Detected**:
- No h1 on page (accessibility landmark issue)
- Multiple h1s (confuses screen readers)
- Skipped levels (h2 → h4 without h3)
- Heading used for styling only (should use CSS instead)

### check_alt_text.py
**Purpose**: Validates alt text presence and quality on images

**Arguments**:
- `--file` (optional): Single HTML file to analyze
- `--directory` (optional): Directory to scan
- `--recursive` (optional): Scan subdirectories
- `--strict` (optional): Flag decorative images without `alt=""`

**Output**: Image audit report with:
- Total images found
- Images missing alt attribute (FAIL)
- Images with placeholder alt text (WARNING)
- Decorative images without `alt=""` (WARNING in strict mode)
- File and line number for each issue

**Quality Checks**:
- ❌ Missing alt: `<img src="chart.png">` (FAIL)
- ❌ Placeholder alt: `<img src="chart.png" alt="image">` (WARNING)
- ✅ Descriptive alt: `<img src="chart.png" alt="Bar chart showing 40% increase in revenue">` (PASS)
- ✅ Decorative: `<img src="divider.png" alt="">` (PASS)

### check_aria.py
**Purpose**: Validates ARIA attributes and semantic HTML

**Arguments**:
- `--file` (required): HTML file to analyze
- `--verbose` (optional): Include pass results (not just failures)
- `--check` (optional): Specific checks: labels | landmarks | roles | all (default: all)

**Output**: ARIA compliance report with:
- Interactive elements without labels
- Form inputs without associated labels
- Missing landmark regions
- Improper ARIA usage
- Redundant ARIA (semantic HTML preferred)

**Checks Performed**:
- **Labels**: Buttons, links, form inputs have accessible names
- **Landmarks**: Page has header, nav, main, footer regions
- **Roles**: ARIA roles used correctly (not conflicting with HTML5)
- **Decorative**: `aria-hidden="true"` on purely visual elements

## When to Use This Skill

**Accessibility-auditor agent should invoke when**:
- User requests "check accessibility" or "WCAG compliance"
- User uploads HTML/CSS files for review
- User asks about "color contrast" or "screen reader support"
- User needs "accessibility report"

**Other agents should invoke when**:
- Creating new educational content (proactive accessibility check)
- After content edits (regression testing)
- Before publishing/deploying (quality gate)

## Example Invocations

### From accessibility-auditor agent:

```
User: "Check if my module pages meet WCAG 2.2 AA standards"

Agent: I'll run comprehensive accessibility checks on your module pages.

*Invokes Skill tool*:
Skill: accessibility-audit-tools

Commands (run in sequence):
1. python scripts/check_contrast.py --directory modules/ --report html --output contrast-report.html
2. python scripts/check_headings.py --directory modules/ --strict
3. python scripts/check_alt_text.py --directory modules/ --recursive --strict
4. python scripts/check_aria.py --directory modules/ --verbose

*Analyzes results and presents summary to user*
```

```
User: "Is the color contrast on my dashboard sufficient for accessibility?"

Agent: I'll check the color contrast ratios in your dashboard HTML.

*Invokes Skill tool*:
Skill: accessibility-audit-tools
Command: python scripts/check_contrast.py --file dashboard.html --report json

*If violations found*:
Agent: Found 3 contrast violations:
1. Line 45: .sidebar-text (#666666 on #FFFFFF) = 3.2:1 (needs 4.5:1)
   → Suggested fix: Use #595959 or darker
2. [etc.]
```

## Installation & Dependencies

### Required Python Packages
```bash
pip install beautifulsoup4 lxml
```

### Optional Packages (Enhanced Features)
```bash
pip install colorthief  # For auto-detecting colors from screenshots
pip install pillow      # For image analysis
```

## Limitations

**What These Tools CAN Do**:
- Detect missing alt text
- Calculate color contrast ratios
- Validate heading structure
- Check ARIA attribute presence

**What These Tools CANNOT Do**:
- Judge alt text quality (requires human review)
- Test keyboard navigation (requires manual testing)
- Assess screen reader UX (requires assistive tech testing)
- Evaluate content readability (requires human judgment)

**Recommendation**: Use these tools as first-pass automation, then conduct manual accessibility testing with:
- Keyboard-only navigation
- Screen reader testing (NVDA, JAWS, VoiceOver)
- Browser accessibility extensions (axe DevTools, WAVE)

## Additional Resources

See `REFERENCE.md` for:
- Complete WCAG 2.2 AA compliance checklist
- Color contrast calculation methodology
- ARIA best practices guide
- Manual accessibility testing procedures
- Common accessibility issues in educational content
