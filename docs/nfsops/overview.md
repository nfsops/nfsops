# Overview

<p align="left">
    <img src="_static/logo.svg" width="100" title="NFSops"/>
</p>

NFSops Python SDK.

Storage management for workspaces.

## Prerequisites

* [Python (>=3.8.0)](https://www.python.org)
* [rsync (>=3.1.0)](https://rsync.samba.org)

```{note}
This package requires `rsync` executable in the system environment.
```

## Installation

Install package:

```console
pip install nfsops
```

## CLI

### List backup versions

```{warning}
`version` is a temporary alias for backup `timestamp`.
Please do not restore backups without verify the backup timestamp using the `list` command.
```

```console
nfsops backup list
```

### Restore and merge backup versions

```{warning}
The `restore` command restores the most recent files
for the current working directory.
```

Restore and merge files from all backup versions:

```console
nfsops backup restore *
```

```{note}
This step will restore files from all backup versions.
```

Restore and merge files from a single backup version:

```console
nfsops backup restore 0
```

```{note}
This step will restore files from latest backup version.
```

Restore and merge files from a range of backup versions:

```console
nfsops backup restore 0 4
```

```{note}
This step will restore files from last 5 backup versions.
```

```console
nfsops backup restore 6 *
```

```{note}
This step will restore files from all backup versions older than version 5.
```

Restore and merge `path/to/document.txt` from all backup versions:

```console
nfsops backup --filter-path path/to/document.txt restore *
```

```{note}
This step will restore `path/to/document.txt` file from all backup versions.
```

### Manage multiple backups using root context

```{warning}
For root context, the `restore` command sets
the root template as the current working directory.
```

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

```{note}
The root template also supports `{legacy_escaped_name}` placeholder.
```

```{hint}
Try `nfsops --help` for more details.
```

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
