'''
Backup operator object.
'''

from datetime import datetime
from typing import List

from .. import utils
from ..configurations.backup import BackupConfiguration
from ..configurations.backup_version import BackupVersionConfiguration
from ..configurations.context import ContextConfiguration
from ..configurations.restore import RestoreConfiguration
from ..configurations.restore_report import RestoreReportConfiguration
from ..context_type import ContextType
from .operator import Operator


class BackupOperator(Operator):
    '''
    Backup operator object.
    '''

    #: Backup configuration.
    configuration: BackupConfiguration

    def __init__(self, context: ContextConfiguration, configuration: BackupConfiguration):
        '''
        Initialize backup operator object.

        Parameters:
            context (ContextConfiguration): Context configuration.
            configuration (BackupConfiguration): Backup configuration.
        '''

        super().__init__(context)
        self.configuration = configuration

        self.logger.info(
            'using backup configuration %s.',
            utils.format_configuration_string(self.configuration)
        )

        if (
            context.context != ContextType.ROOT and
            self.configuration.name is not None
        ):
            self.logger.info(
                f'ignoring [name={self.configuration.name}] parameter for non-root context.'
            )

    def list_versions(self) -> List[BackupVersionConfiguration]:
        '''
        Restore backup versions.

        Returns:
            List[BackupVersionConfiguration]: A list reporting available backup versions.
        Raises:
            Exception: Expected operation failed.
        '''

        # TODO: implement it.

        return [
            BackupVersionConfiguration(
                version=0,
                timestamp=datetime.now()
            ),
            BackupVersionConfiguration(
                version=1,
                timestamp=datetime.now()
            )
        ]

    def restore(self, options: RestoreConfiguration) -> RestoreReportConfiguration:
        '''
        Restore backup versions.

        Parameters:
            options (RestoreConfiguration): Restore configuration.
        Returns:
            RestoreReportConfiguration: A restore report for operation.
        Raises:
            Exception: Expected operation failed.
        '''

        # TODO: implement it.

        return RestoreReportConfiguration(version=0)


__all__ = [
    'BackupOperator'
]
