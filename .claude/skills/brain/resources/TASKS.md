# Task Properties Reference

Complete reference for Tasks database properties in Ultimate Brain.

## Core Properties

| Property | Type | Values | Description |
|----------|------|--------|-------------|
| Name | title | text | Task name/description |
| Status | status | To Do, Doing, Done | Current state |
| Priority | select | Low, Medium, High | Importance level |
| Due | date | date | When it's due |

## Organization

| Property | Type | Description |
|----------|------|-------------|
| Project | relation | Link to Projects database |
| Tag | relation | Link to Tags (Areas/Resources) |
| Smart List | select | Do Next, Delegated, Someday |
| My Day | checkbox | Include in daily focus |

## Scheduling

| Property | Type | Description |
|----------|------|-------------|
| Due | date | Hard deadline |
| Snooze | date | Hide until this date (deferred) |
| Completed | date | When marked done |

## Recurring Tasks

| Property | Type | Description |
|----------|------|-------------|
| Recur Interval | number | How many units between |
| Recur Unit | select | Days, Weeks, Months, Years |
| Days | multi_select | Mon-Sun (for weekly) |

## Relationships

| Property | Type | Description |
|----------|------|-------------|
| People | relation | Delegated to / associated with |
| Parent Task | relation | For sub-tasks |
| Sub-Tasks | relation | Child tasks |
| Sessions | relation | Time tracking records |

## GTD Smart List Logic

Tasks automatically appear in views based on:

| View | Condition |
|------|-----------|
| Inbox | No Project AND No Tag AND No Due |
| Calendar | Has Due date |
| Do Next | Smart List = "Do Next" |
| Delegated | Smart List = "Delegated" |
| Someday | Smart List = "Someday" |
| Deferred | Has Snooze date |

## Creating Tasks via API

Use `mcp__notion__notion-create-pages` with:

```json
{
  "parent": {
    "data_source_id": "2fafc9f9-93ac-812f-b26f-000b0644d2cb"
  },
  "pages": [{
    "properties": {
      "Name": "Task description",
      "Status": "To Do",
      "Priority": "Medium",
      "date:Due:start": "2026-02-15",
      "date:Due:is_datetime": 0
    }
  }]
}
```

## Updating Tasks via API

Use `mcp__notion__notion-update-page` with page_id and properties to update.
