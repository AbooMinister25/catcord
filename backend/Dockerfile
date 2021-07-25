FROM python:3.9-slim-buster

# Create working directory
WORKDIR /app

ENV PIP_NO_CACHE_DIR=false \
    POETRY_VIRTUALENVS_CREATE=false

# Install Poetry
RUN pip install -U poetry

# Copy files 
COPY pyproject.toml poetry.lock ./

# Install with poetry
RUN poetry install --no-dev

COPY . .

EXPOSE 3000

CMD ["poetry", "run", "task", "start"]
