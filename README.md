# Setup
1. Install pipenv `pip install pipenv` (if you don't have it already)
2. Activate the shell `pipenv shell`

## Add a dependency
1. Install the dependency `pipenv install <package>`

# Run
1. Run the server `pipenv run python asgi.py`
2. Or alternatively `pipenv run uvicorn asgi:app --reload`

# Database Migration
1. To create a new migration, run `pipenv run alembic revision -m "<message>"`
2. To run the migration, run `pipenv run alembic upgrade head`
3. To rollback, run `pipenv run alembic downgrade -1`