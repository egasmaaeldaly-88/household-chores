# Shared Household Chores MVP Backlog

## 1. Verify Django Project and Test Runner
Goal: Verify that the empty Django project runs correctly and passes initial test execution.
Description: Run the Django test suite using `uv run python manage.py test` to ensure dependencies and project configuration are correct. Add a basic sanity test if needed to verify test execution.

## 2. Implement Core Data Models
Goal: Define database models for Households, Memberships, Chores, and History with appropriate fields and relationships.
Description: Create Django models in the `chores` app covering Household, Membership (with roles Organizer/Member), Chores (with title, description, due date, recurrence, assignees, and statuses), and History audit logs. Generate and apply initial database migrations.

## 3. Household Creation and Membership Management
Goal: Enable Organizers to create households and invite members.
Description: Implement views and forms allowing users to create a new household (becoming its Organizer) and invite or add new members via Memberships. Ensure proper authentication and authorization checks.

## 4. Household Switching and Access Control
Goal: Allow users to belong to multiple households and switch between them securely.
Description: Implement session or profile-based household switching so users can toggle their active household context. Enforce data isolation so household data is visible only to that household's members.

## 5. Chore CRUD and Scheduling
Goal: Implement creation, editing, and scheduling for one-time and recurring chores.
Description: Build views and forms for creating and editing chores with titles, descriptions, due dates, and recurrence rules. Ensure chores are scoped correctly to the active household.

## 6. Chore Assignment and Claiming
Goal: Allow assignment of chores to household members or self-claiming of available tasks.
Description: Implement functionality allowing organizers or members to assign chores to specific members or allow members to claim unassigned tasks. Update chore states and assignees accordingly.

## 7. Shared Dashboard View
Goal: Provide a shared household dashboard to view chores, assignees, due dates, and statuses.
Description: Create a server-rendered dashboard template and view displaying all household chores categorized or filtered by status (To do, In progress, Completed, Overdue). Style the UI using clean Vanilla CSS.

## 8. Completion History View
Goal: Provide a completion history view tracking completed chores and who completed them.
Description: Implement logic to record completion events into the History model when chores are marked complete. Build a history view and template allowing household members to review past completions.
