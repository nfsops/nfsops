'''
Backup version configuration model.
'''

from datetime import datetime
from typing import Literal

from pydantic import NonNegativeInt

from .configuration import Configuration


class BackupVersionConfiguration(Configuration):
    '''
    Backup version configuration model.
    '''

    #: Configuration type.
    type: Literal['backup-version'] = 'backup-version'
    #: Backup version.
    version: NonNegativeInt
    #: Backup timestamp
    timestamp: datetime


__all__ = [
    'BackupVersionConfiguration'
]
