====================
commit-msg-jira-hook
====================

+---------------+----------------------------------------------------------------------+
| **General**   | |maintenance| |license| |black|                                      |
+---------------+----------------------------------------------------------------------+
| **Pipeline**  | |azure_pipeline| |azure_coverage|                                    |
+---------------+----------------------------------------------------------------------+
| **Tools**     | |poetry| |tox| |pytest|                                              |
+---------------+----------------------------------------------------------------------+
| **VC**        | |vcs| |gpg| |semver| |pre-commit|                                    |
+---------------+----------------------------------------------------------------------+
| **Github**    | |gh_release| |gh_commits_since| |gh_last_commit|                     |
|               +----------------------------------------------------------------------+
|               | |gh_stars| |gh_forks| |gh_contributors| |gh_watchers|                |
+---------------+----------------------------------------------------------------------+


Git hooks used with pre-commit to ensure proper jira issue linking in your commit messages.

See also: https://github.com/pre-commit/pre-commit


Prerequisites
=============

*Works only with python version >= 3.6*

A new version of ``pip`` that supports PEP-517/PEP-518 is required.
When the setup fails try updating ``pip``.


Usage
=====


jira_commit_msg hook
--------------------

This hook checks if the specified JIRA tag with issue number is present
in the commit messages and can verify via the JRIA API if the issue number is valid.

Add this to your project's ``.pre-commit-config.yaml`` file:

.. code-block:: yaml

    repos:
    - repo: https://github.com/Cielquan/commit-msg-jira-hook
      rev: '' # Use the ref you want to point at
      hooks:
      - id: jira_commit_msg
        args: ["--jira-tag=<TAG>", "--verify", "--jira-url=<URL>"]

Exchange the placeholders with your actual config. <URL> may be ``https://jira.atlassian.com``.

Args to specify hook behavior:
    - ``--jira-tag`` is mandatory.
    - ``--verify`` can be omitted or changed to ``--no-verify`` to disable online verification.
    - ``--jira-url`` is mandatory if online verification is enabled or can be omitted otherwise.


Then add a ``.jira.ini`` file to your home directory, if you want to use online verification
for the issue numbers, with the following config:

.. code-block:: ini

    [jira]
    JIRA_USERNAME = <YOUR EMAIL>
    JIRA_TOKEN = <API TOKEN>

Get api token from here: https://id.atlassian.com/manage/api-tokens


Lastly install the hook:

.. code-block:: console

    $ pre-commit install -t commit-msg


jira_prepare_commit_msg hook
----------------------------

This hook extracts this specified JIRA tag and the issue number from your
current git branch and add them to the beginning of your commit message.

Add this to your project's ``.pre-commit-config.yaml`` file:

.. code-block:: yaml

    repos:
    - repo: https://github.com/Cielquan/commit-msg-jira-hook
      rev: '' # Use the ref you want to point at
      hooks:
      - id: jira_prepare_commit_msg
        args: ["--jira-tag=<TAG>"]

Exchange the placeholders with your actual config.

Args to specify hook behavior:
    - ``--jira-tag`` is mandatory.
    - ``--auto`` can be omitted or changed to ``--always`` to always prepend JIRA tag to
      commit msg even when its already there.
    - ``--deactivate-with`` takes a string which, when present at the start of the commit msg,
      deactivates adding the JIRA tag to commit msg and removes the string from the commit msg.
    - ``--no-error`` silences the error which occurs when the current branch has no JIRA tag.


Lastly install the hook:

.. code-block:: console

    $ pre-commit install -t prepare-commit-msg


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
.. |azure_pipeline| image:: https://img.shields.io/azure-devops/build/cielquan/7c9eeb3a-e648-46c5-a423-596beea9d8e1/6?style=flat-square&logo=azure-pipelines&label=Azure%20Pipelines
    :target: https://dev.azure.com/cielquan/commit-msg-jira-hook/_build/latest?definitionId=6&branchName=master
    :alt: Azure DevOps builds

.. |azure_coverage| image:: https://img.shields.io/azure-devops/coverage/cielquan/commit-msg-jira-hook/6?style=flat-square&logo=azure-pipelines&label=Coverage
    :target: https://dev.azure.com/cielquan/commit-msg-jira-hook/_build/latest?definitionId=6&branchName=master
    :alt: Azure DevOps Coverage


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
