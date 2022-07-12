# noqa: D205,D208,D400
"""
    commit_msg_jira_hook.add_jira_tag
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Prepend issue tag to commit message.

    :copyright: (c) 2020 Christian Riedel
    :license: GPLv3, see LICENSE for more details
"""
import re
import sys

from pathlib import Path

import click

from git import Repo  # type: ignore[import]


@click.command()
@click.option(
    "--always/--auto",
    default=False,
    help=(
        "Switch between always adding JIRA issue in front or only adding if missing. "
        "Default=auto"
    ),
)
@click.option(
    "--deactivate-with",
    type=str,
    help=(
        "Don't add JIRA issue when commit message starts with given string. "
        "Instead remove the string from the commit message."
    ),
)
@click.option(
    "--no-error",
    type=bool,
    is_flag=True,
    help=(
        "Exit with exit code 0 when no JIRA issue can be found in current branch name."
    ),
)
@click.option(
    "--jira-tag", required=True, type=str, help="TAG of jira project. [Mandatory]"
)
@click.argument("commit-msg-file", required=True, nargs=1)
@click.pass_context
def main(  # pylint: disable=too-many-arguments
    ctx,
    jira_tag: str,
    deactivate_with: str,
    always: bool,
    no_error: bool,
    commit_msg_file: str,
) -> None:
    """Prepend commit msg with JIRA issue number.

    Extract JIRA issue number from current branch name and
    add it the front of your commit message.

    COMMIT_MSG_FILE: Path to file with commit-msg. Passed by pre-commit."
    """
    #: Get commit msg
    with open(commit_msg_file) as cm_file:
        c_msg = cm_file.read()

    #: Exit if commit msg beginns with deactivate_with string
    if deactivate_with and c_msg and c_msg.startswith(deactivate_with):
        #: Remove deactivate_with string
        with open(commit_msg_file, mode="w") as cm_file:
            cm_file.write(c_msg.lstrip(deactivate_with).lstrip())
        ctx.exit()

    #: JIRA issue regex
    jira_issue_re = re.compile(r"(" + jira_tag.upper() + r")-?([0-9]+)?")

    #: Get JIRA issue from current branch
    extract = jira_issue_re.search(Repo(Path.cwd()).active_branch.name)

    #: Exit if no issue found in branch name
    if not extract:
        if no_error:
            ctx.exit()
        click.echo(
            "JIRA tag with issue number could not be found in current branch name."
        )
        ctx.abort()

    branch_jira_issue = extract.group(0)  # type: ignore[union-attr]

    #: Cleanse commit msg from comments
    c_msg_lines = [l for l in c_msg.split("\n") if not l.startswith("#") and l != ""]
    c_msg_cleaned = "\n".join(c_msg_lines)

    #: Exit if issue already in commit msg
    if jira_issue_re.search(c_msg_cleaned) and not always:
        ctx.exit()

    #: Update commit msg
    with open(commit_msg_file, mode="w") as cm_file:
        cm_file.write(f"{branch_jira_issue}: {c_msg}")


if __name__ == "__main__":
    sys.exit(main())  # pylint: disable=E1120
