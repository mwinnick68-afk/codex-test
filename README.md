# codex-test

Starter Python project skeleton with a `src/` layout, tests, and basic developer tooling.

## Prerequisites

- Python 3.10 or newer

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -e ".[dev]"
```

## Run

```bash
python -m codex_test.main
python -m codex_test.main Alice
```

## Test

```bash
pytest
```

## Features

- `src/`-layout for packaging
- Test suite using `pytest`
- Formatting and linting configured via `black`, `isort`, and `ruff`
- Input hardening in `greet` (normalization, empty/control-char rejection, max length)

## Quickstart (developer)

Create and activate a virtualenv, then install development dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
pip install -e '[dev]'
```

Run tests:

```bash
pytest
```

The pytest configuration enforces branch coverage with a minimum of 95%.

Run the package (module entrypoint):

```bash
python -m codex_test.main
```

Lint and format:

```bash
# format
black .
isort .

# lint
ruff check .

# type-check
mypy src
```

## CI

GitHub Actions runs on pushes to `main` and pull requests for Python `3.10`, `3.11`, and `3.12`.
The workflow executes:

- `ruff check .`
- `black --check .`
- `isort --check-only .`
- `mypy src`
- `pytest` (with coverage threshold enforcement from `pyproject.toml`)

Development helper (optional): add a `Makefile` with `make test`, `make lint`, `make format` for convenience.

## Contributing

1. Fork the repo and create a feature branch.
2. Run tests and linters locally.
3. Open a PR with a clear description of changes.

## License

This project is available under the MIT License. See the `LICENSE` file for details.

## Contact

Project repository: [https://github.com/mwinnick68-afk/codex-test](https://github.com/mwinnick68-afk/codex-test)
