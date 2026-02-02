---
description: Time tracking for tasks
argument-hint: start|stop|status [task]
---

Track time spent on tasks via Work Sessions.

## Usage

- `/track start <task>` - Start tracking time on a task
- `/track stop` - End current session
- `/track status` - Show active session and today's total

## Starting a Session

Creates a Work Session with:
- Name: Auto-generated from task name
- Tasks: Link to the task
- Start: Current datetime

```json
{
  "parent": {"data_source_id": "2fafc9f9-93ac-8193-95f6-000bc15d8e5d"},
  "properties": {
    "Name": "Working on <task name>",
    "Tasks": "[\"<task_url>\"]",
    "date:Start:start": "<ISO datetime>",
    "date:Start:is_datetime": 1
  }
}
```

## Stopping a Session

Update the active session with:
- `date:End:start`: Current datetime
- `date:End:is_datetime`: 1

The Duration formula automatically calculates elapsed time.

## Work Sessions Database

Collection ID: `2fafc9f9-93ac-8193-95f6-000bc15d8e5d`

| Property | Type | Description |
|----------|------|-------------|
| Name | title | Session name |
| Tasks | relation | Linked task |
| Start | date | Start datetime |
| End | date | End datetime |
| Duration | formula | HH:MM:SS format |
| Duration (Mins) | formula | Minutes as number |
