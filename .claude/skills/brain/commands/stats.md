---
description: Productivity statistics and metrics
argument-hint: [today|week|month]
---

Show productivity statistics and insights.

## Usage

- `/stats` - Overall dashboard
- `/stats today` - Today's metrics
- `/stats week` - This week's metrics
- `/stats month` - This month's metrics

## Metrics to Calculate

### Task Metrics

| Metric | Query |
|--------|-------|
| Completed today | Status = Done AND Completed = today |
| Completed this week | Status = Done AND Completed >= week start |
| Currently active | Status = Doing |
| Overdue | Due < today AND Status != Done |
| In inbox | No Project AND No Tag AND No Due |

### Project Metrics

| Metric | Calculation |
|--------|-------------|
| Active projects | Status = Doing |
| Progress % | Tasks Done / Total Tasks per project |
| Stalled projects | No task activity in 14+ days |

### Time Tracking Metrics

Query Work Sessions collection:

| Metric | Query |
|--------|-------|
| Time today | Sessions where Start = today, sum Duration (Mins) |
| Time this week | Sessions where Start >= week start |
| Avg session length | Average of Duration (Mins) |

### Goal Metrics

| Metric | Calculation |
|--------|-------------|
| Active goals | Goals with Target Date >= today |
| Milestones hit | Milestones with Done = checked |
| On track | Projects progressing toward deadline |

## Output Format

```
## Productivity Stats

### Today
- Completed: 5 tasks
- Time tracked: 3h 45m
- Active: 2 tasks in progress

### This Week
- Completed: 23 tasks
- Time tracked: 18h 30m
- Completion rate: 85%

### Projects
- 4 active projects
- "Website Redesign" 75% complete
- "Q1 Planning" stalled (no activity 12 days)

### Attention Needed
- 3 overdue tasks
- 8 items in inbox
```

## Calculations

### Completion Rate
```
completed_this_week / (completed_this_week + overdue + still_active_from_week_start)
```

### Project Progress
```
tasks_done / total_tasks * 100
```

### Average Task Age (Inbox)
```
sum(today - created_date) / inbox_count
```
