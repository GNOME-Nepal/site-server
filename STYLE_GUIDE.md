# Style Guide

This style guide provides guidelines for writing and formatting code, commit messages, and branch names to ensure consistency and maintainability across the project.


## Table of Contents
- [Code Archiecture](#code-architecture)
- [General Guidelines](#general-guidelines)
- [Commit Message Conventions](#commit-message-conventions)
- [Branch Naming Conventions](#branch-naming-conventions)
- [Code Formatting](#code-formatting)


## Code Architecture

Djate follows a standard Django project structure with `apps` and `manage.py` in the root directory. Each app contains components such as `views.py`, `models.py`, and `urls.py`, while Celery tasks are defined in `tasks.py` for each application.

The code architecture leverages Django REST Framework (DRF) generics and viewsets for building APIs efficiently, ensuring modularity and efficiency in development.

## General Guidelines

- Write clear, concise, and self-explanatory code.
- Use meaningful variable and function names.
- Adhere to the language-specific best practices.
- Ensure your code is modular and reusable.
- Avoid code duplication.

## Commit Message Conventions

Commit messages should be clear and descriptive. Follow these conventions for commit messages:

- Use the present tense ("Add feature" not "Added feature").
- Use the imperative mood ("Fix bug" not "Fixed bug").
- Keep the subject line (first line) under 50 characters.
- Separate subject from body with a blank line.
- Provide a detailed description of the changes in the body.
- Include references to relevant issues or pull requests.

### Examples:

```
feat: Add user authentication module

Implemented user login and registration functionalities.
Updated the database schema to include user credentials.
```

```
fix: Resolve crash on app startup

Fixed an issue causing the app to crash on startup due to a null pointer exception.
Closes #42.
```

## Branch Naming Conventions

Branch names should be descriptive and follow a consistent pattern. Use the following conventions for naming branches:

- Use lowercase letters and hyphens (`-`) to separate words.
- Include a prefix to indicate the type of branch:
  - `feat/` for new features
  - `fix/` for bug fixes
  - `chore/` for maintenance tasks
  - `docs/` for documentation updates

### Examples:

```
feat/add-user-authentication
fix/crash-on-startup
chore/update-dependencies
docs/improve-readme
```

## Code Formatting

Consistent code formatting improves readability and maintainability. We use black to format our code automatically. You can use the default black configuration with max_line_length=79 and we use double quotes everywhere. and we target for python3.11.
We also want the most optimial code linting and that is ensured by flake8. Before pushing you can check by performing
```
python3 -m flake8
```

---

By following this style guide, you contribute to a consistent and maintainable codebase, making it easier for everyone to collaborate and improve the project. Thank you for your contributions!
