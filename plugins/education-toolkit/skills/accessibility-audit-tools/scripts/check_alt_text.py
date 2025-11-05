#!/usr/bin/env python3
"""
Alt Text Accessibility Checker

Validates alt text presence and quality on images for WCAG 2.2 AA compliance.
"""

import argparse
import sys
from pathlib import Path
from bs4 import BeautifulSoup


# Placeholder alt text patterns (considered poor quality)
PLACEHOLDER_PATTERNS = [
    'image', 'img', 'picture', 'photo', 'graphic', 'untitled',
    'dsc', 'img_', 'photo_', 'screenshot', 'scan', 'pic',
    'image.jpg', 'photo.png', 'graphic.svg'
]


def check_alt_text_quality(alt_text):
    """Evaluate alt text quality"""
    if not alt_text:
        return 'missing', "Image missing alt attribute"

    alt_lower = alt_text.lower().strip()

    # Empty alt (decorative image - this is GOOD)
    if alt_lower == '':
        return 'decorative', "Empty alt (decorative image)"

    # Check for placeholder text
    for pattern in PLACEHOLDER_PATTERNS:
        if pattern in alt_lower and len(alt_lower) < 20:
            return 'placeholder', f"Placeholder alt text: '{alt_text}'"

    # Check for filename-like alt text
    if any(ext in alt_lower for ext in ['.jpg', '.png', '.gif', '.svg', '.webp']):
        return 'filename', f"Alt text appears to be filename: '{alt_text}'"

    # Too short (likely not descriptive enough)
    if len(alt_text) < 10:
        return 'too_short', f"Alt text may be too brief: '{alt_text}' (consider adding context)"

    # Too long (should use longdesc or surrounding text instead)
    if len(alt_text) > 150:
        return 'too_long', f"Alt text exceeds 150 chars ({len(alt_text)} chars) - consider moving to caption or longdesc"

    # Redundant phrases
    redundant_phrases = ['image of', 'picture of', 'graphic of', 'photo of', 'screenshot of']
    for phrase in redundant_phrases:
        if alt_lower.startswith(phrase):
            return 'redundant', f"Alt text starts with redundant phrase: '{phrase}'"

    return 'good', "Alt text appears descriptive"


