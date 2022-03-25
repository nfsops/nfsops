'''
Base configuration model.
'''

from pydantic import BaseModel


class Configuration(BaseModel):
    '''
    Base configuration model.
    '''

    class Config:
        '''
        Model configuration properties.
        '''

        #: Whether to perform validation on assignment to attributes.
        validate_assignment = True


__all__ = [
    'Configuration'
]
