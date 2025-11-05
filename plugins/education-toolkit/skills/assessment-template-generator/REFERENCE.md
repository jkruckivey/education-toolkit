# Assessment Template Generator - Reference Documentation

## Research Foundations

### PAIRR Methodology
**Full Citation**: Hammond, M. (2025). "PAIRR: Peer and AI Review + Reflection for Equitable Writing Pedagogy." *Frontiers in Communication*, 10.

**Key Findings**:
- Dual-feedback (peer + AI) promotes AI literacy through comparative analysis
- Students develop critical evaluation skills by contrasting feedback sources
- Bonus points structure (5-7% of grade) incentivizes participation without high-stakes pressure
- Comparative reflection maintains student writerly agency (they choose which feedback to apply)
- Effective in graduate/professional programs (MBA, communications, marketing)

**Implementation Notes**:
- Works best with 80% complete drafts (not outlines or 30% drafts)
- Structured rubrics ensure peer and AI evaluate same criteria
- Post-revision reflection captures metacognitive learning
- Typical participation rate: 90% of students complete all PAIRR components

### AI Roleplay Exercises
**Pedagogical Rationale**:
- Tests application/synthesis (Bloom's Apply/Analyze/Evaluate levels)
- Authentic professional communication practice
- Immediate conversational feedback
- Lower faculty grading burden (AI provides initial evaluation)
- Accessibility: Oral alternative to written exams

**Types and Use Cases**:

1. **Diagnostic (Pre-Learning)**
   - Purpose: Reveal knowledge gaps BEFORE content delivery
   - Timing: Week 0 or start of unit
   - Grading: Participation only (5 pts)
   - Expected distribution: 50% Beginning, 35% Developing, 15% Proficient
   - Student experience: "I realized how much I didn't know—it motivated me to pay attention"

2. **Formative (Practice)**
   - Purpose: Safe space to rehearse application with feedback
   - Timing: Mid-unit before summative assessment
   - Grading: Optional bonus points or formative feedback only
   - Expected distribution: 20% Beginning, 40% Developing, 30% Proficient, 10% Exemplary
   - Student experience: "Helpful practice without the pressure of a grade"

3. **Summative (Graded)**
   - Purpose: Demonstrate mastery for grade
   - Timing: End of unit or as final assessment
   - Grading: Full rubric with point values (typically 25-30 pts)
   - Expected distribution: 5% Beginning, 25% Developing, 45% Proficient, 25% Exemplary
   - Student experience: "Better than written exams—I could explain my thinking in real-time"

**Uplimit Configuration Best Practices**:
- Hidden context should be 2-3x longer than visible context (detailed AI behavioral guidelines)
- Include "strong performance indicators" and "weak performance indicators" in hidden context
- Test AI character with 3-5 sample student responses before deployment
- Provide students with rubric access BEFORE conversation (transparency)
- Set realistic time limits (5-12 minutes depending on type)

### Diagnostic Rubrics (3-Level)
**Pedagogical Rationale**:
- Assesses CURRENT understanding, not mastery (so no "Exemplary" level)
- Non-evaluative language reduces anxiety about pre-learning gaps
- Support flags enable targeted interventions
- Creates baseline for measuring learning growth

**Why 3 Levels Instead of 4-5?**
- Faster grading (2-3 min per student vs. 5-7 min for summative rubrics)
- Less intimidating for students (simpler = more honest self-assessment)
- Sufficient granularity for diagnostic purposes
- Beginning → Developing → Proficient maps to: "Gaps to address" → "Some foundation" → "Ready for depth"

**Support Flag System**:
- **Red Flag** (all Beginning): Immediate intervention (office hours, tutoring referral)
- **Yellow Flag** (2+ Beginning OR all Developing): Monitor during learning
- **Green Flag** (mix Developing/Proficient): Standard instruction

**Using Diagnostic Results to Adjust Instruction**:
- >60% Beginning → Increase scaffolding, slow pacing, add glossary
- >40% Developing/Proficient → Quick review basics, add depth, use peer teaching
- Significant misconceptions → Address explicitly ("Many thought X, but actually...")

## Customization Examples

### Example 1: PAIRR for Business Memo (MBA Course)

**Context**: Week 3 assignment asks students to write investment recommendation memo

**Generated Command**:
```bash
python scripts/generate_pairr.py \
  --assignment-name "Week 3 Investment Memo" \
  --points 30 \
  --criteria "Strategic analysis, Evidence-based recommendations, Financial modeling, Professional writing"
```

**Customization After Generation**:
1. Replace `[DESCRIBE ASSIGNMENT GOAL HERE]` with: "write a 3-page investment recommendation memo analyzing whether a PE firm should acquire a professional sports franchise"
2. Set specific due dates in PAIRR participation rubric
3. Add course-specific rubric descriptors (e.g., "Strategic analysis: Must reference Porter's Five Forces and sports revenue ecosystem models from Week 2")

### Example 2: Diagnostic AI Roleplay (Sports Business Course)

**Context**: Week 1 pre-learning assessment on revenue streams knowledge

**Generated Command**:
```bash
python scripts/generate_ai_roleplay.py \
  --scenario "Explain Revenue Ecosystem to Team Owner" \
  --type diagnostic \
  --learning-outcome "Identify and explain interdependencies among major revenue streams in sports business"
```

**Customization After Generation**:
1. In scenario context, add: "Reference the Golden State Warriors case we'll study in Week 1"
2. In hidden context, add: "If student mentions 'star player effect,' probe with: 'Can you explain how that affects ALL revenue streams, not just one?'"
3. Test with sample responses: "Tickets and jerseys go up" (Beginning) vs. "Star player increases media rights value, which funds better facilities, which increases ticket demand" (Proficient)

### Example 3: Diagnostic Rubric (Data Analytics Course)

**Context**: Week 4 pre-learning assessment on SQL joins

**Generated Command**:
```bash
python scripts/generate_diagnostic_rubric.py \
  --skill-area "SQL Joins" \
  --week 4 \
  --criteria-count 3
```

**Customization After Generation**:
1. Replace generic criteria with course-specific examples:
   - Beginning: "Cannot distinguish between INNER JOIN and LEFT JOIN"
   - Developing: "Can describe difference but struggles to choose correct join type for scenario"
   - Proficient: "Correctly identifies when to use INNER vs. LEFT vs. RIGHT JOIN with rationale"

2. Add "typical responses" after first use with real student data:
   - Beginning: "They all do the same thing, right?" OR "I would just use INNER JOIN"
   - Developing: "LEFT JOIN includes all rows from left table... I think?"
   - Proficient: "Use LEFT JOIN to preserve all customers even if they have no orders, because the business question asks for customers who haven't purchased yet"

## Script Usage Tips

### generate_pairr.py

**Optimal Criteria Count**: 4 criteria (balanced between comprehensive and manageable)
- Too few (2-3): May miss important dimensions of quality
- Too many (6+): Overwhelming for peer reviewers and hard to calibrate

**Point Allocation**:
- Typical range: 25-35 points (allows 5 pt bonus to meaningfully impact grade)
- If assignment is <20 pts, consider reducing bonus to 3 pts
- If assignment is >50 pts, consider increasing bonus to 7-10 pts

**Best For**:
- Written assignments: essays, memos, reports, case analyses
- Graduate/professional programs (undergrads may need more PAIRR scaffolding)
- Courses emphasizing professional writing or AI literacy

### generate_ai_roleplay.py

**Scenario Type Detection**: Script auto-detects scenario type from title keywords:
- "pitch", "present", "investment" → pitch scenario (VC/PE partner)
- "negotiate", "sales", "deal" → negotiation scenario (buyer/seller)
- "consult", "advise", "counsel" → consultation scenario (expert advisor)
- "defend", "justify", "board" → defense scenario (board Q&A)

**Custom AI Characters**: Override auto-generated defaults:
```bash
--ai-character-name "Dr. Elena Rodriguez, Chief Medical Officer" \
--ai-character-role "Hospital CMO evaluating new treatment protocol"
```

**Time Limits by Type**:
- Diagnostic: 5-7 minutes (quick knowledge check)
- Formative: 8-10 minutes (practice with feedback)
- Summative: 10-12 minutes (thorough mastery demonstration)

### generate_diagnostic_rubric.py

**Criteria Count Recommendations**:
- 2 criteria: Too narrow (use only for very focused diagnostics)
- 3 criteria: Sweet spot (balanced depth and grading speed)
- 4 criteria: Maximum (any more slows grading too much for formative assessment)

**Week/Module Numbering**: Used contextually in:
- Student instructions: "before Week 4 begins"
- Support flags: "check in during Week 4"
- Timeline: "assign at end of Week 3"

**Skill Area Naming**: Use specific, student-facing language:
- ✅ "Revenue Streams Knowledge" (clear, concrete)
- ❌ "Financial Acumen" (too vague)
- ✅ "SQL Joins Syntax and Application" (precise)
- ❌ "Database Skills" (too broad)

## Integration with Agents

### assessment-designer agent invocations

**User Request**: "Create a PAIRR assignment for my marketing strategy memo"

**Agent Action**:
1. Ask clarifying questions: point value? rubric criteria?
2. Invoke skill: `Skill: assessment-template-generator`
3. Run command: `python scripts/generate_pairr.py --assignment-name "Marketing Strategy Memo" --points 30 --criteria "Market analysis, Competitive positioning, Creative strategy, Budget justification"`
4. Read generated file
5. Customize template with course-specific details
6. Present to user

**User Request**: "Design a pre-learning diagnostic for Week 2 on design thinking"

**Agent Action**:
1. Determine diagnostic type: rubric or AI roleplay?
2. If rubric: Invoke `generate_diagnostic_rubric.py --skill-area "Design Thinking Principles" --week 2`
3. If AI roleplay: Invoke `generate_ai_roleplay.py --scenario "Apply Design Thinking to Product Challenge" --type diagnostic --learning-outcome "Identify and apply 5 stages of design thinking"`
4. Customize generated template
5. Present to user

### rubric-generator agent invocations

**User Request**: "Generate a diagnostic rubric for my stats course"

**Agent Action**:
1. Ask: what skill area? which week?
2. Invoke skill: `Skill: assessment-template-generator`
3. Run: `python scripts/generate_diagnostic_rubric.py --skill-area "Hypothesis Testing" --week 3`
4. Present to user

**Note**: rubric-generator focuses on quick rubric generation. For comprehensive assessment design with PAIRR or AI roleplay, user should use assessment-designer agent instead.

## Common Issues & Troubleshooting

### Issue: PAIRR Rubric Points Don't Add Up
**Cause**: Remainder points from division not distributed evenly
**Fix**: Script automatically distributes remainder to first N criteria
**Example**: 30 pts ÷ 4 criteria = 7.5 pts each → 8, 8, 7, 7 pts

### Issue: AI Roleplay Character Too Easy/Hard
**Cause**: Hidden context needs calibration
**Fix**:
- Too easy: Add "Probe deeply with 'How do you know that?'" and "Don't accept surface-level claims"
- Too hard: Add "Use Socratic questions to guide, not stump" and "If student struggles, offer hints"

### Issue: Diagnostic Rubric "Beginning" Level Sounds Punitive
**Cause**: Language needs to be descriptive, not evaluative
**Fix**:
- ❌ "Poor understanding, fails to identify..."
- ✅ "Cannot yet demonstrate... Typical responses: [neutral examples]"

### Issue: Students Complain PAIRR Is "Extra Work"
**Cause**: Bonus points perceived as insufficient motivation
**Fix**:
- Frame as "this replaces peer review, not adds to it"
- Emphasize AI literacy skill development (workplace-relevant)
- Increase bonus to 7-10% of grade if feasible
- Show data: "Students who complete PAIRR score 8% higher on average"

### Issue: AI Roleplay Doesn't Match Uplimit Platform Format
**Cause**: Uplimit updates field names/structure
**Fix**: Generated template uses standard Uplimit tabs (Learning Objective, Scenario, Hidden Context, Criteria). If Uplimit changes, update script templates to match new field names.

## Future Enhancements

**Planned Features**:
1. **Multi-language support**: Generate PAIRR/rubrics in Spanish, French, Mandarin
2. **Discipline-specific templates**: Pre-configured for business, STEM, humanities, healthcare
3. **Integration with LMS APIs**: Auto-upload generated rubrics to Canvas/D2L
4. **Student data import**: Use past student responses to improve "typical responses" in diagnostic rubrics
5. **AI character personality profiles**: Library of tested AI characters (skeptical VC, supportive mentor, detail-oriented analyst)

**Community Contributions Welcome**:
- Share customized templates that worked well in your courses
- Report bugs or edge cases
- Suggest new assessment methodologies to automate
- Contribute discipline-specific rubric criteria libraries

## Additional Resources

**Research Articles**:
- Hammond (2025) - PAIRR methodology
- Frontiers in Communication (2025) - AI literacy through comparative feedback
- [Additional research citations in assessment-designer agent knowledge base]

**Uplimit Documentation**:
- AI Roleplay configuration: [Uplimit help docs]
- Rubric builder: [Uplimit help docs]

**WCAG Accessibility**:
- Ensure generated templates use semantic HTML when converted
- Provide alternative formats (text, audio) for rubrics
- Caption any video examples

**Quality Matters Standards**:
- Generated rubrics align with QM Standard 3 (Assessment and Measurement)
- Include clear instructions (QM Standard 5)
- Support learner success (QM Standard 7)
