# Session 4 Field Guide: Modules, Packages, and Imports

Use this guide for learning and quick revision. Read the detailed explanation first. Later, use the compact reference near the end.

## 1. The whole picture in two minutes

Your project changed from notebook-only code into a small Python package:

```text
python_engineering/
|-- pyproject.toml
|-- notebooks/
|   `-- 04_modules_packages_imports.ipynb
`-- src/
    `-- ml_utils/
        |-- __init__.py
        |-- __main__.py
        |-- config.py
        |-- metrics.py
        `-- validation.py
```

The important flow is:

```text
PowerShell command
    -> active Python environment
        -> installed ml_utils package
            -> module and function
                -> returned value or raised exception
```

You used an editable installation so the MLS environment can locate `src/ml_utils`. You also created `__main__.py`, allowing this command:

```powershell
python -m ml_utils
```

## 2. File, module, package, and distribution

These words are related, but they do not mean the same thing.

| Term | Simple meaning | Example here |
|---|---|---|
| File | Something stored on disk | `metrics.py` |
| Module | A Python file loaded as a unit of code | `ml_utils.metrics` |
| Package | A directory grouping related modules | `ml_utils` |
| Distribution | The installable project known to `pip` | `ml-utils-learning` |

The file is the physical object. A module is the Python code object created when Python loads the file. A package provides a namespace for several modules. A distribution is what installation tools manage.

This explains why these names can differ:

```toml
name = "ml-utils-learning"
```

```python
import ml_utils
```

Hyphens are normal in distribution names. Python import identifiers use underscores.

## 3. What each project file does

### `validation.py`

Contains rules that decide whether an input is acceptable. Your validator returns `None` when a label is valid and raises `ValueError` when it is invalid.

```text
valid label -> function reaches the end -> None
invalid label -> raise ValueError -> caller stops unless it catches the error
```

Returning `None` does not mean the function failed. The useful outcome is that no exception occurred.

### `metrics.py`

Contains `calculate_accuracy()`. It imports the validator rather than copying validation logic.

```python
from ml_utils.validation import validate_binary_label
```

Read this from left to right: from the `validation` module inside the `ml_utils` package, make the name `validate_binary_label` available here.

The call flow is:

```text
caller
  -> calculate_accuracy(y_true, y_pred)
       -> validate_binary_label(label)
            -> None when valid
            -> ValueError when invalid
       -> count correct predictions
       -> return accuracy float
  <- float result
```

### `config.py`

Contains the immutable `TrainingConfig` dataclass. It groups settings that belong to one training run and validates them during construction.

```python
config = TrainingConfig(learning_rate=0.01, epochs=5)
```

This call returns a `TrainingConfig` instance. Its default threshold is `0.5`.

### `__init__.py`

Python executes this file while initializing the package. Here it defines a small public interface:

```python
from ml_utils import TrainingConfig, calculate_accuracy
```

Without those exports, callers would use longer module paths:

```python
from ml_utils.config import TrainingConfig
from ml_utils.metrics import calculate_accuracy
```

`__init__.py` does not automatically import every file. Only explicitly imported names become available through the shorter package interface.

### `__main__.py`

This is the package entry point used by:

```powershell
python -m ml_utils
```

It is allowed to print because it is the outer command-line program. Reusable modules normally return values or raise errors so different callers can decide what to do.

## 4. Imports: what Python actually does

For this statement:

```python
from ml_utils import calculate_accuracy
```

Python roughly performs these steps:

1. Search its import locations for `ml_utils`.
2. Initialize the package by executing `ml_utils/__init__.py`.
3. Find the exported name `calculate_accuracy`.
4. Bind that function name in the importing module.

Python normally caches loaded modules in `sys.modules`. Repeating the same import does not normally rerun the complete module body.

Keep imports directional:

```text
__main__.py -> public ml_utils interface
metrics.py  -> validation.py
config.py   -> no ml_utils module
validation.py -> no ml_utils module
```

A circular import would occur if, for example, `metrics.py` imported `validation.py` while `validation.py` tried to import `metrics.py` during initialization. Each module would be waiting for a module that was only partly initialized.

## 5. `pyproject.toml`, line by line

```toml
[build-system]
requires = ["setuptools>=68"]
build-backend = "setuptools.build_meta"
```

This tells packaging tools to use setuptools to build or install the project.

```toml
[project]
name = "ml-utils-learning"
version = "0.1.0"
description = "Small typed ML utilities used for Python engineering practice"
requires-python = ">=3.10"
```

This is project metadata. `requires-python` states the supported Python version. It does not create or activate an environment.

```toml
[tool.setuptools.packages.find]
where = ["src"]
```

Your package is inside a `src` layout. This line tells setuptools where to search for packages.

`pyproject.toml` belongs in the project root because the final dot in the installation command refers to that directory:

```powershell
python -m pip install -e .
```

## 6. Environments and `python -m pip`

A computer may have several Python installations. Yours had:

- Global Python 3.12.
- The MLS virtual environment used by Jupyter.

An installation belongs to one Python environment. Installing into global Python does not make the package available inside the MLS environment.

Check the active interpreter:

```powershell
python -c "import sys; print(sys.executable)"
```

Activate the MLS environment when needed:

```powershell
& 'C:\Users\Pony\Desktop\MLS_AI\.venv\Scripts\Activate.ps1'
```

Then install:

```powershell
python -m pip install -e .
```

Command anatomy:

| Part | Meaning |
|---|---|
| `python` | The currently active Python executable |
| `-m pip` | Run that Python's installed `pip` module |
| `install` | Request a package installation |
| `-e` | Use editable mode |
| `.` | Use the project in the current directory |

