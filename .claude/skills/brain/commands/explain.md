---
description: Explain PARA/GTD methodology or Ultimate Brain features
argument-hint: para|gtd|<feature>
---

Provide contextual explanations of productivity systems and Ultimate Brain features.

## Usage

- `/explain para` - PARA methodology overview
- `/explain gtd` - Getting Things Done overview
- `/explain <feature>` - Specific feature explanation

## Feature Topics

| Topic | What to Explain |
|-------|-----------------|
| myday | My Day workflow: Plan → Execute → Wrap-Up |
| inbox | GTD inbox and processing workflow |
| projects | Project types: Goals, Ongoing, SOPs |
| tags | Areas vs Resources distinction |
| smartlists | Do Next, Delegated, Someday, Deferred |
| goals | Goals and Milestones tracking |
| recurring | Recurring task setup and behavior |
| tracking | Time tracking with Work Sessions |
| snooze | Deferred tasks via Snooze date |

## Response Guidelines

When explaining, always:
1. Start with the concept in 1-2 sentences
2. Explain how it's implemented in Ultimate Brain
3. Give a practical example
4. Suggest when to use it

## PARA Quick Reference

Read `resources/PARA.md` for full details.

| Component | UB Implementation | Use For |
|-----------|-------------------|---------|
| Projects | Projects database | Outcomes with deadlines |
| Areas | Tags with type=Area | Ongoing responsibilities |
| Resources | Tags with type=Resource | Reference material |
| Archive | Done status / Archive | Completed/inactive |

## GTD Quick Reference

Read `resources/GTD.md` for full details.

| GTD Concept | UB Implementation |
|-------------|-------------------|
| Inbox | Tasks with no Project, Tag, or Due |
| Next Actions | Smart List: Do Next |
| Calendar | Tasks with Due date |
| Waiting For | Smart List: Delegated |
| Someday/Maybe | Smart List: Someday |
| Tickler | Snooze date (deferred) |

## Coaching Triggers

Proactively offer explanations when:
- User creates first task (explain inbox processing)
- User asks "what should I do?" (explain GTD engage criteria)
- User has >10 inbox items (nudge toward processing)
- User hasn't reviewed in >7 days (suggest weekly review)
