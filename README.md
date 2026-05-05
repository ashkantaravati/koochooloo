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

## Run tests
```bash
python manage.py test
```


## Developer quality workflow
- Lint locally with `ruff check .`
- Optional: install pre-commit hooks with `pre-commit install`
- CI runs lint + tests on all pushes and pull requests (`.github/workflows/ci.yml`).
- Tests can run without a custom `.env` because safe development defaults are provided in settings.

## Docker
Build and run with Docker Compose:
```bash
docker compose up --build
```

The app is exposed at `http://localhost:8000`.

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

## Notes
- Short-link redirects are served under `/r/<id>/`.
- Servables are served under `/servable/<id>/`.
