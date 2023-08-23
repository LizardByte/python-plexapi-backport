Python-PlexAPI-Backport
=======================
.. image:: https://img.shields.io/github/actions/workflow/status/reenignearcher/python-plexapi-backport/CI.yml.svg?branch=master&label=CI%20build&logo=github&style=for-the-badge
   :alt: GitHub Workflow Status (CI)
   :target: https://github.com/ReenigneArcher/python-plexapi-backport/actions/workflows/CI.yml?query=branch%3Amaster
.. image:: https://img.shields.io/pypi/v/PlexAPI-backport.svg?style=for-the-badge&logo=pypi&label=pypi%20package
   :alt: PyPI
   :target: https://pypi.org/project/PlexAPI-backport/
.. image:: https://img.shields.io/github/last-commit/reenignearcher/python-plexapi-backport.svg?style=for-the-badge&label=last%20commit%20(master)
   :alt: GitHub last commit
   :target: https://github.com/reenignearcher/python-plexapi-backport/commits/master
.. image:: https://img.shields.io/github/last-commit/reenignearcher/python-plexapi-backport/dist.svg?style=for-the-badge&label=last%20commit%20(dist)
   :alt: GitHub last commit
   :target: https://github.com/reenignearcher/python-plexapi-backport/commits/dist
.. image:: https://img.shields.io/github/last-commit/pkkid/python-plexapi.svg?style=for-the-badge&label=last%20commit%20(upstream)
   :alt: GitHub last commit (upstream)
   :target: https://github.com/pkkid/python-plexapi/commits/master


Overview
--------
This is a backport of `Python-PlexAPI <https://github.com/pkkid/python-plexapi>`_ to Python 2.7.
The main purpose of this backport is to allow the library to be used within Plex Media Server plugins,
which are currently limited to Python 2.7.

This project is not affiliated with the original project, or Plex Inc.

.. Warning::
   Python 2.7 reached end-of-life on January 1, 2020. There are many known security vulnerabilities within Python 2.7
   including some of the requirements of this backport. By using this backport, you may be exposing yourself to
   security vulnerabilities. Use at your own risk.

Validation
----------
This backport is tested against the same tests as the original library.

.. csv-table::
   :header: "Python", "Host OS"
   :widths: 10, 10

    "2.7", "Ubuntu 22.04"
    "3.7", "Ubuntu 22.04"
    "3.8", "Ubuntu 22.04"
    "3.9", "Ubuntu 22.04"
    "3.10", "Ubuntu 22.04"
    "3.11", "Ubuntu 22.04"

This backport may work on some of the versions between Python 2.7 and 3.7, but they have not been tested and there is
no guarantee that it will work.

Todo
----

* Move repo to LizardByte org
* Add dependabot
* Test claimed Plex server
* Add github environment for tests and deployment

