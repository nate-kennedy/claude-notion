---
description: Set up recurring task schedule
argument-hint: <task> <schedule>
---

Create or update a recurring task schedule.

## Usage

- `/recur <task> daily` - Every day
- `/recur <task> weekly` - Every week  
- `/recur <task> MWF` - Monday, Wednesday, Friday
- `/recur <task> monthly` - Every month

## Recur Unit Values

| Schedule | Recur Unit | Recur Interval |
|----------|------------|----------------|
| Daily | Day(s) | 1 |
| Every 2 days | Day(s) | 2 |
| Weekly | Week(s) | 1 |
| Biweekly | Week(s) | 2 |
| Monthly | Month(s) | 1 |
| Quarterly | Month(s) | 3 |
| Yearly | Year(s) | 1 |

## Special Monthly Options

- `Month(s) on the First Weekday`
- `Month(s) on the Last Weekday`
- `Month(s) on the Last Day`
- `Nth Weekday of Month`

## Implementation

Update task with:
- `Recur Interval`: number
- `Recur Unit`: select value from above
- `Days`: multi-select for weekly (Monday-Sunday)
- `Due`: next occurrence date
