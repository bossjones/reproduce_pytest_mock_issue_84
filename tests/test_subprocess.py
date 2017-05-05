#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_subprocess
----------------------------------
"""

import os
import sys
import pytest
from _pytest.monkeypatch import MonkeyPatch


import repoduce_pytest_mock_issue_84
from repoduce_pytest_mock_issue_84 import subprocess

import signal
import builtins
import re

# R0201 = Method could be a function Used when a method doesn't use its bound instance,
# and so could be written as a function.
# pylint: disable=R0201
# pylint: disable=C0111


@pytest.fixture(scope="session")
def monkeysession(request):
    mpatch = MonkeyPatch()
    yield mpatch
    mpatch.undo()


class TestSubprocess(object):
    '''Units tests for Scarlett Subprocess, subclass of GObject.Gobject.'''

    def test_check_pid_os_error(self, mocker):
        if os.environ.get('ENABLE_STOPALL'):
            mocker.stopall()
        
        kill_mock = mocker.MagicMock(name=__name__ + "_kill_mock_OSError")
        kill_mock.side_effect = OSError

        # patch
        mocker.patch.object(
            repoduce_pytest_mock_issue_84.subprocess.os, 'kill', kill_mock)

        # When OSError occurs, throw False
        assert not repoduce_pytest_mock_issue_84.subprocess.check_pid(
            4353634632623)
        # Verify that os.kill only called once
        assert kill_mock.call_count == 1

        # mocker.stopall()

    def test_check_pid(self, mocker):
        # mocker.stopall()

        # mock
        kill_mock = mocker.MagicMock(name=__name__ + "_kill_mock")

        mocker.patch.object(
            repoduce_pytest_mock_issue_84.subprocess.os, 'kill', kill_mock)

        result = repoduce_pytest_mock_issue_84.subprocess.check_pid(123)
        assert kill_mock.called
        # NOTE: test against signal 0
        # sending the signal 0 to a given PID just checks if any
        # process with the given PID is running and you have the
        # permission to send a signal to it.
        kill_mock.assert_called_once_with(123, 0)
        assert result is True

        
        if os.environ.get('ENABLE_STOPALL'):
            mocker.stopall()

    # FIXME: This guy is causing the problem somehow!
    def test_subprocess_init(self, mocker):
        
        if os.environ.get('ENABLE_STOPALL'):
            mocker.stopall()

        mock_check_command_type = mocker.MagicMock(
            name=__name__ + "_mock_check_command_type")
        mock_check_command_type.return_value = True
        mock_fork = mocker.MagicMock(name=__name__ + "_mock_fork")
        mock_logging_debug = mocker.MagicMock(
            name=__name__ + "_mock_logging_debug")

        # mock
        mocker.patch.object(
            repoduce_pytest_mock_issue_84.subprocess.logging.Logger, 'debug', mock_logging_debug)
        mocker.patch.object(repoduce_pytest_mock_issue_84.subprocess.Subprocess,
                            'check_command_type', mock_check_command_type)
        mocker.patch.object(
            repoduce_pytest_mock_issue_84.subprocess.Subprocess, 'fork', mock_fork)

        # NOTE: On purpose this is an invalid cmd. Should be of type array
        test_command = ['who']

        test_name = 'test_who'
        test_fork = False

        s_test = repoduce_pytest_mock_issue_84.subprocess.Subprocess(test_command,
                                                                     name=test_name,
                                                                     fork=test_fork)

        # action
        assert s_test.check_command_type(test_command) is True
        mock_check_command_type.assert_called_with(['who'])
        assert not s_test.process
        assert not s_test.pid
        assert s_test.name == 'test_who'
        assert not s_test.forked
        assert s_test.stdout is True
        assert s_test.stderr is True

        mock_logging_debug.assert_any_call("command: ['who']")
        mock_logging_debug.assert_any_call("name: test_who")
        mock_logging_debug.assert_any_call("forked: False")
        mock_logging_debug.assert_any_call("process: None")
        mock_logging_debug.assert_any_call("pid: None")
        mock_fork.assert_not_called()

        
        if os.environ.get('ENABLE_STOPALL'):
            mocker.stopall()

    # FIXME: This guy is causing problems too!
    def test_subprocess_map_type_to_command(self, mocker):
        """Using the mock.patch decorator (removes the need to import builtins)"""
        
        if os.environ.get('ENABLE_STOPALL'):
            mocker.stopall()

        mock_logging_debug = mocker.MagicMock(
            name=__name__ + "_mock_logging_debug")

        # mock
        mocker.patch.object(
            repoduce_pytest_mock_issue_84.subprocess.logging.Logger, 'debug', mock_logging_debug)\

        # NOTE: On purpose this is an invalid cmd. Should be of type array
        test_command = ["who", "-b"]
        test_name = 'test_who'
        test_fork = False

        # create subprocess object
        s_test = repoduce_pytest_mock_issue_84.subprocess.Subprocess(test_command,
                                                                     name=test_name,
                                                                     fork=test_fork,
                                                                     run_check_command=False)

        spy = mocker.spy(s_test, 'map_type_to_command')
        assert isinstance(s_test.map_type_to_command(test_command), list)
        # NOTE: According to this blog post, assert_called_once didn't get added till 3.6??
        # source: https://allanderek.github.io/posts/unittestmock-small-gotcha/
        # "So Python 3.4 and 3.6 pass as we expect. But Python3.5 gives an error stating that
        # there is no assert_called_once method on the mock object, which is true since that
        # method was not added until version 3.6. This is arguably what Python3.4 should have done."
        # assert s_test.map_type_to_command.assert_called_once_with(test_command)
        spy.assert_called_once_with(test_command)
        
        if os.environ.get('ENABLE_STOPALL'):
            mocker.stopall()

    def test_subprocess_check_command_type(self, mocker):
        """Using the mock.patch decorator (removes the need to import builtins)"""
        
        if os.environ.get('ENABLE_STOPALL'):
            mocker.stopall()

        test_command = ["who", "-b"]
        test_name = 'test_who'
        test_fork = False

        # mock
        mock_map_type_to_command = mocker.MagicMock(
            name="mock_map_type_to_command")
        mock_map_type_to_command.side_effect = [int, [int, int]]
        mock_fork = mocker.MagicMock(name="mock_fork")
        mock_logging_debug = mocker.MagicMock(name="mock_logging_debug")

        mocker.patch.object(
            repoduce_pytest_mock_issue_84.subprocess.logging.Logger, 'debug', mock_logging_debug)
        mocker.patch.object(repoduce_pytest_mock_issue_84.subprocess.Subprocess,
                            'map_type_to_command', mock_map_type_to_command)
        mocker.patch.object(
            repoduce_pytest_mock_issue_84.subprocess.Subprocess, 'fork', mock_fork)

        # action
        with pytest.raises(TypeError) as excinfo:
            repoduce_pytest_mock_issue_84.subprocess.Subprocess(test_command,
                                                                name=test_name,
                                                                fork=test_fork,
                                                                run_check_command=True)
        assert str(
            excinfo.value) == "Variable types should return a list in python3. Got: <class 'int'>"

        with pytest.raises(TypeError) as excinfo:
            repoduce_pytest_mock_issue_84.subprocess.Subprocess(test_command,
                                                                name=test_name,
                                                                fork=test_fork,
                                                                run_check_command=True)

        assert str(
            excinfo.value) == "Executables and arguments must be str objects. types: <class 'int'>"

        
        if os.environ.get('ENABLE_STOPALL'):
            mocker.stopall()
