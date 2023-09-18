# -*- coding: utf-8 -*-


from __future__ import absolute_import
from __future__ import division
def test_refresh_section(tvshows):
    tvshows.refresh()


def test_refresh_video(movie):
    movie.refresh()
