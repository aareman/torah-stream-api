FROM python:3.9.15-slim-buster

RUN apt update && apt install python3-dev libpq-dev postgresql postgresql-contrib -y

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock poetry.toml ./

RUN poetry install --no-root

COPY . .

RUN chmod +x docker-entrypoint.sh docker-deploy.sh
