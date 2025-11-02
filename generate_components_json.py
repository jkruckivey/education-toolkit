#!/usr/bin/env python3
"""
Generate components.json for individual component installation in Claude Code marketplace.
Scans agents/, commands/, and skills/ directories and creates a catalog.
"""

import os
import json
import re
from pathlib import Path


def extract_frontmatter(content):
    """
    Extract YAML frontmatter from markdown file.
    Returns (frontmatter_dict, content_without_frontmatter).
    """
    if not content.startswith('---'):
        return {}, content

    # Find the closing ---
    end_index = content.find('---', 3)
    if end_index == -1:
        return {}, content

    frontmatter_text = content[3:end_index].strip()
    remaining_content = content[end_index + 3:].strip()

    # Parse YAML frontmatter (simple key: value pairs)
    frontmatter = {}
    for line in frontmatter_text.split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            frontmatter[key.strip()] = value.strip()

    return frontmatter, remaining_content


def scan_agents(agents_path):
    """Scan agents/ directory and return list of agent components."""
    agents = []

    if not os.path.isdir(agents_path):
        print(f"Warning: Agents directory not found: {agents_path}")
        return agents

    print(f"Scanning agents in {agents_path}...")

    for file_name in os.listdir(agents_path):
        if file_name.endswith('.md') and not file_name.endswith('DEPRECATED.md'):
            file_path = os.path.join(agents_path, file_name)

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                frontmatter, _ = extract_frontmatter(content)

                name = frontmatter.get('name', os.path.splitext(file_name)[0])
                description = frontmatter.get('description', '')

                # Determine category based on agent purpose
                category = categorize_agent(name, description)

                agent = {
                    'name': name,
                    'path': f"{category}/{file_name}",
                    'category': category,
                    'type': 'agent',
                    'content': content,
                    'description': description,
                    'downloads': 0,
                    'metadata': {
                        'tools': frontmatter.get('tools', ''),
                        'model': frontmatter.get('model', 'sonnet')
                    }
                }

                agents.append(agent)
                print(f"  [OK] Processed agent: {name} ({category})")

            except Exception as e:
                print(f"  [ERROR] Error reading {file_name}: {e}")

    return agents


def scan_commands(commands_path):
    """Scan commands/ directory and return list of command components."""
    commands = []

    if not os.path.isdir(commands_path):
        print(f"Warning: Commands directory not found: {commands_path}")
        return commands

    print(f"Scanning commands in {commands_path}...")

    for file_name in os.listdir(commands_path):
        if file_name.endswith('.md'):
            file_path = os.path.join(commands_path, file_name)

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                frontmatter, _ = extract_frontmatter(content)

                name = os.path.splitext(file_name)[0]
                description = frontmatter.get('description', '')

                # Determine category
                category = categorize_command(name, description)

                command = {
                    'name': name,
                    'path': f"{category}/{file_name}",
                    'category': category,
                    'type': 'command',
                    'content': content,
                    'description': description,
                    'downloads': 0
                }

                commands.append(command)
                print(f"  [OK] Processed command: {name} ({category})")

            except Exception as e:
                print(f"  [ERROR] Error reading {file_name}: {e}")

    return commands


def scan_skills(skills_path):
    """Scan skills/ directory and return list of skill components."""
    skills = []

    if not os.path.isdir(skills_path):
        print(f"Warning: Skills directory not found: {skills_path}")
        return skills

    print(f"Scanning skills in {skills_path}...")

    # Skills have structure: skills/skill-name/SKILL.md
    for skill_dir in os.listdir(skills_path):
        skill_dir_path = os.path.join(skills_path, skill_dir)

        if os.path.isdir(skill_dir_path) and not skill_dir.startswith('.'):
            skill_file = os.path.join(skill_dir_path, 'SKILL.md')

            if os.path.isfile(skill_file):
                try:
                    with open(skill_file, 'r', encoding='utf-8') as f:
                        content = f.read()

                    frontmatter, _ = extract_frontmatter(content)

                    name = frontmatter.get('name', skill_dir)
                    description = frontmatter.get('description', '')
                    version = frontmatter.get('version', '1.0.0')

                    # Determine category
                    category = categorize_skill(name, description)

                    skill = {
                        'name': name,
                        'path': f"{category}/{skill_dir}",
                        'category': category,
                        'type': 'skill',
                        'content': content,
                        'description': description,
                        'downloads': 0,
                        'metadata': {
                            'version': version
                        }
                    }

                    skills.append(skill)
                    print(f"  [OK] Processed skill: {name} ({category})")

                except Exception as e:
                    print(f"  [ERROR] Error reading {skill_dir}/SKILL.md: {e}")

    return skills


