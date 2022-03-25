'''
NFSops syntax highlighting style.
'''

from pygments.style import Style  # type: ignore
from pygments.token import (  # type: ignore
    Comment,
    Error,
    Keyword,
    Literal,
    Name,
    Number,
    Operator,
    String
)


class NFSopsStyle(Style):
    '''
    NFSops syntax highlighting style.
    '''

    #: Base style.
    default_style = ''

    #: Style properties.
    styles = {
        Comment: '#666f78',
        Comment.Preproc: '#666f78',
        Operator: '#000000',
        Name: '#000000',
        Name.Builtin: '#015493',
        Name.Builtin.Pseudo: '#015493',
        Name.Variable: '#000000',
        Name.Tag: 'bold #015493',
        Name.Decorator: '#000000',
        Name.Label: '#000000',
        Name.Attribute: '#000000',
        Name.Class: '#000000',
        Name.Function: '#000000',
        Keyword: 'bold #015493',
        String: '#dd2458',
        String.Char: '#dd2458',
        Literal: '#009b44',
        Number: '#009b44',
        Error: '#000000'
    }


__all__ = [
    'NFSopsStyle'
]
