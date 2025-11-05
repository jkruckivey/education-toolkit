# Hooks Windows Compatibility

## Issue

On Windows, the Education Toolkit hooks were failing with:
```
Plugin hook error: 'bash' is not recognized as an internal or external command
```

## Solution Applied (Commit XXXXX)

### Changes Made to `hooks/hooks.json`:

1. **Changed `bash` to `sh`**:
   - Git for Windows includes `sh.exe` in PATH by default
   - More portable than requiring `bash` specifically

2. **Changed `python3` to `python`**:
   - Windows Python installs typically provide `python` not `python3`

3. **Added `"continueOnError": true`** to all hooks:
   - Hooks fail gracefully if shell isn't available
   - Claude Code starts normally even if hooks can't run
   - User sees error message but can continue working

4. **Removed timestamp logging hook**:
   - Used Unix-specific `date` command
   - Not essential for core functionality

## Windows Requirements

### For Hooks to Work (Optional)

Hooks provide automatic quality checks but are **not required** for the plugin to function. If you want hooks to work on Windows:

**Option 1: Install Git for Windows (Recommended)**
```
https://git-scm.com/download/win
```
- Includes `sh.exe` in PATH automatically
- Most Windows developers already have this installed
- ✅ Hooks will work after installation

**Option 2: Install Python** (For format-storyboard hook only)
```
https://www.python.org/downloads/
```
- Make sure to check "Add Python to PATH" during installation
- ✅ Python-based hooks will work

**Option 3: Use Windows Subsystem for Linux (WSL)**
```
wsl --install
```
- Full Linux environment in Windows
- ✅ All hooks will work

### What Happens If Requirements Not Met

With `continueOnError: true`, hooks that fail will:
- ✅ Show a brief error message
- ✅ Let Claude Code continue normally
- ✅ Don't block plugin functionality
- ✅ Other hooks (that work) still run

**Core plugin features work WITHOUT hooks**:
- ✅ All 17 agents work
- ✅ All 14 slash commands work
- ✅ All 3 skills work
- ❌ Automatic quality checks (hooks) won't run

## What Each Hook Does

### 1. validate-content.sh (PostToolUse)
- **Purpose**: Auto-validates HTML for WCAG 2.2 AA, checks Bloom's verbs in markdown
- **Requires**: `sh` (Git for Windows)
- **Impact if missing**: No automatic accessibility/pedagogy validation

### 2. format-storyboard.py (PostToolUse)
- **Purpose**: Auto-formats storyboards (converts colored emoji → black symbols)
- **Requires**: `python`
- **Impact if missing**: Manual emoji conversion needed

### 3. test-widget.sh (PostToolUse)
- **Purpose**: Auto-tests widgets after creation (accessibility checks)
- **Requires**: `sh` (Git for Windows)
- **Impact if missing**: Manual widget testing needed

### 4. check-protected.sh (PreToolUse)
- **Purpose**: Warns before editing published/production content
- **Requires**: `sh` (Git for Windows)
- **Impact if missing**: No warnings for protected content edits

### 5. load-context.sh (SessionStart)
- **Purpose**: Displays educational standards and available commands at startup
- **Requires**: `sh` (Git for Windows)
- **Impact if missing**: No startup context message (not critical)

## Testing Your Setup

### Check if sh is available:
```bash
# Windows Command Prompt:
where sh

# Expected output if Git for Windows installed:
C:\Program Files\Git\usr\bin\sh.exe
```

### Check if Python is available:
```bash
# Windows Command Prompt:
python --version

# Expected output:
Python 3.x.x
```

### Test a Hook Manually:
```bash
# From plugin directory:
cd %USERPROFILE%\.claude\plugins\education-toolkit\hooks\scripts

# Test context loader:
sh load-context.sh

# Expected output: JSON with educational standards info
```

## Disabling Hooks Completely (Optional)

If you don't want hooks at all, create empty hooks.json:

```json
{
  "hooks": {}
}
```

Or rename the file:
```bash
cd %USERPROFILE%\.claude\plugins\education-toolkit\hooks
ren hooks.json hooks.json.disabled
```

## Troubleshooting

### "sh is not recognized"
- **Solution**: Install Git for Windows
- **Alternative**: Disable hooks (see above)

### "python is not recognized"
- **Solution**: Install Python and add to PATH
- **Alternative**: Only Python hook (format-storyboard.py) will fail, others work fine

### Hooks run but show warnings
- **Normal behavior**: Some hooks check for specific conditions (educational project, protected paths)
- **No action needed** if plugins and agents work

### Claude Code starts slowly after installing plugin
- **Cause**: SessionStart hook runs on startup (load-context.sh)
- **Impact**: ~1-3 second delay (one-time per session)
- **Solution if annoying**: Disable SessionStart hook only:
  - Edit `hooks/hooks.json`
  - Remove the entire `"SessionStart": [...]` section

## Summary

**TL;DR**:
- Install **Git for Windows** → hooks work
- Don't want to install? → hooks fail gracefully, plugin still works
- Only want Python hook? → Install **Python** only

The hooks enhance the plugin but aren't required for core functionality (agents, commands, skills).
