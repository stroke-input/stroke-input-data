#!/usr/bin/env python3

"""
# process.py

Process the raw files
* `raw/CNS_strokes_sequence.txt`: (CNS code, stroke sequence) pairs
* `raw/CNS2UNICODE_Unicode {2,15,BMP}.txt`: (CNS code, unicode) pairs
to produce a file containing (stroke sequence, character list) pairs,
dumping the result into the file `stroke-data.txt`.

Licensed under "MIT No Attribution" (MIT-0),
see <https://spdx.org/licenses/MIT-0>.
"""


################################################################
# Helpers
################################################################


def file_to_dict(file_name, dict_={}):
  """
  Read a file into a dictionary.
  """
  
  with open(file_name, 'r', encoding='utf-8') as text_file:
    for line in text_file:
      (key, value) = line.split()
      dict_[key] = value
  
  return dict_


################################################################
# Main function
################################################################


if __name__ == '__main__':
  
  # Read the raw data files and construct dictionaries.
  sequence_from_cns = file_to_dict('raw/CNS_strokes_sequence.txt')
  unicode_from_cns = {}
  for unicode_plane in ['2', '15', 'BMP']:
    file_name = f'raw/CNS2UNICODE_Unicode {unicode_plane}.txt'
    file_to_dict(file_name, unicode_from_cns)
