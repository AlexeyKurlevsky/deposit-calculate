FROM python:3.12.4-bookworm

USER root

COPY .  /app/
WORKDIR /app

RUN pip install poetry
RUN poetry install

CMD poetry run python src/main.py