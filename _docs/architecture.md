# Architecture: Shared Household Chores MVP

## 1. Overview
A lightweight web application enabling households to organize chores, assign or claim tasks, track statuses on a shared dashboard, and review completion history.

## 2. Tech Stack
- **Language**: Python `>=3.14`
- **Framework**: Django `6.1.2`
- **UI Approach**: Server-rendered Django HTML templates with Vanilla CSS
- **Database**: SQLite (MVP)
- **Package Manager**: uv (`uv.lock`)

## 3. Dependencies Table
| Name | Version | Purpose |
| --- | --- | --- |
| `django` | 6.1.2 | Core MVT framework for routing, ORM, views, and authentication |
| `asgiref` | 3.13.0 | ASGI utility library supporting Django async/sync operations |
| `sqlparse` | 0.6.0 | Non-validating SQL parser used by Django ORM |
| `tzdata` | 2026.5 | Timezone database for Python and Django time handling |

## 4. Database Decision
- **MVP Choice**: SQLite. Zero configuration, lightweight file-based storage, ideal for rapid local development and small households.
- **Future Scale**: PostgreSQL can be adopted later for higher concurrency and production multi-user scaling.

## 5. Project Structure
- `chores_project/`: Django project configuration (`settings.py`, `urls.py`, `wsgi.py`, `asgi.py`).
- `chores/`: Core Django application (`models.py`, `views.py`, `admin.py`, `tests.py`, `migrations/`).
- `_docs/`: Project documentation (`plan.md`, `architecture.md`).

## 6. Data Model & Relationships
- **`Households`**: Represents a shared home unit.
- **`Memberships`**: Links Django `User` to `Households` with roles (`Organizer`, `Member`). Supports multi-household switching.
- **`Chores`**: Tasks belonging to a `Household`. Features title, description, due date, recurrence, assignee(s) via `Memberships`, and status (`To do`, `In progress`, `Completed`, `Overdue`).
- **`History`**: Completion audit log recording completed chores, completing member, and timestamp.

## 7. Main User Flows & Pages
- **Shared Dashboard**: View household chores, assignees, due dates, and statuses.
- **Household Management**: Create households, invite members, switch active households.
- **Chore Management**: Create, edit, assign, claim, and mark chores complete.
- **History View**: Review completed chores and completion records.

## 8. Engineering Strategies
- **Testing**: Django test runner executed via `uv run python manage.py test`.
- **Migrations**: Schema evolution managed via Django migrations (`manage.py makemigrations` / `migrate`).
- **Configuration & Secrets**: Environment variables (`.env`). Secrets must never be committed.
- **Git Workflow**: Clean feature/documentation branches with descriptive commit messages.

## 9. Out of Scope
- Email/push notifications, household chat, gamification (points/badges), and advanced analytics.
