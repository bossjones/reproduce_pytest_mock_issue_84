#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
repoduce_pytest_mock_issue_84 unit tests
"""

import glob
import os
import sys
# import unittest


def get_dir():
    """
    Gets the repoduce_pytest_mock_issue_84 root directory.
    """
    tests_dir = os.path.dirname(os.path.abspath(__file__))
    os_dir = os.path.join(tests_dir, os.path.pardir)
    return os.path.abspath(os_dir)


PROJECT_ROOT = get_dir()


def setup():
    """Sets paths and initializes modules, to be able to run the tests."""
    return True
