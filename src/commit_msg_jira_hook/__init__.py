# noqa: D205,D208,D400
"""
    commit_msg_jira_hook
    ~~~~~~~~~~~~~~~~~~~~

    Check commit message for valid issue tag.

    :copyright: (c) 2020 Christian Riedel
    :license: GPLv3, see LICENSE for more details
"""
try:
    from importlib.metadata import version
except ModuleNotFoundError:
    from importlib_metadata import version  # type: ignore[import,no-redef]

__version__ = version(__name__)
