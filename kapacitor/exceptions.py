# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function


class KapacitorClientError(Exception):
    """Raised when error occurs on the client side or in the request"""
    def __init__(self, content, code=None):
        if isinstance(content, type(b'')):
            content = content.decode('UTF-8', 'replace')

        if code is not None:
            message = "%s: %s" % (code, content)
        else:
            message = content

        super(KapacitorClientError, self).__init__(message)
        self.content = content
        self.code = code


class KapacitorServerError(Exception):
    """Raised when error occurs on server side"""
    def __init__(self, content):
        super(KapacitorServerError, self).__init__(content)


class ImplementationError(Exception):
    """Usually raised when some method is not yet implemented"""
    def __init__(self, content):
        super(ImplementationError, self).__init__(content)
