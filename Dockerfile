FROM python:3.9.18-slim

WORKDIR /app

# installing dependencies for psycopg2
RUN apt-get update && apt-get -y install libpq-dev gcc

RUN pip install --upgrade pip
RUN pip install pipenv

COPY Pipfile /app
COPY Pipfile.lock /app

# installing python packages system-wide
RUN pipenv install --system --deploy --ignore-pipfile --${PIPENV_ARGS}

COPY . /app

EXPOSE 3000
CMD ["uvicorn", "asgi:app", "--host", "0.0.0.0", "--port", "3000"]