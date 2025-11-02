#!/usr/bin/env python3
"""
AI Roleplay Exercise Configuration Generator

Generates Uplimit-compatible AI roleplay scenarios with student instructions,
AI character setup, system prompts, and rubrics.
"""

import argparse
import sys
from datetime import datetime


SCENARIO_TEMPLATES = {
    "pitch": {
        "ai_name": "Jordan Martinez, Senior Partner",
        "ai_role": "Senior partner at private equity firm evaluating investment opportunity",
        "student_role": "Junior analyst pitching investment recommendation"
    },
    "negotiation": {
        "ai_name": "Alex Chen, Procurement Director",
        "ai_role": "Potential client evaluating purchase decision",
        "student_role": "Sales representative"
    },
    "consultation": {
        "ai_name": "Dr. Sarah Williams, Department Head",
        "ai_role": "Department leader seeking expert advice",
        "student_role": "Subject matter expert consultant"
    },
    "defense": {
        "ai_name": "Board Member Panel",
        "ai_role": "Board members evaluating strategic recommendation",
        "student_role": "Executive presenting strategic plan"
    }
}


def detect_scenario_type(scenario_title: str) -> str:
    """Auto-detect scenario type from title"""
    title_lower = scenario_title.lower()
    if any(word in title_lower for word in ['pitch', 'present', 'investment']):
        return "pitch"
    elif any(word in title_lower for word in ['negotiate', 'sales', 'deal']):
        return "negotiation"
    elif any(word in title_lower for word in ['consult', 'advise', 'counsel']):
        return "consultation"
    elif any(word in title_lower for word in ['defend', 'justify', 'board']):
        return "defense"
    return "pitch"  # default


def generate_rubric_criteria(assessment_type: str, learning_outcome: str) -> list[dict]:
    """Generate appropriate rubric criteria based on assessment type"""

    if assessment_type == "diagnostic":
        # 3 criteria without points
        return [
            {
                "name": "Knowledge Application",
                "description": f"Demonstrates understanding related to: {learning_outcome}",
                "points": None,
                "levels": ["Beginning", "Developing", "Proficient"]
            },
            {
                "name": "Communication Clarity",
                "description": "Expresses ideas clearly and responds to questions",
                "points": None,
                "levels": ["Beginning", "Developing", "Proficient"]
            },
            {
                "name": "Critical Thinking",
                "description": "Addresses challenges and refines arguments when questioned",
                "points": None,
                "levels": ["Beginning", "Developing", "Proficient"]
            }
        ]

    elif assessment_type == "formative":
        # 3-4 criteria with optional points
        return [
            {
                "name": "Content Knowledge",
                "description": f"Applies concepts from course content: {learning_outcome}",
                "points": 5,
                "levels": ["Exemplary", "Proficient", "Developing", "Beginning"]
            },
            {
                "name": "Evidence-Based Argumentation",
                "description": "Supports claims with specific examples and data",
                "points": 5,
                "levels": ["Exemplary", "Proficient", "Developing", "Beginning"]
            },
            {
                "name": "Professional Communication",
                "description": "Communicates clearly, listens actively, asks clarifying questions",
                "points": 3,
                "levels": ["Exemplary", "Proficient", "Developing", "Beginning"]
            }
        ]

    else:  # summative
        # 4-5 criteria with point values
        return [
            {
                "name": "Mastery of Learning Outcome",
                "description": f"Demonstrates mastery: {learning_outcome}",
                "points": 10,
                "levels": ["Exemplary", "Proficient", "Developing", "Beginning"]
            },
            {
                "name": "Evidence-Based Argumentation",
                "description": "Supports claims with specific data, examples, and course references",
                "points": 10,
                "levels": ["Exemplary", "Proficient", "Developing", "Beginning"]
            },
            {
                "name": "Critical Thinking Under Pressure",
                "description": "Responds thoughtfully to challenges, refines arguments, acknowledges limitations",
                "points": 5,
                "levels": ["Exemplary", "Proficient", "Developing", "Beginning"]
            },
            {
                "name": "Professional Communication",
                "description": "Communicates clearly, listens actively, manages time effectively",
                "points": 5,
                "levels": ["Exemplary", "Proficient", "Developing", "Beginning"]
            }
        ]


