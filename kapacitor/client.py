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
        self._host = host,
        self._port = port,
        self._proto = proto
        self._url = '%s://%s:%s/kapacitor/v1' % (proto, host, port)

        self._session = requests.Session()

        # TODO: implement aliases so it will be possible to use both:
        # self.tasks.list()
        # self.list.tasks()

        self.tasks = KapacitorTaskClient(self._url, self._session)
        self.task = self.tasks  # alias
        self.templates = KapacitorTemplateClient(self._url, self._session)
        self.template = self.templates  # alias

    @property
    def url(self):
        return self._url
