#!/usr/bin/python -tt
'''
Create on January 12, 2014

@author: Gabriel de la Cruz
'''
class Pattern:
  def __init__(self, number=-1, startIndex=-1, endIndex=-1):
    self.startIndex = startIndex
    self.endIndex = endIndex
    self.num = number
    self.size = (endIndex - startIndex)

class Sample:
  def __init__(self, startIndex=-1, endIndex=-1, number=None):
    self.startIndex = startIndex
    self.endIndex = endIndex
    self.num = number
    self.snippets = []
    self.size = (endIndex - startIndex)


def ListToString(items, delim="", sort=False):
  string = ""
  if sort:
    items = sorted(items)
  for item in items:
    string = string + str(item+1) + delim
  return string[:-1]
