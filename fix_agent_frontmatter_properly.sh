#!/bin/bash

cd "$(dirname "$0")"

# Function to update agent frontmatter properly
update_agent() {
  local agent_name="$1"
  local new_description="$2"
  local agent_file="plugins/$agent_name/agents/$agent_name.md"

  if [ -f "$agent_file" ]; then
    # Extract tools and model from current frontmatter
    tools=$(grep "^tools:" "$agent_file" | head -1 | sed 's/^tools: //')
    model=$(grep "^model:" "$agent_file" | head -1 | sed 's/^model: //')

    # Extract body (everything after the second ---)
    body=$(awk '/^---$/{count++; if(count==2){flag=1; next}} flag' "$agent_file")

    # Write new file with fixed frontmatter
    cat > "$agent_file" << EOF
---
name: $agent_name
description: $new_description
tools: $tools
model: $model
---
$body
EOF

    echo "✓ Fixed $agent_name"
  fi
}

# Update all 17 agents
update_agent "accessibility-auditor" "Audits HTML/CSS files for WCAG 2.2 AA compliance, identifying accessibility issues with specific fixes for color contrast, alt text, heading hierarchy, ARIA labels, and keyboard navigation"

update_agent "assessment-consistency-checker" "Validates assessment consistency across course weeks by checking PAIRR methodology alignment, rubric point totals, learning outcome connections, grading distribution, and course-type compliance (cohort vs self-paced)"

update_agent "assessment-designer" "Designs comprehensive assessments with AI integration strategies, UDL/QM compliance checking, and alternative assessment approaches. Includes 464 KB bundled knowledge base with frameworks and AI assessment research"

update_agent "backend-reviewer" "Reviews FastAPI/Python code for educational technology projects, focusing on security vulnerabilities, error handling patterns, API design conventions, and performance optimization"

update_agent "branding-checker" "Validates course content against platform branding guidelines for Canvas LMS and Uplimit, ensuring design consistency, symbol usage, and visual standards compliance"

update_agent "cohort-structure-checker" "Validates cohort course structural consistency by verifying module sequences, element patterns, learning outcomes widgets placement, Final Project Connections quality, and PAIRR methodology implementation"

update_agent "concept-threading-checker" "Validates concept threading across course weeks by tracking Week 1 concepts through later modules, identifying orphaned concepts, verifying progressive complexity, and checking callback language"

update_agent "course-outline-creator" "Creates strategic course outlines with Course Learning Outcomes (CLOs), weekly structure, Module Learning Outcomes (MLOs), assessment strategy, and concept threading plans for new or restructured courses"

update_agent "frontend-reviewer" "Reviews React/JSX code with WCAG 2.2 AA accessibility specialization, checking React best practices, accessibility compliance, UX patterns, error messaging, and performance optimization"

update_agent "peer-review-simulator" "Simulates a design review panel with 6 instructional design specialists (Content, Accessibility, Visual Design, Technical, Pedagogical, UX), providing comprehensive multi-perspective feedback with prioritized action plans"

update_agent "rubric-generator" "Generates QM-aligned rubrics from learning outcomes with student-facing and faculty versions, quick scaffolding for assignments and projects"

update_agent "student-journey-simulator" "Simulates student experiences through course content with 4 learning personas (Visual, Analytical, Collaborative, Time-Constrained), identifying pedagogical issues and testing course flow across multiple weeks"

update_agent "terminology-consistency-checker" "Validates terminology consistency across course weeks by building course glossaries, flagging term variations, identifying undefined terms and acronyms, and checking capitalization patterns"

update_agent "udl-content-generator" "Creates alternative content formats and implements Universal Design for Learning (UDL) principles by generating audio scripts, infographic suggestions, and transformations for diverse learners"

update_agent "uplimit-storyboard-builder" "Creates comprehensive storyboards (BUILD MODE) and audits existing storyboards (AUDIT MODE) for Uplimit platform compliance, generating copy-paste-ready implementation guides and verifying interactivity standards"

update_agent "widget-designer" "Generates new interactive widgets with standardized design system (Geist typography, neutral color palette, no emojis) and audits existing widgets for design consistency, accessibility compliance, and export format standards"

update_agent "widget-tester" "Tests interactive educational widgets with 3 simulated student personas (Quick Learner, Methodical Analyst, Struggling Student), identifying UX issues, accessibility problems, and usability concerns"

echo ""
echo "✓ Fixed all 17 agent frontmatter sections properly"
