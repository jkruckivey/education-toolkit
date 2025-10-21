#!/bin/bash
# Hook 2: Educational Context Loader
# Automatically loads educational standards and course context at session start
# Runs: SessionStart

# Check if we're in an educational project
IS_EDUCATIONAL=false

# Indicators of educational project
if [[ -f "CLAUDE.md" ]] || [[ -d "modules" ]] || [[ -d "storyboards" ]] || [[ -d "assessments" ]] || [[ -f ".education-toolkit-config.json" ]]; then
    IS_EDUCATIONAL=true
fi

# If not educational project, exit silently
if [[ "$IS_EDUCATIONAL" != "true" ]]; then
    exit 0
fi

# Build context message
CONTEXT="📚 **Education Toolkit Active**\n\n"

# ============================================================================
# EDUCATIONAL STANDARDS (Always loaded)
# ============================================================================
CONTEXT+="**Active Standards:**\n"
CONTEXT+="- WCAG: 2.2 Level AA (current as of 2023)\n"
CONTEXT+="- Quality Matters: 6th Edition (2024)\n"
CONTEXT+="- Bloom's Taxonomy: Revised version (Anderson & Krathwohl, 2001)\n"
CONTEXT+="- UDL: CAST Guidelines 3.0\n\n"

# ============================================================================
# COURSE-SPECIFIC CONFIGURATION (If exists)
# ============================================================================
if [[ -f ".education-toolkit-config.json" ]]; then
    # Check if jq is available for JSON parsing
    if command -v jq &> /dev/null; then
        COURSE_NAME=$(jq -r '.courseName // ""' .education-toolkit-config.json 2>/dev/null)
        INSTITUTION=$(jq -r '.institution // ""' .education-toolkit-config.json 2>/dev/null)
        PLATFORM=$(jq -r '.platform // ""' .education-toolkit-config.json 2>/dev/null)
        OUTCOME_PREFIX=$(jq -r '.conventions.learningOutcomePrefix // "MLO"' .education-toolkit-config.json 2>/dev/null)

        if [[ -n "$COURSE_NAME" ]]; then
            CONTEXT+="**Course Configuration:**\n"
            CONTEXT+="- Course: $COURSE_NAME\n"
            [[ -n "$INSTITUTION" ]] && CONTEXT+="- Institution: $INSTITUTION\n"
            [[ -n "$PLATFORM" ]] && CONTEXT+="- Platform: $PLATFORM\n"
            [[ -n "$OUTCOME_PREFIX" ]] && CONTEXT+="- Learning Outcome Prefix: $OUTCOME_PREFIX\n"
            CONTEXT+="\n"
        fi
    fi
fi

# ============================================================================
# AVAILABLE QUICK COMMANDS
# ============================================================================
CONTEXT+="**Quick Commands:**\n"
CONTEXT+="- \`/design-assessment\` - Design comprehensive assessments (PAIRR, AI Roleplay, etc.)\n"
CONTEXT+="- \`/peer-review\` - Simulate 6-expert design review panel\n"
CONTEXT+="- \`/audit-module\` - Run WCAG 2.2 AA accessibility audit\n"
CONTEXT+="- \`/check-consistency\` - Validate cross-module consistency\n"
CONTEXT+="- \`/generate-rubric\` - Generate QM-aligned rubric\n"
CONTEXT+="- \`/build-storyboard\` - Create Uplimit storyboard\n"
CONTEXT+="- \`/simulate-journey\` - Test student experience (4 personas)\n"
CONTEXT+="- \`/test-widget\` - Test interactive widget UX (3 personas)\n"
CONTEXT+="- \`/check-branding\` - Validate platform branding compliance\n\n"

# ============================================================================
# AUTOMATIC QUALITY CHECKS (Hooks)
# ============================================================================
CONTEXT+="**Automatic Quality Checks (Hooks):**\n"
CONTEXT+="✓ WCAG 2.2 AA validation after HTML edits\n"
CONTEXT+="✓ Measurable learning outcomes (Bloom's verbs)\n"
CONTEXT+="✓ Rubric point math validation\n"
CONTEXT+="✓ Colored emoji → black symbol conversion\n"
CONTEXT+="✓ Protected content warnings (published materials)\n"
CONTEXT+="✓ Auto-formatting (storyboard conventions)\n\n"

# ============================================================================
# RESEARCH-BACKED METHODOLOGIES
# ============================================================================
CONTEXT+="**Available Methodologies:**\n"
CONTEXT+="- **PAIRR**: Peer and AI Review + Reflection (dual feedback)\n"
CONTEXT+="- **AI Roleplay**: Conversational assessments (diagnostic/formative/summative)\n"
CONTEXT+="- **Diagnostic Rubrics**: 3-level formative rubrics (Beginning/Developing/Proficient)\n"
CONTEXT+="- **Three-Tier AI Policy**: Prohibited/Permitted/Required framework\n\n"

# ============================================================================
# BUNDLED KNOWLEDGE BASE
# ============================================================================
CONTEXT+="**Bundled Knowledge (464 KB):**\n"
CONTEXT+="- UDL Guidelines, QM Standards, Inclusive Teaching frameworks\n"
CONTEXT+="- AI Assessment research (5 papers): Acceptable AI use, Academic integrity, Alternative assessments\n\n"

CONTEXT+="_Ready to help with educational content development. All quality checks active._"

# ============================================================================
# OUTPUT AS JSON (additionalContext field)
# ============================================================================
# Escape the context string for JSON
CONTEXT_ESCAPED=$(echo -e "$CONTEXT" | sed 's/\\/\\\\/g' | sed 's/"/\\"/g' | awk '{printf "%s\\n", $0}')

cat <<EOF
{
  "additionalContext": "$CONTEXT_ESCAPED"
}
EOF

exit 0
