'''
Context type enumeration.
'''

from enum import Enum


class ContextType(str, Enum):
    '''
    Context type enumeration.
    '''

    #: Root context type.
    ROOT = 'root'
    #: Subpath context type.
    SUBPATH = 'subpath'


__all__ = [
    'ContextType'
]
