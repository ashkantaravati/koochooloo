# AGENTS.md

## Scope
These instructions apply to the entire repository.

## Development workflow
- Run tests with `python manage.py test` before committing.
- Keep dependencies in `requirements.txt` minimal and pinned.
- Prefer small, focused pull requests with a clear summary and test evidence.
- Use semantic branch names: `feat/`, `fix/`, `docs/`, `chore/`.
- Use semantic commit messages (Conventional Commits), e.g. `feat: add docker release workflow`.

## Documentation
- Update `README.md` whenever setup, runtime behavior, or developer workflow changes.
- Include Docker usage whenever container-related files are added or modified.
- Keep `CONTRIBUTING.md` aligned with branch and commit conventions.
