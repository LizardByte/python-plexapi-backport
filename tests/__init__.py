# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from future import standard_library
standard_library.install_aliases()
import sys
from os.path import dirname, abspath

# Make sure plexapi is in the systempath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
