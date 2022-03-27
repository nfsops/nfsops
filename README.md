[![Releases](https://img.shields.io/github/v/release/nfsops/nfsops?color=blue)](https://github.com/nfsops/nfsops/releases)
[![Issues](https://img.shields.io/github/issues/nfsops/nfsops?color=blue)](https://github.com/nfsops/nfsops/issues)
[![Pull requests](https://img.shields.io/github/issues-pr/nfsops/nfsops?color=blue)](https://github.com/nfsops/nfsops/pulls)
[![Documentation](https://img.shields.io/badge/docs-latest-blue.svg)](https://nfsops.readthedocs.io)
[![License](https://img.shields.io/pypi/l/nfsops?color=blue)](https://nfsops.readthedocs.io/en/latest/license.html)

# NFSops

<p align="left">
    <img src="https://nfsops.readthedocs.io/en/latest/_static/images/logo.svg" width="100" title="NFSops"/>
</p>

NFSops Python SDK.

Storage management for workspaces.

## Prerequisites

* [Python (>=3.8.0)](https://www.python.org)
* [rsync (>=3.1.0)](https://rsync.samba.org)

> **Note** This package requires `rsync` executable in the system environment.

## Installation

### Production

Install package:

```console
pip install nfsops
```

### Development

Install package:

```console
pip install -e .[development]
```

> **Note** Use the `-e, --editable` flag to install the package in development mode.

> **Note** Set up a virtual environment for development.

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

> **Note** This step will generate the API reference before building.

> **Hint** See also the [`Makefile`](Makefile) for development.

## CLI

### List backup versions

> **Warning** `version` is a temporary alias for backup `timestamp`.
> Please do not restore backups without verify the backup timestamp using the `list` command.

```console
nfsops backup list
```

### Restore and merge backup versions

> **Warning** The `restore` command restores the most recent files
> for the current working directory.

Restore and merge files from all backup versions:

```console
nfsops backup restore *
```

> **Note** This step will restore files from all backup versions.

Restore and merge files from a single backup version:

```console
nfsops backup restore 0
```

> **Note** This step will restore files from latest backup version.

Restore and merge files from a range of backup versions:

```console
nfsops backup restore 0 4
```

> **Note** This step will restore files from last 5 backup versions.

```console
nfsops backup restore 6 *
```

> **Note** This step will restore files from all backup versions older than version 5.

Restore and merge `path/to/document.txt` from all backup versions:

```console
nfsops backup --filter-path path/to/document.txt restore *
```

> **Note** This step will restore `path/to/document.txt` file from all backup versions.

### Manage multiple backups using root context

> **Warning** For root context, the `restore` command sets
> the root template as the current working directory.

Set up the environment variables below:

```console
export NFSOPS_CONTEXT=root
export NFSOPS_ROOT_TEMPLATE=namespace-{name}-resource*
export NFSOPS_PATH=<path>
```

Or use the CLI options:

```console
nfsops --context root --root-template namespace-{name}-resource* --path <path> backup --name <name> ..
```

> **Note** The root template also supports `{legacy_escaped_name}` placeholder.

> **Hint** Try `nfsops --help` for more details.

### Logs

Set the `NFSOPS_LOG_LEVEL` environment variable to define the application log level.

Levels:

- `critical` (default)
- `fatal`
- `error`
- `warn`
- `warning`
- `info`
- `debug`
- `notset`

## SDK

### List backup versions

```python
from nfsops import (
    ContextConfiguration,
    BackupConfiguration,
    BackupOperator
)


context = ContextConfiguration()
configuration = BackupConfiguration()
operator = BackupOperator(context, configuration)

operator.list_versions()
```

### Restore and merge backup versions

```python
from nfsops import (
    ContextConfiguration,
    BackupConfiguration,
    RestoreConfiguration,
    BackupOperator
)


context = ContextConfiguration()
configuration = BackupConfiguration()
operator = BackupOperator(context, configuration)

options = RestoreConfiguration(version=0)
operator.restore(options)
```

## Documentation

Please refer to the official [NFSops Documentation](https://nfsops.readthedocs.io).

## Changelog

[Changelog](https://nfsops.readthedocs.io/en/latest/changelog.html) contains information about new features, improvements, known issues, and bug fixes in each release.

## TODOs

- [ ] Tests

## Copyright and license

Copyright (c) 2022, NFSops Developers. All rights reserved.

Project developed under a [BSD-3-Clause License](https://nfsops.readthedocs.io/en/latest/license.html).
