#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `click_demo` package."""

import unittest
from click.testing import CliRunner

from click_demo import click_demo
from click_demo import cli


class TestClick_demo(unittest.TestCase):
    """Tests for `click_demo` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_command_hi(self):
        """Testing Command Hi"""

        runner = CliRunner()
        result = runner.invoke(click_demo.hi)
        assert result.exit_code == 0

        result = runner.invoke(click_demo.hi, ['--help'])
        assert '--name TEXT' in result.output

        result = runner.invoke(click_demo.hi, ['-n', 'PSP'])
        assert 'Hi PSP' in result.output

        result = runner.invoke(click_demo.hi, ['--name', 'PSP'])
        assert 'Hi PSP' in result.output

        result = runner.invoke(click_demo.hi)
        assert 'Hi there!' in result.output

    def test_command_bye(self):
        """Testing Command Bye"""

        runner = CliRunner()
        result = runner.invoke(click_demo.bye)
        assert result.exit_code == 0

        result = runner.invoke(click_demo.bye, ['--help'])
        assert '--name TEXT' in result.output

        result = runner.invoke(click_demo.bye, ['-n', 'PSP'])
        assert 'Bye PSP' in result.output

        result = runner.invoke(click_demo.bye, ['--name', 'PSP'])
        assert 'Bye PSP' in result.output

        result = runner.invoke(click_demo.bye)
        assert 'Bye there!' in result.output
