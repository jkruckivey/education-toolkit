#!/bin/bash

cd "$(dirname "$0")"

# Function to extract description from agent YAML frontmatter
extract_description() {
  local agent_file="$1"
  # Extract description line, remove 'description: ' prefix, and clean up
  grep "^description:" "$agent_file" | sed 's/^description: //' | sed 's/Use this subagent to //' | sed 's/Use this agent to //'
}

# List of agents
agents=(
  "accessibility-auditor"
  "assessment-consistency-checker"
  "assessment-designer"
  "backend-reviewer"
  "branding-checker"
  "cohort-structure-checker"
  "concept-threading-checker"
  "course-outline-creator"
  "frontend-reviewer"
  "peer-review-simulator"
  "rubric-generator"
  "student-journey-simulator"
  "terminology-consistency-checker"
  "udl-content-generator"
  "uplimit-storyboard-builder"
  "widget-designer"
  "widget-tester"
)

for agent in "${agents[@]}"; do
  agent_file="plugins/$agent/agents/$agent.md"
  plugin_json="plugins/$agent/.claude-plugin/plugin.json"

  if [ -f "$agent_file" ]; then
    # Extract description
    desc=$(extract_description "$agent_file")

    # Truncate to first 200 chars for plugin description
    desc_short=$(echo "$desc" | cut -c1-200)

    echo "Updating $agent..."
    echo "  Description: $desc_short"

    # Update plugin.json with description
    cat > "$plugin_json" << EOF
{
  "name": "$agent",
  "version": "2.8.2",
  "description": "$desc_short",
  "author": {
    "name": "James Kruck",
    "email": "jkruck@ivey.ca"
  },
  "homepage": "https://github.com/jkruckivey/education-toolkit",
  "repository": {
    "type": "git",
    "url": "https://github.com/jkruckivey/education-toolkit"
  },
  "category": "education",
  "license": "MIT"
}
EOF
  fi
done

echo ""
echo "✓ Updated all plugin.json files with descriptions"
