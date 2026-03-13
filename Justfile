# Default command lists all available recipes
_default:
    @just --list --unsorted

alias b := bump
alias c := clean
alias d := dist
alias t := test


# run tests with coverage
test:
    uv run pytest tests/

# run tests for all the supported Python versions
testall:
    uv run --python=3.10 pytest
    uv run --python=3.11 pytest
    uv run --python=3.12 pytest
    uv run --python=3.13 pytest
    uv run --python=3.14 pytest

# clean all python build/compilation files and directories
clean: clean-build clean-pyc clean-test

# remove build artifacts
[private]
clean-build:
    rm -fr build/
    rm -fr _build/
    rm -fr dist/
    rm -fr .eggs/
    find . -name '*.egg-info' -exec rm -fr {} +
    find . -name '*.egg' -exec rm -f {} +

# remove Python file artifacts
[private]
clean-pyc:
    find . -name '*.pyc' -exec rm -f {} +
    find . -name '*.pyo' -exec rm -f {} +
    find . -name '*~' -exec rm -f {} +
    find . -name '__pycache__' -exec rm -fr {} +

# remove test and coverage artifacts
[private]
clean-test:
    rm -f .coverage
    rm -fr htmlcov/
    rm -fr .pytest_cache

# install dependencies in local venv
venv:
    uv sync

[confirm("Do you really want to bump? (y/n)")]
[private]
prompt-confirm:

# bump the version, commit and add a tag <major|minor|patch|...>
bump INCREMENT="patch":
    @uv version --bump {{ INCREMENT }} --dry-run
    @just prompt-confirm
    uv version --bump {{ INCREMENT }}

# preview the documentation locally (serve the myst website)
docs:
    uv run myst

# build the source distribution and wheel file
dist:
    uv build
