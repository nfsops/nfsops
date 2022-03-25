'''
Python setup script.
'''

import os
from distutils.util import convert_path
from typing import Dict

from setuptools import find_packages, setup  # type: ignore


def get_package_info(name: str) -> Dict[str, str]:
    '''
    Get package description information.

    Parameters:
        name (str): Main package name.
    Returns:
        Dict[str, str]: A dictionary containing package information.
    '''

    with open(
        convert_path(os.path.join(name, 'package.py')),
        encoding='utf-8'
    ) as file:
        package_dict: Dict[str, str] = {}
        exec(file.read(), package_dict)  # pylint: disable=W0122

        return package_dict


def parse_long_description() -> str:
    '''
    Get package long description.

    Returns:
        str: A string representing package long description.
    '''

    with open(convert_path('README.md'), encoding='utf-8') as file:
        return file.read()


PACKAGE_NAME = 'nfsops'

package_info = get_package_info(PACKAGE_NAME)

setup(
    name=PACKAGE_NAME,
    version=package_info['__version__'],
    description=package_info['__description__'],
    long_description=parse_long_description(),
    long_description_content_type='text/markdown',
    author=package_info['__author__'],
    author_email=package_info['__email__'],
    license=package_info['__license__'],
    url='https://nfsops.readthedocs.io',
    download_url='https://pypi.org/project/nfsops',
    project_urls={
        'Code': 'https://github.com/nfsops/nfsops',
        'Issue tracker': 'https://github.com/nfsops/nfsops/issues'
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: BSD License'
    ],
    python_requires='>=3.8.0',
    install_requires=[
        'pydantic>=1.9.0',
        'typer>=0.4.0',
    ],
    extras_require={
        'development': [
            'setuptools>=58.2.0',
            'wheel>=0.37.0',
            'autopep8>=1.6.0',
            'isort>=5.10.0',
            'mypy>=0.9.0',
            'pylint>=2.12.0',
            'pytest>=6.2.0',
            'pytest-cov>=3.0.0',
            'sphinx>=4.3.0',
            'myst-parser>=0.15.0',
            'pydata-sphinx-theme>=0.7.0',
            'twine>=3.7.0',
            'bump2version>=1.0.0'
        ]
    },
    entry_points={
        'console_scripts': [
            f'{PACKAGE_NAME} = {PACKAGE_NAME}.cli:app'
        ]
    },
    packages=find_packages(),
    package_data={
        PACKAGE_NAME: [
            '../README.md',
            '../CHANGELOG.md',
            '../LICENSE.md'
        ]
    },
    zip_safe=False
)
