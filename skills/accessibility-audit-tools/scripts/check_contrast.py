#!/usr/bin/env python3
"""
WCAG 2.2 AA Color Contrast Checker

Analyzes HTML/CSS files for color contrast violations against WCAG 2.2 AA standards.
"""

import argparse
import re
import sys
import json
from pathlib import Path


def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def relative_luminance(rgb):
    """Calculate relative luminance for contrast ratio"""
    # Normalize RGB values
    r, g, b = [x / 255.0 for x in rgb]

    # Apply gamma correction
    r = r / 12.92 if r <= 0.03928 else ((r + 0.055) / 1.055) ** 2.4
    g = g / 12.92 if g <= 0.03928 else ((g + 0.055) / 1.055) ** 2.4
    b = b / 12.92 if b <= 0.03928 else ((b + 0.055) / 1.055) ** 2.4

    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(color1_hex, color2_hex):
    """Calculate WCAG contrast ratio between two colors"""
    rgb1 = hex_to_rgb(color1_hex)
    rgb2 = hex_to_rgb(color2_hex)

    lum1 = relative_luminance(rgb1)
    lum2 = relative_luminance(rgb2)

    lighter = max(lum1, lum2)
    darker = min(lum1, lum2)

    return (lighter + 0.05) / (darker + 0.05)


def suggest_fix_color(foreground_hex, background_hex, required_ratio):
    """Suggest darker/lighter foreground color to meet required ratio"""
    bg_rgb = hex_to_rgb(background_hex)
    bg_lum = relative_luminance(bg_rgb)

    # Calculate required luminance for foreground
    # Formula: (lighter + 0.05) / (darker + 0.05) = required_ratio
    if bg_lum > 0.5:  # Light background, need darker foreground
        # (bg_lum + 0.05) / (fg_lum + 0.05) = required_ratio
        required_fg_lum = (bg_lum + 0.05) / required_ratio - 0.05
        # Ensure it's darker than background
        required_fg_lum = min(required_fg_lum, bg_lum - 0.05)
    else:  # Dark background, need lighter foreground
        # (fg_lum + 0.05) / (bg_lum + 0.05) = required_ratio
        required_fg_lum = required_ratio * (bg_lum + 0.05) - 0.05
        # Ensure it's lighter than background
        required_fg_lum = max(required_fg_lum, bg_lum + 0.05)

    # Clamp to valid range
    required_fg_lum = max(0, min(1, required_fg_lum))

    # Reverse gamma correction (approximate)
    def lum_to_srgb(lum_channel):
        if lum_channel <= 0.0031308:
            return lum_channel * 12.92
        return 1.055 * (lum_channel ** (1/2.4)) - 0.055

    # Simple grayscale approach (maintain hue would be more complex)
    rgb_channel = lum_to_srgb(required_fg_lum / 0.2126)  # Simplified
    rgb_channel = max(0, min(1, rgb_channel))

    # Convert back to hex
    rgb_int = int(rgb_channel * 255)
    suggested_hex = f"#{rgb_int:02x}{rgb_int:02x}{rgb_int:02x}"

    return suggested_hex


def extract_color_pairs_from_html(file_path):
    """Extract foreground/background color pairs from HTML/CSS"""
    # Simplified extraction (full implementation would parse CSS properly)
    violations = []

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find inline style color pairs (simplified regex)
    # Example: style="color: #666666; background-color: #FFFFFF;"
    style_pattern = r'style="[^"]*color:\s*([#\w]+)[^"]*background(?:-color)?:\s*([#\w]+)'

    for i, line in enumerate(content.split('\n'), 1):
        matches = re.finditer(style_pattern, line, re.IGNORECASE)
        for match in matches:
            fg_color = match.group(1)
            bg_color = match.group(2)

            # Normalize hex colors
            if fg_color.startswith('#') and len(fg_color) in [4, 7]:
                if len(fg_color) == 4:  # Convert #RGB to #RRGGBB
                    fg_color = f"#{fg_color[1]*2}{fg_color[2]*2}{fg_color[3]*2}"

            if bg_color.startswith('#') and len(bg_color) in [4, 7]:
                if len(bg_color) == 4:
                    bg_color = f"#{bg_color[1]*2}{bg_color[2]*2}{bg_color[3]*2}"

            violations.append({
                'line': i,
                'foreground': fg_color,
                'background': bg_color,
                'context': line.strip()[:80]
            })

    # Find CSS class color pairs (simplified)
    css_class_pattern = r'\.(\w+)\s*\{[^}]*color:\s*([#\w]+);[^}]*background(?:-color)?:\s*([#\w]+);[^}]*\}'
    matches = re.finditer(css_class_pattern, content, re.IGNORECASE | re.DOTALL)

    for match in matches:
        class_name = match.group(1)
        fg_color = match.group(2)
        bg_color = match.group(3)

        # Find line number
        line_num = content[:match.start()].count('\n') + 1

        violations.append({
            'line': line_num,
            'foreground': fg_color,
            'background': bg_color,
            'context': f'.{class_name} {{ ... }}'
        })

    return violations


