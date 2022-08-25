# Koochooloo - Simple Self-Hosted URL Shortener with Admin Panel

## Features

- Create a link (We call it a reference)
- Activate and deactivate links
- Get an automatically generated hashed short link
- Get both http and https URLS for your short link
- Add and manage users
- Add and manage user tokens
- Get reference data using API
- Create references from API
- See number of visits to a reference
- See details of each visit to a reference
- See a log of all visits/requests
- Create and serve static content (Servables) with user-defined MIME types.

## Setup

1. Clone this repository
2. Setup a Python Virtual Environment (using virtualenv or similar)

   virtualenv example:

```sh
    virtualenv env
```

3. Activate the virtual environment

```sh
    source env/bin/activate
```

4. Install the dependencies from the requirements.txt file

```sh
    pip install -r requirements.txt
```

5. Migrate the database

```sh
    python manage.py migrate
```

6. Create a superuser

```sh
    python manage.py createsuperuser
```

7. Create a `.env` file in the root directory (right besid manage.py)

## Run in development

Don't forget the .env file.

```sh
    python manage.py runserver
```

## Run in Production

Use a WSGI Application Server such as gunicorn or uWSGI together with NGINX/Apache.
Again, don't forget the .env file.

## Environment Variables

- SECRET_KEY: Django secret key
- DEBUG: Django DEBUG
- HASHID_FIELD_SALT
- BASE_HOST:Used for creating Short links
- ALLOWED_HOSTS: Django ALLOWED_HOSTS. _A String of Comma-separated Values_

## Web API

### Endpoints

| Action                   | HTTP Verb | Endpoint                       | Payload | Auth               |
| ------------------------ | --------- | ------------------------------ | ------- | ------------------ |
| Get all references       | GET       | `/api/references/`             |         |                    |
| Get a specific reference | GET       | `/api/references/?id=<hashid>` | none    | none               |
| Create a new reference   | POST      | `/api/references/`             |         | `is_authenticated` |

### Schema for Creating a New Reference

API endpoint that allows external systems to create, list, and retrieve references.


| Field Name                    | Type      | Optional      | Descriptions                                                                                                                           |
| ----------------------------- | --------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| title                         | String    | Required      | The title of the reference                                                                                                             |
| destination                   | Valid URL | Required      | The destination of the reference                                                                                                       |
| is_active                     | Boolean   | default=true  | Whether or not the reference is active                                                                                                 |
| short_url                     | Valid URL | Response Only | The resulting short URL for the reference created with the configured BASE_HOST and hashid generated for this reference automatically. |
| short_url_with_protocol_http  | Valid URL | Response Only | short_url with protocol http prepended. read-only                                                                                      |
| short_url_with_protocol_https | Valid URL | Response Only | short_url with protocol https prepended. read-only                                                                                     |
| created_at                    | string    | Response Only | The date and time the reference was created.                                                                                           |
| updated_at                    | string    | Response Only | The date and time the reference was last updated. read-only                                                                            |

Sample POST Payload:

```json
{
    "title": "Your Desired Title",
    "destination": "https://google.com",
    "is_active": true,
    "description": "a short link to google.com"
}
```

### Token-based Authentication

First create and assign a token to your desired user from the admin panel. Then include the token in an `Authorization` header of your requests like the following:

`Authorization : Bearer <YOUR_TOKEN_STRING>`
