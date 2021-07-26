#!/usr/bin/env python3

"""
# test_generate.py

Perform unit testing on `generate.py`.

Licensed under "MIT No Attribution" (MIT-0),
see <https://spdx.org/licenses/MIT-0>.
"""


import generate
import unittest


class TestStrokeSequenceParsing(unittest.TestCase):
  
  actual_sequence_set_from_regex = {
    '1': {'1'},
    '12345': {'12345'},
    '(444)': {'444'},
    '(1)(2)(3)(4)(5)': {'12345'},
    '()123': {'123'},
    '(5|5)43': {'543'},
    '(|1)123': {'123', '1123'},
    '(1|2)(3|45)': {'13', '145', '23', '245'},
    '(|1|11)(|2|22)3': {
      '3', '23', '223',
      '13', '123', '1223',
      '113', '1123', '11223',
    },
    '(55555|4444|333|22|1|)': {'55555', '4444', '333', '22', '1', ''},
  }
  
  def test_sequence_set_from_regex(self):
    for regex, set_ in self.actual_sequence_set_from_regex.items():
      self.assertEqual(generate.sequence_set_from_regex(regex), set_)

if __name__ == '__main__':
  unittest.main()

