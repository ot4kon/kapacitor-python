# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import requests
from json import dumps
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

    # TODO: make retry support and timeout support
    def request(self, url, method='GET', params=None, data=None, headers=None):
        '''Makes request to Kapacitor instance

        :param url: url of Kapacitor instance
        :type url: str
        :param method: method used to make request
        :type method: str
        :param params: request parameters
        :type params: any
        :param data: request body
        :type data: any
        :param headers: request headers
        :type headers: dict
        :return: response dictionary
        :rtype: dict
        '''
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
            # TODO: also throw custom error
            raise

        # TODO: better support for other HTTP codes, also check if status code is valid
        if response.status_code > 400:
            raise KapacitorServerError(response.content)

        return {
            'status': response.status_code,
            'data': response.json(),
            'headers': response.headers
        }

    def create(self, data):
        '''Defines a task in Kapacitor instance (alias for define)

        :param data: json payload to be sent
        :type data: dict
        :returns: response dictionary
        :rtype: dict
        '''
        return self.define(data)

    def define(self, data):
        # TODO: pass body as one argument 'data' or use **kwargs (task_id, template-id, type, dbrps, script, status, vars, etc.)
        '''Defines a task in Kapacitor instance

        :param data: json payload to be sent
        :type data: dict
        :returns: response dictionary
        :rtype: dict
        '''
        return self.request(
            url=self.__url,
            method='POST',
            data=dumps(data),
        )

    def delete(self, task_id):
        '''Deletes specific tasks from Kapacitor

        :param task_id: task id
        :type task_id: str
        :returns: response dictionary
        :rtype: dict
        '''
        url = join_path(self.__url, task_id)

        return self.request(
            url=url,
            method='DELETE'
        )

    def disable(self, task_id):
        '''Disables specific task

        :param task_id: task id
        :type task_id: str
        :returns: response dictionary
        :rtype: dict
        '''
        url = join_path(self.__url, task_id)

        return self.request(
            url=url,
            method='PATCH',
            data=dumps({'status': 'disabled'})
        )

    def enable(self, task_id):
        '''Enables specific task

        :param task_id: task id
        :type task_id: str
        :returns: response dictionary
        :rtype: dict
        '''
        url = join_path(self.__url, task_id)

        return self.request(
            url=url,
            method='PATCH',
            data=dumps({'status': 'enabled'})
        )

    def force_update(self, task_id, data):
        '''Updates a task and reenables it in order for changes to take effect (it sends additional 'enable' request)

        :param task_id: task id
        :type task_id: str
        :param data: json payload to be sent
        :type data: dict
        :return: list of response dictionaries
        :rtype: list
        '''
        results = []
        data['status'] = 'disabled' # disable task first (do it in one request)

        results.append(self.update(task_id, data))
        results.append(self.enable(task_id))

        return results


    def get(self, task_id):
        '''Gets specific tasks out of Kapacitor

        :param task_id: task id
        :type task_id: str
        :returns: response dictionary
        :rtype: dict
        '''
        url = join_path(self.__url, task_id)

        return self.request(
            url=url,
            method='GET'
        )

    def list(self, pattern=None):
        '''Lists tasks from Kapacitor

        :param pattern: id or id pattern of a task
        :type pattern: str
        :returns: response dictionary
        :rtype: dict
        '''
        if not pattern:
            url = self.__url
        else:
            url = join_path(self.__url, pattern)

        return self.request(
            url=url,
            method='GET'
        )

    def modify(self, task_id, data):
        '''Update specific task in Kapacitor (alias for update)

        :param task_id: task id
        :type task_id: str
        :param data: json payload to be sent
        :type data: dict
        :returns: response dictionary
        :rtype: dict
        '''
        return self.update(task_id, data)

    def update(self, task_id, data):
        # TODO: task_id is not necessary when patching a task
        '''Update specific task in Kapacitor

        :param task_id: task id
        :type task_id: str
        :param data: json payload to be sent
        :type data: dict
        :returns: response dictionary
        :rtype: dict
        '''
        url = join_path(self.__url, task_id)

        return self.request(
            url=url,
            method='PATCH',
            data=dumps(data)
        )
