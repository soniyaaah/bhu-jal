# Coding Guidelines

This document outlines the coding standards for contributing to the Groundwater Intelligence Platform.

## Folder Conventions
- Code must reside in its designated module (`backend/`, `frontend/`, `ml/`).
- Shared scripts (e.g., data ingestion, database seeding) belong in `scripts/`.
- Documentation should always be placed in `docs/` or directly in the `README.md`.

## Naming Conventions
- **Python Variables & Functions**: `snake_case`
- **Python Classes**: `PascalCase`
- **Constants**: `UPPER_SNAKE_CASE` (e.g., `MAX_RETRIES = 3`)
- **TypeScript/JavaScript Variables & Functions**: `camelCase`
- **React Components**: `PascalCase` (e.g., `StationMap.tsx`)
- **Database Tables**: Plural `snake_case` (e.g., `groundwater_readings`)

## Logging
- Do not use `print()` in production code.
- Python: Use the `loguru` library. 
  - `logger.info()` for general flow.
  - `logger.debug()` for detailed variable inspection.
  - `logger.error()` for exceptions, including tracebacks.

## Typing
- Python: Strict type hinting is enforced using the `typing` module. Mypy should pass without errors.
- Frontend: TypeScript is mandatory. Avoid using `any`; define interfaces for all data structures.

## Formatting
- **Python**: Use `black` with an 88-character line limit. Use `isort` for import sorting.
- **Frontend**: Use `Prettier` and `ESLint` with the recommended configurations.

## Error Handling
- Never silently catch exceptions (`except Exception: pass`).
- Log the error and raise a specific, informative custom exception.
- APIs should return standardized JSON error responses with appropriate HTTP status codes.

## Testing
- **Backend**: Use `pytest`. Aim for >80% test coverage for API endpoints and core services.
- **Frontend**: Use `Jest` and `React Testing Library` for component and utility testing.
- Write tests for both successful paths and expected failure cases.

## Git Workflow
1. Create a feature branch from `main` (`feature/short-description` or `bugfix/issue-description`).
2. Commit frequently with descriptive messages.
3. Push to origin and open a Pull Request against `main`.
4. Ensure CI checks (linting, tests) pass before requesting a review.
5. Merge using "Squash and Merge" to keep the main history clean.
