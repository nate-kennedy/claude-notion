---
description: Process Ultimate Brain inbox items using GTD
argument-hint: [count]
---

Process inbox items following GTD methodology. Inbox = tasks with no Project, no Tag, no Due date.

## Usage

- `/inbox` - Show inbox and process interactively
- `/inbox 5` - Process next 5 items  
- `/inbox count` - Just show count

## GTD Processing Flow

For each item ask:

1. **Actionable?** No → Archive/delete/reference. Yes → continue
2. **Next action?** Clarify the specific physical action
3. **< 2 minutes?** Yes → Do now. No → continue
4. **Delegate?** Yes → Smart List: Delegated + Person
5. **Part of project?** Yes → Link to Project
6. **When?** Date → Due. Soon → Do Next. Maybe → Someday. Later → Snooze
7. **What area?** Link to Tag (Area)

## Implementation

Find inbox items: Search Tasks where Project is empty AND Tag is empty AND Due is empty AND Status != Done.

Update items: Use `mcp__notion__notion-update-page` to set properties based on user decisions.
