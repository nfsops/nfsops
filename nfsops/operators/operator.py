'''
Base operator object.
'''

import logging
from abc import ABC

from .. import utils
from ..configurations.context import ContextConfiguration


class Operator(ABC):
    '''
    Base operator object.
    '''

    #: Context configuration.
    context: ContextConfiguration
    #: Logger instance.
    logger: logging.Logger

    def __init__(self, context: ContextConfiguration):
        '''
        Initialize base operator object.

        Parameters:
            context (ContextConfiguration): Context configuration.
        '''

        self.context = context
        self.logger = utils.get_default_logger()

        self.logger.info(
            'using context configuration %s.',
            utils.format_configuration(self.context)
        )


__all__ = [
    'Operator'
]
