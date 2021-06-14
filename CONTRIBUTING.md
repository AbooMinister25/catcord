# Contributing to Catcord

If you are interested in contributing to Catcord, follow the guidelines and steps documented below.

## Requirements

-   [Python 3.8+](https://www.python.org/downloads/)
-   [Poetry](https://python-poetry.org/docs/)
-   Some experience with [Git](https://git-scm.com/downloads)
-   [A GitHub Account](https://github.com/join)

## Quickstart

1. Make a fork of the catcord github repository.
2. Clone the catcord github repo you just forked by doing `git clone https://www.github.com/YourGithubUsername/catcord`
3. Initialize the venv by doing `poetry shell` and install the dependencies by doing `poetry install`.
4. Make your changes/additions to the code.
5. Do `git add .` to stage your changes.
6. Run git commit -m "commit message" to commit your changes. Make sure to write a meaningful and concise commit message.
7. Do `git push -u origin branch-name` to push your changes to your forked repo.
8. Create a PR on the official catcord repo, your code will be reviewed and eventually merged.
9. FOLLOW THE CONTRIBUTING GUIDELINES BELOW, WE WONT MERGE YOUR PR UNLESS YOU DO.

## Contributing Guidelines

1. Make sure to lint your code before you push. Our projects use the `black` python formatter to keep a consistent style throughout our code. You can install black with `pip` and run `black filename.py` to format your code.
2. Write meaningful but concise commit messages. We want to be reading a commit message that describes what your PR does, without having to spend half an hour on it.
3. Our projects use `poetry` for dependency management, so make sure to use a poetry venv, and add all new dependencies to our `pyproject.toml` file.
