#!/bin/bash
# Hook 1: Smart Content Validator
# Automatically validates educational content after edits for WCAG/QM compliance
# Runs: PostToolUse (after Edit or Write operations)

FILE_PATH="$1"
TOOL_NAME="$2"

# Skip if no file path provided
if [[ -z "$FILE_PATH" ]]; then
    exit 0
fi

# Skip if file doesn't exist
if [[ ! -f "$FILE_PATH" ]]; then
    exit 0
fi

# Extract file extension and name
EXT="${FILE_PATH##*.}"
FILENAME=$(basename "$FILE_PATH")

# Initialize results
ISSUES_FOUND=0
OUTPUT=""

# ============================================================================
# HTML FILES → WCAG 2.2 AA ACCESSIBILITY CHECKS
# ============================================================================
if [[ "$EXT" == "html" || "$EXT" == "htm" ]]; then
    echo "🔍 Running WCAG 2.2 AA quick checks on $FILENAME..." >&2

    # Quick color contrast check (look for common patterns)
    # Check for inline styles with potentially problematic colors
    LOW_CONTRAST_COUNT=$(grep -ciE 'color:\s*(#999|#aaa|#bbb|#ccc|gray|lightgray)' "$FILE_PATH" 2>/dev/null || echo 0)
    if [[ $LOW_CONTRAST_COUNT -gt 0 ]]; then
        OUTPUT="${OUTPUT}⚠️  Potential color contrast issues detected ($LOW_CONTRAST_COUNT instances)\n"
        OUTPUT="${OUTPUT}   Common low-contrast colors found - verify 4.5:1 ratio minimum\n"
        ISSUES_FOUND=$((ISSUES_FOUND + 1))
    fi

    # Check for images without alt text
    IMG_TOTAL=$(grep -coiE '<img[^>]+>' "$FILE_PATH" 2>/dev/null || echo 0)
    IMG_WITH_ALT=$(grep -coiE '<img[^>]+alt=' "$FILE_PATH" 2>/dev/null || echo 0)
    IMG_MISSING_ALT=$((IMG_TOTAL - IMG_WITH_ALT))

    if [[ $IMG_MISSING_ALT -gt 0 ]]; then
        OUTPUT="${OUTPUT}⚠️  Missing alt text on $IMG_MISSING_ALT image(s)\n"
        OUTPUT="${OUTPUT}   All images need alt=\"description\" or alt=\"\" (if decorative)\n"
        ISSUES_FOUND=$((ISSUES_FOUND + 1))
    elif [[ $IMG_TOTAL -gt 0 ]]; then
        OUTPUT="${OUTPUT}✅ Alt text: All $IMG_TOTAL images have alt attributes\n"
    fi

    # Check for heading hierarchy (h1 should exist, no skips)
    if ! grep -qiE '<h1[^>]*>' "$FILE_PATH" 2>/dev/null; then
        OUTPUT="${OUTPUT}⚠️  No <h1> heading found - pages should have exactly one h1\n"
        ISSUES_FOUND=$((ISSUES_FOUND + 1))
    fi

    # Check for buttons/links without text or aria-label
    EMPTY_BUTTONS=$(grep -oiE '<button[^>]*>(\s|&nbsp;)*</button>' "$FILE_PATH" 2>/dev/null | wc -l || echo 0)
    if [[ $EMPTY_BUTTONS -gt 0 ]]; then
        OUTPUT="${OUTPUT}⚠️  Found $EMPTY_BUTTONS button(s) without text or aria-label\n"
        ISSUES_FOUND=$((ISSUES_FOUND + 1))
    fi

    # Check for tables without proper headers
    TABLE_COUNT=$(grep -ciE '<table[^>]*>' "$FILE_PATH" 2>/dev/null || echo 0)
    TH_COUNT=$(grep -ciE '<th[^>]*>' "$FILE_PATH" 2>/dev/null || echo 0)
    if [[ $TABLE_COUNT -gt 0 ]] && [[ $TH_COUNT -eq 0 ]]; then
        OUTPUT="${OUTPUT}⚠️  Data table(s) found without <th> header cells\n"
        OUTPUT="${OUTPUT}   Use <th scope=\"col\"> or <th scope=\"row\"> for accessibility\n"
        ISSUES_FOUND=$((ISSUES_FOUND + 1))
    fi
fi