def analyze_html_file(file_path, strict=False):
    """Analyze a single HTML file for alt text issues"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {'error': str(e), 'images': []}

    soup = BeautifulSoup(content, 'html.parser')
    images = soup.find_all('img')

    results = []
    for img in images:
        src = img.get('src', '[no src]')
        alt = img.get('alt', None)

        # Get line number (approximate)
        line_number = content[:content.find(str(img))].count('\n') + 1 if str(img) in content else 'unknown'

        if alt is None:
            status, message = 'missing', "Missing alt attribute"
            severity = 'error'
        else:
            status, message = check_alt_text_quality(alt)
            if status == 'decorative' and not strict:
                severity = 'pass'
            elif status == 'good':
                severity = 'pass'
            elif status in ['placeholder', 'filename', 'missing']:
                severity = 'error'
            else:
                severity = 'warning'

        results.append({
            'file': str(file_path),
            'line': line_number,
            'src': src,
            'alt': alt,
            'status': status,
            'severity': severity,
            'message': message,
            'tag': str(img)[:100]
        })

    return {
        'file': str(file_path),
        'total_images': len(images),
        'images': results
    }


def analyze_directory(directory, recursive=False, strict=False):
    """Analyze all HTML files in a directory"""
    path = Path(directory)
    pattern = '**/*.html' if recursive else '*.html'

    all_results = []
    for html_file in path.glob(pattern):
        result = analyze_html_file(html_file, strict)
        if result.get('images'):
            all_results.append(result)

    return all_results


def generate_report(all_results, strict=False):
    """Generate text report from analysis results"""
    total_images = sum(r['total_images'] for r in all_results)
    total_errors = sum(1 for r in all_results for img in r['images'] if img['severity'] == 'error')
    total_warnings = sum(1 for r in all_results for img in r['images'] if img['severity'] == 'warning')
    total_pass = sum(1 for r in all_results for img in r['images'] if img['severity'] == 'pass')

    report = "Alt Text Accessibility Report\n"
    report += "=" * 60 + "\n\n"
    report += f"Files analyzed: {len(all_results)}\n"
    report += f"Total images: {total_images}\n"
    report += f"✅ Pass: {total_pass}\n"
    report += f"⚠️  Warnings: {total_warnings}\n"
    report += f"❌ Errors: {total_errors}\n\n"

    if total_errors == 0 and total_warnings == 0:
        report += "🎉 No alt text issues found!\n"
        return report

    report += "Issues by File:\n"
    report += "-" * 60 + "\n\n"

    for file_result in all_results:
        errors = [img for img in file_result['images'] if img['severity'] == 'error']
        warnings = [img for img in file_result['images'] if img['severity'] == 'warning']

        if not errors and not warnings:
            continue

        report += f"\n📄 {file_result['file']}\n"
        report += f"   Images: {file_result['total_images']} | Errors: {len(errors)} | Warnings: {len(warnings)}\n\n"

        # Report errors
        for img in errors:
            report += f"   ❌ Line {img['line']}: {img['message']}\n"
            report += f"      Src: {img['src']}\n"
            if img['alt'] is not None:
                report += f"      Current alt: \"{img['alt']}\"\n"
            report += f"      Fix: Add descriptive alt text that explains the image's purpose and content\n\n"

        # Report warnings
        for img in warnings:
            report += f"   ⚠️  Line {img['line']}: {img['message']}\n"
            report += f"      Src: {img['src']}\n"
            if img['alt'] is not None:
                report += f"      Current alt: \"{img['alt']}\"\n"
            report += f"      Suggestion: Review and improve alt text quality\n\n"

    report += "\n" + "=" * 60 + "\n"
    report += "Alt Text Best Practices:\n"
    report += "=" * 60 + "\n"
    report += "✅ DO: Describe the content and function of the image\n"
    report += "✅ DO: Be concise (aim for 10-150 characters)\n"
    report += "✅ DO: Use alt=\"\" for purely decorative images\n"
    report += "✅ DO: Include text that appears in the image\n"
    report += "❌ DON'T: Start with 'image of' or 'picture of'\n"
    report += "❌ DON'T: Use filenames as alt text\n"
    report += "❌ DON'T: Use generic placeholders like 'image' or 'untitled'\n\n"

    report += "Examples:\n"
    report += "-" * 60 + "\n"
    report += "❌ Bad:  <img src=\"chart.png\" alt=\"image\">\n"
    report += "❌ Bad:  <img src=\"chart.png\" alt=\"chart.png\">\n"
    report += "✅ Good: <img src=\"chart.png\" alt=\"Bar chart showing 40% revenue increase in Q3\">\n\n"
    report += "❌ Bad:  <img src=\"divider.png\" alt=\"divider\">\n"
    report += "✅ Good: <img src=\"divider.png\" alt=\"\"> (decorative)\n\n"

    return report


def main():
    parser = argparse.ArgumentParser(
        description='Check alt text accessibility in HTML files'
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--file',
                       help='Single HTML file to analyze')
    group.add_argument('--directory',
                       help='Directory containing HTML files')

    parser.add_argument('--recursive', action='store_true',
                        help='Scan subdirectories recursively')
    parser.add_argument('--strict', action='store_true',
                        help='Flag decorative images without explicit alt=""')
    parser.add_argument('--output',
                        help='Save report to file (default: print to stdout)')

    args = parser.parse_args()

    # Analyze files
    if args.file:
        file_path = Path(args.file)
        if not file_path.exists():
            print(f"Error: File not found: {file_path}")
            return 1
        results = [analyze_html_file(file_path, args.strict)]
    else:
        dir_path = Path(args.directory)
        if not dir_path.exists():
            print(f"Error: Directory not found: {dir_path}")
            return 1
        results = analyze_directory(dir_path, args.recursive, args.strict)

    if not results or not any(r.get('images') for r in results):
        print("No images found in analyzed files.")
        return 0

    # Generate report
    report = generate_report(results, args.strict)

    # Output report
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"✅ Report saved to: {args.output}")
    else:
        print(report)

    # Count errors for exit code
    total_errors = sum(1 for r in results for img in r.get('images', []) if img['severity'] == 'error')

    if total_errors > 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    sys.exit(main())
