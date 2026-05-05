# Contributing

Thank you for contributing to Koochooloo.

## Branch naming
Use semantic branch prefixes:
- `feat/<short-description>` for new features
- `fix/<short-description>` for bug fixes
- `docs/<short-description>` for documentation
- `chore/<short-description>` for maintenance and tooling

## Commit messages
Use Conventional Commits format:
- `feat: add internationalized model verbose names`
- `fix: prevent null redirect host handling`
- `docs: expand docker publishing instructions`

General format:
`<type>(optional-scope): <short imperative summary>`

Common types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `ci`.

## Local development
1. Create a virtual environment and install dependencies.
2. Run migrations.
3. Run tests:
   ```bash
   python manage.py test
   ```

## Pull requests
- Keep pull requests focused and small.
- Include test evidence in the PR description.
- Update README when setup/runtime/developer workflow changes.
