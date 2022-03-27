'''
Restore report configuration model.
'''

from typing import Literal

from pydantic import NonNegativeInt

from .configuration import Configuration


class RestoreReportConfiguration(Configuration):
    '''
    Restore report configuration model.
    '''

    #: Configuration type.
    type: Literal['restore-report'] = 'restore-report'
    #: Backup name for root context.
    name: str
    #: Path matching pattern relative to template if root context,
    #: relative to current working directory otherwise.
    filter_path: str
    #: Single/initial backup version.
    version: NonNegativeInt
    #: Final backup version.
    final_version: NonNegativeInt


__all__ = [
    'RestoreReportConfiguration'
]
