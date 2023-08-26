# -*- coding: utf-8 -*-
"""Constants used by plexapi."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# Library version
from future import standard_library
standard_library.install_aliases()
MAJOR_VERSION = 4
MINOR_VERSION = 15
PATCH_VERSION = 0
__short_version__ = "{}.{}".format((MAJOR_VERSION), (MINOR_VERSION))
__version__ = "{}.{}".format((__short_version__), (PATCH_VERSION))
