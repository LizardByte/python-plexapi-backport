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

Python-PlexAPI
==============
.. image:: https://github.com/pkkid/python-plexapi/workflows/CI/badge.svg
    :target: https://github.com/pkkid/python-plexapi/actions?query=workflow%3ACI
.. image:: https://readthedocs.org/projects/python-plexapi/badge/?version=latest
    :target: http://python-plexapi.readthedocs.io/en/latest/?badge=latest
.. image:: https://codecov.io/gh/pkkid/python-plexapi/branch/master/graph/badge.svg?token=fOECznuMtw
    :target: https://codecov.io/gh/pkkid/python-plexapi
.. image:: https://img.shields.io/github/tag/pkkid/python-plexapi.svg?label=github+release
    :target: https://github.com/pkkid/python-plexapi/releases
.. image:: https://badge.fury.io/py/PlexAPI.svg
    :target: https://badge.fury.io/py/PlexAPI
.. image:: https://img.shields.io/github/last-commit/pkkid/python-plexapi.svg
    :target: https://img.shields.io/github/last-commit/pkkid/python-plexapi.svg


Overview
--------
Unofficial Python bindings for the Plex API. Our goal is to match all capabilities of the official
Plex Web Client. A few of the many features we currently support are:

* Navigate local or remote shared libraries.
* Perform library actions such as scan, analyze, empty trash.
* Remote control and play media on connected clients, including `Controlling Sonos speakers`_
* Listen in on all Plex Server notifications.
 

Installation & Documentation
----------------------------

.. code-block:: python

    pip install plexapi

*Install extra features:*

.. code-block:: python

    pip install plexapi[alert]  # Install with dependencies required for plexapi.alert

Documentation_ can be found at Read the Docs.

.. _Documentation: http://python-plexapi.readthedocs.io/en/latest/

Join our Discord_ for support and discussion.

.. _Discord: https://discord.gg/GtAnnZAkuw


Getting a PlexServer Instance
-----------------------------

There are two types of authentication. If you are running on a separate network
or using Plex Users you can log into MyPlex to get a PlexServer instance. An
example of this is below. NOTE: Servername below is the name of the server (not
the hostname and port).  If logged into Plex Web you can see the server name in
the top left above your available libraries.

.. code-block:: python

    from plexapi.myplex import MyPlexAccount
    account = MyPlexAccount('<USERNAME>', '<PASSWORD>')
    plex = account.resource('<SERVERNAME>').connect()  # returns a PlexServer instance

If you want to avoid logging into MyPlex and you already know your auth token
string, you can use the PlexServer object directly as above, by passing in
the baseurl and auth token directly.

.. code-block:: python

    from plexapi.server import PlexServer
    baseurl = 'http://plexserver:32400'
    token = '2ffLuB84dqLswk9skLos'
    plex = PlexServer(baseurl, token)


Usage Examples
--------------

.. code-block:: python

    # Example 1: List all unwatched movies.
    movies = plex.library.section('Movies')
    for video in movies.search(unwatched=True):
        print(video.title)


.. code-block:: python

    # Example 2: Mark all Game of Thrones episodes as played.
    plex.library.section('TV Shows').get('Game of Thrones').markPlayed()


.. code-block:: python

    # Example 3: List all clients connected to the Server.
    for client in plex.clients():
        print(client.title)


.. code-block:: python

    # Example 4: Play the movie Cars on another client.
    # Note: Client must be on same network as server.
    cars = plex.library.section('Movies').get('Cars')
    client = plex.client("Michael's iPhone")
    client.playMedia(cars)


.. code-block:: python

    # Example 5: List all content with the word 'Game' in the title.
    for video in plex.search('Game'):
        print('{} ({})'.format((video.title), (video.TYPE)))


.. code-block:: python

    # Example 6: List all movies directed by the same person as Elephants Dream.
    movies = plex.library.section('Movies')
    elephants_dream = movies.get('Elephants Dream')
    director = elephants_dream.directors[0]
    for movie in movies.search(None, director=director):
        print(movie.title)


.. code-block:: python

    # Example 7: List files for the latest episode of The 100.
    last_episode = plex.library.section('TV Shows').get('The 100').episodes()[-1]
    for part in last_episode.iterParts():
        print(part.file)


