====================
commit-msg-jira-hook
====================

| |license| |black|
|
| |release| |commits_since| |last_commit|
| |stars| |forks| |contributors|
|


commit-msg hook for jira issue verification with pre-commit.

*Works only with python version >= 3.6*

See also: https://github.com/pre-commit/pre-commit

Add this to your ``.pre-commit-config.yaml``:

.. code-block:: yaml

    - repo: https://github.com/Cielquan/commit-msg-jira-hook
      rev: v0.2.0 # Use the ref you want to point at
      hooks:
      - id: jira_commit_msg
        stages: [commit-msg]

Then add a ``jira.ini`` to you projects root directory with following data:

.. code-block:: ini

    [jira]
    JIRA_URL = e.g. https://jira.atlassian.com
    JIRA_TAG = tag

Then add a ``.jira.ini`` to your home direcotry with the following data:

.. code-block:: ini

    [jira]
    JIRA_USERNAME = email
    JIRA_TOKEN = api-token

Get api token from here: https://id.atlassian.com/manage/api-tokens

The split into two ``*.ini`` files is so you do not commit your credentials into your repo.

Lastly install the hook:

.. code-block:: console

    $ pre-commit install -t commit-msg


.. .############################### LINKS ###############################

.. BADGES START

.. info block
.. |license| image:: https://img.shields.io/github/license/Cielquan/commit-msg-jira-hook.svg?style=flat-square
    :alt: License
    :target: https://github.com/Cielquan/commit-msg-jira-hook/blob/master/LICENSE.rst

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square
    :alt: Code Style: Black
    :target: https://github.com/psf/black


.. Github block
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
