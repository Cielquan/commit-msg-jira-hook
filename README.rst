====================
commit-msg-jira-hook
====================

| |maintenance| |license| |black|
|
| |release| |commits_since| |last_commit|
| |stars| |forks| |contributors|
|


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

.. highlight:: yaml

.. code-block:: yaml

    repos:
    - repo: https://github.com/Cielquan/commit-msg-jira-hook
      rev: v0.6.0 # Use the ref you want to point at
      hooks:
      - id: jira_commit_msg
        stages: [commit-msg]
        args: ["--jira-tag=<TAG>", "--verify", "--jira-url=<URL>"]

Exchange the placeholders with your actual config. <URL> may be ``https://jira.atlassian.com``.
``--jira-tag`` is mandatory.
``--verify`` can be omitted or changed to ``--no-verify`` to disable online verification.
``--jira-url`` is mandatory if online verification is enabled or can be omitted otherwise.


Then add a ``.jira.ini`` file to your home directory with the following config:

.. highlight:: ini

.. code-block:: ini

    [jira]
    JIRA_USERNAME = email
    JIRA_TOKEN = api-token

Get api token from here: https://id.atlassian.com/manage/api-tokens


Lastly install the hook:

.. highlight:: console

.. code-block:: console

    $ pre-commit install -t commit-msg


Disclaimer
==========

No active maintenance is intended for this project.
You may leave an issue if you have a questions, bug report or feature request,
but I cannot promise a quick response time.


.. .############################### LINKS ###############################

.. BADGES START

.. General
.. |maintenance| image:: https://img.shields.io/badge/No%20Maintenance%20Intended-X-red.svg?style=flat-square
    :target: http://unmaintained.tech/
    :alt: Maintenance - not intended

.. |license| image:: https://img.shields.io/github/license/Cielquan/commit-msg-jira-hook.svg?style=flat-square
    :alt: License
    :target: https://github.com/Cielquan/commit-msg-jira-hook/blob/master/LICENSE.rst

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square
    :alt: Code Style: Black
    :target: https://github.com/psf/black


.. Github
.. |release| image:: https://img.shields.io/github/v/release/Cielquan/commit-msg-jira-hook.svg?style=flat-square&logo=github
    :alt: Github Latest Release
    :target: https://github.com/Cielquan/commit-msg-jira-hook/releases/latest

.. |commits_since| image:: https://img.shields.io/github/commits-since/Cielquan/commit-msg-jira-hook/latest.svg?style=flat-square&logo=github
    :alt: GitHub commits since latest release
    :target: https://github.com/Cielquan/commit-msg-jira-hook/commits/master

.. |last_commit| image:: https://img.shields.io/github/last-commit/Cielquan/commit-msg-jira-hook.svg?style=flat-square&logo=github
    :alt: GitHub last commit
    :target: https://github.com/Cielquan/commit-msg-jira-hook/commits/master

.. |stars| image:: https://img.shields.io/github/stars/Cielquan/commit-msg-jira-hook.svg?style=flat-square&logo=github
    :alt: Github stars
    :target: https://github.com/Cielquan/commit-msg-jira-hook/stargazers

.. |forks| image:: https://img.shields.io/github/forks/Cielquan/commit-msg-jira-hook.svg?style=flat-square&logo=github
    :alt: Github forks
    :target: https://github.com/Cielquan/commit-msg-jira-hook/network/members

.. |contributors| image:: https://img.shields.io/github/contributors/Cielquan/commit-msg-jira-hook.svg?style=flat-square&logo=github
    :alt: Github Contributors
    :target: https://github.com/Cielquan/commit-msg-jira-hook/graphs/contributors

..  BADGES END

.. highlight:: default
