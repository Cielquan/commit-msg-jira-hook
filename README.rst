====================
commit-msg-jira-hook
====================

+---------------+----------------------------------------------------------------------+
| **General**   | |maintenance| |license| |black|                                      |
+---------------+----------------------------------------------------------------------+
| **Pipeline**  | |travis| |codecov|                                                   |
+---------------+----------------------------------------------------------------------+
| **Tools**     | |poetry| |tox| |pytest|                                              |
+---------------+----------------------------------------------------------------------+
| **VC**        | |vcs| |gpg| |semver| |pre-commit|                                    |
+---------------+----------------------------------------------------------------------+
| **Github**    | |gh_release| |gh_commits_since| |gh_last_commit|                     |
|               +----------------------------------------------------------------------+
|               | |gh_stars| |gh_forks| |gh_contributors| |gh_watchers|                |
+---------------+----------------------------------------------------------------------+


commit-msg hook for pre-commit to verify jira issues in commit messages.

See also: https://github.com/pre-commit/pre-commit

Prerequisites
=============

*Works only with python version >= 3.6*

A new version of ``pip`` that supports PEP-517/PEP-518 is required.
When the setup fails try updating ``pip``.


Usage
=====

Add this to your project's ``.pre-commit-config.yaml`` file:

.. code-block:: yaml

    repos:
    - repo: https://github.com/Cielquan/commit-msg-jira-hook
      rev: 0.6.2 # Use the ref you want to point at
      hooks:
      - id: jira_commit_msg
        stages: [commit-msg]
        args: ["--jira-tag=<TAG>", "--verify", "--jira-url=<URL>"]

Exchange the placeholders with your actual config. <URL> may be ``https://jira.atlassian.com``.
``--jira-tag`` is mandatory.
``--verify`` can be omitted or changed to ``--no-verify`` to disable online verification.
``--jira-url`` is mandatory if online verification is enabled or can be omitted otherwise.


Then add a ``.jira.ini`` file to your home directory with the following config:

.. code-block:: ini

    [jira]
    JIRA_USERNAME = email
    JIRA_TOKEN = api-token

Get api token from here: https://id.atlassian.com/manage/api-tokens


Lastly install the hook:

.. code-block:: console

    $ pre-commit install -t commit-msg


Disclaimer
==========

No active maintenance is intended for this project.
You may leave an issue if you have a questions, bug report or feature request,
but I cannot promise a quick response time.


.. .############################### LINKS ###############################


.. General
.. |maintenance| image:: https://img.shields.io/badge/No%20Maintenance%20Intended-X-red.svg?style=flat-square
    :target: http://unmaintained.tech/
    :alt: Maintenance - not intended

.. |license| image:: https://img.shields.io/github/license/Cielquan/commit-msg-jira-hook.svg?style=flat-square&label=License
    :alt: License
    :target: https://github.com/Cielquan/commit-msg-jira-hook/blob/master/LICENSE.rst

.. |black| image:: https://img.shields.io/badge/Code%20Style-black-000000.svg?style=flat-square
    :alt: Code Style - Black
    :target: https://github.com/psf/black


.. Pipeline
.. |travis| image:: https://img.shields.io/travis/com/Cielquan/commit-msg-jira-hook/master.svg?style=flat-square&logo=travis-ci&logoColor=FBE072
    :alt: Travis - Build Status
    :target: https://travis-ci.com/Cielquan/commit-msg-jira-hook

.. |codecov| image:: https://img.shields.io/codecov/c/github/Cielquan/commit-msg-jira-hook/master.svg?style=flat-square&logo=codecov
    :alt: Codecov - Test Coverage
    :target: https://codecov.io/gh/Cielquan/commit-msg-jira-hook


.. Tools
.. |poetry| image:: https://img.shields.io/badge/Packaging-poetry-brightgreen.svg?style=flat-square
    :target: https://python-poetry.org/
    :alt: Poetry

.. |tox| image:: https://img.shields.io/badge/Automation-tox-brightgreen.svg?style=flat-square
    :target: https://tox.readthedocs.io/en/latest/
    :alt: tox

.. |pytest| image:: https://img.shields.io/badge/Test%20framework-pytest-brightgreen.svg?style=flat-square
    :target: https://docs.pytest.org/en/latest/
    :alt: Pytest


.. VC
.. |vcs| image:: https://img.shields.io/badge/VCS-git-orange.svg?style=flat-square&logo=git
    :target: https://git-scm.com/
    :alt: VCS

.. |gpg| image:: https://img.shields.io/badge/GPG-signed-blue.svg?style=flat-square&logo=gnu-privacy-guard
    :target: https://gnupg.org/
    :alt: Website

.. |semver| image:: https://img.shields.io/badge/Versioning-semantic-brightgreen.svg?style=flat-square
    :alt: Versioning - semantic
    :target: https://semver.org/

.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?style=flat-square&logo=pre-commit&logoColor=yellow
    :target: https://github.com/pre-commit/pre-commit
    :alt: pre-commit


.. Github
.. |gh_release| image:: https://img.shields.io/github/v/release/Cielquan/commit-msg-jira-hook.svg?style=flat-square&logo=github
    :alt: Github - Latest Release
    :target: https://github.com/Cielquan/commit-msg-jira-hook/releases/latest

.. |gh_commits_since| image:: https://img.shields.io/github/commits-since/Cielquan/commit-msg-jira-hook/latest.svg?style=flat-square&logo=github
    :alt: Github - Commits since latest release
    :target: https://github.com/Cielquan/commit-msg-jira-hook/commits/master

.. |gh_last_commit| image:: https://img.shields.io/github/last-commit/Cielquan/commit-msg-jira-hook.svg?style=flat-square&logo=github
    :alt: Github - Last Commit
    :target: https://github.com/Cielquan/commit-msg-jira-hook/commits/master

.. |gh_stars| image:: https://img.shields.io/github/stars/Cielquan/commit-msg-jira-hook.svg?style=flat-square&logo=github
    :alt: Github - Stars
    :target: https://github.com/Cielquan/commit-msg-jira-hook/stargazers

.. |gh_forks| image:: https://img.shields.io/github/forks/Cielquan/commit-msg-jira-hook.svg?style=flat-square&logo=github
    :alt: Github - Forks
    :target: https://github.com/Cielquan/commit-msg-jira-hook/network/members

.. |gh_contributors| image:: https://img.shields.io/github/contributors/Cielquan/commit-msg-jira-hook.svg?style=flat-square&logo=github
    :alt: Github - Contributors
    :target: https://github.com/Cielquan/commit-msg-jira-hook/graphs/contributors

.. |gh_watchers| image:: https://img.shields.io/github/watchers/Cielquan/commit-msg-jira-hook.svg?style=flat-square&logo=github
    :alt: Github - Watchers
    :target: https://github.com/Cielquan/commit-msg-jira-hook/watchers
