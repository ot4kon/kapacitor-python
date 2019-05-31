# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .exceptions import InvalidTaskType

class Type(object):
    def __init__(self, task_type='stream'):
        self._type = task_type

    def __str__(self):
        return self._type

    def __repr__(self):
        return self._type

    def _check_type(self, task_type):
        if task_type not in ['stream', 'batch']:
            raise InvalidTaskType('Type can be "stream" or "batch", "%s" provided' % task_type)

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, task_type):
        self._check_type(task_type)
        self._type = task_type

    def change(self, task_type):
        self.type = task_type
