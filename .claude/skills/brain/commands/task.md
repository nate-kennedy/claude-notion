---
description: Create or manage Ultimate Brain tasks
argument-hint: [task description] [options]
---

Create a new task or manage existing tasks in Ultimate Brain.

## Usage

```
/task <description>           # Create new task (interactive)
/task done <search>           # Mark task as done
/task update <search>         # Update a task
/task list [filter]           # List tasks
```

## Creating a Task

When creating a task, gather these details:
1. **Name** (required) - The task description
2. **Project** (optional) - Ask if it should belong to a project
3. **Priority** (optional) - Low, Medium, or High
4. **Due date** (optional) - When it's due
5. **Smart List** (optional) - Do Next, Delegated, or Someday

Parse natural language for dates and context:
- "tomorrow" → Due: tomorrow's date
- "next week" → Due: 7 days from now
- "delegate to John" → Smart List: Delegated, People: John
- "someday" → Smart List: Someday

## Task Properties

| Property | Type | Values |
|----------|------|--------|
| Status | status | To Do, Doing, Done |
| Priority | select | Low, Medium, High |
| Smart List | select | Do Next, Delegated, Someday |
| My Day | checkbox | Adds to daily focus |
| Due | date | Due date |
| Snooze | date | Defer until date |
| Project | relation | Link to Projects |
| Tag | relation | Link to Tags (Areas) |

## Examples

**Create with context:**
```
User: /task Review budget report by Friday for Finance project, high priority
Assistant: Created task:
- Name: Review budget report
- Due: Friday (Feb 7)
- Project: Finance
- Priority: High
[View in Notion](https://notion.so/...)
```

**Mark done:**
```
User: /task done budget report
Assistant: Found "Review budget report" - marking as Done.
Completed! Any follow-up tasks to create?
```

## Implementation

**Create task:** Use `mcp__notion__notion-create-pages` with:
- `parent.data_source_id`: `2fafc9f9-93ac-812f-b26f-000b0644d2cb`

**Find task:** Use `mcp__notion__notion-search` with query in Tasks

**Update task:** Use `mcp__notion__notion-update-page`
