'''
Restore configuration model.
'''

from typing import Any, Dict, Literal, Optional, Union

from pydantic import NonNegativeInt, validator

from .configuration import Configuration


class RestoreConfiguration(Configuration):
    '''
    Restore configuration model.
    '''

    #: Configuration type.
    type: Literal['restore'] = 'restore'
    #: Single/initial backup version.
    version: Union[Literal['*'], NonNegativeInt]
    #: Final backup version.
    final_version: Optional[Union[Literal['*'], NonNegativeInt]] = None

    @validator('final_version', always=True)
    @classmethod
    def validate_root_template(
        cls,
        value: Optional[Union[Literal['*'], NonNegativeInt]],
        values: Dict[str, Any]
    ) -> Optional[Union[Literal['*'], NonNegativeInt]]:
        '''
        Return original value if the range of backup versions is valid,
        raise exception otherwise.

        Parameters:
            value (Optional[Union[Literal['*'], NonNegativeInt]]): Final backup version or `None`.
            values (Dict[str, Any]): Dictionary containing all parameter values.
        Returns:
            Optional[Union[Literal['*'], NonNegativeInt]]: A valid final backup version.
        Raises:
            ValueError: Expected range of backup versions is invalid.
        '''

        if value is None:
            return value

        if isinstance(value, str) or isinstance(values['version'], str):
            return value

        if value < values['version']:
            raise ValueError(
                'parameter value must be greater than "version" value.'
            )

        return value


__all__ = [
    'RestoreConfiguration'
]
