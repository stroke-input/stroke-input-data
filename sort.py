#!/usr/bin/env python3

"""
# sort.py

Sort (in-place) certain sections of
`phrases-traditional.txt` and `phrases-simplified.txt`.

Licensed under "MIT No Attribution" (MIT-0),
see <https://spdx.org/licenses/MIT-0>.
"""


import os
import re
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


def sort_variant_sections(text):
  """
  Sort (in-place) the variant sections of the supplied text.
  """
  
  return \
          re.sub(
            '(?<=^# <variants>\n)([\s\S]+?)(?=\n# </variants>)',
            sort_variant_section_match,
            text,
            flags=re.MULTILINE
          )


def sort_variant_section_match(match_object):
  """
  Sort the variants in a variant section match object.
  
  This involves both inline sorting
  (variants in each line after the leading hash and space)
  and sorting of the lines.
  """
  
  variants_text = match_object.group()
  variants_text = \
          re.sub(
            '(?<=^# )(\S+)',
            sort_inline_variants_match,
            variants_text,
            flags=re.MULTILINE
          )
  sorted_variants_list = \
          sorted(set(variants_text.splitlines()), key=simple_phrase_sorting_key)
  sorted_variants_text = '\n'.join(sorted_variants_list)
  
  return sorted_variants_text


def sort_inline_variants_match(match_object):
  """
  Sort the variants in an inline variants match object.
  """
  
  inline_variants_text = match_object.group()
  sorted_inline_variants_list = \
          sorted(inline_variants_text, key=simple_character_sorting_key)
  inline_variants_text = ''.join(sorted_inline_variants_list)
  
  return inline_variants_text


def sort_phrase_sections(text):
  """
  Sort (in-place) the phrase sections of the supplied text.
  """
  
  return \
          re.sub(
            '(?<=^# <phrases>\n)([\s\S]+?)(?=\n# </phrases>)',
            sort_phrase_section_match,
            text,
            flags=re.MULTILINE
          )


def sort_phrase_section_match(match_object):
  """
  Sort the phrases in a phrase section match object.
  """
  
  phrases_text = match_object.group()
  sorted_phrases_list = \
          sorted(set(phrases_text.splitlines()), key=simple_phrase_sorting_key)
  sorted_phrases_text = '\n'.join(sorted_phrases_list)
  
  return sorted_phrases_text


PHRASE_FILE_NAMES = [
  'phrases-traditional.txt',
  'phrases-simplified.txt',
]


if __name__ == '__main__':
  
  for phrase_file_name in PHRASE_FILE_NAMES:
    
    create_backup_file(phrase_file_name)
    
    with open(phrase_file_name ,'r', encoding='utf-8') as phrase_file:
      phrase_file_text = phrase_file.read()
    
    phrase_file_text = sort_variant_sections(phrase_file_text)
    phrase_file_text = sort_phrase_sections(phrase_file_text)
    
    with open(phrase_file_name ,'w', encoding='utf-8') as phrase_file:
      phrase_file.write(phrase_file_text)
