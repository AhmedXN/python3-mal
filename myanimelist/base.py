#!/usr/bin/python
# -*- coding: utf-8 -*-

import functools

class Error(Exception):
  def __init__(self, message=None):
    super(Error, self).__init__()
    self.message = message
  def __str__(self):
    return unicode(self.message) if self.message is not None else u""

def loadable(func_name):
  '''
    Decorator for getters that require a load() upon first access.
  '''
  def inner(func):
    cached_name = '_' + func.__name__
    @functools.wraps(func)
    def _decorator(self, *args, **kwargs):
      if getattr(self, cached_name) is None:
        getattr(self, func_name)()
      return func(self, *args, **kwargs)
    return _decorator
  return inner

class Base(object):
  '''
    Provides autoloading, auto-setting functionality for other MAL objects.
  '''
  def __init__(self, session):
    self.session = session

  def load(self):
    raise NotImplementedError("Subclasses must implement load()")

  def set(self, attr_dict):
    """
    Sets attributes of this user object with keys found in dict.
    """
    for key in attr_dict:
      if key == 'id':
        self.id = attr_dict[key]
      else:
        setattr(self, "_" + key, attr_dict[key])
    return self