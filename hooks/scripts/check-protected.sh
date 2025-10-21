#!/bin/bash
# Hook 3: Protected Content Guardian
# Prevents accidental edits to published/production educational content
# Runs: PreToolUse (before Edit or Write operations)

FILE_PATH="$1"

# Skip if no file path provided
if [[ -z "$FILE_PATH" ]]; then
    echo '{"permissionDecision": "allow"}'
    exit 0
fi

# ============================================================================
# DEFAULT PROTECTED PATH PATTERNS
# ============================================================================
PROTECTED_PATTERNS=(
    "published/"
    "production/"
    "final/"
    "released/"
    "student-facing/"
    "graded/"
    "live/"
)

# ============================================================================
# CHECK AGAINST DEFAULT PATTERNS
# ============================================================================
IS_PROTECTED=false
PROTECTED_REASON=""

for pattern in "${PROTECTED_PATTERNS[@]}"; do
    if [[ "$FILE_PATH" == *"$pattern"* ]]; then
        IS_PROTECTED=true
        PROTECTED_REASON="$pattern content (default protection)"
        break
    fi
done

# ============================================================================
# CHECK CUSTOM PROTECTED PATHS FROM CONFIG
# ============================================================================
if [[ -f ".education-toolkit-config.json" ]] && command -v jq &> /dev/null; then
    # Read custom protected paths from config
    while IFS= read -r pattern; do
        # Use bash glob matching
        if [[ "$FILE_PATH" == $pattern ]]; then
            IS_PROTECTED=true
            PROTECTED_REASON="custom protected path (from .education-toolkit-config.json)"
            break
        fi
    done < <(jq -r '.protectedPaths[]? // empty' .education-toolkit-config.json 2>/dev/null)
fi

# ============================================================================
# IF NOT PROTECTED, ALLOW IMMEDIATELY
# ============================================================================
if [[ "$IS_PROTECTED" != "true" ]]; then
    echo '{"permissionDecision": "allow"}'
    exit 0
fi

# ============================================================================
# FILE IS PROTECTED - SHOW WARNING AND REQUEST PERMISSION
# ============================================================================
FILENAME=$(basename "$FILE_PATH")

# Try to get last modified date
if [[ -f "$FILE_PATH" ]]; then
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        LAST_MODIFIED=$(stat -f "%Sm" -t "%Y-%m-%d" "$FILE_PATH" 2>/dev/null || echo "unknown")
    else
        # Linux/Windows Git Bash
        LAST_MODIFIED=$(stat -c "%y" "$FILE_PATH" 2>/dev/null | cut -d' ' -f1 || echo "unknown")
    fi
else
    LAST_MODIFIED="(new file)"
fi

# Build warning message
cat >&2 <<EOF

🛡️  PROTECTED CONTENT WARNING

File: $FILE_PATH
Filename: $FILENAME
Category: $PROTECTED_REASON
Last Modified: $LAST_MODIFIED

⚠️  This file is marked as published or student-facing content.

RISKS OF EDITING AFTER PUBLICATION:
  • Assessment fairness - Students may be graded on different criteria
  • Academic integrity - Changing standards mid-assessment creates confusion
  • Student trust - Unpredictable changes undermine transparency
  • Version control - Published materials should have clear version history

RECOMMENDED WORKFLOW:
  1. Create draft version first (e.g., draft/$FILENAME)
  2. Review changes with stakeholders
  3. Communicate changes to students/faculty before applying
  4. Update published version with clear changelog/version notes
  5. Consider "grandfather clause" for existing student submissions

ALTERNATIVES:
  • Edit draft version: draft/$FILENAME
  • Create new version: ${FILENAME%.md}-v2.md
  • Add errata document: ${FILENAME%.md}-errata.md

This is a safety check to prevent accidental modifications.

EOF

# Output JSON requesting permission
cat <<EOF
{
  "permissionDecision": "ask",
  "systemMessage": "⚠️  Attempting to edit protected published content. Please review the risks above and confirm if you want to proceed."
}
EOF

exit 0
