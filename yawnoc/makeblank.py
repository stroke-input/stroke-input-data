#!/usr/bin/env python3

"""
# makeblank.py

Make a tab-separated file of (code point, character, empty string) triplets,
for Chinese characters in the Basic Multilingual Plane (BMP),
excluding Compatibility characters,
ready for @yawnoc to manually populate with stroke sequences.

Licensed under "MIT No Attribution" (MIT-0),
see <https://spdx.org/licenses/MIT-0>.
"""


import itertools
import os


SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE_NAME = os.path.join(SCRIPT_DIRECTORY, 'blank.txt')


if __name__ == '__main__':
  
  CJK_INT_RANGE = itertools.chain(
    # CJK Unified Ideographs
    range(0x4E00, 0x9FFC + 1),
    # CJK Unified Ideographs Extension A
    range(0x3400, 0x4DBF + 1),
  )
  
  with open(OUTPUT_FILE_NAME, 'w', encoding='utf-8') as text_file:
    for cjk_int in CJK_INT_RANGE:
      code_point = f'U+{cjk_int:X}'
      character = chr(cjk_int)
      text_file.write(f'{code_point}\t{character}\t\n')
