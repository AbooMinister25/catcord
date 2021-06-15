FROM python:3.9-slim-buster

ENV PIP_NO_CACHE_DIR=false \
    POETRY_VIRTUALENVS_CREATE=false

# Install Poetry
RUN pip install -U poetry

# Create working directory
WORKDIR /catcord

# Copy files 
COPY pyproject.toml poetry.lock ./

# Install with poetry
RUN poetry install


COPY . .

RUN poetry install

