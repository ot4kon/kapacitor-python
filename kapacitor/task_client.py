# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import json
import requests
from six.moves.urllib.parse import urljoin

from .common import join_path
from .exceptions import KapacitorClientError, KapacitorServerError, ImplementationError


# TODO: create parent class for specific clients like this one and TemplateClient
class KapacitorTaskClient(object):
    def __init__(self, url, session):
        self.__path = 'tasks'
        self.__url = join_path(url, self.__path)
        self.__session = session

    @property
    def _url(self):
        return self.__url

    @property
    def url(self):
        return self._url

    # TODO: make retry support, ssl support and timeout support
    def request(self, url, method='GET', params=None, data=None, headers=None):
        try:
            response = self.__session.request(
                method=method,
                url=url,
                data=data,
                params=params,
                headers=headers
            )
        except (requests.exceptions.ConnectionError,
                requests.exceptions.HTTPError,
                requests.exceptions.Timeout):
            # TODO: retry support here, for now reraising
            raise

        # TODO: better support for other HTTP codes, also check if status code is valid
        if response.status_code > 400:
            raise KapacitorServerError(response.content)

        return response

    def define(self):
        raise ImplementationError('Method "define" has not been yet implemented!')

    def delete(self, task_id):
        """Deletes specific tasks from Kapacitor

        :param task_id: task id
        :type task_id: str
        """
        url = join_path(self.__url, task_id)

        return self.request(
            url=url,
            method='DELETE',
        )

    def disable(self):
        raise ImplementationError('Method "disable" has not been yet implemented!')

    def enable(self):
        raise ImplementationError('Method "enable" has not been yet implemented!')

    def get(self, task_id):
        """Gets specific tasks out of Kapacitor

        :param task_id: task id
        :type task_id: str
        """
        url = join_path(self.__url, task_id)

        response = self.request(
            url=url,
            method='GET',
        )

        return response.json()

    def list(self, pattern=None):
        """Deletes specific task from Kapacitor

        ::param pattern: id or id pattern of a task
        :type pattern: str
        """
        if not pattern:
            url = self.__url
        else:
            url = join_path(self.__url, pattern)

        response = self.request(
            url=url,
            method='GET'
        )

        return response.json()
