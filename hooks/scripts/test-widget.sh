#!/bin/bash
# Auto-test widgets after creation/modification
# Runs accessibility tests and optionally opens in browser

FILE_PATH="$1"
TOOL_NAME="$2"

# Only process HTML files in widget directories
if [[ ! "$FILE_PATH" =~ \.html$ ]] || [[ ! "$FILE_PATH" =~ widget ]]; then
    exit 0
fi

# Only process Write operations (new widgets), not Edit
if [[ "$TOOL_NAME" != "Write" ]]; then
    exit 0
fi

echo ""
echo "🧪 AUTO-TESTING NEW WIDGET: $(basename "$FILE_PATH")"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

# Check if webapp-testing skill is available
SKILL_PATH="${HOME}/.claude/skills/webapp-testing/scripts/accessibility_dynamic_test.py"

if [[ -f "$SKILL_PATH" ]]; then
    echo "✓ Running accessibility tests..."

    # Run accessibility tests
    OUTPUT_FILE="${FILE_PATH%.html}_accessibility_results.json"
    python3 "$SKILL_PATH" --file "$FILE_PATH" --output "$OUTPUT_FILE" 2>/dev/null

    if [[ $? -eq 0 ]]; then
        echo "✓ Accessibility test complete: $OUTPUT_FILE"

        # Show quick summary if jq is available
        if command -v jq &> /dev/null && [[ -f "$OUTPUT_FILE" ]]; then
            VIOLATIONS=$(jq -r '.violations | length' "$OUTPUT_FILE" 2>/dev/null)
            if [[ -n "$VIOLATIONS" ]]; then
                echo "  • Found $VIOLATIONS accessibility issue(s)"
            fi
        fi
    else
        echo "⚠ Accessibility test failed (widget may need a server to run)"
    fi
else
    echo "ℹ webapp-testing skill not installed (skipping automated tests)"
    echo "  Install with: npx claude-code-templates@latest --skill=development/webapp-testing --yes"
fi

# Check if user wants to auto-open widgets in browser
if [[ -f "${HOME}/.claude/plugins/education-toolkit/.auto-open-widgets" ]]; then
    echo "✓ Opening widget in browser..."

    # Detect OS and open appropriately
    if [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS
        open "$FILE_PATH"
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Linux
        xdg-open "$FILE_PATH" &>/dev/null &
    elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "cygwin" ]] || [[ "$OSTYPE" == "win32" ]]; then
        # Windows (Git Bash, Cygwin, or native)
        start "$FILE_PATH"
    fi
fi

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

exit 0
