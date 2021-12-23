#!/usr/bin/env python3

"""
# sort.py

Sort (in-place) the phrases listed
in `phrases-traditional.txt` and `phrases-simplified.txt`.

Licensed under "MIT No Attribution" (MIT-0),
see <https://spdx.org/licenses/MIT-0>.
"""


import os
import shutil


def backupise_name(file_name, counter):
  """
  Return the backupised name.
  
  We ignore `.*.bak` in `.gitignore`.
  The leading dot makes it hidden on Linux.
  Bad luck if you use Windows.
  """
  
  return f'.{file_name}-{counter}.bak'


def create_backup_file(file_name):
  """
  Create a backup file.
  """
  
  counter = 0
  while True:
    backup_file_name = backupise_name(file_name, counter)
    if not os.path.exists(backup_file_name):
      break
    counter += 1
  
  shutil.copy(file_name, backup_file_name)


CJK_UNIFIED_IDEOGRAPHS_START = 0x4E00
CJK_UNIFIED_IDEOGRAPHS_END = 0x9FFF


def simple_character_sorting_key(character):
  """
  Return a key for simple sorting of Chinese characters.
  
  Puts characters in the main CJK Unified Ideographs block
  (U+4E00 to U+9FFF) first, but otherwise sorts by code point.
  """
  
  code_point = ord(character)
  
  if CJK_UNIFIED_IDEOGRAPHS_START <= code_point <= CJK_UNIFIED_IDEOGRAPHS_END:
    block_rank = 0
  else:
    block_rank = 1
  
  return (block_rank, code_point)


def simple_phrase_sorting_key(phrase):
  """
  Return a key for simple sorting of Chinese phrases.
  """
  
  return tuple(simple_character_sorting_key(character) for character in phrase)


PHRASE_FILE_NAMES = [
  'phrases-traditional.txt',
  'phrases-simplified.txt',
]
PHRASE_SECTION_DELIMITER = '\n\n'


if __name__ == '__main__':
  
  for phrase_file_name in PHRASE_FILE_NAMES:
    
    create_backup_file(phrase_file_name)
    
    with open(phrase_file_name ,'r', encoding='utf-8') as phrase_file:
      
      preamble_text, _, phrase_text = \
              phrase_file \
                .read() \
                .rpartition(PHRASE_SECTION_DELIMITER)
    
    sorted_phrase_list = \
            sorted(set(phrase_text.splitlines()), key=simple_phrase_sorting_key)
    
    with open(phrase_file_name ,'w', encoding='utf-8') as phrase_file:
      
      phrase_file.write(preamble_text)
      phrase_file.write(PHRASE_SECTION_DELIMITER)
      for phrase in sorted_phrase_list:
        phrase_file.write(f'{phrase}\n')
