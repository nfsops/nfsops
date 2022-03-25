# Contributing

## Prerequisites

* [Python (>=3.8.0)](https://www.python.org)
* [rsync (>=3.1.0)](https://rsync.samba.org)

```{note}
The package development requires `rsync` executable in the system environment.
```

## Development

Install package:

```console
pip install -e .[development]
```

```{note}
Use the `-e, --editable` flag to install the package in development mode.
```

```{note}
Set up a virtual environment for development.
```

Sort imports:

```console
isort setup.py nfsops/ docs/ tests/
```

Format source code:

```console
autopep8 --recursive --in-place setup.py nfsops/ docs/ tests/
```

Check static typing:

```console
mypy setup.py nfsops/ docs/ tests/
```

Lint source code:

```console
pylint setup.py nfsops/ docs/ tests/
```

Test package:

```console
pytest
```

Report test coverage:

```console
pytest --cov nfsops/
```

Build documentation:

```console
cd docs/
sphinx-build -b html nfsops/ build/
```

```{note}
This step will generate the API reference before building.
```

```{hint}
See also the [`Makefile`](https://github.com/nfsops/nfsops/blob/main/Makefile) for development.
```
