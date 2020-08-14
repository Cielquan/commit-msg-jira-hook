commit-msg-jira-hook Change Log
===============================
.. note::
  These changes are listed in decreasing version number order and not necessarily chronological.
  Version numbers follow the `SemVer <https://semver.org/>`__ principle.
  See the `tags on this repository <https://github.com/Cielquan/commit-msg-jira-hook/tags>`__ for all available versions.

.. towncrier release notes start

v0.7.0 (2020-08-14)
-------------------

New Features
~~~~~~~~~~~~

- Added `prepare-commit-msg` hook to add JIRA tag from branch name.
  `#9 <https://github.com/cielquan/commit-msg-jira-hook/issues/9>`_
- Added default stages for both hooks.
  `#11 <https://github.com/cielquan/commit-msg-jira-hook/issues/11>`_


Documentation
~~~~~~~~~~~~~

- Update README with new hook and default stages.
  `#12 <https://github.com/cielquan/commit-msg-jira-hook/issues/12>`_


Miscellaneous
~~~~~~~~~~~~~

- Updated tools used for development.
  `#10 <https://github.com/cielquan/commit-msg-jira-hook/issues/10>`_


----


v0.6.1 (2020-05-22)
-------------------

Miscellaneous
~~~~~~~~~~~~~

- Added `pytest` tests with 100% coverage
  `#3 <https://github.com/cielquan/commit-msg-jira-hook/issues/3>`_
- Added cielquan's default `pre-commit` config
  `#4 <https://github.com/cielquan/commit-msg-jira-hook/issues/4>`_
- Added test automation with `tox`
  `#5 <https://github.com/cielquan/commit-msg-jira-hook/issues/5>`_
- Added CI config to run `tox` in a pipeline
  `#6 <https://github.com/cielquan/commit-msg-jira-hook/issues/6>`_
- Added `towncrier` for changelog updates
  `#7 <https://github.com/cielquan/commit-msg-jira-hook/issues/7>`_


----


.. note::
    Release notes below were written by hand prior usage of ``towncrier``.


v0.6.0 (19.05.2020)
-------------------

- Switched from ``setuptools`` to ``poetry``
- Updated Readme


v0.5.0 (11.05.2020)
-------------------

- Added "--verify" switch
  `#1 <https://github.com/Cielquan/commit-msg-jira-hook/issues/1>`_
- Improved error message for missing tag or tag-number
  `#2 <https://github.com/Cielquan/commit-msg-jira-hook/issues/2>`_
- Fixed link in changelog for v0.4.0
- Updated Readme


v0.4.0 (25.04.2020)
-------------------

- Rewrote script as click command
- Updated Readme


v0.3.0 (05.03.2020)
-------------------

- Improved output for missing keys in ini files
- Fixed CHANGELOG.rst


v0.2.0 (06.02.2020)
-------------------

- Split content of jira.ini file into two files


v0.1.0 (05.02.2020)
-------------------

- Initial release