def generate_hidden_context(assessment_type: str, scenario_title: str) -> str:
    """Generate AI character behavioral guidelines"""

    if assessment_type == "diagnostic":
        return """You are assessing the student's CURRENT understanding BEFORE formal learning. Students are expected to struggle—your goal is to reveal knowledge gaps, not evaluate performance.

Behavioral guidelines:
- Start with an open-ended question: "Explain your thinking about [topic]"
- Ask "How do you know that?" when they make claims
- Probe for depth: "Can you give me a specific example?"
- DO NOT teach or provide correct answers
- Use Socratic questioning to reveal what they don't know
- If they're completely stuck, note it and move to next question (don't rescue them)
- Keep conversation to 5-7 minutes
- End with: "Thank you. This helps me understand where you're starting from."

Assessment focus:
- What do they already know?
- What misconceptions exist?
- Where are the biggest gaps?
- Are they aware of what they don't know?"""

    elif assessment_type == "formative":
        return f"""You are a supportive {scenario_title.lower()} partner helping the student PRACTICE applying course concepts. This is a learning opportunity, not a final evaluation.

Behavioral guidelines:
- Start by asking them to explain their approach
- Gently challenge weak points with "What about [alternative perspective]?"
- Reward strong reasoning with "That's a good point. Can you expand on that?"
- If they struggle, offer guiding questions (not answers)
- Encourage them to reference specific course content
- Allow course correction and revised arguments
- Keep conversation to 8-10 minutes
- End with 1-2 specific suggestions for improvement

Assessment focus:
- Are they applying course concepts correctly?
- Can they support claims with evidence?
- Do they respond well to feedback in real-time?
- Where do they need more practice before summative assessment?"""

    else:  # summative
        return f"""You are a professional {scenario_title.lower()} evaluator assessing the student's MASTERY of course concepts. This is a graded, high-stakes conversation.

Behavioral guidelines:
- Start by asking them to present their main argument (30-60 seconds)
- Probe deeply on any claim without evidence: "How do you know that?"
- Challenge assumptions: "What if [scenario]?"
- Reward specific course references: "Good—can you connect that to [related concept]?"
- DO NOT let them off easy—push for depth and precision
- If they make errors, note them but don't correct (this is assessment, not teaching)
- Use Socratic questioning to test understanding limits
- Keep conversation to 10-12 minutes
- End when you've assessed all rubric criteria OR time expires

Strong performance indicators:
- References specific course content (frameworks, data, case examples)
- Acknowledges limitations and trade-offs
- Responds to challenges by refining (not abandoning) arguments
- Asks clarifying questions about your concerns
- Demonstrates synthesis across multiple course concepts

Weak performance indicators:
- Vague or generic claims without evidence
- Ignores your challenges or repeats same points
- Cannot connect ideas to course content
- Defensive rather than analytical responses"""


