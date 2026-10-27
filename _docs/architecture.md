# Architecture: Shared Household Chores MVP

## Project & App Structure
- **`chores_project/`**: Django project root containing configuration settings (`settings.py`, `urls.py`, `wsgi.py`, `asgi.py`).
- **`chores/`**: Core Django app housing business logic, data models, views, and test suites.

## Data Models & Relationships
- **`Households`**: Represents a distinct household unit.
- **`Memberships`**: Intermediary model linking Django `User` instances to `Households` with specific roles (`Organizer`, `Member`), enabling multi-household membership and switching.
- **`Chores`**: Task items scoped to a `Household`. Includes title, optional description, due date, recurrence rules, assignee(s) via `Memberships`, and status (`To do`, `In progress`, `Completed`, `Overdue`).
- **`History`**: Audit/completion log tracking completed chores, the member responsible, and timestamps.

## Main Pages & Views
- **Shared Dashboard**: Overview of active chores, assignees, due dates, and real-time statuses.
- **Household & Member Management**: Interface for creating households, inviting members, and switching active contexts.
- **Chore CRUD / Action Views**: Forms and endpoints to create, edit, assign, claim, and mark chores complete.
- **History Log View**: Chronological view of completed household tasks.

## Running & Testing
- **Run Server**:
  ```bash
  uv run python manage.py runserver
  ```
- **Run Tests**:
  ```bash
  uv run python manage.py test
  ```
