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
    r'(123)\1': {'123123'},
    r'(11|44)(2|3|5)111\2\1': {
      '112111211', '113111311', '115111511',
      '442111244', '443111344', '445111544',
    },
  }
  
  actual_parse_sequence_regex_groups = {
    '1': ('1', []),
    '12345': ('12345', []),
    '(444)': (r'\1', [{'444'}]),
    '(1)(2)(3)(4)(5)': (r'\1\2\3\4\5', [{'1'}, {'2'}, {'3'}, {'4'}, {'5'}]),
    '()123': (r'\1123', [{''}]),
    '(5|5)43': (r'\143', [{'5'}]),
    '(|1)123': (r'\1123', [{'', '1'}]),
    '(1|2)(3|45)': (r'\1\2', [{'1', '2'}, {'3', '45'}]),
    '(|1|11)(|2|22)3': (r'\1\23', [{'', '1', '11'}, {'', '2', '22'}]),
    '(55555|4444|333|22|1|)':
      (r'\1', [{'55555', '4444', '333', '22', '1', ''}]),
    r'(123)\1': (r'\1\1', [{'123'}]),
    r'(11|44)(2|3|5)111\2\1':
      (r'\1\2111\2\1', [{'11', '44'}, {'2', '3', '5'}]),
  }
  
  def test_sequence_set_from_regex(self):
    for regex, set_ in self.actual_sequence_set_from_regex.items():
      self.assertEqual(generate.sequence_set_from_regex(regex), set_)
  
  def test_parse_sequence_regex_groups(self):
    for regex, tuple_ in self.actual_parse_sequence_regex_groups.items():
      self.assertEqual(generate.parse_sequence_regex_groups(regex), tuple_)

if __name__ == '__main__':
  unittest.main()

