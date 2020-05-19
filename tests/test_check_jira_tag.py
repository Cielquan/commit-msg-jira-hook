#!/usr/bin/env python3

# ======================================================================================
# Copyright (c) 2020 Christian Riedel
#
# This file 'test_check_jira_tag.py' created 2020-05-19
# is part of the project/program 'commit-msg-jira-hook'.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# Github: https://github.com/Cielquan/
# ======================================================================================
"""
    tests.test_check_jira_tag
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    test check_jira_tag

    :copyright: (c) 2020 Christian Riedel
    :license: GPLv3, see LICENSE for more details
"""
import configparser

from pathlib import Path

import pytest

from click.testing import CliRunner

from commit_msg_jira_hook.check_jira_tag import main


def test_missing_jira_url():
    runner = CliRunner()
    result = runner.invoke(main, ["--jira-tag=TAG", "--verify", "TESTFILE"])
    assert result.exit_code == 1
    assert "Please provide '--jira-url'" in result.output


def test_missing_ini_file(monkeypatch):
    monkeypatch.setattr(Path, "is_file", lambda _: False)
    runner = CliRunner()
    result = runner.invoke(
        main, ["--jira-tag=TAG", "--jira-url=URL", "--verify", "TESTFILE"]
    )
    assert result.exit_code == 1
    assert "No '~/.jira.ini' file found." in result.output


def test_missing_jira_section(monkeypatch):
    monkeypatch.setattr(Path, "is_file", lambda _: True)
    monkeypatch.setattr(configparser.ConfigParser, "read", lambda self, _: "")
    # mock jira ini file
    runner = CliRunner()
    result = runner.invoke(
        main, ["--jira-tag=TAG", "--jira-url=URL", "--verify", "TESTFILE"]
    )
    assert result.exit_code == 1
    assert "No 'jira' section" in result.output
