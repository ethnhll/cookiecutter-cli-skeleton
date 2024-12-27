# Cookiecutter CLI Skeleton

This template is an opinionated scaffolding for developing command-line
interfaces with Python.

## Template Stack

Below are the technologies coming with this template:

Material mkdocs

- Typer
- uv
- Pydantic
- Github Actions
- pytest
- pre-commit
- ruff
- gitlint

TODO: look into copier
<https://copier.readthedocs.io/en/stable/>

## Setup

### MacOS

```shell
# python package manager
brew install uv

# some silliness with built-in ruby, so get a ruby version manager
brew install frum
# follow these instructions
# https://github.com/TaKO8Ki/frum?tab=readme-ov-file#shell-setup

brew install openssl
# install latest stable ruby (ie not rc or preview)
frum install $(frum install -l | grep -ve "^.*-.*$" | tail -1) \
--with-openssl-dir=$(brew --prefix openssl)
# make sure ruby uses the newer version of openssl

# install project dependencies
uv sync

# setup pre-commit hooks
uvx pre-commit install

# necessary for gitlint
uvx pre-commit install --hook-type commit-msg
```

### Windows

Not attempted on Windows yet.

## Usage

```shell
uvx cookiecutter cookiecutter-cli-skeleton
```

## Contributing

Contributions are always welcome! Please submit a pull request for review when
you have a change.
