#!/usr/bin/env python3
"""
Outcome-Criteria Alignment Checker

Validates that rubric criteria align with learning outcomes per QM Standard 3.1.
"""

import argparse
import re
import sys
from pathlib import Path


# Bloom's taxonomy verb mapping
BLOOMS_VERBS = {
    'remember': ['define', 'list', 'recall', 'identify', 'name', 'recognize', 'label', 'match', 'state', 'select'],
    'understand': ['explain', 'describe', 'summarize', 'interpret', 'discuss', 'paraphrase', 'classify', 'compare', 'infer'],
    'apply': ['apply', 'demonstrate', 'use', 'solve', 'calculate', 'implement', 'execute', 'perform', 'operate'],
    'analyze': ['analyze', 'compare', 'contrast', 'differentiate', 'examine', 'distinguish', 'categorize', 'investigate', 'deconstruct'],
    'evaluate': ['evaluate', 'justify', 'critique', 'assess', 'defend', 'judge', 'appraise', 'argue', 'prioritize'],
    'create': ['create', 'design', 'develop', 'formulate', 'construct', 'generate', 'produce', 'plan', 'compose']
}


def detect_blooms_level(text):
    """Detect Bloom's taxonomy level from text"""
    text_lower = text.lower()

    for level, verbs in BLOOMS_VERBS.items():
        for verb in verbs:
            # Look for verb at start of outcome or after "will"
            if re.search(rf'\b{verb}\b', text_lower):
                return level, verb

    return 'unknown', None


def extract_outcomes(outcomes_file):
    """Extract learning outcomes from file"""
    with open(outcomes_file, 'r', encoding='utf-8') as f:
        content = f.read()

    outcomes = []

    # Pattern 1: Numbered outcomes (e.g., "1. Students will...")
    pattern1 = r'^\s*\d+\.\s*(.+?)(?=\n\d+\.|$)'
    matches1 = re.findall(pattern1, content, re.MULTILINE | re.DOTALL)
    outcomes.extend([m.strip() for m in matches1])

    # Pattern 2: Bullet points (e.g., "- Analyze...")
    pattern2 = r'^\s*[-*]\s*(.+?)(?=\n[-*]|$)'
    matches2 = re.findall(pattern2, content, re.MULTILINE | re.DOTALL)
    outcomes.extend([m.strip() for m in matches2])

    # Pattern 3: "CLO" or "MLO" prefixed (e.g., "CLO 1: Analyze...")
    pattern3 = r'(?:CLO|MLO)\s*\d+:\s*(.+?)(?=\n|$)'
    matches3 = re.findall(pattern3, content, re.IGNORECASE)
    outcomes.extend([m.strip() for m in matches3])

    # Remove duplicates while preserving order
    seen = set()
    unique_outcomes = []
    for outcome in outcomes:
        if outcome not in seen and len(outcome) > 10:  # Filter out very short non-outcomes
            seen.add(outcome)
            unique_outcomes.append(outcome)

    # Analyze Bloom's levels
    analyzed_outcomes = []
    for i, outcome in enumerate(unique_outcomes, 1):
        level, verb = detect_blooms_level(outcome)
        analyzed_outcomes.append({
            'id': i,
            'text': outcome,
            'blooms_level': level,
            'blooms_verb': verb
        })

    return analyzed_outcomes


def extract_criteria(rubric_file):
    """Extract rubric criteria from markdown file"""
    with open(rubric_file, 'r', encoding='utf-8') as f:
        content = f.read()

    criteria = []

    # Pattern 1: Markdown table format
    # | Criterion | ... |
    table_pattern = r'\|\s*([^|]+?)\s*\|[^|]*\|[^|]*\|[^|]*\|[^|]*\|\s*(\d+)\s*(?:pts?|points?)?'
    matches = re.findall(table_pattern, content, re.IGNORECASE)

    for name, points in matches:
        name_clean = name.strip()
        if name_clean.lower() not in ['criterion', 'criteria', 'performance level']:
            level, verb = detect_blooms_level(name_clean)
            criteria.append({
                'name': name_clean,
                'points': int(points) if points else 0,
                'blooms_level': level,
                'blooms_verb': verb
            })

    # Pattern 2: Heading-based criteria (e.g., "## Criterion 1: Analysis Quality")
    heading_pattern = r'^#{1,3}\s*(?:Criterion\s*\d+:?\s*)?(.+?)(?:\((\d+)\s*pts?\))?$'
    for match in re.finditer(heading_pattern, content, re.MULTILINE):
        name = match.group(1).strip()
        points = match.group(2)

        if len(name) > 5 and name.lower() not in ['criteria', 'rubric', 'assessment']:
            level, verb = detect_blooms_level(name)
            criteria.append({
                'name': name,
                'points': int(points) if points else 0,
                'blooms_level': level,
                'blooms_verb': verb
            })

    return criteria


