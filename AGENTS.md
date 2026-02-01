# Agent Instructions

This project uses **bd** (beads) for issue tracking. Run `bd onboard` to get started.

## Project Overview

**claude-notion** is an intelligent personal assistant skill that interfaces with a Notion Ultimate Brain template. The goal is to 100x productivity by providing an AI-powered front-end that:

- **Interprets requests** - Understands natural language and maps to the right Ultimate Brain action
- **Recommends usage** - Suggests how to use features based on PARA methodology and GTD principles
- **Manages workflow** - Creates tasks, captures notes, organizes projects, and tracks progress
- **Provides insights** - Reviews status, identifies stuck items, suggests prioritization
- **Coaches productivity** - Guides users unfamiliar with PARA/GTD through the system

## Ultimate Brain Structure

The user's Notion workspace "Nate's Notes" contains Ultimate Brain 3.0 with these core components:

### Core Databases
| Database | Purpose | Key Views |
|----------|---------|-----------|
| **Tasks** | Action items with due dates, priorities, projects | Inbox, Today, Week, Month, Someday, Priority, Recurring |
| **Notes** | Knowledge capture and reference | Inbox, Favorites, All, Review Queue, Journal, Meeting Notes |
| **Projects** | Multi-task initiatives with goals | Active, Completed, by Area |
| **Tags** | PARA Areas and Resources for organization | Areas, Resources |
| **Goals** | Objectives and milestones | Active goals with progress tracking |

### Additional Databases
- **People** - Contacts and relationships (with meeting notes)
- **Books** - Reading list with notes and genres
- **Recipes** - Meal planning and cooking
- **Work Sessions** - Time tracking
- **Milestones** - Goal sub-targets

### Key Views/Pages
- **Quick Capture** - Fast entry point for new items
- **My Day** - Daily focus dashboard
- **My Week** - Weekly planning view
- **My Year** - Annual goals and progress
- **Process (GTD)** - GTD workflow implementation
- **Archive** - Completed/inactive items

### Important Page IDs
```
Nate's Notes (root):  2fafc9f9-93ac-80c5-b47d-e87f85734c38
Tasks:                2fafc9f9-93ac-8105-9a68-e9376c60dab3
Notes:                2fafc9f9-93ac-814c-a537-da5657737fbe
Projects:             2fafc9f9-93ac-811c-bcfb-e393451d04cd
Tags:                 2fafc9f9-93ac-8112-a4df-cd5fc0551dff
Goals:                2fafc9f9-93ac-8162-b5c8-e6aaa03afb99
Quick Capture:        2fafc9f9-93ac-8141-bdc4-c9cc1fd66dc1
My Day:               2fafc9f9-93ac-812a-b068-ccb4312807c1
Process (GTD):        2fafc9f9-93ac-81ba-a26b-d58ad39eeb2b
Archive:              2fafc9f9-93ac-81c2-bc6a-d9c933a096d2
```

## PARA Methodology

The skill should understand and apply PARA:

- **Projects** - Outcomes requiring multiple tasks (have end dates)
- **Areas** - Ongoing responsibilities to maintain (no end date)
- **Resources** - Reference material for future use
- **Archive** - Inactive items from the above categories

## GTD Principles

The skill should support Getting Things Done workflow:

1. **Capture** - Quick capture of all inputs
2. **Clarify** - Process inbox items (actionable? next action?)
3. **Organize** - Put items in the right place (project, someday, reference, trash)
4. **Reflect** - Regular reviews (daily, weekly)
5. **Engage** - Work from prioritized lists

### Smart Lists (GTD in UB)
| List | Trigger | Description |
|------|---------|-------------|
| **Inbox** | No Project, Tag, or Due | Unprocessed items |
| **Calendar** | Has Due date | Time-bound tasks |
| **Do Next** | Smart List = "Do Next" | Next actions ready to do |
| **Delegated** | Smart List = "Delegated" | Waiting on others |
| **Someday** | Smart List = "Someday" | Maybe later |
| **Deferred** | Has Snooze date | Snoozed until future |

## My Day Workflow (Thomas's Preferred Method)

The **My Day** page implements a 3-step daily planning process:

