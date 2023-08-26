#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Plex-GetToken is a simple method to retrieve a Plex account token.
"""
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from builtins import input
from future import standard_library
standard_library.install_aliases()
from plexapi.myplex import MyPlexAccount

username = input("Plex username: ")
password = input("Plex password: ")

account = MyPlexAccount(username, password)
print(account.authenticationToken)
