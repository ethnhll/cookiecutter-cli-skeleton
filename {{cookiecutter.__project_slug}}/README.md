# {{ cookiecutter.project_name }}

## Setup

This assumes [uv](https://docs.astral.sh/uv/) is installed.

```shell
uv sync
uvx pre-commit install
# necessary for gitlint
uvx pre-commit install --hook-type commit-msg
```

## Usage

```shell
{{ cookiecutter.__project_slug }} --help
```

## Contributing

Contributions are always welcome! Please submit a pull request for review when
you have a change.