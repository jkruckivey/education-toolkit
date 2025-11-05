#!/usr/bin/env python3
"""
Hook 4: Markdown Storyboard Auto-Formatter
Automatically formats educational storyboards to match platform conventions
Runs: PostToolUse (after Edit or Write operations on .md files)
"""

import sys
import re
import os

def should_format(file_path):
    """Determine if this file should be auto-formatted"""
    # Only process markdown files
    if not file_path.lower().endswith('.md'):
        return False

    # Only format storyboards and modules
    filename_lower = os.path.basename(file_path).lower()
    if any(keyword in filename_lower for keyword in ['storyboard', 'module', 'week', 'lesson']):
        return True

    return False

def format_storyboard(file_path):
    """Auto-format educational storyboard content"""

    if not should_format(file_path):
        return False

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"⚠️  Could not read file: {e}", file=sys.stderr)
        return False

    original_content = content
    changes = []

    # =========================================================================
    # 1. CONVERT COLORED EMOJI TO BLACK SYMBOLS (Uplimit branding)
    # =========================================================================
    emoji_map = {
        # Priority badges
        '🔴': '⬤',  # Required → Filled circle
        '🟡': '◐',  # Recommended → Half-filled circle
        '🟢': '○',  # Optional → Empty circle

        # Content type icons
        '🎯': '◉',  # Content/Learning → Bullseye
        '📺': '▶',  # Video → Play symbol
        '📊': '▪',  # Data/Chart → Small square
        '🏟️': '■',  # Venue/Stadium → Filled square
        '💡': '◆',  # Idea/Insight → Diamond
        '🎮': '▸',  # Interactive/Widget → Right triangle
        '⭐': '★',  # Star → Black star
        '✅': '✓',  # Checkmark → Simple check
    }

    total_emoji_replaced = 0
    for emoji, symbol in emoji_map.items():
        if emoji in content:
            count = content.count(emoji)
            content = content.replace(emoji, symbol)
            changes.append(f"Converted {count}× {emoji} → {symbol}")
            total_emoji_replaced += count

    # =========================================================================
    # 2. STANDARDIZE PRIORITY BADGE FORMAT
    # =========================================================================
    # Ensure consistent format: Priority: ⬤ (Required)
    priority_replacements = [
        (r'Priority:\s*⬤\s*Required', 'Priority: ⬤ (Required)'),
        (r'Priority:\s*◐\s*Recommended', 'Priority: ◐ (Recommended)'),
        (r'Priority:\s*○\s*Optional', 'Priority: ○ (Optional)'),
        # Also handle cases without parentheses
        (r'Priority:\s*⬤(?!\s*\()', 'Priority: ⬤ (Required)'),
        (r'Priority:\s*◐(?!\s*\()', 'Priority: ◐ (Recommended)'),
        (r'Priority:\s*○(?!\s*\()', 'Priority: ○ (Optional)'),
    ]

    for pattern, replacement in priority_replacements:
        if re.search(pattern, content):
            content = re.sub(pattern, replacement, content)
            changes.append(f"Standardized priority badge format")
            break  # Only report once

    # =========================================================================
    # 3. ENSURE CONSISTENT TABLE FORMATTING
    # =========================================================================
    # Add spaces around pipe symbols in markdown tables
    def format_table_row(match):
        row = match.group(0)
        # Add space after | and before | if missing
        row = re.sub(r'\|(?! )', '| ', row)  # Space after |
        row = re.sub(r'(?<! )\|', ' |', row)  # Space before |
        return row

    # Find table rows (lines with multiple pipes)
    if '|' in content:
        formatted_content = re.sub(r'\|.+\|', format_table_row, content)
        if formatted_content != content:
            content = formatted_content
            changes.append("Fixed table spacing")

    # =========================================================================
    # 4. STANDARDIZE ELEMENT HEADING FORMAT
    # =========================================================================
    # Convert: "### Element 1 - Title" → "### Element 1: Title"
    element_heading_pattern = r'^(###\s+Element\s+\d+)\s*-\s*'
    if re.search(element_heading_pattern, content, re.MULTILINE):
        content = re.sub(element_heading_pattern, r'\1: ', content, flags=re.MULTILINE)
        changes.append("Standardized element heading format (dash → colon)")

    # =========================================================================
    # 5. FIX SPACING AROUND HEADINGS
    # =========================================================================
    # Ensure blank line before headings (except at start of file)
    content = re.sub(r'([^\n])\n(#{1,4}\s)', r'\1\n\n\2', content)

    # Ensure blank line after headings (except before another heading or list)
    content = re.sub(r'(#{1,4}\s.+)\n([^#\n-*])', r'\1\n\n\2', content)

    # =========================================================================
    # 6. STANDARDIZE LEARNING OUTCOME REFERENCES
    # =========================================================================
    # Add space in MLO references: "MLO1.1" → "MLO 1.1"
    mlo_pattern = r'\bMLO(\d+)\.(\d+)\b'
    if re.search(mlo_pattern, content):
        content = re.sub(mlo_pattern, r'MLO \1.\2', content)
        changes.append("Standardized MLO reference format (added space)")

    # =========================================================================
    # 7. FIX COMMON MARKDOWN ISSUES
    # =========================================================================
    # Remove multiple blank lines (more than 2 consecutive)
    content = re.sub(r'\n{3,}', '\n\n', content)

    # Remove trailing spaces at end of lines
    content = re.sub(r' +$', '', content, flags=re.MULTILINE)

    # Ensure file ends with single newline
    content = content.rstrip() + '\n'

    # =========================================================================
    # 8. STANDARDIZE TIME ESTIMATES
    # =========================================================================
    # Convert "10min" → "10 min", "2hrs" → "2 hours"
    time_patterns = [
        (r'(\d+)\s*mins?\b', r'\1 min'),
        (r'(\d+)\s*hrs?\b', r'\1 hours'),
        (r'(\d+)\s*h\b', r'\1 hours'),
    ]
    for pattern, replacement in time_patterns:
        content = re.sub(pattern, replacement, content, flags=re.IGNORECASE)

    # =========================================================================
    # WRITE CHANGES IF ANY
    # =========================================================================
    if content != original_content:
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

            # Report changes to stderr (visible to user)
            if changes:
                print("✨ Auto-formatted storyboard:", file=sys.stderr)
                for change in changes[:5]:  # Show max 5 changes
                    print(f"  • {change}", file=sys.stderr)
                if len(changes) > 5:
                    print(f"  • ... and {len(changes) - 5} more formatting fixes", file=sys.stderr)

            return True
        except Exception as e:
            print(f"⚠️  Could not write formatted file: {e}", file=sys.stderr)
            return False

    return False  # No changes needed

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(0)

    file_path = sys.argv[1]

    # Format the file
    formatted = format_storyboard(file_path)

    # Always exit 0 (don't block on formatting errors)
    sys.exit(0)
