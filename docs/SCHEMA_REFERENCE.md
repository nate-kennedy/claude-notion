# Ultimate Brain Database Schema Reference

This document contains the complete database schemas from the user's Ultimate Brain Notion workspace. Use this reference when building queries and creating/updating pages.

## Collection IDs Quick Reference

| Database | Collection ID |
|----------|---------------|
| Tasks | `collection://2fafc9f9-93ac-812f-b26f-000b0644d2cb` |
| Projects | `collection://2fafc9f9-93ac-8164-ae7b-000bd485c59b` |
| Notes | `collection://2fafc9f9-93ac-811f-b5f5-000b37c070b2` |
| Tags | `collection://2fafc9f9-93ac-81c6-ac00-000b62072c37` |
| Goals | `collection://2fafc9f9-93ac-81da-9aa7-000b8daff150` |
| Work Sessions | `collection://2fafc9f9-93ac-8193-95f6-000bc15d8e5d` |
| People | `collection://2fafc9f9-93ac-81ea-aa18-000b3452a11f` |
| Milestones | `collection://2fafc9f9-93ac-81d9-83bc-000b27377ba1` |

---

## Tasks Database

**Collection ID:** `collection://2fafc9f9-93ac-812f-b26f-000b0644d2cb`

### Key Properties

| Property | Type | Description |
|----------|------|-------------|
| **Name** | title | The task name |
| **Status** | status | To Do, Doing, Done |
| **Priority** | select | Low, Medium, High |
| **Due** | date | Due date for the task |
| **My Day** | checkbox | Adds task to My Day Execute view |
| **Smart List** | select | Do Next, Delegated, Someday |
| **Snooze** | date | Deferred until this date |
| **Project** | relation → Projects | Project this task belongs to |
| **Tag** | relation → Tags | Direct tag association |
| **People** | relation → People | People associated (delegation) |
| **Parent Task** | relation → Tasks | For sub-tasks |
| **Sub-Tasks** | relation → Tasks | Child tasks |
| **Sessions** | relation → Work Sessions | Time tracking sessions |

### Recurring Task Properties

| Property | Type | Description |
|----------|------|-------------|
| **Recur Interval** | number | How many units between recurrences |
| **Recur Unit** | select | Days, Weeks, Months, Years |
| **Days** | multi_select | Monday-Sunday (weekly recurrence) |
| **Recurring** | formula | TRUE if Recur Interval is set |

### GTD Smart List Logic

Tasks automatically appear in Smart Lists based on these conditions:
- **Inbox**: No Project AND No Tag AND No Due date
- **Calendar**: Has Due date
- **Do Next**: Smart List = "Do Next"
- **Delegated**: Smart List = "Delegated"
- **Someday**: Smart List = "Someday"
- **Deferred**: Has Snooze date

### Status Values

| Status | Group | Description |
|--------|-------|-------------|
| To Do | to_do | Not started |
| Doing | in_progress | Currently working on |
| Done | complete | Completed |

### Priority Values

| Priority | Color |
|----------|-------|
| Low | gray |
| Medium | orange |
| High | red |

### SQLite Schema

```sql
CREATE TABLE IF NOT EXISTS "collection://2fafc9f9-93ac-812f-b26f-000b0644d2cb" (
    url TEXT UNIQUE,
    createdTime TEXT,
    "Archived" TEXT, -- "__YES__" or "__NO__"
    "Status" TEXT, -- "To Do", "Doing", "Done"
    "Priority" TEXT, -- "Low", "Medium", "High"
    "Smart List" TEXT, -- "Do Next", "Delegated", "Someday"
    "My Day" TEXT, -- "__YES__" or "__NO__"
    "Project" TEXT, -- JSON single page URL
    "Tag" TEXT, -- JSON array of page URLs
    "Sub-Tasks" TEXT, -- JSON array of page URLs
    "Sessions" TEXT, -- JSON array of page URLs
    "People" TEXT, -- JSON array of page URLs
    "Recur Interval" REAL,
    "Recur Unit" TEXT, -- "Days", "Weeks", "Months", "Years"
    "Days" TEXT, -- JSON array: ["Monday", "Tuesday", etc.]
    "Parent Task" TEXT, -- JSON single page URL
    "date:Due:start" TEXT,
    "date:Due:end" TEXT,
    "date:Due:is_datetime" INTEGER,
    "date:Snooze:start" TEXT,
    "date:Snooze:end" TEXT,
    "date:Snooze:is_datetime" INTEGER,
    "date:Completed:start" TEXT,
    "date:Completed:end" TEXT,
    "date:Completed:is_datetime" INTEGER,
    "Name" TEXT
)
```

---

## Projects Database

