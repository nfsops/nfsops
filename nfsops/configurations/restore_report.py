'''
Restore report configuration model.
'''

from typing import Literal, Optional

from pydantic import NonNegativeInt

from .configuration import Configuration


class RestoreReportConfiguration(Configuration):
    '''
    Restore report configuration model.
    '''

    #: Configuration type.
    type: Literal['restore-report'] = 'restore-report'
    #: Single/initial backup version.
    version: NonNegativeInt
    #: Final backup version.
    final_version: Optional[NonNegativeInt] = None


__all__ = [
    'RestoreReportConfiguration'
]
