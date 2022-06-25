#! /usr/bin/env python3

from setuptools import setup, find_packages
from pathlib import Path

try:
    import importlib.resources as pkg_resources
except ImportError:
    # Try backported to PY<37 `importlib_resources`.
    import importlib_resources as pkg_resources

from . import resources

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='dashport',
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    description='Dashport curses wrapper for Python',
    long_description_content_type="text/markdown",
    long_description=long_description,
    author='JP Etcheber',
    author_email='jetcheber@gmail.com',
    url='https://github.com/numbertheory/dashport',
    license_files=('LICENSE'),
    packages=find_packages(exclude=('tests', 'docs', 'examples')),
    package_data={'dashport': ['resources/*.json']},
    include_package_data=True
)
