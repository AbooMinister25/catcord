---
id: frontend
title: Frontend
description: The Catcord frontend
slug: /frontend
---

The Catcord frontend is a [SvelteKit](https://kit.svelte.dev) application.

## Setup the frontend

The frontend can be set up one of two ways - Node.js or Docker. We recommend using Node for local
development and Docker for testing the final build.

### Node.js

There are a couple prerequisites for setting up the frontend with Node.

- [Node v14](https://nodejs.org) - This is the version we use and recommend
- [Yarn](https://yarnpkg.com) - The package manager we use

There are a couple key commands you need to know to get started:

```shell
yarn # Install the required dependencies
yarn dev # Start the SvelteKit dev server with hot reload
yarn build # Build for production
yarn start # Start the production build locally
yarn lint # Lint with ESLint
yarn tsc # Run the TypeScript compiler
```

You'll primary develop with `yarn dev` and test with the various other commands. Make sure to run
ESLint and the TypeScript compiler before you push.

### Docker

You'll need [Docker](https://docker.com) installed to run the production build with Docker. You
cannot develop in Docker as our Dockerfile uses the production build command.

To start the Docker container, run these commands:

```
docker build . -t catcord-frontend
docker run -p 3000:3000 catcord-frontend
```

Or if you'd like a shorter command, simply run `yarn docker`.

You can use [Docker Compose](https://docs.docker.com/compose/) to start both the frontend and
backend together if you wish. Just run

```
docker-compose up --build
```

in the root directory of the project.