1. **Plan** - Review task manager, deliberately add tasks to empty daily plan
2. **Execute** - Order tasks, work through them (optional time tracking)
3. **Wrap-Up** - Review what got done, clear list, plan tomorrow

Key property: `My Day` checkbox - adds task to Execute view regardless of due date.

## Key Database Relationships

```
Tasks ─────┬───→ Projects ────→ Tags (Areas) ────→ Goals
           │         │              │                │
           │         ↓              ↓                ↓
           ├───→ People         Notes           Milestones
           │
           └───→ Work Sessions (time tracking)
```

### Task Properties of Note
- **Status**: To Do → Doing → Done
- **Priority**: Low / Medium / High
- **Smart List**: Do Next / Delegated / Someday (for GTD)
- **My Day**: Checkbox for daily planning
- **Due**: Date (filters to Calendar)
- **Snooze**: Date (filters to Deferred)
- **Recur Interval/Unit/Days**: For recurring tasks
- **Parent Task / Sub-Tasks**: For task hierarchy

### Project Statuses
- **Planned** - Not started yet
- **On Hold** - Paused
- **Doing** - Active with defined end goal
- **Ongoing** - Maintenance tasks (no end goal, e.g., "Work Ongoing")
- **Done** - Completed

### "Ongoing" Projects Pattern
Use **Ongoing** status projects to organize recurring/maintenance tasks within an Area:
- "Work Ongoing" for recurring work tasks
- "Home Ongoing" for household maintenance
- "Well-Being Ongoing" for health habits

This associates tasks with Areas without directly relating Tasks→Tags.

## Skill Capabilities (Target)

### Quick Actions
- `capture <text>` - Quick capture to inbox
- `task <text>` - Create a new task
- `note <text>` - Create a new note
- `done <task>` - Mark task complete

### Status & Review
- `today` - What's on my plate today?
- `inbox` - What needs processing?
- `stuck` - What's blocked or overdue?
- `weekly review` - Guide through GTD weekly review

### Smart Recommendations
- Suggest when to break a task into a project
- Recommend tags/areas for new items
- Identify tasks without due dates or projects
- Surface forgotten someday items

### Insights
- Project progress and health
- Goal tracking
- Productivity patterns

## Documentation Reference

The `/docs` folder contains scraped Ultimate Brain documentation:
- `docs/index.json` - Index of all doc pages
- `docs/text/` - Plain text content of each doc
- `docs/html/` - Raw HTML for reference

Key docs for skill development:
- `tasks.txt` - Complete Tasks database documentation
- `projects.txt` - Projects database documentation
- `notes.txt` - Notes database documentation
- `tags.txt` - Tags/Areas documentation
- `gtd-process.txt` - GTD implementation guide
- `managing-tasks.txt` - Task management workflows
- `daily-planning.txt` - My Day usage

## Tech Stack

- **Python 3.14** - Scripting (venv in `/venv`)
- **Notion MCP** - API access to user's Notion workspace
- **Claude Code Skills** - Skill definition format

---

## Quick Reference

```bash
bd ready              # Find available work
bd show <id>          # View issue details
bd update <id> --status in_progress  # Claim work
bd close <id>         # Complete work
bd sync               # Sync with git
```

## Landing the Plane (Session Completion)

**When ending a work session**, you MUST complete ALL steps below. Work is NOT complete until `git push` succeeds.

**MANDATORY WORKFLOW:**

1. **File issues for remaining work** - Create issues for anything that needs follow-up
2. **Run quality gates** (if code changed) - Tests, linters, builds
3. **Update issue status** - Close finished work, update in-progress items
4. **PUSH TO REMOTE** - This is MANDATORY:
   ```bash
   git pull --rebase
   bd sync
   git push
   git status  # MUST show "up to date with origin"
   ```
5. **Clean up** - Clear stashes, prune remote branches
6. **Verify** - All changes committed AND pushed
7. **Hand off** - Provide context for next session

**CRITICAL RULES:**
- Work is NOT complete until `git push` succeeds
- NEVER stop before pushing - that leaves work stranded locally
- NEVER say "ready to push when you are" - YOU must push
- If push fails, resolve and retry until it succeeds
