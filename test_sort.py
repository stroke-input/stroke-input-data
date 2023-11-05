#!/usr/bin/env python3

"""
# test_sort.py

Perform unit testing on `sort.py`.

Licensed under "MIT No Attribution" (MIT-0), see <https://spdx.org/licenses/MIT-0>.
"""

import unittest

from sort import character_sorting_key, sort_variants


class TestSort(unittest.TestCase):
    def test_character_sorting_key(self):
        self.assertEqual(character_sorting_key('㐀'), (1, 0x3400))
        self.assertEqual(character_sorting_key('䶵'), (1, 0x4DB5))
        self.assertEqual(character_sorting_key('䷿'), (1, 0x4DFF))

        self.assertEqual(character_sorting_key('一'), (0, 0x4E00))
        self.assertEqual(character_sorting_key('鿐'), (0, 0x9FD0))
        self.assertEqual(character_sorting_key('鿿'), (0, 0x9FFF))

        self.assertEqual(character_sorting_key('ꀀ'), (1, 0xA000))
        self.assertEqual(character_sorting_key('𠀋'), (1, 0x2000B))
        self.assertEqual(character_sorting_key('𪚲'), (1, 0x2A6B2))

    def test_sort_variants(self):
        self.assertEqual(sort_variants('# CBA'), '# ABC')
        self.assertEqual(sort_variants('# CBC'), '# BC')

        self.assertEqual(sort_variants('# CBA (comment)'), '# ABC (comment)')
        self.assertEqual(sort_variants('# CBC (comment)'), '# BC (comment)')


if __name__ == '__main__':
    unittest.main()
