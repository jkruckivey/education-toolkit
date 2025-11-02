#!/usr/bin/env python3
"""
Rubric Math Validator

Validates point totals, distributions, and performance level percentages in rubrics.
"""

import argparse
import re
import sys
from pathlib import Path


def extract_rubric_data(rubric_file):
    """Extract rubric structure and point values from markdown"""
    with open(rubric_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find stated total points
    stated_total = None
    total_patterns = [
        r'[Tt]otal\s*[Pp]oints?:?\s*(\d+)',
        r'\*\*[Tt]otal\*\*:?\s*(\d+)',
        r'Total:\s*\*\*(\d+)\*\*'
    ]

    for pattern in total_patterns:
        match = re.search(pattern, content)
        if match:
            stated_total = int(match.group(1))
            break

    # Extract criteria with points
    criteria = []

    # Pattern 1: Markdown table format
    # | Criterion | ... | 10 pts |
    table_pattern = r'\|\s*([^|]+?)\s*\|[^|]*\|[^|]*\|[^|]*\|[^|]*\|\s*(\d+)\s*(?:pts?|points?)?'
    for match in re.finditer(table_pattern, content, re.IGNORECASE):
        name = match.group(1).strip()
        points = match.group(2)

        if name.lower() not in ['criterion', 'criteria', 'performance level', 'points']:
            criteria.append({
                'name': name,
                'points': int(points),
                'line': content[:match.start()].count('\n') + 1
            })

    # Pattern 2: Heading with points (e.g., "## Analysis Quality (10 pts)")
    heading_pattern = r'^#{1,3}\s*(.+?)\s*\((\d+)\s*pts?\)'
    for match in re.finditer(heading_pattern, content, re.MULTILINE):
        name = match.group(1).strip()
        points = int(match.group(2))

        criteria.append({
            'name': name,
            'points': points,
            'line': content[:match.start()].count('\n') + 1
        })

    # Pattern 3: Performance level percentages
    # Exemplary (90-100%)
    performance_levels = []
    perf_pattern = r'(Exemplary|Proficient|Developing|Beginning|Missing|Advanced|Competent)\s*\((\d+)-(\d+)%\)'

    for match in re.finditer(perf_pattern, content, re.IGNORECASE):
        level = match.group(1)
        low = int(match.group(2))
        high = int(match.group(3))

        performance_levels.append({
            'level': level,
            'low': low,
            'high': high
        })

    return {
        'stated_total': stated_total,
        'criteria': criteria,
        'performance_levels': performance_levels,
        'file': str(rubric_file)
    }


def validate_rubric_math(data, tolerance=0):
    """Validate rubric mathematical consistency"""
    issues = []

    # Check 1: Calculate actual total from criteria
    actual_total = sum(c['points'] for c in data['criteria'])

    if data['stated_total'] is not None:
        if abs(actual_total - data['stated_total']) > tolerance:
            issues.append({
                'type': 'total_mismatch',
                'severity': 'error',
                'message': f"Stated total ({data['stated_total']} pts) doesn't match sum of criteria ({actual_total} pts)",
                'fix': f"Either update total to {actual_total} or adjust criterion point values"
            })

    # Check 2: Point distribution balance
    if actual_total > 0:
        for criterion in data['criteria']:
            percentage = (criterion['points'] / actual_total) * 100

            if percentage > 50:
                issues.append({
                    'type': 'overweight_criterion',
                    'severity': 'warning',
                    'message': f"Criterion '{criterion['name']}' is {percentage:.1f}% of total grade (>{criterion['points']}/{actual_total} pts)",
                    'fix': "Consider breaking this criterion into smaller, more specific criteria"
                })

            if percentage < 5 and actual_total > 20:  # Only flag if it's a substantial rubric
                issues.append({
                    'type': 'underweight_criterion',
                    'severity': 'info',
                    'message': f"Criterion '{criterion['name']}' is only {percentage:.1f}% of grade ({criterion['points']}/{actual_total} pts)",
                    'fix': "Consider if this criterion merits its own scoring or should be combined with another"
                })

    # Check 3: Duplicate point values (might indicate copy-paste error)
    point_counts = {}
    for criterion in data['criteria']:
        pts = criterion['points']
        if pts not in point_counts:
            point_counts[pts] = []
        point_counts[pts].append(criterion['name'])

    for points, criteria_with_points in point_counts.items():
        if len(criteria_with_points) >= 3:  # 3+ criteria with same points
            issues.append({
                'type': 'duplicate_points',
                'severity': 'info',
                'message': f"{len(criteria_with_points)} criteria all worth {points} pts: {', '.join(criteria_with_points[:3])}{'...' if len(criteria_with_points) > 3 else ''}",
                'fix': "This may be intentional, but verify that point distribution reflects relative importance"
            })

    # Check 4: Performance level percentage consistency
    if data['performance_levels']:
        for i, level in enumerate(data['performance_levels']):
            # Check for gaps between levels
            if i < len(data['performance_levels']) - 1:
                next_level = data['performance_levels'][i + 1]
                if level['low'] != next_level['high'] + 1:
                    issues.append({
                        'type': 'performance_level_gap',
                        'severity': 'warning',
                        'message': f"Gap between {level['level']} ({level['low']}-{level['high']}%) and {next_level['level']} ({next_level['low']}-{next_level['high']}%)",
                        'fix': "Ensure performance levels are continuous with no gaps"
                    })

            # Check if level percentages make sense
            if data['stated_total']:
                expected_low = int((level['low'] / 100) * data['stated_total'])
                expected_high = int((level['high'] / 100) * data['stated_total'])

                # This is informational - helps users understand point ranges
                if i == 0:  # Only show for first level to avoid spam
                    issues.append({
                        'type': 'performance_level_points',
                        'severity': 'info',
                        'message': f"{level['level']} ({level['low']}-{level['high']}%) = {expected_low}-{expected_high} pts out of {data['stated_total']}",
                        'fix': "Verify this point range matches your grading intent"
                    })

    # Check 5: Missing point values
    if not data['criteria']:
        issues.append({
            'type': 'no_criteria',
            'severity': 'error',
            'message': "No rubric criteria with point values found in file",
            'fix': "Ensure rubric uses standard format: | Criterion | ... | X pts |"
        })

    if data['stated_total'] is None:
        issues.append({
            'type': 'no_total',
            'severity': 'warning',
            'message': "No total points statement found (e.g., 'Total Points: 30')",
            'fix': "Add a clear total points statement for student clarity"
        })

    return {
        'stated_total': data['stated_total'],
        'actual_total': actual_total,
        'criteria_count': len(data['criteria']),
        'issues': issues,
        'criteria': data['criteria']
    }


def generate_report(results):
    """Generate validation report"""
    report = "Rubric Math Validation Report\n"
    report += "=" * 60 + "\n\n"

    # Summary
    report += f"Stated Total: {results['stated_total'] or 'NOT FOUND'} pts\n"
    report += f"Actual Total: {results['actual_total']} pts (sum of criteria)\n"
    report += f"Criteria Count: {results['criteria_count']}\n\n"

    errors = [i for i in results['issues'] if i['severity'] == 'error']
    warnings = [i for i in results['issues'] if i['severity'] == 'warning']
    info = [i for i in results['issues'] if i['severity'] == 'info']

    report += f"Issues: {len(errors)} errors, {len(warnings)} warnings, {len(info)} info\n\n"

    # Pass/Fail
    if not errors:
        report += "✅ PASS: Rubric math is correct\n\n"
    else:
        report += "❌ FAIL: Rubric math errors detected\n\n"

    # Criteria breakdown
    if results['criteria']:
        report += "CRITERIA BREAKDOWN\n"
        report += "-" * 60 + "\n"
        for i, criterion in enumerate(results['criteria'], 1):
            percentage = (criterion['points'] / results['actual_total'] * 100) if results['actual_total'] > 0 else 0
            report += f"{i}. {criterion['name']}: {criterion['points']} pts ({percentage:.1f}%)\n"
        report += f"\nTotal: {results['actual_total']} pts\n\n"

    # Errors
    if errors:
        report += "❌ ERRORS (Must Fix)\n"
        report += "-" * 60 + "\n"
        for i, issue in enumerate(errors, 1):
            report += f"{i}. {issue['message']}\n"
            report += f"   Fix: {issue['fix']}\n\n"

    # Warnings
    if warnings:
        report += "⚠️  WARNINGS (Review Recommended)\n"
        report += "-" * 60 + "\n"
        for i, issue in enumerate(warnings, 1):
            report += f"{i}. {issue['message']}\n"
            report += f"   Fix: {issue['fix']}\n\n"

    # Info
    if info:
        report += "ℹ️  INFORMATION (FYI)\n"
        report += "-" * 60 + "\n"
        for i, issue in enumerate(info, 1):
            report += f"{i}. {issue['message']}\n"
            if 'fix' in issue and not issue['message'].startswith('Verify'):
                report += f"   {issue['fix']}\n"
            report += "\n"

    return report


def main():
    parser = argparse.ArgumentParser(
        description='Validate rubric point calculations and distributions'
    )
    parser.add_argument('--file', required=True,
                        help='Rubric markdown file')
    parser.add_argument('--tolerance', type=int, default=0,
                        help='Allowed point variance (default: 0)')

    args = parser.parse_args()

    # Validate file exists
    rubric_path = Path(args.file)
    if not rubric_path.exists():
        print(f"Error: Rubric file not found: {rubric_path}")
        return 1

    # Extract rubric data
    print(f"Analyzing rubric: {rubric_path}")
    data = extract_rubric_data(rubric_path)

    # Validate math
    results = validate_rubric_math(data, args.tolerance)

    # Generate report
    report = generate_report(results)
    print(report)

    # Exit code based on errors
    errors = [i for i in results['issues'] if i['severity'] == 'error']
    if errors:
        return 1
    else:
        return 0


if __name__ == '__main__':
    sys.exit(main())
