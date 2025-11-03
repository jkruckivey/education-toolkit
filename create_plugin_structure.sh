#!/bin/bash

# Create 18 individual plugins from agents
cd "$(dirname "$0")"

# List of agents (excluding DEPRECATED)
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
  echo "Creating plugin: $agent"

  # Create plugin directory structure
  mkdir -p "plugins/$agent/.claude-plugin"
  mkdir -p "plugins/$agent/agents"

  # Copy agent file
  cp "agents/$agent.md" "plugins/$agent/agents/"

  # Create plugin.json
  cat > "plugins/$agent/.claude-plugin/plugin.json" << EOF
{
  "name": "$agent",
  "version": "2.8.2",
  "description": "TODO: Add description from agent file",
  "author": {
    "name": "James Kruck",
    "email": "jkruck@ivey.ca"
  },
  "category": "education",
  "license": "MIT"
}
EOF

  echo "  ✓ Created plugins/$agent/"
done

echo ""
echo "✓ Created 17 plugin directories"
echo "Next steps:"
echo "1. Update plugin.json descriptions"
echo "2. Update marketplace.json to list all plugins"
echo "3. Copy knowledge bases for assessment-designer"
