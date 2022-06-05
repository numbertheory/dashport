#! /usr/bin/env python3

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='dashport',
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    description='Dashport curses wrapper for Python',
    long_description=readme,
    author='JP Etcheber',
    author_email='jetcheber@gmail.com',
    url='https://github.com/numbertheory/dashport',
    license_files=('LICENSE'),
    packages=find_packages(exclude=('tests', 'docs', 'examples'))
)