# ============================================================================
# MARKDOWN FILES → EDUCATIONAL CONTENT CHECKS
# ============================================================================
if [[ "$EXT" == "md" ]]; then
    echo "🔍 Checking educational content in $FILENAME..." >&2

    # -----------------------------------------------------------------------
    # Check 1: Learning outcomes with measurable language
    # -----------------------------------------------------------------------
    if grep -qiE '(learning outcome|MLO|objective|by the end|students will)' "$FILE_PATH" 2>/dev/null; then
        # Flag vague/unmeasurable language
        VAGUE_PATTERNS='(understand|know|learn about|be familiar|appreciate|be aware|comprehend)'
        VAGUE_COUNT=$(grep -ciE "$VAGUE_PATTERNS" "$FILE_PATH" 2>/dev/null || echo 0)

        if [[ $VAGUE_COUNT -gt 0 ]]; then
            OUTPUT="${OUTPUT}⚠️  Found $VAGUE_COUNT instance(s) of vague learning outcome language\n"
            OUTPUT="${OUTPUT}   Avoid: understand, know, learn about, be familiar, appreciate\n"
            OUTPUT="${OUTPUT}   Use measurable Bloom's verbs: explain, identify, analyze, evaluate, create\n"
            ISSUES_FOUND=$((ISSUES_FOUND + 1))
        else
            OUTPUT="${OUTPUT}✅ Learning outcomes use measurable language\n"
        fi
    fi

    # -----------------------------------------------------------------------
    # Check 2: Rubric point math validation
    # -----------------------------------------------------------------------
    if grep -qiE '\|\s*(points?|pts?|criteria)\s*\|' "$FILE_PATH" 2>/dev/null; then
        # Extract stated total
        TOTAL_STATED=$(grep -oiE 'total:\s*([0-9]+)\s*(points?|pts?)?' "$FILE_PATH" 2>/dev/null | grep -oE '[0-9]+' | head -1)

        if [[ -n "$TOTAL_STATED" ]]; then
            # Sum all point values in tables (simplified - looks for |NUMBER pts|)
            POINT_SUM=0
            while IFS= read -r num; do
                POINT_SUM=$((POINT_SUM + num))
            done < <(grep -oiE '\|\s*([0-9]+)\s*(pts?|points?)\s*\|' "$FILE_PATH" 2>/dev/null | grep -oE '[0-9]+')

            if [[ $POINT_SUM -gt 0 ]] && [[ $POINT_SUM -ne $TOTAL_STATED ]]; then
                OUTPUT="${OUTPUT}⚠️  Rubric math error: Stated total = ${TOTAL_STATED}, criteria sum = ${POINT_SUM}\n"
                OUTPUT="${OUTPUT}   Verify all point allocations add up correctly\n"
                ISSUES_FOUND=$((ISSUES_FOUND + 1))
            elif [[ $POINT_SUM -eq $TOTAL_STATED ]]; then
                OUTPUT="${OUTPUT}✅ Rubric points add up correctly (${TOTAL_STATED} points)\n"
            fi
        fi
    fi

    # -----------------------------------------------------------------------
    # Check 3: Colored emoji in storyboards (should be black symbols)
    # -----------------------------------------------------------------------
    if [[ "$FILENAME" == *"storyboard"* ]] || [[ "$FILENAME" == *"module"* ]]; then
        COLORED_EMOJI_COUNT=0
        COLORED_EMOJI_LIST=""

        # Priority badges (should be black symbols)
        RED_CIRCLE=$(grep -o '🔴' "$FILE_PATH" 2>/dev/null | wc -l || echo 0)
        YELLOW_CIRCLE=$(grep -o '🟡' "$FILE_PATH" 2>/dev/null | wc -l || echo 0)
        GREEN_CIRCLE=$(grep -o '🟢' "$FILE_PATH" 2>/dev/null | wc -l || echo 0)

        # Content icons (should be black symbols)
        TARGET=$(grep -o '🎯' "$FILE_PATH" 2>/dev/null | wc -l || echo 0)
        VIDEO=$(grep -o '📺' "$FILE_PATH" 2>/dev/null | wc -l || echo 0)
        CHART=$(grep -o '📊' "$FILE_PATH" 2>/dev/null | wc -l || echo 0)
        STADIUM=$(grep -o '🏟️' "$FILE_PATH" 2>/dev/null | wc -l || echo 0)
        BULB=$(grep -o '💡' "$FILE_PATH" 2>/dev/null | wc -l || echo 0)
        GAME=$(grep -o '🎮' "$FILE_PATH" 2>/dev/null | wc -l || echo 0)

        COLORED_EMOJI_COUNT=$((RED_CIRCLE + YELLOW_CIRCLE + GREEN_CIRCLE + TARGET + VIDEO + CHART + STADIUM + BULB + GAME))

        if [[ $COLORED_EMOJI_COUNT -gt 0 ]]; then
            OUTPUT="${OUTPUT}⚠️  Found $COLORED_EMOJI_COUNT colored emoji (Uplimit uses black symbols)\n"
            OUTPUT="${OUTPUT}   Replace: 🔴→⬤ 🟡→◐ 🟢→○ 🎯→◉ 📺→▶ 📊→▪ 🏟️→■ 💡→◆ 🎮→▸\n"
            OUTPUT="${OUTPUT}   (Auto-formatter will fix this automatically)\n"
            ISSUES_FOUND=$((ISSUES_FOUND + 1))
        fi
    fi

    # -----------------------------------------------------------------------
    # Check 4: PAIRR components (if mentioned)
    # -----------------------------------------------------------------------
    if grep -qiE 'PAIRR|peer.*AI.*review' "$FILE_PATH" 2>/dev/null; then
        HAS_PEER_REVIEW=$(grep -ciE '(peer review|peer feedback)' "$FILE_PATH" || echo 0)
        HAS_AI_FEEDBACK=$(grep -ciE '(AI feedback|AI review)' "$FILE_PATH" || echo 0)
        HAS_COMPARISON=$(grep -ciE '(comparative reflection|compare.*feedback)' "$FILE_PATH" || echo 0)
        HAS_BONUS=$(grep -ciE '(bonus.*points?|extra.*credit)' "$FILE_PATH" || echo 0)

        MISSING_COMPONENTS=""
        if [[ $HAS_PEER_REVIEW -eq 0 ]]; then MISSING_COMPONENTS="${MISSING_COMPONENTS}peer review, "; fi
        if [[ $HAS_AI_FEEDBACK -eq 0 ]]; then MISSING_COMPONENTS="${MISSING_COMPONENTS}AI feedback, "; fi
        if [[ $HAS_COMPARISON -eq 0 ]]; then MISSING_COMPONENTS="${MISSING_COMPONENTS}comparative reflection, "; fi

        if [[ -n "$MISSING_COMPONENTS" ]]; then
            MISSING_COMPONENTS=${MISSING_COMPONENTS%, }  # Remove trailing comma
            OUTPUT="${OUTPUT}⚠️  PAIRR methodology incomplete - missing: ${MISSING_COMPONENTS}\n"
            OUTPUT="${OUTPUT}   Complete PAIRR requires: peer review + AI feedback + comparative reflection\n"
            ISSUES_FOUND=$((ISSUES_FOUND + 1))
        else
            OUTPUT="${OUTPUT}✅ PAIRR methodology components present\n"
        fi
    fi

    # -----------------------------------------------------------------------
    # Check 5: Accessibility terminology (WCAG version)
    # -----------------------------------------------------------------------
    if grep -qiE 'WCAG' "$FILE_PATH" 2>/dev/null; then
        WCAG_21_COUNT=$(grep -ciE 'WCAG\s*2\.1' "$FILE_PATH" || echo 0)
        if [[ $WCAG_21_COUNT -gt 0 ]]; then
            OUTPUT="${OUTPUT}⚠️  Found reference to WCAG 2.1 (current standard is WCAG 2.2 AA)\n"
            OUTPUT="${OUTPUT}   Update to WCAG 2.2 for latest success criteria\n"
            ISSUES_FOUND=$((ISSUES_FOUND + 1))
        fi
    fi
fi

# ============================================================================
# OUTPUT RESULTS
# ============================================================================
if [[ $ISSUES_FOUND -eq 0 ]]; then
    # Silent success - no output (keeps transcript clean)
    exit 0
else
    echo -e "\n📋 Auto-validation found $ISSUES_FOUND issue(s):\n" >&2
    echo -e "$OUTPUT" >&2
    echo -e "Run /audit-module or /check-consistency for detailed analysis.\n" >&2
    exit 0  # Don't block - just inform
fi