def check_file_contrast(file_path, threshold='AA'):
    """Check color contrast in a single file"""
    # WCAG 2.2 AA thresholds
    required_ratios = {
        'normal_text': 4.5 if threshold == 'AA' else 7.0,
        'large_text': 3.0 if threshold == 'AA' else 4.5,
        'focus_indicator': 3.0
    }

    color_pairs = extract_color_pairs_from_html(file_path)
    violations = []

    for pair in color_pairs:
        try:
            ratio = contrast_ratio(pair['foreground'], pair['background'])

            # Assume normal text unless we detect large text (would need more parsing)
            required = required_ratios['normal_text']
            text_type = 'normal text'

            if ratio < required:
                suggested = suggest_fix_color(pair['foreground'], pair['background'], required)
                suggested_ratio = contrast_ratio(suggested, pair['background'])

                violations.append({
                    'file': str(file_path),
                    'line': pair['line'],
                    'foreground': pair['foreground'],
                    'background': pair['background'],
                    'ratio': round(ratio, 2),
                    'required': required,
                    'text_type': text_type,
                    'status': 'FAIL',
                    'suggested_foreground': suggested,
                    'suggested_ratio': round(suggested_ratio, 2),
                    'context': pair['context']
                })
        except (ValueError, ZeroDivisionError):
            # Invalid color format or calculation error
            continue

    return violations


def format_report(violations, format_type='text'):
    """Format violations report"""
    if format_type == 'json':
        return json.dumps({
            'total_violations': len(violations),
            'violations': violations
        }, indent=2)

    elif format_type == 'html':
        html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>WCAG Contrast Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .violation { border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 5px; }
        .fail { border-left: 5px solid #d32f2f; }
        .color-swatch { display: inline-block; width: 60px; height: 30px; border: 1px solid #333; margin: 0 5px; vertical-align: middle; }
        .fix { background: #e8f5e9; padding: 10px; margin-top: 10px; border-radius: 3px; }
    </style>
</head>
<body>
    <h1>WCAG 2.2 AA Color Contrast Report</h1>
    <p><strong>Total Violations:</strong> {}</p>
""".format(len(violations))

        for v in violations:
            html += f"""
    <div class="violation fail">
        <p><strong>File:</strong> {v['file']} <strong>Line:</strong> {v['line']}</p>
        <p><strong>Current:</strong>
            <span class="color-swatch" style="background: {v['foreground']}; color: {v['background']};">Aa</span>
            {v['foreground']} on {v['background']} = <strong>{v['ratio']}:1</strong> (needs {v['required']}:1)
        </p>
        <div class="fix">
            <strong>✅ Suggested Fix:</strong>
            <span class="color-swatch" style="background: {v['suggested_foreground']}; color: {v['background']};">Aa</span>
            Use {v['suggested_foreground']} = <strong>{v['suggested_ratio']}:1</strong>
        </div>
        <p><small><code>{v['context']}</code></small></p>
    </div>
"""

        html += "</body></html>"
        return html

    else:  # text format
        report = f"WCAG 2.2 AA Color Contrast Report\n"
        report += f"{'=' * 60}\n\n"
        report += f"Total Violations: {len(violations)}\n\n"

        for i, v in enumerate(violations, 1):
            report += f"{i}. {v['file']}:{v['line']}\n"
            report += f"   Current: {v['foreground']} on {v['background']} = {v['ratio']}:1\n"
            report += f"   Required: {v['required']}:1 for {v['text_type']}\n"
            report += f"   Status: ❌ {v['status']}\n"
            report += f"   Fix: Use {v['suggested_foreground']} (ratio: {v['suggested_ratio']}:1)\n"
            report += f"   Context: {v['context']}\n\n"

        return report


def main():
    parser = argparse.ArgumentParser(
        description='Check WCAG 2.2 AA color contrast compliance'
    )
    parser.add_argument('--file', required=True,
                        help='HTML/CSS file to analyze')
    parser.add_argument('--report', choices=['text', 'json', 'html'], default='text',
                        help='Report output format')
    parser.add_argument('--threshold', choices=['AA', 'AAA'], default='AA',
                        help='WCAG threshold level')
    parser.add_argument('--output',
                        help='Save report to file (default: print to stdout)')

    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        return 1

    # Check contrast
    violations = check_file_contrast(file_path, args.threshold)

    # Format report
    report = format_report(violations, args.report)

    # Output report
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"✅ Report saved to: {args.output}")
    else:
        print(report)

    # Exit code
    if len(violations) > 0:
        print(f"\n❌ Found {len(violations)} contrast violations")
        return 1
    else:
        print(f"\n✅ No contrast violations found")
        return 0


if __name__ == '__main__':
    sys.exit(main())
