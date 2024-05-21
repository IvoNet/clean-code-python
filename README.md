# python-reference-project

## Pre-requisites

- [Python](https://www.python.org/) (3.8 or higher)
- [pip](https://pypi.org/project/pip/)
- [Poetry](https://python-poetry.org/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Setup

### Virtual Environment

Create a virtual environment using the following command:

```bash
poetry install
```

If poetry can't locate a Python executable with the correct version, ensure
that you have the correct version installed and run these commands to force
poetry to use it:

```bash
poetry env use PATH_TO_PYTHON_EXECUTABLE
poetry install
```

### Project Setup

Run the following command to setup the project:

```bash
poetry run poe setup
```

## Usage

## Activate the virtual environment

```bash
poetry shell
```

## Developer section

### Usage - Poetry

```bash
poetry shell  # to activate the virtual environment
poetry run COMMAND  # run a command in the venv without first activating it
poetry add DEPENDENCY  # add a production dependency
poetry add --group=dev DEVDEPENDENCY  # add a dev dependency
poetry add --group=GROUPNAME DEPENDENCY  # add a dependency to another group

poetry lock  # update the lock file
poetry install  # install dependencies from the lock file
poetry install --sync  # also remove untracked dependencies from venv
poetry update  # lock & install
poetry update --sync  # lock & install --sync
```

For more information about Poetry, see the [Poetry docs][poetry-docs].

### Usage - Poe

We use `poe` to run tasks that simplify running things like tests, QA-tools, and
docker. This is similar to how one might use `make` to simplify running commands
with arguments or combinations of commands.

You can run `poe` in two ways:

```bash
# By first activating the virtual environment
poetry shell
poe TASKNAME [OPTIONAL_ADDITIONAL_ARGS]

# By using `poetry run` without activing the environment
poetry run poe TASKNAME [OPTIONAL_ADDITIONAL_ARGS]
```

For example, to run all tools that reformat code, you can run:

```bash
poetry shell
poe reformat

# or
poetry run poe refactor
```

For a list of all the available tasks, run `poe --help` or look at the task
definitions in [`pypoetry.toml`](pyproject.toml).

For more information about Poe the Poet, look at the [Poe docs][poe-docs].

### Dockerfile

- The `Dockerfile` is for the default build of the project, you can change it to your needs.

### Initial Structure

Minimal structure for a Python project:

```text
.
├── pyproject.toml
├── .gitignore
├── README.md
├── src
└── tests
```

# ADR

The decisions for this tool are recorded as [architecture decision records in the project repository](doc/adr)
They can be modified with the tool [adr-tools-python](https://pypi.org/project/adr-tools-python/), or any other tool
that supports ADRs.

[ADRs]: http://thinkrelevance.com/blog/2011/11/15/documenting-architecture-decisions

[poetry-docs]: https://python-poetry.org/docs/

[poe-docs]: https://poethepoet.natn.io/
