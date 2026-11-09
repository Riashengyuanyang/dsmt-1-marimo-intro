# Intro to Marimo Notebooks

Marimo Notebooks are reactive documents that combine code, text, and visualizations to facilitate data analysis and
sharing. They share some similarities with Jupyter Notebooks, but Marimo has a modern feature set and look & feel.
One of the major differences is that Marimo Notebooks are plain Python files, making them easier to version control
and collaborate on.

## Installing Marimo

Marimo is designed to work with `uv`, so it is best installed with `uv`.
Which means we need to have `uv` installed first!

## `uv`

### Installation

**Search for the `uv` documentation to find the installation script and run it in the terminal of this Codespace**

### Initialisation

After installing `uv`, we need to initialise it. This can be done by running the following command in the terminal:

```bash
uv init --python 3.12
```

`--python` sets the project's Python version. uv writes it to `.python-version` and to `requires-python` in `pyproject.toml`.
It's much easier to set it now than to change it later.

*Notice the several files and folders have been created in the file explorer. You may delete main.py*

## Back to Marimo

### Installation

With `uv` installed and init'd, we can now install Marimo. We recommend installing Marimo
as a developer package, to keep production builds lighter.

```bash
uv add --dev marimo
```

### Opening Marimo Notebooks

To open a Marimo Notebook, you can use the following command in the terminal:

```bash
uv run marimo edit <notebook-name>.py --no-token
```

`--no-token` stops marimo asking for an access code. A Codespace's ports are already private to you, so the code isn't needed here.

**Try it out on `intro_marimo.py` !**

## Testing Marimo Notebooks

### Reusable Functions

Any [reusable functions](https://docs.marimo.io/guides/reusing_functions/)
in a Marimo Notebook can be tested. `pytest` is a modern testing framework
for Python, but you can use any testing framework you like.

### Pytest

First add `pytest` to your development dependencies:

```bash
uv add --dev pytest
```

### VS Code

Next, we'll need to sort out the VS Code running in this Codespace. The Python extension is already installed,
so we only need to tell it to use the environment `uv` created.

* Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open the command palette
* Start typing **Python: Select Interpreter** and select it
* Select the interpreter that includes `.venv` in the path (this is the virtual environment created by `uv`)
* Open the **Testing** tab on the left sidebar (it looks like a flask)
* Click **Configure Python Tests**, select **pytest**, then select the `tests` folder

### Running tests

There is already one test in this project, in `tests/test_penguins.py`. Run it from the **Testing** tab with the
play button.

If you want, you can also run the tests in the terminal with:

```bash
uv run python -m pytest
```

## Linting Marimo Notebooks

Since Marimo Notebooks are just Python files, they can be linted, or checked for code quality issues,
just like any other Python code.

The modern Python linter is `ruff`, which can be installed either as a development dependency,
or used as a `tool`. The options are:

- `uv add --dev` dependency: if part of a CI/CD pipeline, or important for your collaborators
- `uv tool install`: if just for local use, but you use it regularly
- `uvx`: if just for use in one-off situations, like this Codespace!

To lint the files in your project use:

```bash
uvx ruff check
```

You can add `--fix` to automatically fix some issues, or fix them manually.


## Formatting Marimo Notebooks

Where linting checks for code quality issues, formatting makes sure the code
is consistently styled. `ruff` also has formatting capabilities, used via:

```bash
uvx ruff format --check
```

When you leave out `--check`, it will modify files to apply the formatting.

## Sorting Imports in Marimo Notebooks

For sorting imports, we can use `isort`, another modern tool for Python.

```bash
uvx isort . --check
```

As with `ruff`, leaving out `--check` will modify files to sort the imports.

## Type Checking Marimo Notebooks

When writing Python code, it's a good idea to add type hints to function signatures.
This helps with code readability, and can also help catch bugs before they happen.

From the creators of `ruff` and `uv`, we have `ty`, a modern type checker for Python.

```bash
uvx ty check
```

Try to fix any type issues that are reported.

## Making Marimo Notebooks Interactive

Marimo notebooks are reactive. When a value changes, every cell that uses it runs again.

In `intro_marimo.py` the number of trees and the depth of the random forest are fixed in one cell:

```python
n_estimators = 3
max_depth = 2
```

Replace that cell with two widgets, each in its own cell:

```python
n_estimators = mo.ui.slider(start=10, stop=500, step=20, value=100, label="Estimators (n_estimators)")
n_estimators
```

```python
max_depth = mo.ui.number(value=10, start=1, stop=30, step=1, label="Max depth")
max_depth
```

A widget only shows if it's the last line of its cell. Then use the widgets' values in the model:

```python
rf = RandomForestClassifier(n_estimators=n_estimators.value, max_depth=max_depth.value, random_state=42)
```

To see the effect, print the report with `print(classification_report(y_test, preds))`. Move the slider and the model is fitted again.

## Committing Changes and Syncing to GitHub

When you're happy with your changes, you can commit them to git and push them to GitHub.

Have a look at the **Source Control** tab on the left sidebar (it looks like a branch icon),
where you can see the changes you've made. You can add files to commit using the plus icon
next to each file, add a commit message in the text box at the top.

Then click the checkmark **Commit** icon to commit the changes, and once again to push them to GitHub.


# The End!