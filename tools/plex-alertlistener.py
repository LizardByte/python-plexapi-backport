#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Listen to plex alerts and print them to the console.
Because we're using print as a function, example only works in Python3.
"""
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from future import standard_library
standard_library.install_aliases()
import time
from plexapi.server import PlexServer


def _print(msg):
    print(msg)


if __name__ == '__main__':
    try:
        plex = PlexServer()
        listener = plex.startAlertListener(_print)
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        listener.stop()
