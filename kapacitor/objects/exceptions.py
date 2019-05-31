# -*- coding: utf-8 -*-
from __future__ import absolute_import

from ..exceptions import KapacitorClientError


class InvalidTaskType(KapacitorClientError):
    '''Raised when trying to provide wrong task type'''
    def __init__(self, content):
        super(InvalidTaskType, self).__init__(content)


class InvalidStatusOption(KapacitorClientError):
    '''Raised when trying to provide "status" other than "enabled" or "disabled"'''
    def __init__(self, content):
        super(InvalidStatusOption, self).__init__(content)
