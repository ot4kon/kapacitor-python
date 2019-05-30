# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import json
import random
import requests
import requests.exceptions
import socket
import time

from .exceptions import KapacitorClientError, KapacitorServerError
from .task_client import KapacitorTaskClient
from .template_client import KapacitorTemplateClient


class KapacitorClient(object):
    def __init__(self,
                 host='localhost',
                 port=9092,
                 proto='http'
                 ):
        self.__host = host,
        self.__port = port,
        self.__proto = proto
        self.__url = '%s://%s:%s/kapacitor/v1' % (proto, host, port)

        self.__session = requests.Session()

        self.tasks = KapacitorTaskClient(self.__url, self.__session)
        self.task = self.tasks  # alias
        self.templates = KapacitorTemplateClient(self.__url, self.__session)
        self.template = self.templates  # alias

    @property
    def _host(self):
        return self.__host

    @property
    def _port(self):
        return self.__port

    @property
    def _proto(self):
        return self.__proto

    @property
    def _url(self):
        return self.__url

    @property
    def url(self):
        return self.__url
