#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import platform
import pprint
import re
import sys
import warnings

from setuptools import find_packages, setup
from setuptools.command import install_lib
from setuptools.command.test import test as TestCommand

from repoduce_pytest_mock_issue_84.const import (GITHUB_URL, PROJECT_AUTHOR,
                                                 PROJECT_CLASSIFIERS,
                                                 PROJECT_DESCRIPTION,
                                                 PROJECT_EMAIL,
                                                 PROJECT_LICENSE,
                                                 PROJECT_PACKAGE_NAME,
                                                 PROJECT_URL, __version__)

pp = pprint.PrettyPrinter(indent=4)


# Don't force people to install setuptools unless
# we have to.
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup


HERE = os.path.abspath(os.path.dirname(__file__))
DOWNLOAD_URL = ('{}/archive/'
                '{}.zip'.format(GITHUB_URL, __version__))

# PACKAGES = find_packages(exclude=['tests', 'tests.*'])
PACKAGE_NAME = PROJECT_PACKAGE_NAME

print('Current Python Version, B: {}'.format(sys.version_info))

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

static = {}

for root, dirs, files in os.walk('static'):
    for filename in files:
        filepath = os.path.join(root, filename)

        if root not in static:
            static[root] = []

        static[root].append(filepath)

# Might use this later
try:
    here = os.path.abspath(os.path.dirname(__file__))
except:
    pass


def read_requirements(filename):
    content = open(os.path.join(here, filename)).read()
    requirements = map(lambda r: r.strip(), content.splitlines())
    return requirements

# from distutils.core import setup

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
    name=PROJECT_PACKAGE_NAME,
    version=__version__,
    description=PROJECT_DESCRIPTION,
    long_description=readme + '\n\n' + history,
    author=PROJECT_AUTHOR,
    author_email=PROJECT_EMAIL,
    url=PROJECT_URL,
    download_url=DOWNLOAD_URL,

    # name='repoduce_pytest_mock_issue_84',
    # version='0.0.1',
    # description='Reproduces marathon issue #84',
    # author='Malcolm Jones',
    # author_email='bossjones@theblacktonystark.com',
    # url='https://github.com/pytest-dev/pytest-mock/issues/84',
    packages=[
        'repoduce_pytest_mock_issue_84',
    ],
    package_dir={'repoduce_pytest_mock_issue_84':
                 'repoduce_pytest_mock_issue_84'},
    include_package_data=True,
    install_requires=requirements,
    license=PROJECT_LICENSE,
    zip_safe=False,
    keywords='repoduce_pytest_mock_issue_84',
    classifiers=PROJECT_CLASSIFIERS,
    test_suite='tests',
    cmdclass={'test': PyTest}
)
