#!/usr/bin/env python3

"""
# process.py

Process the raw files
* `raw/CNS_strokes_sequence.txt`: (CNS code, stroke sequence) pairs
* `raw/CNS2UNICODE_Unicode {2,15,BMP}.txt`: (CNS code, unicode) pairs
to produce a dictionary of (character, stroke sequence) pairs,
dumping the result into the files `stroke-data-{all,bmp}.txt`.
Also dump (code point, character, stroke sequence) triplets
into the file `stroke-data-triplets.txt`.

Licensed under "MIT No Attribution" (MIT-0),
see <https://spdx.org/licenses/MIT-0>.
"""


import csv
import os


SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


def absolute_file_name(file_name_relative_to_script):
  """
  Return absolute file name for a file name relative to this script.
  """
  
  return os.path.join(SCRIPT_DIRECTORY, file_name_relative_to_script)


def dict_to_file(dict_, file_name):
  """
  Write a dictionary into a file (tab-separated).
  """
  
  file_name = absolute_file_name(file_name)
  with open(file_name, 'w', encoding='utf-8') as text_file:
    writer = csv.writer(text_file, delimiter='\t')
    writer.writerows(dict_.items())


def file_to_dict(file_name, dict_={}):
  """
  Read a file into a dictionary.
  """
  
  file_name = absolute_file_name(file_name)
  with open(file_name, 'r', encoding='utf-8') as text_file:
    for line in text_file:
      (key, value) = line.split()
      dict_[key] = value
  
  return dict_


if __name__ == '__main__':
  
  # Read the raw data files and construct dictionaries
  sequence_from_cns = file_to_dict('raw/CNS_strokes_sequence.txt')
  unicode_from_cns = {}
  for unicode_plane in ['2', '15', 'BMP']:
    file_name = f'raw/CNS2UNICODE_Unicode {unicode_plane}.txt'
    file_to_dict(file_name, unicode_from_cns)
  
  # Process dictionaries into a single dictionary
  sequence_from_character = {}
  for cns in sequence_from_cns:
    sequence = sequence_from_cns[cns]
    unicode_hex = unicode_from_cns[cns]
    unicode_int = int(unicode_hex, 16)
    character = chr(unicode_int)
    sequence_from_character[character] = sequence
  
  # Sort dictionary by (strokes, stroke sequence, character)
  sorted_sequence_from_character = dict(
    sorted(
      sequence_from_character.items(),
      key=lambda x: (len(x[1]), x[1], x[0])
    )
  )
  
  # Create filtered dictionary containing only Basic Multilingual Plane (BMP)
  BMP_START = '\u0000'
  BMP_END = '\uFFFF'
  sorted_sequence_from_character_bmp = {
    character: sequence
      for character, sequence in sorted_sequence_from_character.items()
        if BMP_START <= character <= BMP_END
  }
  
  # Write dictionaries to files
  dict_to_file(sorted_sequence_from_character, 'stroke-data-all.txt')
  dict_to_file(sorted_sequence_from_character_bmp, 'stroke-data-bmp.txt')
  
  # Write triplets sorted by character
  TRIPLETS_FILE_NAME = absolute_file_name('stroke-data-triplets.txt')
  with open(TRIPLETS_FILE_NAME, 'w', encoding='utf-8') as text_file:
    CJK_INT_START = 0x4E00
    CJK_INT_END = 0x9FFF
    for cjk_int in range(CJK_INT_START, CJK_INT_END+1):
      code_point = f'U+{cjk_int:X}'
      character = chr(cjk_int)
      sequence = sorted_sequence_from_character_bmp.get(character, '')
      text_file.write(f'{code_point}\t{character}\t{sequence}\n')
