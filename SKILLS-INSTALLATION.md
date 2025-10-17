# Skills Installation Guide

## 🎯 Two Ways to Use Skills

### Option 1: Automatic (Bundled with Plugin) - Recommended

**Skills are automatically included when you install the education-toolkit plugin.**

```bash
# Install plugin (includes all skills)
/plugin marketplace add jameskruck/education-toolkit

# Skills are ready to use immediately!
# No additional installation needed.
```

**What you get:**
- ✅ 3 skills pre-installed
- ✅ Agents invoke skills automatically
- ✅ Zero configuration

---

### Option 2: Manual (Standalone ZIP files)

**If you want to use skills with other plugins or install separately:**

#### Step 1: Download Skill ZIPs

Download from [GitHub Releases](https://github.com/jkruckivey/education-toolkit/releases):
- `assessment-template-generator.zip` (24 KB)
- `accessibility-audit-tools.zip` (9.6 KB)
- `qm-validator.zip` (11 KB)

#### Step 2: Install to Claude Code Skills Directory

**On macOS/Linux:**
```bash
# Unzip to skills directory
unzip assessment-template-generator.zip -d ~/.claude/skills/
unzip accessibility-audit-tools.zip -d ~/.claude/skills/
unzip qm-validator.zip -d ~/.claude/skills/
```

**On Windows:**
```powershell
# Unzip to skills directory
Expand-Archive -Path assessment-template-generator.zip -DestinationPath $env:USERPROFILE\.claude\skills\
Expand-Archive -Path accessibility-audit-tools.zip -DestinationPath $env:USERPROFILE\.claude\skills\
Expand-Archive -Path qm-validator.zip -DestinationPath $env:USERPROFILE\.claude\skills\
```

#### Step 3: Verify Installation

```bash
# List installed skills
ls ~/.claude/skills/

# Should show:
# assessment-template-generator/
# accessibility-audit-tools/
# qm-validator/
```

---

## 📋 Requirements

### Python 3.8+
**Required for skills to work:**

```bash
# Check Python version
python --version  # Should be 3.8 or higher

# If not installed:
# macOS: brew install python3
# Windows: Download from python.org
# Linux: sudo apt install python3
```

### Python Dependencies
**Required for accessibility-audit-tools:**

```bash
pip install beautifulsoup4 lxml
```

**Optional for enhanced features:**
```bash
pip install colorthief pillow
```

---

## 🧪 Testing Skills

### Test PAIRR Generator
```bash
cd ~/.claude/skills/assessment-template-generator/scripts
python generate_pairr.py --assignment-name "Test Memo" --points 30 --criteria "Analysis, Writing"

# Expected output:
# [OK] PAIRR template generated: pairr-test-memo.md
```

### Test Accessibility Checker
```bash
cd ~/.claude/skills/accessibility-audit-tools/scripts
python check_contrast.py --file /path/to/your/file.html

# Expected output:
# WCAG 2.2 AA Color Contrast Report
# [compliance results...]
```

### Test QM Validator
```bash
cd ~/.claude/skills/qm-validator/scripts
python check_rubric_math.py --file /path/to/rubric.md

# Expected output:
# Rubric Math Validation Report
# [validation results...]
```

---

## 🔍 Skill Details

### assessment-template-generator
**Automates PAIRR, AI Roleplay, and Diagnostic Rubric creation**

**Scripts:**
- `generate_pairr.py` - Complete PAIRR assignment templates
- `generate_ai_roleplay.py` - Uplimit AI roleplay configurations
- `generate_diagnostic_rubric.py` - 3-level formative rubrics

**Example Usage:**
```bash
python generate_pairr.py \
  --assignment-name "Marketing Strategy Memo" \
  --points 30 \
  --criteria "Market analysis, Competitive positioning, Creative strategy"
```

### accessibility-audit-tools
**WCAG 2.2 AA automated compliance checking**

**Scripts:**
- `check_contrast.py` - Color contrast validation
- `check_alt_text.py` - Alt text presence and quality

**Example Usage:**
```bash
python check_contrast.py \
  --file module1.html \
  --report html \
  --output contrast-report.html
```

### qm-validator
**Quality Matters standards validation**

**Scripts:**
- `check_alignment.py` - Outcome-criteria alignment checker
- `check_rubric_math.py` - Rubric point validation

**Example Usage:**
```bash
python check_alignment.py \
  --rubric rubric.md \
  --outcomes outcomes.txt \
  --verbose
```

---

## 🤝 Using Skills with Agents

**If you installed via plugin (Option 1):**
- Agents automatically invoke skills when you make relevant requests
- Example: "Create a PAIRR assignment for my memo" → assessment-designer agent invokes skill

**If you installed manually (Option 2):**
- Agents from ANY plugin can invoke your skills
- Skills are available system-wide in `~/.claude/skills/`

---

## ❓ Troubleshooting

### "Python not found" Error
**Solution:** Install Python 3.8+ from python.org or via package manager

### "beautifulsoup4 not found" Error
**Solution:** Run `pip install beautifulsoup4 lxml`

### Skills Not Working with Agents
**Check installation location:**
```bash
# Skills should be here:
ls ~/.claude/skills/assessment-template-generator/Skill.md

# If not found, reinstall using instructions above
```

### Permission Errors on Scripts
**Make scripts executable:**
```bash
chmod +x ~/.claude/skills/*/scripts/*.py
```

---

## 📦 Distribution for Plugin Authors

**Want to bundle these skills in YOUR plugin?**

1. Copy skill directories to your plugin:
   ```bash
   cp -r ~/.claude/skills/assessment-template-generator /path/to/your-plugin/skills/
   ```

2. Skills auto-discovered by Claude Code (no config needed)

3. Your agents can invoke with:
   ```
   Skill: assessment-template-generator
   Command: python scripts/generate_pairr.py [args]
   ```

---

## 📄 License

MIT License - Free to use, modify, and distribute

## 🐛 Issues & Support

**Found a bug or need help?**
- GitHub Issues: https://github.com/jkruckivey/education-toolkit/issues
- Email: jkruck@ivey.ca

---

## 🎓 Learn More

**Full documentation:** [education-toolkit README](https://github.com/jkruckivey/education-toolkit)

**Research foundations:**
- PAIRR: Frontiers in Communication (2025)
- WCAG 2.2 AA: W3C Accessibility Guidelines
- Quality Matters: QM Higher Education Rubric
