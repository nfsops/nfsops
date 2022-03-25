'''
Sphinx configuration file.
'''

# pylint: disable=C0103

import os
import sys
from typing import Any, Dict, Tuple

from sphinx.application import Sphinx
from sphinx.ext import apidoc

import nfsops

sys.path.append(os.path.abspath('_pygments/'))


def generate_documentation(*args: Tuple[Any], **kwargs: Dict[str, Any]):  # pylint: disable=W0613
    '''
    Generate API reference documentation.

    Parameters:
        *args (Tuple[Any]): Additional arguments.
        **kwargs (Dict[str, Any]): Additional keyword arguments.
    '''

    config_directory = os.path.abspath(os.path.dirname(__file__))

    module_path = os.path.join(config_directory, '..', '..', 'nfsops/')
    output_path = os.path.join(config_directory, 'api-reference/')

    apidoc.main(['-f', '-e', '-T', '-d', '2', '-o', output_path, module_path])


def setup(app: Sphinx):
    '''
    Sphinx setup stage.

    Parameters:
        app (Sphinx): Sphinx application instance.
    '''

    app.connect('builder-inited', generate_documentation)


project = nfsops.__title__
version = nfsops.__version__
author = nfsops.__author__
copyright = nfsops.__copyright__[:-1]  # pylint: disable=W0622

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'myst_parser'
]

autodoc_default_options = {
    'special-members': (
        '__title__, '
        '__version__, '
        '__description__, '
        '__author__, '
        '__email__, '
        '__license__, '
        '__copyright__, '
        '__init__'
    )
}

napoleon_use_rtype = False

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}
exclude_patterns = [
    'build'
]

html_theme = 'pydata_sphinx_theme'

html_static_path = [
    '_static'
]
html_css_files = [
    'styles/custom.css'
]
templates_path = [
    '_templates'
]

html_title = f'{project} Documentation'
html_favicon = '_static/images/favicon.ico'
html_logo = '_static/images/logo.svg'

html_theme_options = {
    'icon_links': [
        {
            'name': 'GitHub',
            'url': 'https://github.com/nfsops/nfsops',
            'icon': 'fab fa-github'
        },
        {
            'name': 'PyPI',
            'url': 'https://pypi.org/project/nfsops',
            'icon': 'fab fa-python'
        }
    ]
}

pygments_style = 'nfsops_style.NFSopsStyle'
