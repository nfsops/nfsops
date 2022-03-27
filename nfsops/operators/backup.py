'''
Backup operator object.
'''

from operator import itemgetter
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
        Raises:
            ValueError: Expected name parameter is invalid for root context.
            KeyError: Expected backup path not found for root context.
        '''

        super().__init__(context)
        self.configuration = configuration

        self.logger.info(
            'using backup configuration %s.',
            utils.format_configuration(self.configuration)
        )

        if (
            self.context.context == ContextType.SUBPATH and
            self.configuration.name is not None
        ):
            self.logger.info(
                f'ignoring [backup.name={self.configuration.name}] parameter for non-root context.'
            )

        if self.context.context == ContextType.ROOT:
            if self.configuration.name is None:
                raise ValueError(
                    '"name" parameter is required for root context.'
                )

            subpath_pattern = utils.expand_name_template(
                utils.unwrap(self.context.root_template),
                utils.unwrap(self.configuration.name)
            )

            subpaths = list(
                utils.unwrap(self.context.path).glob(subpath_pattern)
            )

            if len(subpaths) != 1:
                raise KeyError(
                    'cannot find or infer backup path using name template.'
                )

            self.context.path = subpaths[0].absolute()

        if self.configuration.filter_path is None:
            self.configuration.filter_path = '**/*'

            self.logger.info(
                f'using [backup.filter_path={self.configuration.name}] as default parameter.'
            )

    def list_versions(self) -> List[BackupVersionConfiguration]:
        '''
        Restore backup versions.

        Returns:
            List[BackupVersionConfiguration]: A list reporting available backup versions.
        '''

        snapshot_path = utils.get_default_snapshot_path(
            utils.unwrap(self.context.path)
        )

        version_paths = sorted(
            filter(
                lambda result: result[0].is_dir(),
                utils.glob_datetime(
                    snapshot_path,
                    self.configuration.version_template
                )
            ),
            reverse=True,
            key=itemgetter(0)
        )

        return list(
            BackupVersionConfiguration(
                version=version_path[0],
                timestamp=version_path[1][1]
            )
            for version_path in enumerate(version_paths)
        )

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

        return RestoreReportConfiguration(
            name='username',
            filter_path='/home/user/*',
            version=0,
            final_version=0
        )


__all__ = [
    'BackupOperator'
]
