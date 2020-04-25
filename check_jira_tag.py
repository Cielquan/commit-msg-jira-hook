#!/usr/bin/env python3

# ======================================================================================
# Copyright (c) 2020 Christian Riedel
#
# This file 'check_jira_tag.py' created 2020-02-05
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
    check_jira_tag
    ~~~~~~~~~~~~~~

    Check commit message for valid issue tag

    :copyright: (c) 2020 Christian Riedel
    :license: GPLv3, see LICENSE for more details
"""
import configparser
import re
import sys

from pathlib import Path
from typing import Dict

import click

from jira import JIRA
from jira import exceptions as jira_exc


@click.command()
@click.option("--jira-url", required=True, type=str, help="URL for jira server.")
@click.option("--jira-tag", required=True, type=str, help="TAG of jira project.")
@click.argument("commit-msg-file", required=True, nargs=1)
@click.pass_context
def main(ctx, jira_url: str, jira_tag: str, commit_msg_file: str) -> None:
    """Check commit messages for issue tags

    COMMIT_MSG_FILE: Path to file with commit-msg. Passed by pre-commit."
    """
    #: Check for '~/.jira.ini' file
    jira_user_conf_file = Path(Path.home(), ".jira.ini")
    if not jira_user_conf_file.is_file():
        click.echo("No '~/.jira.ini' file found.")
        ctx.abort()

    #: Load ini file
    jira_user_conf = configparser.ConfigParser()
    jira_user_conf.read(jira_user_conf_file)

    #: Check for 'jira' section in ini file
    if "jira" not in jira_user_conf:
        click.echo("No 'jira' section found in '~/.jira.ini' file.")
        ctx.abort()

    #: Extract configs from ini file
    jira_user_conf_dict: Dict[str, str] = {}
    for config_key in ("JIRA_USERNAME", "JIRA_TOKEN"):
        try:
            jira_user_conf_dict[config_key] = jira_user_conf["jira"][config_key]
        except KeyError:
            click.echo(f"Missing '{config_key}' in '~/.jira.ini' file.")
            ctx.abort()

    #: Get commit msg
    with open(commit_msg_file) as cm_file:
        c_msg = cm_file.read()
        click.echo(c_msg)

    #: Abort with empty commit-msg
    if c_msg == "":
        click.echo("Commit message is empty.")
        ctx.abort()

    #: Extract tag from commit msg
    extract = re.search(jira_tag.upper() + r"-([0-9]+)", c_msg)

    #: Check if tag is in commit msg
    if extract is None:
        click.echo(f"'{jira_tag.upper()}' tag not found in commit message.")
        ctx.abort()

    #: Get tag from extract
    issue = str(extract.group(0))

    try:
        jira_inst = JIRA(
            {"server": jira_url},
            basic_auth=(
                jira_user_conf_dict.get("JIRA_USERNAME"),
                jira_user_conf_dict.get("JIRA_TOKEN"),
            ),
        )
    except jira_exc.JIRAError:
        click.echo(
            "Error connecting to jira. "
            "Please check JIRA_URL, JIRA_USERNAME and JIRA_TOKEN."
        )
        ctx.abort()

    #: Check existence of id
    try:
        jira_inst.issue(issue)
    except jira_exc.JIRAError:
        click.echo(f"{issue} does not exist or no permission to view the issue.")
        ctx.abort()


if __name__ == "__main__":
    sys.exit(main())
