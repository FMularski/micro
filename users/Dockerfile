ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

WORKDIR /app

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

ENV POETRY_VERSION=1.5.1
RUN pip3 install "poetry==${POETRY_VERSION}"
COPY pyproject.toml poetry.lock /app/
RUN poetry export -f requirements.txt --output requirements.txt

RUN pip3 install -r requirements.txt

USER appuser

COPY . .

RUN python3 manage.py collectstatic --noinput
