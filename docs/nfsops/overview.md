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

```console
nfsops backup list
```

### Restore and merge backup versions

```{warning}
The `backup` command always restores the most recent files.
```

Restore and merge files from all backup versions:

```console
nfsops backup restore *
```

Restore and merge files from a single backup version:

```console
nfsops backup restore 0
```

```{note}
This step will restore the latest backup version.
```

Restore and merge files from a range of backup versions:

```console
nfsops backup restore 0 4
```

```{note}
This step will restore the last 5 backup versions.
```

```console
nfsops backup restore 5 *
```

```{note}
This step will restore all backup versions older than version 5.
```

### Manage multiple backups using root context

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
