from __future__ import absolute_import

import json
import mock
import requests
import unittest

from nose.tools import raises

from kapacitor import KapacitorClient
from kapacitor.exceptions import KapacitorServerError

def is_valid_json(json_string):
    try:
        json.loads(json_string)
    except ValueError:
        return False

    return True

def get_response_object(status_code=200, content=''):
    response = requests.Response()
    response.status_code = status_code
    response._content = content.encode('utf-8')

    return response

def session_request_mock(*args, **kwargs):
    return get_response_object()

def mock_session(client, method='GET', status_code=200, content=json.dumps(''), expected_data=None):
    assert is_valid_json(content)

    def session_request_mock(*args, **kwargs):
        request_method = kwargs.get('method', 'GET')
        request_data = kwargs.get('data', None)

        # check if methods are the same
        assert method == request_method

        # check if request data is in string format and is valid json
        if request_data is not None:
            assert isinstance(request_data, str)
            assert is_valid_json(request_data)

        # check if data sent in requests corresponds expected data
        if expected_data is not None:
            assert isinstance(expected_data, str)
            assert is_valid_json(expected_data)
            assert request_data == expected_data

        return get_response_object(status_code, content)

    return mock.patch.object(client._session, 'request', side_effect=session_request_mock)

def get_response_dict(response):
    return {
        'status': response.status_code,
        'data': response.json(),
        'headers': response.headers
    }


class TestKapacitorClient(unittest.TestCase):
    def setUp(self):
        self.client = KapacitorClient(host='localhost', port=9092, proto='http')

    def test_request(self):
        pass

    @raises(KapacitorServerError) # TODO: make it more specific
    def test_request_raises(self):
        '''Raises error when response status code is 400 and greater'''
        with mock_session(self.client, 'GET', 400):
            self.client.tasks.request(url='http://someurl.com', method='GET')

    def test_enable(self):
        pass

    def test_disable(self):
        pass

if __name__ == '__main__':
    unittest.main()
