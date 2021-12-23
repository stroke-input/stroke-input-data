#!/usr/bin/env python3

"""
# test_sort.py

Perform unit testing on `sort.py`.

Licensed under "MIT No Attribution" (MIT-0),
see <https://spdx.org/licenses/MIT-0>.
"""


import sort
import unittest


class TestSort(unittest.TestCase):
  
  def test_backupise_name(self):
    self.assertEqual(sort.backupise_name('foo', 1234), '.foo-1234.bak')
    self.assertEqual(sort.backupise_name('bar', 0), '.bar-0.bak')


if __name__ == '__main__':
  unittest.main()
