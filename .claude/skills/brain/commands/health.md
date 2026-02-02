---
description: System health check - find items needing attention
argument-hint: [full]
---

Identify items in your Ultimate Brain that need attention.

## Usage

- `/health` - Quick health summary
- `/health full` - Detailed report with all issues

## Health Checks

### Inbox Status
Query Tasks collection for items with no Project, no Tag, no Due date.

```
Filter: Project is empty AND Tag is empty AND Due is empty AND Status != Done
```

**Thresholds:**
- 0-5 items: ✓ Healthy
- 6-10 items: ⚠️ Process soon
- 11+ items: ❌ Inbox overflow

### Stale Inbox Items
Items in inbox > 7 days without processing.

```
Filter: (inbox criteria) AND Created < 7 days ago
```

### Active Tasks Without Dates
Tasks marked "Doing" in projects but no Due date.

```
Filter: Status = Doing AND Due is empty
```

### Dormant Projects
Projects with Status = Doing but no task activity in 14+ days.

```
Check: Project.Tasks where any modified in last 14 days
```

### Forgotten Someday
Tasks with Smart List = Someday, not reviewed in 30+ days.

```
Filter: Smart List = Someday AND Last Edited < 30 days ago
```

### Overdue Tasks
Tasks past their Due date.

```
Filter: Due < today AND Status != Done
```

## Output Format

```
## System Health Report

### ✓ Healthy
- Inbox: 3 items (process within 24h)

### ⚠️ Needs Attention
- 2 tasks in Doing without due dates
- 1 project dormant for 3 weeks

### ❌ Action Required
- 5 overdue tasks
- 12 inbox items (overflow)
```

## Recommendations

For each issue found, suggest specific action:
- Overdue → Reschedule or complete
- Inbox overflow → Schedule processing session
- Dormant project → Review: still active? Someday? Archive?
- Forgotten someday → Review: still want? Delete? Activate?