def check_alignment(outcomes, criteria, verbose=False):
    """Check outcome-criteria alignment"""

    # Build alignment matrix
    alignment_matrix = []

    for criterion in criteria:
        aligned_outcomes = []

        for outcome in outcomes:
            # Check for explicit alignment (keywords match)
            criterion_keywords = set(re.findall(r'\b\w{4,}\b', criterion['name'].lower()))
            outcome_keywords = set(re.findall(r'\b\w{4,}\b', outcome['text'].lower()))

            keyword_overlap = criterion_keywords & outcome_keywords

            # Check for Bloom's level match
            blooms_match = (
                criterion['blooms_level'] == outcome['blooms_level'] or
                criterion['blooms_level'] in ['unknown', outcome['blooms_level']]
            )

            if len(keyword_overlap) >= 2 or blooms_match:
                aligned_outcomes.append({
                    'outcome_id': outcome['id'],
                    'confidence': 'high' if len(keyword_overlap) >= 2 else 'medium'
                })

        alignment_matrix.append({
            'criterion': criterion['name'],
            'aligned_outcomes': aligned_outcomes
        })

    # Find issues
    orphaned_criteria = [
        item['criterion'] for item in alignment_matrix
        if not item['aligned_outcomes']
    ]

    tested_outcome_ids = set()
    for item in alignment_matrix:
        for outcome in item['aligned_outcomes']:
            tested_outcome_ids.add(outcome['outcome_id'])

    untested_outcomes = [
        outcome for outcome in outcomes
        if outcome['id'] not in tested_outcome_ids
    ]

    return {
        'alignment_matrix': alignment_matrix,
        'orphaned_criteria': orphaned_criteria,
        'untested_outcomes': untested_outcomes,
        'total_outcomes': len(outcomes),
        'total_criteria': len(criteria),
        'outcomes': outcomes,
        'criteria': criteria
    }


