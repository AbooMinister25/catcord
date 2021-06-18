# Contributing to Catcord

If you are interested in contributing to Catcord, follow the guidelines and steps documented below.

## Requirements

### All

- Some experience with [Git](https://git-scm.com/downloads)
- [A GitHub Account](https://github.com/join)
- [Docker](https://www.docker.com)


### Frontend
- [Node.js v14](https://nodejs.org)
- [Yarn](https://yarnpkg.com/)

### Backend

- [Python 3.8+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/)

## Frontend
1. Make a fork of the catcord github repository.
2. Clone the catcord github repo you just forked by running `git clone https://www.github.com/YourGithubUsername/catcord` in your terminal.
3. Run `yarn set version berry && yarn set version latest` to use Yarn 2.
4. Install dependencies by running `yarn`
4. Make your changes/additions to the code.
5. Run `git add .` to stage your changes.
6. Run `git commit -m "commit message" -m "commit body"` to commit your changes. Make sure to write a meaningful and concise commit message with a longer explanatory description.
7. Run `git push -u origin branch-name` to push your changes to your forked repo.
8. Create a PR on the official catcord repo, your code will be reviewed and eventually merged.
9. FOLLOW THE CONTRIBUTING GUIDELINES BELOW, WE WONT MERGE YOUR PR UNLESS YOU DO.

## Backend

1. Make a fork of the catcord github repository.
2. Clone the catcord github repo you just forked by running `git clone https://www.github.com/YourGithubUsername/catcord` in your terminal
3. Initialize a venv by doing `poetry shell` and install the dependencies by doing `poetry install`.
4. Make your changes/additions to the code.
5. Run `git add .` to stage your changes.
6. Run `git commit -m "commit message" -m "commit body"` to commit your changes. Make sure to write a meaningful and concise commit message with a longer explanatory description.
7. Run `git push -u origin branch-name` to push your changes to your forked repo.
8. Create a PR on the official catcord repo, your code will be reviewed and eventually merged.
9. FOLLOW THE CONTRIBUTING GUIDELINES BELOW, WE WONT MERGE YOUR PR UNLESS YOU DO.

## Testing
1. Catcord uses docker and docker-compose for deployment and testing, so make sure that you have a docker ready environment.
2. Build the docker image by running `docker-compose build`.
3. Run the docker image by doing `docker-compose up`.

## Contributing Guidelines

1. Make sure to lint your code before you push. Our backend uses the `black` python formatter to keep a consistent style throughout our code. You can install black with `pip` and run `black filename.py` to format your code. For the frontend, we use ESLint, for which you can simply run `yarn lint`.
2. Write meaningful but concise commit messages. We want to be reading a commit message that describes what your PR does, without having to spend half an hour on it.