**Collection ID:** `collection://2fafc9f9-93ac-8164-ae7b-000bd485c59b`

### Key Properties

| Property | Type | Description |
|----------|------|-------------|
| **Name** | title | Project name |
| **Status** | status | Planned, On Hold, Doing, Ongoing, Done |
| **Target Deadline** | date | Planned completion date |
| **Completed** | date | Actual completion date |
| **Tag** | relation → Tags | Area this project belongs to |
| **Goal** | relation → Goals | Goal this project supports |
| **Tasks** | relation → Tasks | Tasks in this project |
| **Notes** | relation → Notes | Notes in this project |
| **People** | relation → People | People involved |
| **Pulled Notes** | relation → Notes | Reference notes pulled in |
| **Pulled Tags** | relation → Tags | Tags pulled for their notes |
| **Progress** | formula | % of tasks completed |
| **Archived** | checkbox | Archive flag |

### Status Values

| Status | Group | Description |
|--------|-------|-------------|
| Planned | to_do | Not started |
| On Hold | to_do | Paused |
| Doing | in_progress | Active with end goal |
| Ongoing | in_progress | Maintenance/recurring (no end) |
| Done | complete | Completed |

### SQLite Schema

```sql
CREATE TABLE IF NOT EXISTS "collection://2fafc9f9-93ac-8164-ae7b-000bd485c59b" (
    url TEXT UNIQUE,
    createdTime TEXT,
    "Archived" TEXT,
    "Review Notes" TEXT,
    "Status" TEXT, -- "Planned", "On Hold", "Doing", "Ongoing", "Done"
    "Goal" TEXT, -- JSON array of page URLs
    "Tasks" TEXT, -- JSON array of page URLs
    "Notes" TEXT, -- JSON array of page URLs
    "Tag" TEXT, -- JSON single page URL
    "Pulled Tags" TEXT, -- JSON array of page URLs
    "People" TEXT, -- JSON array of page URLs
    "Pulled Notes" TEXT, -- JSON array of page URLs
    "Created" TEXT NOT NULL,
    "Edited" TEXT NOT NULL,
    "date:Target Deadline:start" TEXT,
    "date:Target Deadline:end" TEXT,
    "date:Target Deadline:is_datetime" INTEGER,
    "date:Completed:start" TEXT,
    "date:Completed:end" TEXT,
    "date:Completed:is_datetime" INTEGER,
    "Name" TEXT
)
```

---

## Notes Database

**Collection ID:** `collection://2fafc9f9-93ac-811f-b5f5-000b37c070b2`

### Key Properties

| Property | Type | Description |
|----------|------|-------------|
| **Name** | title | Note title |
| **Type** | select | Journal, Meeting, Web Clip, etc. |
| **Tag** | relation → Tags | Tag for organization |
| **Project** | relation → Projects | Direct project relation |
| **People** | relation → People | People mentioned |
| **Note Date** | date | Manual date (for journals) |
| **Review Date** | date | Future review reminder |
| **URL** | url | Web clip source |
| **Favorite** | checkbox | Mark as favorite |
| **Archived** | checkbox | Archive flag |

### Type Values

- Journal
- Meeting
- Web Clip
- Lecture
- Reference
- Book
- Idea
- Plan
- Recipe
- Voice Note
- Daily

### SQLite Schema

```sql
CREATE TABLE IF NOT EXISTS "collection://2fafc9f9-93ac-811f-b5f5-000b37c070b2" (
    url TEXT UNIQUE,
    createdTime TEXT,
    "Archived" TEXT,
    "Type" TEXT, -- "Journal", "Meeting", "Web Clip", etc.
    "Tag" TEXT, -- JSON array of page URLs
    "People" TEXT, -- JSON array of page URLs
    "URL" TEXT,
    "Project" TEXT, -- JSON array of page URLs
    "Pulls" TEXT, -- JSON array of page URLs
    "Image" TEXT,
    "Duration (Seconds)" REAL,
    "AI Cost" REAL,
    "Favorite" TEXT,
    "date:Review Date:start" TEXT,
    "date:Review Date:end" TEXT,
    "date:Review Date:is_datetime" INTEGER,
    "date:Note Date:start" TEXT,
    "date:Note Date:end" TEXT,
    "date:Note Date:is_datetime" INTEGER,
    "Created" TEXT NOT NULL,
    "Updated" TEXT NOT NULL,
    "Name" TEXT
)
```

---

## Tags Database

**Collection ID:** `collection://2fafc9f9-93ac-81c6-ac00-000b62072c37`

### Key Properties

