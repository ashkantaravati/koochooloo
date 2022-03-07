# Setup

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


# Run in development
Don't forget the .env file.
```sh
    python manage.py runserver
```

# Run in Production
Use a WSGI Application Server such as gunicorn or uWSGI together with NGINX/Apache.
Again, don't forget the .env file.

# Environment Variables
* SECRET_KEY: Django secret key
* DEBUG: Django DEBUG
* HASHID_FIELD_SALT
* BASE_HOST:Used for creating Short links
