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

from typing import Dict

from jira import JIRA
from jira import exceptions as jira_exc


def main() -> int:
    """Check commit messages for issue tags"""
    exit_code = 0

    #: Load 'jira.ini'
    ini_config = configparser.ConfigParser()
    ini_config.read("jira.ini")

    #: Check for 'jira' section in 'jira.ini'
    if "jira" not in ini_config:
        print("No 'jira' section found in 'jira.ini' or no 'jira.ini' file at all.")
        exit_code = 1

    jira_dict: Dict[str, str] = {}
    config_list = ["JIRA_URL", "JIRA_TAG", "JIRA_USERNAME", "JIRA_TOKEN"]

    #: Extract configs from 'jira.ini'
    for config_key in config_list:
        try:
            jira_dict.update({config_key: ini_config["jira"][config_key]})
        except KeyError:
            print(f"Missing '{config_key}' in 'jira.ini'.")
            exit_code = 1

    #: Get commit msg
    if len(sys.argv) > 2:
        with open(sys.argv[1]) as file:
            c_msg = file.read()

        if c_msg == "":
            print("Commit message is empty.")
            exit_code = 1

        if exit_code == 0:
            #: Extract tag from commit msg
            extract = re.search(
                jira_dict.get("JIRA_TAG", "").upper() + r"-([0-9]+)", c_msg
            )

            #: Check if tag in commit msg
            if extract is None:
                print(
                    f"'{jira_dict.get('JIRA_TAG', '').upper()}' "
                    f"tag not found in commit message."
                )
                exit_code = 1
            else:
                #: Get tag from extract
                issue = str(extract.group(0))

                try:
                    jira_inst = JIRA(
                        {"server": jira_dict.get("JIRA_URL")},
                        basic_auth=(
                            jira_dict.get("JIRA_USERNAME"),
                            jira_dict.get("JIRA_TOKEN"),
                        ),
                    )
                except jira_exc.JIRAError:
                    print(
                        "Error connecting to jira. "
                        "Please check JIRA_URL, JIRA_USERNAME and JIRA_TOKEN."
                    )
                    exit_code = 1
                else:
                    #: Check existence of id
                    try:
                        jira_inst.issue(issue)
                    except jira_exc.JIRAError:
                        print(
                            f"{issue} does not exist or "
                            f"no permission to view the issue."
                        )
                        exit_code = 1

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