Using `python -m pip` connects pip to the chosen Python. Calling plain `pip` can accidentally select a different environment.

## 7. Editable installation

A regular installation generally installs a fixed copy of the package. An editable installation stores metadata that points back to your working source directory.

```text
MLS environment
    -> editable-install metadata
        -> Code/python_engineering/src
            -> ml_utils
```

Therefore, after editing and saving `metrics.py`, the next Python process sees the new code without reinstalling the project.

Prove the source location:

```powershell
python -c "import ml_utils; print(ml_utils.__file__)"
```

Expected output for this project:

```text
C:\Users\Pony\Documents\MLS work\Ai-ml-journey\Code\python_engineering\src\ml_utils\__init__.py
```

Editable installation does not mean that all Python packages are downloaded. It only changes how this project is connected to the environment.

## 8. `__name__`, `__main__.py`, and `python -m`

Python gives every loaded module a `__name__` variable.

```text
Imported module:  __name__ = "ml_utils.metrics"
Entry-point code: __name__ = "__main__"
```

This guard protects entry-point behavior:

```python
if __name__ == "__main__":
    main()
```

When the file is the entry point, the condition is true and `main()` runs. When ordinary code imports the module, the condition is false, so the demonstration does not run unexpectedly.

For a package command:

```powershell
python -m ml_utils
```

Python locates the installed `ml_utils` package and executes `ml_utils/__main__.py`. It does not treat `__init__.py` as the command, although package initialization can happen while loading the package.

## 9. Actual verification outputs

### Package command

```powershell
python -m ml_utils
```

Output after the clearer variable-name update:

```text
Accuracy: 0.3333333333333333
TrainingConfig(learning_rate=0.5, epochs=5, threshold=0.5)
```

Why accuracy is one third: only the middle prediction matches its true label, so the result is `1 / 3`.

### Public imports

```powershell
python -c "from ml_utils import calculate_accuracy, TrainingConfig; print(calculate_accuracy([1, 0, 1], [1, 0, 0])); print(TrainingConfig(0.01, 5))"
```

Output:

```text
0.6666666666666666
TrainingConfig(learning_rate=0.01, epochs=5, threshold=0.5)
```

Two of three prediction pairs match. Python represents `2 / 3` with a finite floating-point approximation.

### Import without side effects

```powershell
python -c "import ml_utils.metrics; print('import completed')"
```

Output:

```text
import completed
```

No accuracy or configuration appeared. This proves the reusable module did not run command-line demonstration code during import.

### Invalid configuration

```python
TrainingConfig(0.0, 5)
```

Final traceback line:

```text
ValueError: Learning rate and Epochs should be positive
```

Construction calls `__post_init__`. Validation raises before Python returns a usable configuration instance.

### Invalid label

```python
calculate_accuracy([1, 2], [1, 0])
```

Final traceback line:

```text
ValueError: Label is not 0 or 1
```

The metric calls the validator. The exception propagates back through `calculate_accuracy` to the original caller, so no accuracy value is returned.

## 10. Real debugging cases from this lab

### Case 1: Installation used the wrong Python

Symptom: global Python could import `ml_utils`, but the MLS environment raised `ModuleNotFoundError`.

Cause: `python -m pip install -e .` was run while global Python was active.

Diagnosis:

```powershell
python -c "import sys; print(sys.executable)"
python -m pip show ml-utils-learning
```

Fix: activate the MLS environment and install again using its Python.

### Case 2: `pyproject.toml` was in `src`

Symptom:

```text
does not appear to be a Python project: neither 'setup.py' nor 'pyproject.toml' found
```

Cause: pip searched the current project directory, but `pyproject.toml` was one level lower inside `src`.

Fix: place it in `Code/python_engineering`, change to that directory, and rerun the installation.

### Case 3: `NameError` from `rang`

The loop used a name that had never been assigned:

```python
for i in range(rang):
```

Python resolves variable names at runtime. Because `rang` did not exist, the function raised `NameError`. The correct lesson is not merely to fix one typo. Read the final traceback line, find the named variable, and trace where it should have been assigned.

## 11. Import errors

| Error | What Python found | First checks |
|---|---|---|
| `ModuleNotFoundError` | It could not locate the requested module/package | Active environment, editable installation, spelling, `src` configuration |
| `ImportError: cannot import name` | It found the module/package but not the requested name | Definition spelling and `__init__.py` export |

Do not immediately modify `sys.path`. A manual path can make one process work while hiding the wrong environment, missing installation, or incorrect project structure.

## 12. Compact revision reference

```python
import module_name
module_name.public_name(...)

from package_name.module_name import public_name
public_name(...)

if __name__ == "__main__":
    main()
```

```powershell
# Check active Python
python -c "import sys; print(sys.executable)"

# Install current project in editable mode
python -m pip install -e .

# Show installed distribution information
python -m pip show ml-utils-learning

# Show the imported package source
python -c "import ml_utils; print(ml_utils.__file__)"

# Execute package entry point
python -m ml_utils
```

## 13. Retrieval questions

Answer without rereading the guide:

1. How is a file different from a loaded module?
2. Why can the distribution name use hyphens while the import uses underscores?
3. What exactly does `__init__.py` export in this project?
4. Why does an editable installation see saved source changes?
5. Which file does `python -m ml_utils` execute?
6. Why did installing into global Python not help the MLS environment?
7. How does `ModuleNotFoundError` differ from a missing-name `ImportError`?
8. Trace an invalid label from the caller to the validator and back.

Complete the notebook's retrieval task after two or three days. Do not treat recognition while reading as proof that you can reconstruct the package yourself.
