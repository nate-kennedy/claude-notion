---
description: Generate productivity reports
argument-hint: weekly|project <name>|goals
---

Generate detailed reports on productivity and progress.

## Usage

- `/report weekly` - Weekly accomplishment summary
- `/report project <name>` - Deep dive on a project
- `/report goals` - Goal progress overview

## Weekly Summary Report

### Data to Gather

1. **Tasks completed** (Status = Done, Completed >= week start)
   - Group by Project
   - Group by Tag (Area)

2. **Time tracked** (Work Sessions this week)
   - Total hours
   - By project/task

3. **Projects progressed**
   - Tasks completed per project
   - % change from last week

4. **What's coming**
   - Tasks due next week
   - Upcoming milestones

### Output Format

```
## Weekly Summary: Jan 27 - Feb 2

### Accomplishments
Completed 23 tasks across 5 projects

**By Project:**
- Website Redesign: 8 tasks (launched homepage!)
- Q1 Planning: 5 tasks
- Client Onboarding: 4 tasks
- (No project): 6 tasks

**By Area:**
- Work: 18 tasks
- Health: 3 tasks
- Personal: 2 tasks

### Time Invested
Total: 24h 30m tracked

- Website Redesign: 12h 15m
- Client work: 8h 45m
- Planning: 3h 30m

### Looking Ahead
- 12 tasks due next week
- Milestone: "MVP Launch" due Friday
```

## Project Status Report

### Data to Gather

1. **Project details** - Name, status, goal link, dates
2. **Task breakdown**:
   - Total tasks
   - Done / Doing / To Do counts
   - Overdue tasks
3. **Time tracking** - Total time on project tasks
4. **Recent activity** - Last 5 completed tasks
5. **Blockers** - Tasks with no clear next action

### Output Format

```
## Project: Website Redesign

**Status:** Doing | **Goal:** Launch Product
**Progress:** 75% (30/40 tasks)

### Task Breakdown
- Done: 30
- Doing: 4
- To Do: 6
- Overdue: 2

### Time Invested
Total: 45h 30m

### Recent Completions
1. ✓ Finalize homepage design (Feb 1)
2. ✓ Set up hosting (Jan 31)
3. ✓ Create contact form (Jan 30)

### Needs Attention
- "Review analytics setup" - overdue 3 days
- "Write about page" - no due date set
```

## Goals Report

### Data to Gather

1. **Active goals** - Target date >= today
2. **Milestones per goal** - Done vs total
3. **Contributing projects** - Linked projects and their progress
4. **Timeline** - Days until target

### Output Format

```
## Goals Progress

### Get Fit (Target: June 1)
Progress: 40% | 120 days remaining

**Milestones:**
- ✓ Join gym
- ✓ Establish routine
- ○ Lose 10 lbs (in progress)
- ○ Run 5K

**Projects:**
- "Meal Planning" - 60% complete
- "Exercise Routine" - 45% complete

---

### Launch Product (Target: March 15)
Progress: 75% | 42 days remaining

**Milestones:**
- ✓ MVP defined
- ✓ Design complete
- ○ Development done
- ○ Beta testing

**Projects:**
- "Website Redesign" - 75% complete
- "Marketing Prep" - 30% complete
```
