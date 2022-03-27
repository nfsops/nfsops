'''
Utility functions.
'''

import json
import logging
import os
import shutil
import string
from datetime import datetime, timezone
from logging import Logger
from pathlib import Path
from typing import Any, Iterable, Optional, Sequence, Tuple

import datetime_glob
from tabulate import tabulate

from . import package
from .configurations.configuration import Configuration
from .context_type import ContextType


def unwrap(value: Optional[Any]) -> Any:
    '''
    Wrap optional value.
    The value must be different from `None` to avoid runtime exception.

    Parameters:
        value (Optional[Any]): Optional value.
    Returns:
        Any: A non-optional value.
    Raises:
        AssertionError: Expected non-optional value is `None`.
    '''

    assert value is not None, 'cannot unwrap "None" value.'
    return value


def timezone_aware(date: datetime) -> datetime:
    '''
    Convert naive to timezone-aware datetime (UTC timezone).

    Parameters:
        date (datetime): Datetime object.
    Returns:
        datetime: A timezone-aware datetime.
    '''

    return date.replace(tzinfo=timezone.utc) if date.tzinfo is None else date


def get_default_logger() -> Logger:
    '''
    Return the default logger instance.
    Set the `NFSOPS_LOG_LEVEL` environment variable to define log level.

    Levels:

    - `critical` (default)
    - `fatal`
    - `error`
    - `warn`
    - `warning`
    - `info`
    - `debug`
    - `notset`

    Returns:
        Logger: A default logger instance for package.
    '''

    level_mapping = {
        'critical': logging.CRITICAL,
        'fatal': logging.FATAL,
        'error': logging.ERROR,
        'warn': logging.WARNING,
        'warning': logging.WARNING,
        'info': logging.INFO,
        'debug': logging.DEBUG,
        'notset': logging.NOTSET
    }

    try:
        level = level_mapping[os.getenv('NFSOPS_LOG_LEVEL', 'critical')]
    except KeyError as exception:
        level_options = ', '.join([f'"{key}"' for key in level_mapping])

        raise ValueError(
            f'invalid log level, use {level_options} instead.'
        ) from exception

    logging.basicConfig(
        format='%(asctime)s %(levelname)s:%(name)s:%(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=level
    )

    return logging.getLogger(package.__title__.lower())


def get_default_context_path(context: ContextType) -> Path:
    '''
    Return default path for context type.

    Default values:

    - `ContextType.ROOT`: `/var/nfs-shared`
    - `ContextType.SUBPATH`: `$PWD` (current working directory)

    Parameters:
        context (ContextType): Context type.
    Returns:
        Path: A path object referencing the default path.
    '''

    default_mapping = {
        ContextType.ROOT: Path('/var/nfs-shared'),
        ContextType.SUBPATH: Path.cwd()
    }

    return default_mapping[context]


def get_default_snapshot_path(directory: Path):
    '''
    Return default snapshot path for a directory.

    Parameters:
        directory (Path): Directory path.
    Returns:
        Path: A path object referencing a snapshot.
    '''

    return directory / '.snapshot'


def format_configuration(configuration: Configuration) -> str:
    '''
    Format configuration object to string using the formatting style
    `[key0=value0 key1=value1 ... keyn=valuen]`.

    Parameters:
        configuration (Configuration): Configuration object.
    Returns:
        str: A single-line string representing the configuration object.
    '''

    parameters = json.loads(configuration.json(exclude={'type'}))

    inner_string_content = ' '.join(
        f'{key}={value}' for key, value in parameters.items()
    )

    return f'[{inner_string_content}]'


def tabulate_configuration_group(configurations: Sequence[Configuration]) -> str:
    '''
    Format configuration group to string using a tabular style.

    Parameters:
        configurations (List[Configuration]): Configuration group.
    Returns:
        str: A string representing the configuration group as table.
    '''

    if len(configurations) == 0:
        return 'No results'

    groups = [
        json.loads(configuration.json(exclude={'type'}))
        for configuration in configurations
    ]

    table = [group.values() for group in groups]
    headers = groups[0].keys()

    return tabulate(table, headers=headers)


def find_executable(name: str) -> Path:
    '''
    Find the path to a Linux executable by name.

    Parameters:
        name (str): Executable name.
    Returns:
        Path: A path object referencing the executable.
    Raises:
        KeyError: Expected executable path not found.
    '''

    path = shutil.which('rsync')

    if path is None:
        raise KeyError(f'cannot find "{name}" executable.')

    return Path(path)


def expand_name_template(template: str, name: str) -> str:
    '''
    Expand template placeholders to the name value.

    Supported placeholders:

    - `{name}`
    - `{legacy_escaped_name}`

    Parameters:
        template (str): Template string.
        name (str): Name value.
    Returns:
        str: A string with the name value in place of placeholders.
    Raises:
        ValueError: Expected template placeholder not supported.
    '''

    safe_characters = set(string.ascii_lowercase + string.digits)

    legacy_escaped_name = ''.join(
        [
            c if c in safe_characters else '-' for c in name.lower()
        ]
    )

    try:
        return template.format(
            name=name,
            legacy_escaped_name=legacy_escaped_name
        )
    except KeyError as exception:
        raise ValueError(
            f'"{name}" placeholder not supported, use "name" or "legacy_escaped_name" instead.'
        ) from exception


def glob_datetime(path: Path, pattern: str) -> Iterable[Tuple[Path, datetime]]:
    '''
    Match relative pattern with wildcards and datetime directives.

    Parameters:
        path (Path): Path object.
        pattern (str): Relative pattern.
    Returns:
        Generator[Tuple[Path, datetime]]:
            A generator of tuples with path and datetime objects for each match.
    '''

    path = path.absolute()
    matcher = datetime_glob.Matcher(str(path / pattern))

    match_results = filter(
        lambda result: result[1] is not None,
        map(
            lambda path: (path, matcher.match(path)),
            path.iterdir()
        )
    )

    return (
        (result[0], unwrap(result[1]).as_datetime())
        for result in match_results
    )


__all__ = [
    'unwrap',
    'timezone_aware',
    'get_default_logger',
    'get_default_context_path',
    'get_default_snapshot_path',
    'format_configuration',
    'tabulate_configuration_group',
    'find_executable',
    'expand_name_template',
    'glob_datetime'
]
