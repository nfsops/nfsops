'''
Context configuration model.
'''

import os
from typing import Any, Dict, Literal, Optional

from pydantic import DirectoryPath, Field, validator

from .. import utils
from ..context_type import ContextType
from .configuration import Configuration


class ContextConfiguration(Configuration):
    '''
    Context configuration model.
    '''

    #: Configuration type.
    type: Literal['context'] = 'context'
    #: Context type.
    context: ContextType = Field(
        default_factory=lambda: os.getenv(
            'NFSOPS_CONTEXT', ContextType.SUBPATH.value
        )
    )
    #: Path template for backup name reference in the root context.
    root_template: Optional[str] = Field(
        default_factory=lambda: os.getenv('NFSOPS_ROOT_TEMPLATE')
    )
    #: Volume path. Defaults to `$HOME` for subpath context, `/var/nfs-shared` otherwise.
    path: Optional[DirectoryPath] = Field(
        default_factory=lambda: os.getenv('NFSOPS_PATH')
    )

    @validator('root_template', always=True)
    @classmethod
    def validate_root_template(
        cls,
        value: Optional[str],
        values: Dict[str, Any]
    ) -> Optional[str]:
        '''
        Return the original value if the root template is available for root context,
        raise exception otherwise.

        Parameters:
            value (Optional[str]): Root template or `None`.
            values (Dict[str, Any]): Dictionary containing all parameter values.
        Returns:
            Optional[str]: A root template string or `None`.
        Raises:
            ValueError: Expected root template not available for root context.
        '''

        if values['context'] == ContextType.ROOT and value is None:
            raise ValueError(
                'parameter is required for root context.'
            )

        return value

    @validator('path', always=True)
    @classmethod
    def validate_path(
        cls,
        value: Optional[DirectoryPath],
        values: Dict[str, Any]
    ) -> Optional[DirectoryPath]:
        '''
        Return the default volume path based on context if the value is "None",
        original value otherwise.

        Parameters:
            value (Optional[DirectoryPath]): Directory path or `None`.
            values (Dict[str, Any]): Dictionary containing all parameter values.
        Returns:
            Optional[DirectoryPath]: A default directory path or `None`.
        '''

        if value is None:
            logger = utils.get_default_logger()

            context_type = values['context']
            value = utils.get_default_volume_path(context_type)

            logger.info(
                f'using "{value}" as default path for "{context_type}" context.'
            )

            return value

        return value


__all__ = [
    'ContextConfiguration'
]
