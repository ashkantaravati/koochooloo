# Koochooloo

A self-hosted URL shortener built with Django and Django REST Framework.

## What it does
- Create short links ("references") from long URLs.
- Redirect short links and log each visit.
- Activate/deactivate links without deleting them.
- Manage static/text responses using "servables".
- Manage data via Django admin and REST API.

## Requirements
- Python 3.11+ (3.12 recommended)
- pip
- SQLite (default, bundled with Python)
- Docker (optional, for containerized runtime)

## Local setup
1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file next to `manage.py`:
   ```env
   SECRET_KEY=change-me
   DEBUG=True
   HASHID_FIELD_SALT=change-me-too
   BASE_HOST=localhost:8000
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```
5. Run migrations and create a superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Internationalization and localization (i18n/l10n)
- Locale middleware is enabled.
- Project supports `en` and `fa` language codes.
- App names, model verbose names, and admin labels are translation-ready.
- Add translation files with:
  ```bash
  django-admin makemessages -l fa -l en
  django-admin compilemessages
  ```

## Run tests
```bash
python manage.py test
```

## Packaging and release standards
Versioning follows Semantic Versioning (SemVer) and release tags are expected in `vX.Y.Z` format.

### Publish to PyPI
A GitHub Actions workflow (`.github/workflows/release.yml`) publishes to PyPI on version tags:
1. Create a tag (example):
   ```bash
   git tag v0.1.0
   git push origin v0.1.0
   ```
2. Configure PyPI trusted publishing for the repository.

### Publish Docker image
The same release workflow builds and publishes the image to GHCR:
- `ghcr.io/<owner>/<repo>:<tag>`
- `ghcr.io/<owner>/<repo>:latest`

## Docker
Build and run with Docker Compose:
```bash
docker compose up --build
```

The app is exposed at `http://localhost:8000`.

## Demo site publishing (optional)
A manual/`main` branch workflow (`.github/workflows/demo.yml`) can trigger a Render deploy hook.

To enable:
1. Create a Render web service from this repository.
2. Add `RENDER_DEPLOY_HOOK_URL` in GitHub repository secrets.
3. Push to `main` or run the workflow manually.

## API endpoints
Base path: `/api`

| Action                   | Method | Endpoint                       | Auth                         |
|--------------------------|--------|--------------------------------|------------------------------|
| List references          | GET    | `/api/references`              | Public                       |
| Retrieve reference       | GET    | `/api/references/<id>`         | Public                       |
| Create reference         | POST   | `/api/references`              | Bearer token or session auth |

### Bearer token auth
Use:
```http
Authorization: Bearer <token>
```

## Contributing
See [`CONTRIBUTING.md`](CONTRIBUTING.md) for branch naming, semantic commit messages, and pull request expectations.
