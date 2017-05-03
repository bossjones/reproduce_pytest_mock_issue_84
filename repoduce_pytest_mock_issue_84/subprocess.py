#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pylint: disable=C0102, R0201, W1202, W1201, C0123, C0103

"""repoduce_pytest_mock_issue_84. Fake subprocess module."""

# from mock import Mock, patch


# from __future__ import with_statement, division, absolute_import

import os
import sys
import logging

logger = logging.getLogger(__name__)


def check_pid(pid):
    """Check For the existence of a unix pid."""
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True

class Subprocess(object):
    """KungFuPanda object"""

    def __init__(self, command, name=None, fork=False, run_check_command=True):
        """Create instance of Subprocess."""

        self.secret_ingredient = "passion"

        self.process = None
        self.pid = None

        if not fork:
            self.stdout = True
            self.stderr = True
        else:
            self.stdout = False
            self.stderr = False

        self.forked = fork

        if run_check_command:
            self.check_command_type(command)

        self.command = command
        self.name = name

        logger.debug("command: {}".format(self.command))
        logger.debug("name: {}".format(self.name))
        logger.debug("forked: {}".format(self.forked))
        logger.debug("process: {}".format(self.process))
        logger.debug("pid: {}".format(self.pid))

        if fork:
            self.fork()

    def foo(self):
        """foo."""
        return "soup"

    def bar(self, instructor):
        """bar."""
        if instructor.message == "punch":
            return "hug"
        else:
            return "whatever"

    def hello(self):
        """hello."""
        return "ahoy!"

    def spawn_command(self):
        """Return: Tuple (pid(int), stdin, stdout, stderr)"""
        return (1345, None, self.stdout, self.stderr,)

    def map_type_to_command(self, command):
        """Return: Map after applying type to several objects in an array"""
        return list(map(type, command))

    def check_command_type(self, command):
        """check_command_type"""
        types = self.map_type_to_command(command)

        if type(types) is not list:
            raise TypeError(
                "Variable types should return a list in python3. Got: {}".format(types))

        for t in types:
            if t is not str:
                raise TypeError(
                    "Executables and arguments must be str objects. types: {}".format(t))

        logger.debug("Running Command: %r" % " ".join(command))
        return True

    def run(self):
        """Run the process."""

        self.pid, \
        self.stdin, \
        self.stdout, \
        self.stderr = self.spawn_command()

        logger.debug("command: {}".format(self.command))
        logger.debug("stdin: {}".format(self.stdin))
        logger.debug("stdout: {}".format(self.stdout))
        logger.debug("stderr: {}".format(self.stderr))
        logger.debug("pid: {}".format(self.pid))

        # close file descriptor
        # self.pid.close()

        print(self.stderr)

        # NOTE: GLib.PRIORITY_HIGH = -100
        # Use this for high priority event sources.
        # It is not used within GLib or GTK+.
        watch = "this value doesnt matter"

        return self.pid

    def exited_cb(self, pid, condition):
        if not self.forked:
            print("exited: {} {}".format(pid, condition))

    def fork(self):
        """Fork the process."""
        try:
            # first fork
            pid = os.fork()
            if pid > 0:
                logger.debug('pid greater than 0 first time')
                sys.exit(0)
        except OSError as e:
            logger.error('Error forking process first time')
            sys.exit(1)

        # Change the current working directory to path.
        os.chdir("/")

        os.setsid()

        # Set the current numeric umask and return the previous umask.
        os.umask(0)

        try:
            # second fork
            pid = os.fork()
            if pid > 0:
                logger.debug('pid greater than 0 second time')
                sys.exit(0)
        except OSError as e:
            logger.error('Error forking process second time')
            sys.exit(1)


class Instructor(object):

    tribe = "know_it_all"

    def __init__(self, name):
        self.name = name
        self.message = None

    def message(self, message):
        """message"""
        self.message = "What up {}".format(message)

    @classmethod
    def get_tribe(cls):
        """get_tribe"""
        return cls.tribe
