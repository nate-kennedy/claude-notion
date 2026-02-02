---
description: Get organization suggestions for items
argument-hint: [task|note|project]
---

Analyze items and suggest better organization.

## Usage

- `/suggest` - Suggest organization for recent inbox items
- `/suggest task <name>` - Suggestions for specific task
- `/suggest note <name>` - Suggestions for specific note

## Tag Suggestions

Match content keywords to existing Tags:

| Keywords | Suggested Tag (Area) |
|----------|---------------------|
| work, job, office, meeting, client | Work |
| health, exercise, doctor, gym, fitness | Health |
| money, budget, bill, pay, finance | Finance |
| family, kids, home, house | Home & Family |
| learn, course, study, read | Learning |

**Implementation**:
1. Fetch all Tags from collection `2fafc9f9-93ac-81c6-ac00-000b62072c37`
2. Match task/note name against Tag names and descriptions
3. Suggest top 1-2 matches

## Project Suggestions

Suggest creating a project when:
- Task name contains multiple steps ("and", "then", numbered list)
- Task has subtasks
- Task mentions a deadline ("by Friday", "before March")
- Similar tasks exist (potential grouping)

**Example**:
"Research and book flights, then find hotel" → Suggest: Create "Trip Planning" project

## Smart List Suggestions

| Content Pattern | Suggested Smart List |
|-----------------|---------------------|
| "wait for", "follow up", "@person" | Delegated |
| "someday", "maybe", "might", "consider" | Someday |
| "next", "ready", "can do" | Do Next |

## Web Clip Detection

For Notes, detect if content is primarily a URL:
- Starts with http/https
- Contains only a URL and brief description

**Suggestion**: Convert to Web Clip (set Type property)

## Duplicate Detection

When creating items, check for similar existing items:
- Same or very similar name
- Created within last 7 days

**Alert**: "Similar task exists: <name>. Add to that instead?"

## Output Format

```
## Suggestions for "Call dentist about cleaning"

**Tag**: Health (matches: dentist, cleaning)
**Smart List**: Do Next (actionable, no blockers)
**Due Date**: Consider adding - calls often time-sensitive

No similar tasks found.
```
