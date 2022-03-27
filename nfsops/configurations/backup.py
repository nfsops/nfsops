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
    #: Path matching pattern relative to template if root context,
    #: relative to current working directory otherwise.
    filter_path: Optional[str] = None
    version_template: str = '*_%Y-%m-%d_%H:%M'


__all__ = [
    'BackupConfiguration'
]
