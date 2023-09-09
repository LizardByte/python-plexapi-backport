Python-PlexAPI-Backport
=======================
.. image:: https://img.shields.io/github/actions/workflow/status/lizardbyte/python-plexapi-backport/ci.yml.svg?branch=master&label=CI%20build&logo=github&style=for-the-badge
   :alt: GitHub Workflow Status (CI)
   :target: https://github.com/LizardByte/python-plexapi-backport/actions/workflows/ci.yml?query=branch%3Amaster
.. image:: https://img.shields.io/readthedocs/python-plexapi-backport?label=Docs&style=for-the-badge&logo=readthedocs
   :alt: Read the Docs
   :target: http://python-plexapi-backport.readthedocs.io/
.. image:: https://img.shields.io/codecov/c/gh/LizardByte/python-plexapi-backport?token=6YMJYJPCRN&flag=Python-2.7&style=for-the-badge&logo=codecov&label=codecov
   :alt: Codecov
   :target: https://codecov.io/gh/LizardByte/python-plexapi-backport
.. image:: https://img.shields.io/pypi/v/PlexAPI-backport.svg?style=for-the-badge&logo=pypi&label=pypi%20package
   :alt: PyPI
   :target: https://pypi.org/project/PlexAPI-backport/
.. image:: https://img.shields.io/github/last-commit/lizardbyte/python-plexapi-backport.svg?style=for-the-badge&label=last%20commit
   :alt: GitHub last commit
   :target: https://github.com/LizardByte/python-plexapi-backport/commits/master


Overview
--------
This is a backport of `Python-PlexAPI <https://github.com/pkkid/python-plexapi>`_ to Python 2.7.
The main purpose of this backport is to allow the library to be used within Plex Media Server plugins,
which are currently limited to Python 2.7.

Documentation is available on `Read the Docs <http://python-plexapi-backport.readthedocs.io/>`_. The documentation
should be almost identical to the original library, with the exception that they are built with Python 2.7.

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

Installation
------------
This backport is available on PyPI as ``PlexAPI-backport``. It can be installed in several ways.

**PyPI**

.. code-block:: bash

   python -m pip install plexapi-backport

or

.. code-block:: bash

   python -m pip install plexapi-backport[alert]

**git**

.. code-block:: bash

   python -m pip install git+https://github.com/lizardbyte/python-plexapi-backport.git@dist#egg=plexapi-backport

or

.. code-block:: bash

   python -m pip install --install-option="--extras-require=alert" git+https://github.com/lizardbyte/python-plexapi-backport.git@dist#egg=plexapi-backport

**github archive**

.. code-block:: bash

   python -m pip install https://github.com/lizardbyte/python-plexapi-backport/archive/dist.zip#egg=plexapi-backport

or

.. code-block:: bash

   python -m pip install --install-option="--extras-require=alert" https://github.com/lizardbyte/python-plexapi-backport/archive/dist.zip#egg=plexapi-backport

