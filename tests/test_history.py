# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from future import standard_library
standard_library.install_aliases()
from . import conftest as utils


def test_history_Movie(movie):
    movie.markPlayed()
    history = movie.history()
    assert len(history)
    movie.markUnplayed()


def test_history_Show(show):
    show.markPlayed()
    history = show.history()
    assert len(history)
    show.markUnplayed()


def test_history_Season(show):
    season = show.season("Season 1")
    season.markPlayed()
    history = season.history()
    assert len(history)
    season.markUnplayed()


def test_history_Episode(episode):
    episode.markPlayed()
    history = episode.history()
    assert len(history)
    episode.markUnplayed()


def test_history_Artist(artist):
    artist.markPlayed()
    history = artist.history()
    assert len(history)
    artist.markUnplayed()


def test_history_Album(album):
    album.markPlayed()
    history = album.history()
    assert len(history)
    album.markUnplayed()


def test_history_Track(track):
    track.markPlayed()
    history = track.history()
    assert len(history)
    track.markUnplayed()


def test_history_MyAccount(account, movie, show):
    movie.markPlayed()
    show.markPlayed()
    history = account.history()
    assert len(history)
    movie.markUnplayed()
    show.markUnplayed()


def test_history_MyLibrary(plex, movie, show):
    movie.markPlayed()
    show.markPlayed()
    history = plex.library.history()
    assert len(history)
    movie.markUnplayed()
    show.markUnplayed()


def test_history_MySection(plex, movie):
    movie.markPlayed()
    history = plex.library.section("Movies").history()
    assert len(history)
    movie.markUnplayed()


def test_history_MyServer(plex, movie):
    movie.markPlayed()
    history = plex.history()
    assert len(history)
    movie.markUnplayed()


def test_history_PlexHistory(plex, movie):
    movie.markPlayed()
    history = plex.history()
    assert len(history)

    hist = history[0]
    assert hist.source() == movie
    assert hist.accountID
    assert hist.deviceID
    assert hist.historyKey
    assert utils.is_datetime(hist.viewedAt)
    assert hist.guid is None
    hist.delete()

    history = plex.history()
    assert hist not in history


def test_history_User(account, shared_username):
    user = account.user(shared_username)
    history = user.history()

    assert isinstance(history, list)


def test_history_UserServer(account, shared_username, plex):
    userSharedServer = account.user(shared_username).server(plex.friendlyName)
    history = userSharedServer.history()

    assert isinstance(history, list)


def test_history_UserSection(account, shared_username, plex):
    userSharedServerSection = (
        account.user(shared_username).server(plex.friendlyName).section("Movies")
    )
    history = userSharedServerSection.history()

    assert isinstance(history, list)
