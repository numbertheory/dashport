#! /usr/bin/env python3

from setuptools import setup, find_packages
from pathlib import Path
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
    packages=find_packages(exclude=('tests', 'docs', 'examples'))
)
