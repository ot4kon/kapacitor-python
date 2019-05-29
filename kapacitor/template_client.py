# -*- coding: utf-8 -*-
from __future__ import print_function

from .common import join_path
from .exceptions import KapacitorClientError, KapacitorServerError, ImplementationError


class KapacitorTemplateClient(object):
    def __init__(self, url, session):
        self.__path = "/templates"
        self.__url = url
        self.__session = session

        def define(self):
            raise ImplementationError('Method "define" has not been yet implemented!')

        def delete(self):
            raise ImplementationError('Method "delete" has not been yet implemented!')

        def disable(self):
            raise ImplementationError('Method "disable" has not been yet implemented!')

        def enable(self):
            raise ImplementationError('Method "enable" has not been yet implemented!')

        def get(self):
            raise ImplementationError('Method "get" has not been yet implemented!')

        def list(self):
            raise ImplementationError('Method "list" has not been yet implemented!')
