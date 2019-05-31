# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .common import Type
from .exceptions import InvalidTaskType, InvalidStatusOption


STATUS_OPTIONS_TO_STR = {
    True: 'enabled',
    False: 'disabled',
}

STATUS_OPTIONS_TO_BOOL = {
    'enabled': True,
    'disabled': False
}


# TODO: check if valid types or values for passed properties


class TaskStatus(object):
    # TODO: make __setattr__ so it will handle proper setting of 'enabled' property
    # or simple setter
    def __init__(self, enabled=False):
        self._enabled = enabled

    def __str__(self):
        return STATUS_OPTIONS_TO_STR[self._enabled]

    def __repr__(self):
        return STATUS_OPTIONS_TO_STR[self._enabled]

    def _check_status(self, status):
        if status not in ['enabled', 'disabled']:
            raise InvalidStatusOption('Status can be "enabled" or "disabled", "%s" provided' % status)

    @property
    def enabled(self):
        return self._enabled

    @property
    def status(self):
        return STATUS_OPTIONS_TO_STR[self._enabled]

    @status.setter
    def status(self, status):         
        self._check_status(status)
        self._enabled = STATUS_OPTIONS_TO_BOOL[status]

    def enable(self):
        self._enabled = True

    def disable(self):
        self._enabled = False


class TaskType(Type):
    def __init__(self, *args, **kwargs):
        super(TaskType, self).__init__(*args, **kwargs)


class Task(object):
    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.template_id = kwargs.get('template-id', None)
        self.type = kwargs.get('type', None)
        self.dbrps = kwargs.get('dbrps', None)
        self.script = kwargs.get('script', None)
        self.status = kwargs.get('status', None),
        self.vars = kwargs.get('vars', None)
