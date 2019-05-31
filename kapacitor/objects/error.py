# -*- coding: utf-8 -*-

class Error(object):
    def __init__(self, **kwargs):
        # using kwargs because dict can be easily unpacked
        self.error = kwargs.get('error', None)
