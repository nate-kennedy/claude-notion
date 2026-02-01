---
description: Weekly review workflow for Ultimate Brain
argument-hint:
---

Guide through GTD weekly review process to maintain system integrity and clarity.

## Usage

- `/review` - Start full weekly review
- `/review quick` - Abbreviated review (inbox + overdue only)

## Weekly Review Steps

### 1. Get Clear (Collect & Process)
- Process physical inbox (remind user)
- Process email inbox (remind user)
- Process `/inbox` - all captured items
- Empty your head - capture any loose thoughts

### 2. Get Current (Review Lists)
- Review **Calendar** - upcoming deadlines
- Review **Do Next** list - still relevant?
- Review **Delegated** - follow up needed?
- Review **Someday/Maybe** - promote any items?
- Review **Projects** - all have next actions?

### 3. Get Creative (Plan)
- Review **Goals** - on track?
- Review **Areas** - anything neglected?
- Plan next week's priorities
- Update My Day for tomorrow

## Example Flow

```
User: /review
Assistant: Starting weekly review. Let's get your system clear and current.

## Step 1: Get Clear

First, let's process your inbox. You have 7 items waiting.
[Shows inbox items]

Would you like to process these now? (y/n)
```

## Implementation

1. Count items in each list (inbox, overdue, projects without next actions)
2. Guide through each step interactively
3. Track progress through the review
4. Celebrate completion with stats

## Queries Needed

- Inbox count: Tasks with no Project, Tag, or Due
- Overdue: Tasks with Due < today AND Status != Done
- Projects without next actions: Projects with Status = Doing but no incomplete Tasks
- Stale Someday: Tasks in Someday not reviewed in 30+ days
