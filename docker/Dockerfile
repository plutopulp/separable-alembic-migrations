FROM python:3.10-slim

WORKDIR /app

ENV PIP_NO_CACHE_DIR=1

RUN pip install -U pip

RUN pip install poetry==1.4.2 && poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN apt update -y && apt upgrade -y \
    && apt install -y --no-install-recommends build-essential libpq5 libpq-dev \
    && rm -rf /var/lib/apt/lists/* \
    && poetry install \
    && apt purge -y --auto-remove build-essential libpq-dev
  
RUN pip install uvicorn[standard]


COPY ./app_a /app