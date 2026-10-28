## 1. Verify Django Project and Test Suite
Goal: Ensure the base Django project runs correctly and initial tests pass.
Description: Run database migrations and execute the Django test suite using `uv run python manage.py test` to verify the setup is healthy. Confirm that at least one test runs and passes successfully.

## 2. Household and Membership Models
Goal: Implement data models for Households and Memberships with role support.
Description: Create Django models for `Household` and `Membership` linking users to households with roles (`Organizer`, `Member`) and multi-household switching support. Generate and apply database migrations and write unit tests.

## 3. Chore Model and Recurrence Support
Goal: Define the `Chore` model supporting statuses, due dates, and assignments.
Description: Implement the `Chore` model with title, description, due date, recurrence rules, and assignees linked via `Membership`. Configure chore statuses (`To do`, `In progress`, `Completed`, `Overdue`), create migrations, and add unit tests.

## 4. Completion History Model
Goal: Implement the `History` audit log model for completed chores.
Description: Create the `History` model to track completed chores, the member who completed them, and the timestamp. Add database migrations and write unit tests verifying audit record creation upon chore completion.

## 5. Household Management Views and Authentication
Goal: Build household creation, member invitation, and household switching workflows.
Description: Develop views and server-rendered Django templates allowing users to create households, manage memberships, and switch between active households. Implement access controls ensuring data privacy between households.

## 6. Chore Management and Assignment Workflow
Goal: Enable creating, editing, assigning, claiming, and completing chores.
Description: Build views and templates for creating and editing chores, assigning them to members, allowing members to claim tasks, and marking assigned chores complete. Validate form inputs and permissions.

## 7. Shared Dashboard and History Views
Goal: Provide a shared dashboard for active chores and a view for completion history.
Description: Create the shared dashboard view displaying household chores, assignees, due dates, and statuses, alongside a history view listing completed chores and completion records. Ensure responsive and clean Vanilla CSS styling.

## 8. Integration Testing and MVP Validation
Goal: Perform end-to-end testing of core user flows across households and chores.
Description: Write comprehensive integration tests covering the complete MVP user journey from household creation and member joining to chore management, completion, and history tracking. Verify all success criteria.