| Property | Type | Description |
|----------|------|-------------|
| **Name** | title | Tag name |
| **Type** | status | Area, Resource, Entity |
| **Parent Tag** | relation → Tags | Parent tag |
| **Sub-Tags** | relation → Tags | Child tags |
| **Projects** | relation → Projects | Projects in this area |
| **Notes** | relation → Notes | Notes with this tag |
| **Goals** | relation → Goals | Goals in this area |
| **People** | relation → People | People in this area |
| **Favorite** | checkbox | Mark as favorite |
| **Archived** | checkbox | Archive flag |

### Type Values (PARA)

| Type | Group | Description |
|------|-------|-------------|
| Area | in_progress | Ongoing responsibility |
| Resource | in_progress | Reference material |
| Entity | in_progress | Meta-collections (Apps, Essays) |

### SQLite Schema

```sql
CREATE TABLE IF NOT EXISTS "collection://2fafc9f9-93ac-81c6-ac00-000b62072c37" (
    url TEXT UNIQUE,
    createdTime TEXT,
    "Archived" TEXT,
    "Projects" TEXT, -- JSON array of page URLs
    "Pulls" TEXT, -- JSON array of page URLs
    "Sub-Tags" TEXT, -- JSON array of page URLs
    "Type" TEXT, -- "Area", "Resource", "Entity"
    "Notes" TEXT, -- JSON array of page URLs
    "People" TEXT, -- JSON array of page URLs
    "Goals" TEXT, -- JSON array of page URLs
    "Parent Tag" TEXT, -- JSON array of page URLs
    "Favorite" TEXT,
    "Name" TEXT
)
```

---

## Goals Database

**Collection ID:** `collection://2fafc9f9-93ac-81da-9aa7-000b8daff150`

### Key Properties

| Property | Type | Description |
|----------|------|-------------|
| **Name** | title | Goal name (measurable) |
| **Status** | status | Dream, Active, Achieved |
| **Target Deadline** | date | Target achievement date |
| **Goal Set** | date | When goal was set |
| **Achieved** | date | When goal was achieved |
| **Tag** | relation → Tags | Area this goal belongs to |
| **Projects** | relation → Projects | Projects supporting goal |
| **Milestones** | relation → Milestones | Progress milestones |
| **Progress** | formula | % of milestones complete |
| **Archived** | checkbox | Archive flag |

### Status Values

| Status | Group | Description |
|--------|-------|-------------|
| Dream | to_do | Set but not active |
| Active | in_progress | Actively working toward |
| Achieved | complete | Accomplished |

### SQLite Schema

```sql
CREATE TABLE IF NOT EXISTS "collection://2fafc9f9-93ac-81da-9aa7-000b8daff150" (
    url TEXT UNIQUE,
    createdTime TEXT,
    "Status" TEXT, -- "Dream", "Active", "Achieved"
    "Archived" TEXT,
    "Projects" TEXT,
    "Updated" TEXT NOT NULL,
    "Milestones" TEXT,
    "date:Target Deadline:start" TEXT,
    "date:Target Deadline:end" TEXT,
    "date:Target Deadline:is_datetime" INTEGER,
    "date:Goal Set:start" TEXT,
    "date:Goal Set:end" TEXT,
    "date:Goal Set:is_datetime" INTEGER,
    "Tag" TEXT, -- JSON single page URL (limit 1)
    "date:Achieved:start" TEXT,
    "date:Achieved:end" TEXT,
    "date:Achieved:is_datetime" INTEGER,
    "Name" TEXT
)
```

---

## Work Sessions Database

**Collection ID:** `collection://2fafc9f9-93ac-8193-95f6-000bc15d8e5d`

### Key Properties

| Property | Type | Description |
|----------|------|-------------|
| **Name** | title | Session name (auto-generated) |
| **Tasks** | relation → Tasks | Task being tracked |
| **Start** | date | Session start time |
| **End** | date | Session end time |
| **Duration** | formula | HH:MM:SS formatted duration |
| **Duration (Mins)** | formula | Duration in minutes |
| **Team Member** | person | Who worked |
| **End Session** | button | Ends session with current time |

### SQLite Schema

```sql
CREATE TABLE IF NOT EXISTS "collection://2fafc9f9-93ac-8193-95f6-000bc15d8e5d" (
    url TEXT UNIQUE,
    createdTime TEXT,
    "Tasks" TEXT, -- JSON single page URL (limit 1)
    "date:Start:start" TEXT,
    "date:Start:end" TEXT,
    "date:Start:is_datetime" INTEGER,
    "Team Member" TEXT, -- JSON single user ID
    "date:End:start" TEXT,
    "date:End:end" TEXT,
    "date:End:is_datetime" INTEGER,
    "Name" TEXT
)
```

---

## People Database

**Collection ID:** `collection://2fafc9f9-93ac-81ea-aa18-000b3452a11f`

### Key Properties

