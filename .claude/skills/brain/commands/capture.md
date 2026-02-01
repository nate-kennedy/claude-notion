---
description: Quick capture to Ultimate Brain inbox
argument-hint: <text to capture>
---

Quick capture a thought, task, or note to the Ultimate Brain inbox. The goal is speed - get it captured now, process later.

## Usage

```
/capture <text>
```

## Behavior

1. Create a new task in the Tasks database with:
   - **Name**: The captured text
   - **Status**: To Do
   - **No Project, No Tag, No Due date** (this puts it in Inbox)

2. Confirm creation with the task URL

3. Remind user to process inbox later

## Example

```
User: /capture Call dentist about appointment
Assistant: Captured to inbox: "Call dentist about appointment"
[View in Notion](https://notion.so/...)

Tip: Process your inbox with /inbox to clarify and organize.
```

## Implementation

Use `mcp__notion__notion-create-pages` with:
- `parent.data_source_id`: `2fafc9f9-93ac-812f-b26f-000b0644d2cb` (Tasks collection)
- `properties.Name`: The captured text
- `properties.Status`: "To Do"

Do NOT set Project, Tag, or Due - this ensures it appears in the GTD Inbox view.
