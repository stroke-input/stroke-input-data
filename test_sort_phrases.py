#!/usr/bin/env python3

"""
# test_sort_phrases.py

Perform unit testing on `sort_phrases.py`.

Licensed under "MIT No Attribution" (MIT-0),
see <https://spdx.org/licenses/MIT-0>.
"""


import sort_phrases
import unittest


class TestSort(unittest.TestCase):
  
  def test_backupise_name(self):
    self.assertEqual(
      sort_phrases.backupise_name('dir/foo', 1234),
      'dir/.foo-1234.bak'
    )
    self.assertEqual(
      sort_phrases.backupise_name('dir/bar', 0),
      'dir/.bar-0.bak'
    )
  
  simple_sorting_key_from_character = {
    
    '㐀': (1, 0x3400),
    '䶵': (1, 0x4DB5),
    '䷿': (1, 0x4DFF),
    
    '一': (0, 0x4E00),
    '鿐': (0, 0x9FD0),
    '鿿': (0, 0x9FFF),
    
    'ꀀ': (1, 0xA000),
    '𠀋': (1, 0x2000B),
    '𪚲': (1, 0x2A6B2),
    
  }
  
  def test_simple_character_sorting_key(self):
    for character, key in self.simple_sorting_key_from_character.items():
      self.assertEqual(
        sort_phrases.character_sorting_key(character),
        key
      )


if __name__ == '__main__':
  unittest.main()
