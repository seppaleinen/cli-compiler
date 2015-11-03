#!/usr/bin/python

import unittest
from lib.manager import hello


class doCompilerTests(unittest.TestCase):
  def setUp(self):
    print('setup')

  def test_hello(self):
    print('test')
