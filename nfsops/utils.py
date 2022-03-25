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

from . import package
from .configurations.configuration import Configuration
from .context_type import ContextType


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


def get_default_volume_path(context: ContextType) -> Path:
    '''
    Return default volume path for context type.

    Default values:

    - `ContextType.ROOT`: `/var/nfs-shared`
    - `ContextType.SUBPATH`: `$HOME`

    Parameters:
        context (ContextType): Context type.
    Returns:
        Path: A path object referencing the default volume path.
    '''

    default_mapping = {
        ContextType.ROOT: Path('/var/nfs-shared'),
        ContextType.SUBPATH: Path().home()
    }

    return default_mapping[context]


def format_configuration_string(configuration: Configuration) -> str:
    '''
    Format configuration object to string using the formatting style
    `[key0=value0 key1=value1 ... keyn=valuen]`.

    Parameters:
        configuration (Configuration): Configuration instance.
    Returns:
        str: A single-line string using custom formatting style.
    '''

    parameters = json.loads(configuration.json(exclude={'type'}))

    inner_string_content = ' '.join(
        f'{key}={value}' for key, value in parameters.items()
    )

    return f'[{inner_string_content}]'


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


__all__ = [
    'timezone_aware',
    'get_default_logger',
    'get_default_volume_path',
    'format_configuration_string',
    'find_executable',
    'expand_name_template'
]