def categorize_agent(name, description):
    """Determine agent category based on name/description."""
    desc_lower = description.lower()
    name_lower = name.lower()

    # Widget-related
    if 'widget' in name_lower or 'widget' in desc_lower:
        return 'widget-design'

    # Assessment-related
    if 'assessment' in name_lower or 'rubric' in name_lower or 'pairr' in desc_lower:
        return 'assessment'

    # Accessibility-related
    if 'accessibility' in name_lower or 'wcag' in desc_lower:
        return 'accessibility'

    # Consistency/validation-related
    if 'consistency' in name_lower or 'threading' in name_lower or 'terminology' in name_lower or 'cohort-structure' in name_lower:
        return 'validation'

    # Course design
    if 'course' in name_lower or 'outline' in name_lower or 'storyboard' in name_lower:
        return 'course-design'

    # Review/testing
    if 'review' in name_lower or 'tester' in name_lower or 'simulator' in name_lower:
        return 'review-testing'

    # Code review
    if 'backend' in name_lower or 'frontend' in name_lower:
        return 'code-review'

    # Content generation
    if 'generator' in name_lower or 'udl' in name_lower or 'branding' in name_lower:
        return 'content'

    return 'general'


def categorize_command(name, description):
    """Determine command category based on name/description."""
    desc_lower = description.lower()
    name_lower = name.lower()

    if 'assessment' in name_lower or 'rubric' in name_lower:
        return 'assessment'

    if 'widget' in name_lower:
        return 'widget-design'

    if 'consistency' in name_lower or 'audit' in name_lower:
        return 'validation'

    if 'review' in name_lower or 'simulate' in name_lower:
        return 'review-testing'

    if 'storyboard' in name_lower or 'branding' in name_lower:
        return 'course-design'

    return 'general'


def categorize_skill(name, description):
    """Determine skill category based on name/description."""
    desc_lower = description.lower()
    name_lower = name.lower()

    if 'assessment' in name_lower or 'rubric' in desc_lower:
        return 'assessment'

    if 'accessibility' in name_lower or 'wcag' in desc_lower:
        return 'accessibility'

    if 'qm' in name_lower or 'quality' in desc_lower:
        return 'validation'

    return 'automation'


def generate_components_json():
    """Main function to generate components.json."""
    # Determine paths
    base_path = Path(__file__).parent
    agents_path = base_path / 'agents'
    commands_path = base_path / 'commands'
    skills_path = base_path / 'skills'

    # Output to docs/ for GitHub Pages hosting
    docs_path = base_path / 'docs'
    docs_path.mkdir(exist_ok=True)
    output_path = docs_path / 'components.json'

    print("=" * 60)
    print("Education Toolkit - Component Catalog Generator")
    print("=" * 60)
    print()

    # Scan directories
    agents = scan_agents(agents_path)
    commands = scan_commands(commands_path)
    skills = scan_skills(skills_path)

    # Sort alphabetically
    agents.sort(key=lambda x: x['name'])
    commands.sort(key=lambda x: x['name'])
    skills.sort(key=lambda x: x['name'])

    # Build components data
    components_data = {
        'agents': agents,
        'commands': commands,
        'skills': skills
    }

    # Write to file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(components_data, f, indent=2, ensure_ascii=False)

        print()
        print("=" * 60)
        print("SUCCESS: components.json generated")
        print("=" * 60)
        print()
        print(f"Summary:")
        print(f"  - Agents: {len(agents)}")
        print(f"  - Commands: {len(commands)}")
        print(f"  - Skills: {len(skills)}")
        print(f"  - Total: {len(agents) + len(commands) + len(skills)} components")
        print()
        print(f"Output: {output_path}")
        print()

        # Show category breakdown
        print("Category Breakdown:")
        categories = {}
        for component_type, components in components_data.items():
            for component in components:
                cat = component['category']
                if cat not in categories:
                    categories[cat] = {'agents': 0, 'commands': 0, 'skills': 0}
                categories[cat][component_type] += 1

        for category, counts in sorted(categories.items()):
            total = sum(counts.values())
            print(f"  - {category}: {total} ({counts['agents']}a, {counts['commands']}c, {counts['skills']}s)")

        print()
        print("=" * 60)

    except Exception as e:
        print(f"ERROR: Failed to write {output_path}: {e}")


if __name__ == '__main__':
    generate_components_json()
