# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .common import Type


class TemplateType(Type):
  def __init__(self, *args, **kwargs):
    super(TemplateType, self).__init__(*args, **kwargs)


class Template(object):
  def __init__(self, **kwargs):
    self.id = kwargs.get('id', None)
    self.type = kwargs.get('type', None)
    self.script = kwargs.get('script', None)