def generate_ai_roleplay_template(scenario: str, assessment_type: str, learning_outcome: str,
                                   ai_character_name: str = None, ai_character_role: str = None,
                                   output: str = None) -> str:
    """Generate AI roleplay configuration in Uplimit format"""

    # Auto-detect scenario type and get defaults
    scenario_type = detect_scenario_type(scenario)
    defaults = SCENARIO_TEMPLATES.get(scenario_type, SCENARIO_TEMPLATES["pitch"])

    ai_name = ai_character_name or defaults["ai_name"]
    ai_role = ai_character_role or defaults["ai_role"]
    student_role = defaults["student_role"]

    # Generate rubric criteria
    criteria = generate_rubric_criteria(assessment_type, learning_outcome)
    total_points = sum(c["points"] for c in criteria if c["points"])

    # Generate hidden context
    hidden_context = generate_hidden_context(assessment_type, scenario)

    # Generate output filename
    if not output:
        output = f"ai-roleplay-{scenario.lower().replace(' ', '-')}.md"

    # Determine rubric settings based on type
    if assessment_type == "diagnostic":
        grading_enabled = "☐"
        levels_enabled = "☑"
        points_enabled = "☐"
    elif assessment_type == "formative":
        grading_enabled = "☐"  # optional
        levels_enabled = "☑"
        points_enabled = "☑"  # optional bonus points
    else:  # summative
        grading_enabled = "☑"
        levels_enabled = "☑"
        points_enabled = "☑"

    template = f"""# AI Roleplay Exercise: {scenario}

**Assessment Type**: {assessment_type.capitalize()}
**Learning Outcome**: {learning_outcome}
**Generated**: {datetime.now().strftime('%Y-%m-%d')}

---

## Uplimit Configuration

### LEARNING OBJECTIVE TAB

**Name**: {scenario}

**Learning Objective**: {learning_outcome}

**Scenario Setup**: ☑ Set scenario context (controlled by instructor)

---

### SCENARIO TAB

**Context** (visible to students):

You are participating in a conversational assessment to demonstrate your understanding of course concepts. {'This is a PRE-LEARNING diagnostic—you are not expected to know everything yet.' if assessment_type == 'diagnostic' else 'This is a practice opportunity to apply what you have learned.' if assessment_type == 'formative' else 'This is a graded assessment of your mastery.'}

Your task: {f'Engage in this conversation and do your best to explain your current thinking. There are no wrong answers—this helps identify where to focus your learning.' if assessment_type == 'diagnostic' else f'Practice applying course concepts in a realistic scenario. You will receive feedback to help you prepare for summative assessment.' if assessment_type == 'formative' else f'Demonstrate mastery by engaging professionally and supporting your arguments with specific course content.'}

You have {f'5-7 minutes' if assessment_type == 'diagnostic' else f'8-10 minutes' if assessment_type == 'formative' else f'10-12 minutes'} for this conversation.

**Name of AI**: {ai_name}

**Role of AI**: {ai_role}

**Role of student**: {student_role}

---

### HIDDEN CONTEXT TAB

*(This context is invisible to students but guides AI behavior)*

{hidden_context}

---

### CRITERIA TAB (Feedback Rubric)

**Rubric Settings**:
- {grading_enabled} Enable automated AI grading
- {levels_enabled} Include evaluation levels
- {points_enabled} Apply points{f' (Total: {total_points} points)' if total_points else ''}

**Criteria**:

{chr(10).join([f'''
{i+1}. **{c["name"]}** {f"({c['points']} points)" if c["points"] else ""}
   *Description*: {c["description"]}
   *Evaluation Levels*: {" | ".join(c["levels"])}
''' for i, c in enumerate(criteria)])}

---

## Faculty Implementation Guide

### Before Deployment
1. **Test the AI character**: Run through the scenario yourself to ensure AI behaves as expected
2. **Calibrate difficulty**: Adjust hidden context if AI is too easy/hard
3. **Set expectations**: Brief students on conversation length and assessment type
4. **Provide rubric access**: Students should see criteria before conversation (transparency)

### Student Instructions
Provide students with:
- Link to the roleplay exercise in Uplimit
- Rubric criteria (what they'll be evaluated on)
- Time limit ({f'5-7 minutes' if assessment_type == 'diagnostic' else f'8-10 minutes' if assessment_type == 'formative' else f'10-12 minutes'})
- {'Reassurance that struggle is expected and normal' if assessment_type == 'diagnostic' else 'Reminder that this is practice with formative feedback' if assessment_type == 'formative' else 'Expectations for professional communication and evidence-based arguments'}

### Post-Conversation
- **Diagnostic**: Review AI feedback to identify common gaps → adjust Week 1 content
- **Formative**: Students receive AI feedback to guide revision before summative work
- **Summative**: AI provides initial grading → instructor reviews and adjusts if needed

### Customization Tips
- **Scenario context**: Make it course-specific by referencing actual case studies, frameworks, or data from your course
- **AI character personality**: Adjust "hidden context" to be more supportive/challenging based on student needs
- **Rubric criteria**: Modify to align with your specific learning outcomes

---

## Expected Student Performance

### Diagnostic (Pre-Learning)
- **Typical distribution**: 50% Beginning, 35% Developing, 15% Proficient
- **Goal**: Identify gaps, not evaluate performance
- **Student reaction**: Many will feel challenged—this is intentional and pedagogically sound

### Formative (Practice)
- **Typical distribution**: 20% Beginning, 40% Developing, 30% Proficient, 10% Exemplary
- **Goal**: Practice application with feedback before graded assessment
- **Student reaction**: Appreciate low-stakes opportunity to test understanding

### Summative (Graded)
- **Typical distribution**: 5% Beginning, 25% Developing, 45% Proficient, 25% Exemplary
- **Goal**: Demonstrate mastery for grade
- **Student reaction**: Value alternative to written exams; oral assessment reduces AI plagiarism concerns

---

## Research Support for AI Roleplay Assessments

**Benefits**:
- Tests application/synthesis (higher Bloom's levels)
- Authentic professional communication practice
- Immediate conversational feedback
- Accessibility: Oral assessment alternative for diverse learners
- Lower faculty grading time (AI provides initial evaluation)

**Best For**:
- Professional programs (business, healthcare, education, law)
- Communication-focused learning outcomes
- Courses emphasizing real-world application
- Alternative to written exams

**Limitations**:
- Requires student comfort with oral communication (provide practice opportunities first)
- AI character quality depends on hidden context specificity
- May disadvantage students with language barriers (consider accommodations)

---

## Customization Checklist

Before distributing to students:
- [ ] Customize scenario context with course-specific details
- [ ] Adjust AI character personality in hidden context
- [ ] Modify rubric criteria to match your learning outcomes
- [ ] Set appropriate time limit
- [ ] Test AI character behavior with sample conversations
- [ ] Provide students with rubric access and clear expectations
- [ ] Decide on grading approach (AI-generated scores vs. instructor review)
"""

    # Write to file
    with open(output, 'w', encoding='utf-8') as f:
        f.write(template)

    return output


