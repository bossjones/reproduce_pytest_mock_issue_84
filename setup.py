#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import platform
import re
import warnings
import pprint
pp = pprint.PrettyPrinter(indent=4)


# Don't force people to install setuptools unless
# we have to.
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

from setuptools import setup
from setuptools import find_packages
from setuptools.command.test import test as TestCommand
from setuptools.command import install_lib

# from distutils.core import setup

# requirements = [
#     'pytest==3.0.7',
#     'pytest-benchmark[histogram]==3.1.0a2',
#     'pytest-catchlog==1.2.2',
#     'pytest-cov==2.4.0',
#     'pytest-ipdb==0.1.dev2',
#     'pytest-leaks==0.2.2',
#     'pytest-mock==1.6.0',
#     'pytest-rerunfailures==2.1.0',
#     'pytest-sugar==0.8.0',
#     'pytest-timeout==1.2.0',
#     'python-dateutil==2.6.0',
#     'python-dbusmock==0.16.7',
#     'flake8==3.3.0',
#     'flake8-docstrings==1.0.3',
#     'coverage==4.3.4',
#     'pylint==1.7.1',
#     'coveralls==1.1',
#     'ipython==6.0.0',
#     'gnureadline==6.3.3',
#     'mock==2.0.0',
#     'mock-open==1.3.1'
# ]

requirements = [
    'pytest>=3.0',
    'pytest-timeout>=1.0.0',
    'pytest-catchlog>=1.2.2',
    'pytest-cov>=2.3.1',
    'flake8>=2.6.2',
    'flake8-docstrings>=0.2.8',
    'coverage>=4.1',
    'cryptography==1.8.1',
    'pylint>=1.5.6',
    'coveralls>=1.1',
    'ipython>=5.1.0',
    'gnureadline>=6.3.0',
    'requests_mock>=1.0',
    'mock-open>=1.3.1',
    'mock',
    'pytest-benchmark[histogram]>=3.0.0rc1',
    'python-dbusmock',
    # 'pdbpp==0.8.3',
    'pytest-sugar==0.8.0',
    # 'pytest-ipdb',
    'pytest-rerunfailures>=2.1.0',
    'pytest-mock'

]

class PyTest(TestCommand):
    """Run pytest."""

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests', '--ignore', 'tests/sandbox', '--verbose']
        # self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

setup(
    name='repoduce_pytest_mock_issue_84',
    version='0.0.1',
    description='Reproduces marathon issue #84',
    author='Malcolm Jones',
    author_email='bossjones@theblacktonystark.com',
    url='https://github.com/pytest-dev/pytest-mock/issues/84',
    packages=[
        'repoduce_pytest_mock_issue_84',
    ],
    package_dir={'repoduce_pytest_mock_issue_84':
                 'repoduce_pytest_mock_issue_84'},
    install_requires=requirements,
    test_suite='tests',
    cmdclass={'test': PyTest}
)
