# Cheat sheet

The commands from today, in one place.

## uv

| what | command |
|---|---|
| Start a project | `uv init` |
| Start a project on a given Python version | `uv init --python 3.9` |
| Change the Python version later | set `requires-python` in `pyproject.toml`, then `uv python pin 3.9` and `uv sync` |
| Add a package | `uv add pandas` |
| Add an exact version | `uv add "pandas==1.5.3"` |
| Add a development tool | `uv add --dev pytest` |
| Install everything the project needs | `uv sync` |
| Run a command in the project's environment | `uv run <command>` |
| Run a tool without adding it to the project | `uvx <tool>` |

uv writes these files. Commit all of them except `.venv/`.

| file | what it holds |
|---|---|
| `pyproject.toml` | the packages you asked for |
| `uv.lock` | the exact versions that were installed |
| `.python-version` | the Python version |
| `.venv/` | the environment itself |

**If everything goes wrong,** delete the files uv made (`pyproject.toml`, `uv.lock`, `.python-version`, `.venv/` and `main.py`) and
start again with `uv init`. You'll have to add your packages again. Only do this if you created those files yourself.

## marimo

| what | command |
|---|---|
| Edit a notebook | `uv run marimo edit notebook.py --no-token` |
| Run it as an app | `uv run marimo run notebook.py` |

- Imports go in the setup cell (`with app.setup:`).
- A function marked `@app.function` can be imported and tested like any other Python function.
- A widget's current value is in `.value`, for example `slider.value`.

## Tests

| what | command |
|---|---|
| Run the tests | `uv run python -m pytest` |
| Show each test by name | `uv run python -m pytest -v` |

In VS Code, pick the project's environment first. Open the command palette (`Ctrl+Shift+P`, or `Cmd+Shift+P` on a Mac), choose
**Python: Select Interpreter** and pick the one with `.venv` in its path. The **Testing** tab (the flask icon) then finds and runs the
tests.

## Code quality

| what | check | fix |
|---|---|---|
| Lint | `uvx ruff check` | `uvx ruff check --fix` |
| Format | `uvx ruff format --check` | `uvx ruff format` |
| Sort imports | `uvx isort . --check` | `uvx isort .` |
| Type check | `uvx ty check` | by hand |

## Git

Commit small steps as you go, from the **Source Control** tab. Write each message in the Conventional Commits style.

| prefix | for |
|---|---|
| `feat:` | something new, such as a widget |
| `fix:` | a bug fix |
| `docs:` | the README or other documentation |
| `style:` | formatting only |
| `test:` | tests |
| `chore:` | setup, such as the lock file |

Don't commit `.venv/`, `__pycache__/`, `__marimo__/`, `.pytest_cache/` or `.ruff_cache/`. The `.gitignore` already leaves them out.
