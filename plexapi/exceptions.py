# -*- coding: utf-8 -*-


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from future import standard_library
standard_library.install_aliases()
class PlexApiException(Exception):
    """ Base class for all PlexAPI exceptions. """
    pass


class BadRequest(PlexApiException):
    """ An invalid request, generally a user error. """
    pass


class NotFound(PlexApiException):
    """ Request media item or device is not found. """
    pass


class UnknownType(PlexApiException):
    """ Unknown library type. """
    pass


class Unsupported(PlexApiException):
    """ Unsupported client request. """
    pass


class Unauthorized(BadRequest):
    """ Invalid username/password or token. """
    pass
