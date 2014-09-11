#!/usr/bin/python
# -*- coding: utf-8 -*-

import bs4
import re

import utilities
from base import Base, Error, loadable

class MalformedPersonPageError(Error):
  def __init__(self, person_id):
    super(MalformedPersonPageError, self).__init__()
    self.person_id = person_id
  def __str__(self):
    return "\n".join([
      super(MalformedPersonPageError, self).__str__(),
      "Person ID: " + unicode(self.person_id)
    ])

class InvalidPersonError(Error):
  def __init__(self, person_id):
    super(InvalidPersonError, self).__init__()
    self.person_id = person_id
  def __str__(self):
    return "\n".join([
      super(InvalidPersonError, self).__str__(),
      "Person ID: " + unicode(self.person_id)
    ])

class Person(Base):
  def __init__(self, session, person_id):
    super(Person, self).__init__(session)
    self.id = person_id
    if not isinstance(self.id, int) or int(self.id) < 1:
      raise InvalidPersonError(self.id)
    self._name = None

  def load(self):
    # TODO
    pass

  @property
  @loadable('load')
  def name(self):
    return self._name