def main():
    parser = argparse.ArgumentParser(
        description='Generate AI Roleplay exercise configuration in Uplimit format'
    )
    parser.add_argument('--scenario', required=True,
                        help='Scenario title (e.g., "Practice Investment Pitch")')
    parser.add_argument('--type', required=True, choices=['diagnostic', 'formative', 'summative'],
                        help='Assessment type: diagnostic (pre-learning) | formative (practice) | summative (graded)')
    parser.add_argument('--learning-outcome', required=True,
                        help='The course learning outcome being assessed')
    parser.add_argument('--ai-character-name',
                        help='Name of AI role (default: auto-generated from scenario)')
    parser.add_argument('--ai-character-role',
                        help='Role description (default: auto-generated from scenario)')
    parser.add_argument('--output',
                        help='Output filename (default: ai-roleplay-{scenario}.md)')

    args = parser.parse_args()

    # Generate template
    output_file = generate_ai_roleplay_template(
        scenario=args.scenario,
        assessment_type=args.type,
        learning_outcome=args.learning_outcome,
        ai_character_name=args.ai_character_name,
        ai_character_role=args.ai_character_role,
        output=args.output
    )

    print(f"[OK] AI Roleplay configuration generated: {output_file}")
    print(f"   Scenario: {args.scenario}")
    print(f"   Type: {args.type}")
    print(f"   Learning Outcome: {args.learning_outcome}")
    print("\nNext steps:")
    print("1. Review and customize scenario context (make it course-specific)")
    print("2. Test AI character behavior with sample conversations")
    print("3. Adjust hidden context if AI is too easy/challenging")
    print("4. Upload to Uplimit and assign to students")

    return 0


if __name__ == '__main__':
    sys.exit(main())
