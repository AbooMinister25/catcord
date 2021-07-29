---
id: backend
title: Backend
description: The Catcord backend
slug: /backend
---

The Catcord backend is a [FastAPI](https://fastapi.tiangolo.com/) application.

## Setup the backend

The backend can be set up one of two ways - Python or Docker. We recommend using Python for local
development and Docker for testing the final build.

### Python

There are a couple prerequisites for setting up the backend with Python.

- [Python 3.9+](https://python.org)
- [Yarn](https://python-poetry.org) - The package manager we use

There are a couple key commands you need to know to get started:

```shell
poetry install # Install the required dependencies
poetry run task start # Start the FastAPI server
poetry run task lint # Lint with flake8
poetry run task format # Format with black and isort
poetry run task test # Test with Pytest
```

You'll primary develop with `poetry run task start` and test with the various other commands. Make
sure to run the lint, format, and test commands before you push.

### Docker

You'll need [Docker](https://docker.com) installed to run the build with Docker. You cannot develop
in Docker as our Dockerfile copies over files before it runs them, there's no hot reload.

To start the Docker container, run these commands:

```
docker build . -t catcord-backend
docker run -p 8000:8000 catcord-backend
```

Or if you'd like a shorter command, simply run `poetry run task docker`.

You can use [Docker Compose](https://docs.docker.com/compose/) to start both the frontend and
backend together if you wish. Just run

```
docker-compose up --build
```

in the root directory of the project.
