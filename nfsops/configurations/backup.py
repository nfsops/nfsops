'''
Backup configuration model.
'''

from typing import Literal, Optional

from .configuration import Configuration


class BackupConfiguration(Configuration):
    '''
    Backup configuration model.
    '''

    #: Configuration type.
    type: Literal['backup'] = 'backup'
    #: Backup name for root context.
    name: Optional[str] = None


__all__ = [
    'BackupConfiguration'
]