| Property | Type | Description |
|----------|------|-------------|
| **Full Name** | title | Full name (first last) |
| **Email** | email | Email address |
| **Phone** | phone_number | Phone number |
| **Company** | text | Company name |
| **Title** | text | Job title |
| **Location** | text | City, state, country |
| **Relationship** | multi_select | Family, Friend, Client, etc. |
| **Birthday** | date | Birthday |
| **Check-In** | date | Scheduled check-in |
| **Last Check-In** | date | Most recent interaction |
| **Pipeline Status** | status | Prospect, Contacted, etc. |
| **Tags** | relation → Tags | Areas they belong to |
| **Tasks** | relation → Tasks | Tasks associated |
| **Projects** | relation → Projects | Projects associated |
| **Notes** | relation → Notes | Notes about them |

### Relationship Values

- Family
- Friend
- Colleague
- Client
- Customer
- Business Partner
- Vendor
- Senpai
- Teacher

### Pipeline Status Values

| Status | Group |
|--------|-------|
| Prospect | to_do |
| Contacted | in_progress |
| Negotiating | in_progress |
| Closed | complete |
| Rejected | complete |

### SQLite Schema

```sql
CREATE TABLE IF NOT EXISTS "collection://2fafc9f9-93ac-81ea-aa18-000b3452a11f" (
    url TEXT UNIQUE,
    createdTime TEXT,
    "Website" TEXT,
    "Tags" TEXT,
    "Notes" TEXT,
    "Company" TEXT,
    "Email" TEXT,
    "Interests" TEXT,
    "Created" TEXT NOT NULL,
    "date:Birthday:start" TEXT,
    "date:Birthday:end" TEXT,
    "date:Birthday:is_datetime" INTEGER,
    "Twitter/X" TEXT,
    "Location" TEXT,
    "date:Last Check-In:start" TEXT,
    "date:Last Check-In:end" TEXT,
    "date:Last Check-In:is_datetime" INTEGER,
    "Relationship" TEXT, -- JSON array
    "Phone" TEXT,
    "Tasks" TEXT,
    "date:Check-In:start" TEXT,
    "date:Check-In:end" TEXT,
    "date:Check-In:is_datetime" INTEGER,
    "Projects" TEXT,
    "Surname" TEXT,
    "Edited" TEXT NOT NULL,
    "LinkedIn" TEXT,
    "Title" TEXT,
    "Pipeline Status" TEXT,
    "Instagram" TEXT,
    "Full Name" TEXT
)
```

---

## Milestones Database

**Collection ID:** `collection://2fafc9f9-93ac-81d9-83bc-000b27377ba1`

### Key Properties

| Property | Type | Description |
|----------|------|-------------|
| **Name** | title | Milestone name (measurable) |
| **Goal** | relation → Goals | Parent goal |
| **Target Deadline** | date | Target date |
| **Date Completed** | date | When completed |

### SQLite Schema

```sql
CREATE TABLE IF NOT EXISTS "collection://2fafc9f9-93ac-81d9-83bc-000b27377ba1" (
    url TEXT UNIQUE,
    createdTime TEXT,
    "date:Target Deadline:start" TEXT,
    "date:Target Deadline:end" TEXT,
    "date:Target Deadline:is_datetime" INTEGER,
    "date:Date Completed:start" TEXT,
    "date:Date Completed:end" TEXT,
    "date:Date Completed:is_datetime" INTEGER,
    "Goal" TEXT, -- JSON single page URL (limit 1)
    "Name" TEXT
)
```

---

## Key Relationships Diagram

```
Tasks ─────┬───→ Projects ────→ Tags (Areas) ────→ Goals
           │         │              │                │
           │         ↓              ↓                ↓
           ├───→ People         Notes           Milestones
           │
           └───→ Work Sessions (time tracking)
```

## Common Query Patterns

### Get Inbox Tasks (GTD)
Tasks with no Project, no Tag, and no Due date.

### Get Today's Tasks
Tasks where Due date is today OR My Day is checked.

### Get Overdue Tasks
Tasks where Status != Done AND Due date < today.

### Get Active Projects
Projects where Status = "Doing" or Status = "Ongoing".

### Get Unprocessed Notes
Notes with no Tag and no Project (in Inbox).

---

## Date Property Format

All date properties use expanded format:
- `date:{property}:start` - Start date (ISO-8601)
- `date:{property}:end` - End date for ranges (optional)
- `date:{property}:is_datetime` - 1 for datetime, 0 for date only

Example:
```json
{
  "date:Due:start": "2024-02-15",
  "date:Due:is_datetime": 0
}
```

## Checkbox Property Format

- `"__YES__"` = checked/true
- `"__NO__"` = unchecked/false
- `NULL` = defaults to false
