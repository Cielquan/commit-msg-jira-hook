# noqa: D205,D208,D400
"""
    tests.test_check_jira_tag
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    test check_jira_tag

    :copyright: (c) 2020 Christian Riedel
    :license: GPLv3, see LICENSE for more details
"""
# pylint: disable=W0613,W0621
from pathlib import Path

import pytest

from click.testing import CliRunner
from jira import JIRA  # type: ignore[import]
from jira import exceptions as jira_exc

from commit_msg_jira_hook.check_jira_tag import main


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
def mock_ini(mock_home):
    """Yield '.jira.ini' mock path in `home` dir mock."""
    ini = mock_home / ".jira.ini"
    ini.write_text("[jira]\nJIRA_USERNAME=USERNAME\nJIRA_TOKEN=TOKEN\n")
    yield ini


@pytest.fixture
def mock_commit_msg_file(mock_home):
    """Yield 'COMMIT_MSG' path in `home` dir mock."""
    commit_msg_file = mock_home / "COMMIT_MSG"
    yield commit_msg_file


def test_missing_jira_url(cli_runner):
    """Assert error on missing jira-url when `--verify`."""
    result = cli_runner.invoke(main, ["--jira-tag=TAG", "--verify", "NO_FILE"])
    assert result.exit_code == 1
    assert "Please provide '--jira-url'" in result.output


def test_missing_ini_file(mock_home, cli_runner):
    """Assert error on missing '~/.jira.ini' file when `--verify`."""
    result = cli_runner.invoke(
        main, ["--jira-tag=TAG", "--verify", "--jira-url=URL", "NO_FILE"]
    )
    assert result.exit_code == 1
    assert "No '~/.jira.ini' file found." in result.output


def test_missing_jira_section(mock_home, cli_runner):
    """Assert error on missing 'jira' section in '~/.jira.ini' file."""
    mock_ini = mock_home / ".jira.ini"
    mock_ini.write_text("")

    result = cli_runner.invoke(
        main, ["--jira-tag=TAG", "--verify", "--jira-url=URL", "NO_FILE"]
    )
    assert result.exit_code == 1
    assert "No 'jira' section" in result.output


def test_missing_conf_key(mock_home, cli_runner):
    """Assert error on missing conf key in 'jira' section."""
    mock_ini = mock_home / ".jira.ini"
    mock_ini.write_text("[jira]\nJIRA_USERNAME=USERNAME\n")

    result = cli_runner.invoke(
        main, ["--jira-tag=TAG", "--verify", "--jira-url=URL", "NO_FILE"]
    )

    assert result.exit_code == 1
    assert "Missing 'JIRA_TOKEN'" in result.output


def test_empty_commit_msg(mock_ini, mock_commit_msg_file, cli_runner):
    """Assert error on empty commit msg."""
    mock_commit_msg_file.write_text("")

    result = cli_runner.invoke(
        main, ["--jira-tag=TAG", "--jira-url=URL", str(mock_commit_msg_file)]
    )

    assert result.exit_code == 1
    assert "Commit message is empty." in result.output


def test_empty_commit_msg_but_comments(mock_ini, mock_commit_msg_file, cli_runner):
    """Assert error on empty commit msg."""
    mock_commit_msg_file.write_text("\n#Foobar")

    result = cli_runner.invoke(
        main, ["--jira-tag=TAG", "--jira-url=URL", str(mock_commit_msg_file)]
    )

    assert result.exit_code == 1
    assert "Commit message is empty." in result.output


@pytest.mark.parametrize(
    "commit_msg",
    [
        "message",
        "message tag",
        "message tag-",
        "message #tag",
        "message #tag-123",
        "tag message",
        "tag- message",
    ],
)
def test_missing_tag(commit_msg, mock_ini, mock_commit_msg_file, cli_runner):
    """Assert error on missing tag."""
    mock_commit_msg_file.write_text(commit_msg)

    result = cli_runner.invoke(
        main, ["--jira-tag=TAG", "--jira-url=URL", str(mock_commit_msg_file)]
    )

    assert result.exit_code == 1
    assert "'TAG' tag not found" in result.output


@pytest.mark.parametrize(
    "commit_msg",
    [
        "message TAG",
        "message TAG-",
        "message #TAG",
        "message #TAG-",
        "TAG message",
        "TAG- message",
    ],
)
def test_missing_tag_number(commit_msg, mock_ini, mock_commit_msg_file, cli_runner):
    """Assert error on missing tag number."""
    mock_commit_msg_file.write_text(commit_msg)

    result = cli_runner.invoke(
        main, ["--jira-tag=TAG", "--jira-url=URL", str(mock_commit_msg_file)]
    )

    assert result.exit_code == 1
    assert "'TAG' tag but no number" in result.output


def test_jira_error(mock_ini, mock_commit_msg_file, monkeypatch, cli_runner):
    """Assert error on jira api login."""
    mock_commit_msg_file.write_text("TAG-123")

    def mock_init(*args, **kwargs):
        raise jira_exc.JIRAError()

    monkeypatch.setattr(JIRA, "__init__", mock_init)

    result = cli_runner.invoke(
        main, ["--jira-tag=TAG", "--jira-url=URL", str(mock_commit_msg_file)]
    )

    assert result.exit_code == 1
    assert "Error connecting to jira." in result.output


def test_jira_issue_error(mock_ini, mock_commit_msg_file, monkeypatch, cli_runner):
    """Assert error on jira issue api call."""
    mock_commit_msg_file.write_text("TAG-123")

    def mock_init(*args, **kwargs):
        pass

    def mock_issue(*args, **kwargs):
        raise jira_exc.JIRAError()

    monkeypatch.setattr(JIRA, "__init__", mock_init)
    monkeypatch.setattr(JIRA, "issue", mock_issue)

    result = cli_runner.invoke(
        main, ["--jira-tag=TAG", "--jira-url=URL", str(mock_commit_msg_file)]
    )

    assert result.exit_code == 1
    assert "TAG-123 does not exist or no permission" in result.output


def test_no_verify(mock_ini, mock_commit_msg_file, cli_runner):
    """Assert no error on --no-verify."""
    mock_commit_msg_file.write_text("TAG-123")

    result = cli_runner.invoke(
        main, ["--jira-tag=TAG", "--no-verify", str(mock_commit_msg_file)]
    )

    assert result.exit_code == 0


@pytest.mark.parametrize(
    "commit_msg",
    [
        "TAG message TAG123",
        "TAG message TAG-123",
        "message #TAG #TAG-123 #TAG",
    ],
)
def test_all_tag_finds_are_search_for_fullmatch(
    commit_msg, mock_ini, mock_commit_msg_file, cli_runner
):
    """Assert next tag occurance is checked if prior one is missing number."""
    mock_commit_msg_file.write_text(commit_msg)

    result = cli_runner.invoke(
        main, ["--jira-tag=TAG", "--no-verify", str(mock_commit_msg_file)]
    )

    assert result.exit_code == 0
