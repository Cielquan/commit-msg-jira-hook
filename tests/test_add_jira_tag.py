# noqa: D205,D208,D400
"""
    tests.test_add_jira_tag
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    test add_jira_tag

    :copyright: (c) 2020 Christian Riedel
    :license: GPLv3, see LICENSE for more details
"""
# pylint: disable=W0613,W0621
from pathlib import Path

import pytest

from click.testing import CliRunner
from git import Repo  # type: ignore[import]

from commit_msg_jira_hook.add_jira_tag import main


@pytest.fixture
def cli_runner():
    """Yield click cli test runner."""
    yield CliRunner()


@pytest.fixture
def mock_home(monkeypatch, tmp_path):
    """Yield `home` dir mock path."""
    home = tmp_path / "~"
    home.mkdir()
    monkeypatch.setattr(Path, "home", lambda: home)
    yield home


@pytest.fixture
def mock_commit_msg_file(mock_home):
    """Yield 'COMMIT_MSG' path in `home` dir mock."""
    commit_msg_file = mock_home / "COMMIT_MSG"
    yield commit_msg_file


def test_deactivate_with(cli_runner, mock_commit_msg_file):
    """Assert commit msg w/o prepended string."""
    mock_commit_msg_file.write_text("no-tag commit message 0815")
    result = cli_runner.invoke(
        main, ["--jira-tag=TAG", "--deactivate-with=no-tag", str(mock_commit_msg_file)]
    )
    assert result.exit_code == 0
    assert mock_commit_msg_file.read_text() == "commit message 0815"


def test_abort_no_tag_in_branch_name(cli_runner, mock_commit_msg_file, monkeypatch):
    """Assert exit code 1 if no tag found in branch name."""

    class MockBranch:  # pylint: disable=too-few-public-methods, missing-class-docstring
        name = "no-tag-in-branch-name"

    monkeypatch.setattr(Repo, "active_branch", MockBranch())

    mock_commit_msg_file.write_text("DUMMY")
    result = cli_runner.invoke(main, ["--jira-tag=TEST", str(mock_commit_msg_file)])
    assert result.exit_code == 1


def test_exit_no_tag_in_branch_name(cli_runner, mock_commit_msg_file, monkeypatch):
    """Assert exit code 0 if no tag found in branch name."""

    class MockBranch:  # pylint: disable=too-few-public-methods, missing-class-docstring
        name = "no-tag-in-branch-name"

    monkeypatch.setattr(Repo, "active_branch", MockBranch())

    mock_commit_msg_file.write_text("DUMMY")
    result = cli_runner.invoke(
        main, ["--jira-tag=TEST", "--no-error", str(mock_commit_msg_file)]
    )
    assert result.exit_code == 0


def test_tag_in_msg_add_again(cli_runner, mock_commit_msg_file, monkeypatch):
    """Assert tag is always added in front."""

    class MockBranch:  # pylint: disable=too-few-public-methods, missing-class-docstring
        name = "feat/TEST-123-branch"

    monkeypatch.setattr(Repo, "active_branch", MockBranch())

    mock_commit_msg_file.write_text("TEST-123 commit message 0815")
    result = cli_runner.invoke(
        main, ["--jira-tag=TEST", "--always", str(mock_commit_msg_file)]
    )
    assert result.exit_code == 0
    assert mock_commit_msg_file.read_text() == "TEST-123: TEST-123 commit message 0815"


def test_tag_in_msg_not_add_again(cli_runner, mock_commit_msg_file, monkeypatch):
    """Assert tag is not added again."""

    class MockBranch:  # pylint: disable=too-few-public-methods, missing-class-docstring
        name = "feat/TEST-123-branch"

    monkeypatch.setattr(Repo, "active_branch", MockBranch())

    mock_commit_msg_file.write_text("TEST-123 commit message 0815")
    result = cli_runner.invoke(
        main, ["--jira-tag=TEST", "--auto", str(mock_commit_msg_file)]
    )
    assert result.exit_code == 0
    assert mock_commit_msg_file.read_text() == "TEST-123 commit message 0815"


def test_tag_added(cli_runner, mock_commit_msg_file, monkeypatch):
    """Assert normal use works."""

    class MockBranch:  # pylint: disable=too-few-public-methods, missing-class-docstring
        name = "feat/TEST-123-branch"

    monkeypatch.setattr(Repo, "active_branch", MockBranch())

    mock_commit_msg_file.write_text("commit message 0815")
    result = cli_runner.invoke(main, ["--jira-tag=TEST", str(mock_commit_msg_file)])
    assert result.exit_code == 0
    assert mock_commit_msg_file.read_text() == "TEST-123: commit message 0815"


def test_tag_added_even_when_tag_as_comment(cli_runner, mock_commit_msg_file, monkeypatch):
    """Assert normal use works even when tag is already in message but as comment."""

    class MockBranch:  # pylint: disable=too-few-public-methods, missing-class-docstring
        name = "feat/TEST-123-branch"

    monkeypatch.setattr(Repo, "active_branch", MockBranch())

    mock_commit_msg_file.write_text("commit message 0815\n#TEST-123")
    result = cli_runner.invoke(main, ["--jira-tag=TEST", str(mock_commit_msg_file)])
    assert result.exit_code == 0
    assert mock_commit_msg_file.read_text() == "TEST-123: commit message 0815\nTEST-123"
