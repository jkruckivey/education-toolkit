# Auto Code Review Hook

**Trigger**: Runs automatically after Write or Edit tool usage

**Purpose**: Reviews backend and frontend code changes for best practices, security, and performance

## Hook Instructions

When this hook triggers after a Write or Edit operation:

1. **Identify the file type** from the tool result:
   - Backend: `.py` files (especially in `backend/app/`)
   - Frontend: `.jsx`, `.js`, `.css` files (especially in `frontend/src/`)
   - Skip: config files, package.json, etc.

2. **Extract the file path and changes** from the tool result

3. **Route to appropriate reviewer**:
   - Python/FastAPI files → Launch backend-reviewer agent
   - React/JSX files → Launch frontend-reviewer agent
   - CSS files → Quick inline accessibility/design check
   - Skip review for non-code files

4. **Backend Review Criteria** (for .py files):
   - ✅ Endpoint security (authentication, validation)
   - ✅ Pydantic model validation
   - ✅ Error handling (try/except blocks)
   - ✅ Database query efficiency
   - ✅ API response structure consistency
   - ✅ Async/await usage

5. **Frontend Review Criteria** (for .jsx/.js files):
   - ✅ Accessibility (ARIA labels, semantic HTML)
   - ✅ State management patterns
   - ✅ Error handling (try/catch, user feedback)
   - ✅ Component reusability
   - ✅ Performance (unnecessary re-renders, memo usage)
   - ✅ UX feedback (loading states, error messages)

6. **Review Output Format**:
   ```
   📝 Code Review: {filename}

   ✅ Strengths:
   - [Positive aspects of the change]

   ⚠️ Suggestions:
   - [Improvement recommendations]

   🔴 Issues:
   - [Critical problems that should be fixed]
   ```

7. **When to skip review**:
   - Config files (.json, .md, .txt, .env)
   - Package files (package.json, requirements.txt)
   - Build outputs (dist/, build/)
   - Test files (unless explicitly reviewing test quality)

8. **Quick inline review** (don't launch agent) for:
   - Single-line changes
   - Comment-only changes
   - Formatting-only changes
   - CSS variable updates

9. **Launch agent review** for:
   - New functions/components
   - Logic changes (>10 lines)
   - API endpoint modifications
   - State management changes
   - Security-sensitive code

## Example Hook Behavior

**Scenario 1**: User edits `App.jsx` to fix assessment feedback flow
- Hook triggers on Edit tool completion
- Detects: frontend/.jsx file, 40+ line change
- Launches: frontend-reviewer agent
- Agent reviews: state management, error handling, user feedback
- Reports: Strengths (proper error handling), Suggestions (consider memoizing getCalibrationMessage)

**Scenario 2**: User edits `main.py` to add new endpoint
- Hook triggers on Edit tool completion
- Detects: backend/.py file, new endpoint function
- Launches: backend-reviewer agent
- Agent reviews: Pydantic validation, error handling, authentication
- Reports: Issues (missing input validation for confidence parameter)

**Scenario 3**: User edits `README.md`
- Hook triggers on Edit tool completion
- Detects: .md file (non-code)
- Skips review silently

## Important Notes

- **Non-blocking**: Review happens in background, doesn't prevent user from continuing work
- **Contextual**: Only reviews the specific file changed, not entire codebase
- **Actionable**: Focuses on specific line numbers and concrete suggestions
- **Learning**: Teaches best practices through feedback, not just criticism
