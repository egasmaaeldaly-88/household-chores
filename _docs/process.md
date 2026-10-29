# Process

- Tasks come from backlog.md, one at a time
- Read the task and its acceptance criteria before starting and before finishing
- Commit regularly

## Roles

- PM - grooms a task before anyone implements it, follows _docs/team/pm.md
- Engineer - implements one groomed task, follows _docs/team/software-engineer.md
- QA - checks the result against the acceptance criteria, follows _docs/team/qa-engineer.md

## Lifecycle

1. Pick the next open task in backlog.md
2. PM grooms it
3. Engineer implements it
4. QA verifies it and writes PASS or FAIL under the task
5. On FAIL, go back to step 3 with the QA notes
6. On PASS, mark the task as done
7. Repeat

## Rules

- Do not skip grooming
- The PM and the Engineer never mark a task as done, only after QA says PASS
- QA does not fix code, it only reports PASS or FAIL