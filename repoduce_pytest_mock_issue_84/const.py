# coding: utf-8
"""Constants used by repoduce_pytest_mock_issue_84 automations."""

MAJOR_VERSION = 0
MINOR_VERSION = 1
PATCH_VERSION = '0'
__short_version__ = '{}.{}'.format(MAJOR_VERSION, MINOR_VERSION)
__version__ = '{}.{}'.format(__short_version__, PATCH_VERSION)
REQUIRED_PYTHON_VER = (3, 5, 2)

PROJECT_NAME = 'repoduce_pytest_mock_issue_84'
PROJECT_PACKAGE_NAME = 'repoduce_pytest_mock_issue_84'
PROJECT_LICENSE = 'MIT License'
PROJECT_AUTHOR = 'Malcolm Jones'
PROJECT_COPYRIGHT = ' 2017, {}'.format(PROJECT_AUTHOR)
PROJECT_URL = 'https://github.com/bossjones/repoduce_pytest_mock_issue_84'
PROJECT_EMAIL = 'bossjones@theblacktonystark.com'
PROJECT_DESCRIPTION = ('blah blah blah')
PROJECT_LONG_DESCRIPTION = ('blah')
PROJECT_CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: End Users/Desktop',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Natural Language :: English',
    'Programming Language :: Python :: 3.5',
    'Topic :: Home Automation'
]

PROJECT_GITHUB_USERNAME = 'bossjones'
PROJECT_GITHUB_REPOSITORY = 'repoduce_pytest_mock_issue_84'

PYPI_URL = 'https://pypi.python.org/pypi/{}'.format(PROJECT_PACKAGE_NAME)
GITHUB_PATH = '{}/{}'.format(PROJECT_GITHUB_USERNAME,
                             PROJECT_GITHUB_REPOSITORY)
GITHUB_URL = 'https://github.com/{}'.format(GITHUB_PATH)