.. code-block:: python

    # Example 8: Get audio/video/all playlists
    for playlist in plex.playlists():
        print(playlist.title)


.. code-block:: python

    # Example 9: Rate the 100 four stars.
    plex.library.section('TV Shows').get('The 100').rate(8.0)


Controlling Sonos speakers
--------------------------

To control Sonos speakers directly using Plex APIs, the following requirements must be met:

1. Active Plex Pass subscription
2. Sonos account linked to Plex account
3. Plex remote access enabled

Due to the design of Sonos music services, the API calls to control Sonos speakers route through https://sonos.plex.tv
and back via the Plex server's remote access. Actual media playback is local unless networking restrictions prevent the
Sonos speakers from connecting to the Plex server directly.

.. code-block:: python

    from plexapi.myplex import MyPlexAccount
    from plexapi.server import PlexServer

    baseurl = 'http://plexserver:32400'
    token = '2ffLuB84dqLswk9skLos'

    account = MyPlexAccount(token)
    server = PlexServer(baseurl, token)

    # List available speakers/groups
    for speaker in account.sonos_speakers():
        print(speaker.title)

    # Obtain PlexSonosPlayer instance
    speaker = account.sonos_speaker("Kitchen")

    album = server.library.section('Music').get('Stevie Wonder').album('Innervisions')

    # Speaker control examples
    speaker.playMedia(album)
    speaker.pause()
    speaker.setVolume(10)
    speaker.skipNext()


Running tests over PlexAPI
--------------------------

Use:

.. code-block:: bash

     tools/plex-boostraptest.py 
    
with appropriate
arguments and add this new server to a shared user which username is defined in environment variable `SHARED_USERNAME`.
It uses `official docker image`_ to create a proper instance.

For skipping the docker and reuse a existing server use 

.. code-block:: bash

    python plex-bootstraptest.py --no-docker --username USERNAME --password PASSWORD --server-name NAME-OF-YOUR-SEVER

Also in order to run most of the tests you have to provide some environment variables:

* `PLEXAPI_AUTH_SERVER_BASEURL` containing an URL to your Plex instance, e.g. `http://127.0.0.1:32400` (without trailing
  slash)
* `PLEXAPI_AUTH_MYPLEX_USERNAME` and `PLEXAPI_AUTH_MYPLEX_PASSWORD` with your MyPlex username and password accordingly

After this step you can run tests with following command:

.. code-block:: bash

    py.test tests -rxXs --ignore=tests/test_sync.py

Some of the tests in main test-suite require a shared user in your account (e.g. `test_myplex_users`,
`test_myplex_updateFriend`, etc.), you need to provide a valid shared user's username to get them running you need to
provide the username of the shared user as an environment variable `SHARED_USERNAME`. You can enable a Guest account and
simply pass `Guest` as `SHARED_USERNAME` (or just create a user like `plexapitest` and play with it).

To be able to run tests over Mobile Sync api you have to some some more environment variables, to following values
exactly:

* PLEXAPI_HEADER_PROVIDES='controller,sync-target'
* PLEXAPI_HEADER_PLATFORM=iOS
* PLEXAPI_HEADER_PLATFORM_VERSION=11.4.1
* PLEXAPI_HEADER_DEVICE=iPhone

And finally run the sync-related tests:

.. code-block:: bash

    py.test tests/test_sync.py -rxXs

.. _official docker image: https://hub.docker.com/r/plexinc/pms-docker/

Common Questions
----------------

**Why are you using camelCase and not following PEP8 guidelines?**

This API reads XML documents provided by MyPlex and the Plex Server.
We decided to conform to their style so that the API variable names directly
match with the provided XML documents.


**Why don't you offer feature XYZ?**

This library is meant to be a wrapper around the XML pages the Plex
server provides. If we are not providing an API that is offered in the
XML pages, please let us know! -- Adding additional features beyond that
should be done outside the scope of this library.


**What are some helpful links if trying to understand the raw Plex API?**

* https://github.com/plexinc/plex-media-player/wiki/Remote-control-API
* https://forums.plex.tv/discussion/104353/pms-web-api-documentation
* https://github.com/Arcanemagus/plex-api/wiki