def generate_report(results, verbose=False):
    """Generate alignment report"""

    report = "Outcome-Criteria Alignment Report\n"
    report += "=" * 60 + "\n\n"

    # Summary
    report += f"Learning Outcomes: {results['total_outcomes']}\n"
    report += f"Rubric Criteria: {results['total_criteria']}\n"
    report += f"Orphaned Criteria (no outcome link): {len(results['orphaned_criteria'])}\n"
    report += f"Untested Outcomes (no criteria assess): {len(results['untested_outcomes'])}\n\n"

    # Pass/Fail determination
    if not results['orphaned_criteria'] and not results['untested_outcomes']:
        report += "✅ PASS: All criteria align with outcomes, all outcomes assessed\n\n"
    else:
        report += "❌ FAIL: Alignment issues detected\n\n"

    # Detailed issues
    if results['orphaned_criteria']:
        report += "ORPHANED CRITERIA (No Learning Outcome Alignment)\n"
        report += "-" * 60 + "\n"
        for i, criterion in enumerate(results['orphaned_criteria'], 1):
            report += f"{i}. \"{criterion}\"\n"
            report += f"   Issue: This criterion doesn't clearly assess any stated learning outcome\n"
            report += f"   Fix: Either remove this criterion OR add a learning outcome it assesses\n\n"

    if results['untested_outcomes']:
        report += "UNTESTED LEARNING OUTCOMES (No Rubric Criteria)\n"
        report += "-" * 60 + "\n"
        for outcome in results['untested_outcomes']:
            report += f"{outcome['id']}. \"{outcome['text']}\"\n"
            report += f"   Bloom's Level: {outcome['blooms_level'].title()}\n"
            report += f"   Issue: No rubric criterion assesses this outcome\n"
            report += f"   Fix: Add criterion like \"{outcome['blooms_verb'].title() if outcome['blooms_verb'] else 'Assessment of'} [key concept]\"\n\n"

    # Alignment matrix (verbose mode)
    if verbose and results['alignment_matrix']:
        report += "\nALIGNMENT MATRIX (Criterion → Outcomes)\n"
        report += "=" * 60 + "\n"
        for item in results['alignment_matrix']:
            report += f"\n{item['criterion']}\n"
            if item['aligned_outcomes']:
                for alignment in item['aligned_outcomes']:
                    outcome_id = alignment['outcome_id']
                    outcome = next(o for o in results['outcomes'] if o['id'] == outcome_id)
                    report += f"  → Outcome {outcome_id} ({alignment['confidence']} confidence)\n"
                    report += f"     {outcome['text'][:80]}...\n"
            else:
                report += f"  ⚠️  No outcomes aligned\n"

    # Bloom's level analysis
    report += "\n\nBLOOM'S TAXONOMY ANALYSIS\n"
    report += "=" * 60 + "\n"
    report += "Learning Outcomes by Bloom's Level:\n"

    for level in ['remember', 'understand', 'apply', 'analyze', 'evaluate', 'create']:
        count = len([o for o in results['outcomes'] if o['blooms_level'] == level])
        if count > 0:
            report += f"  {level.title()}: {count}\n"

    unknown_count = len([o for o in results['outcomes'] if o['blooms_level'] == 'unknown'])
    if unknown_count > 0:
        report += f"  ⚠️  Unknown/Unmeasurable: {unknown_count}\n"

    report += "\nRubric Criteria by Bloom's Level:\n"
    for level in ['remember', 'understand', 'apply', 'analyze', 'evaluate', 'create']:
        count = len([c for c in results['criteria'] if c['blooms_level'] == level])
        if count > 0:
            report += f"  {level.title()}: {count}\n"

    unknown_criteria_count = len([c for c in results['criteria'] if c['blooms_level'] == 'unknown'])
    if unknown_criteria_count > 0:
        report += f"  ⚠️  Unknown: {unknown_criteria_count}\n"

    # QM compliance summary
    report += "\n\nQM STANDARD 3.1 COMPLIANCE\n"
    report += "=" * 60 + "\n"
    report += "Standard: \"Assessments measure stated learning objectives\"\n\n"

    if not results['orphaned_criteria'] and not results['untested_outcomes']:
        report += "✅ COMPLIANT: All outcomes measured, all criteria aligned\n"
    else:
        report += "❌ NOT COMPLIANT: Fix alignment issues above\n"

    return report


def main():
    parser = argparse.ArgumentParser(
        description='Check outcome-rubric criteria alignment (QM Standard 3.1)'
    )
    parser.add_argument('--rubric', required=True,
                        help='Rubric markdown file')
    parser.add_argument('--outcomes', required=True,
                        help='Learning outcomes file (text or markdown)')
    parser.add_argument('--verbose', action='store_true',
                        help='Show detailed alignment matrix')

    args = parser.parse_args()

    # Validate files exist
    rubric_path = Path(args.rubric)
    outcomes_path = Path(args.outcomes)

    if not rubric_path.exists():
        print(f"Error: Rubric file not found: {rubric_path}")
        return 1

    if not outcomes_path.exists():
        print(f"Error: Outcomes file not found: {outcomes_path}")
        return 1

    # Extract outcomes and criteria
    print("Extracting learning outcomes...")
    outcomes = extract_outcomes(outcomes_path)
    print(f"Found {len(outcomes)} learning outcomes")

    print("Extracting rubric criteria...")
    criteria = extract_criteria(rubric_path)
    print(f"Found {len(criteria)} rubric criteria\n")

    # Check alignment
    results = check_alignment(outcomes, criteria, args.verbose)

    # Generate report
    report = generate_report(results, args.verbose)
    print(report)

    # Exit code
    if results['orphaned_criteria'] or results['untested_outcomes']:
        return 1
    else:
        return 0


if __name__ == '__main__':
    sys.exit(main())
