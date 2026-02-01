---
description: Show today's focus from Ultimate Brain
argument-hint:
---

Display a summary of today's work: My Day tasks, due today, and overdue items.

## Usage

```
/today
```

## Output Sections

### 1. My Day Tasks
Tasks with the "My Day" checkbox checked. These are what the user deliberately chose to focus on today.

### 2. Due Today
Tasks with Due date = today that aren't already in My Day.

### 3. Overdue
Tasks with Due date < today and Status != Done.

### 4. Quick Stats
- Total tasks for today
- Completed today
- Remaining

## Example Output

```
## Today's Focus (Feb 1, 2026)

### My Day (3 tasks)
| Task | Project | Priority | Status |
|------|---------|----------|--------|
| Review Q1 budget | Finance | High | To Do |
| Call dentist | - | Medium | To Do |
| Update website copy | Marketing | Low | Doing |

### Due Today (1 task)
| Task | Project |
|------|---------|
| Submit expense report | Work Ongoing |

### Overdue (2 tasks)
| Task | Due | Days Late |
|------|-----|-----------|
| Renew domain | Jan 28 | 4 |
| Reply to vendor email | Jan 30 | 2 |

---
**Progress:** 2/6 complete | **Focus:** 3 in My Day
```

## Implementation

1. Search Tasks database for:
   - My Day = checked AND Status != Done
   - Due = today AND Status != Done
   - Due < today AND Status != Done

2. Use `mcp__notion__notion-search` with appropriate filters

3. Format results in a scannable table

4. Include Notion URLs for each task

## Tips to Offer

- If My Day is empty: "Add tasks to My Day with /task add-to-day <task>"
- If many overdue: "Consider rescheduling or moving to Someday"
- If all done: "Great work! Plan tomorrow with /review"
