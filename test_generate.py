#!/usr/bin/env python3

"""
# test_generate.py

Perform unit testing on `generate.py`.

Licensed under "MIT No Attribution" (MIT-0), see <https://spdx.org/licenses/MIT-0>.
"""

import unittest

from generate import to_sequence_set


class TestGenerate(unittest.TestCase):
    def test_to_sequence_set(self):
        self.assertEqual(to_sequence_set('1'), {'1'})
        self.assertEqual(to_sequence_set('12345'), {'12345'})
        self.assertEqual(to_sequence_set('(444)'), {'444'})
        self.assertEqual(to_sequence_set('(1)(2)(3)(4)(5)'), {'12345'})
        self.assertEqual(to_sequence_set('()123'), {'123'})
        self.assertEqual(to_sequence_set('(5|5)43'), {'543'})
        self.assertEqual(to_sequence_set('(|1)123'), {'123', '1123'})
        self.assertEqual(to_sequence_set('(1|2)(3|45)'), {'13', '145', '23', '245'})
        self.assertEqual(to_sequence_set('(55555|4444|333|22|1|)'), {'55555', '4444', '333', '22', '1', ''})
        self.assertEqual(
            to_sequence_set('(|1|11)(|2|22)3'),
            {
                '3', '23', '223',
                '13', '123', '1223',
                '113', '1123', '11223',
            },
        )
        self.assertEqual(to_sequence_set(r'(123)\1'), {'123123'})
        self.assertEqual(
            to_sequence_set(r'(11|44)(2|3|5)111\2\1'),
            {
                '112111211', '113111311', '115111511',
                '442111244', '443111344', '445111544',
            },
        )


if __name__ == '__main__':
    unittest.main()
