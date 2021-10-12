#!/usr/bin/env python3

"""
# generate.py

Parse `codepoint-character-sequence.txt`,
generating `sequence-characters.txt`.

Licensed under "MIT No Attribution" (MIT-0),
see <https://spdx.org/licenses/MIT-0>.
"""


import itertools
import re


def get_lines(file_name):
  """
  Get the lines in a file.
  """
  
  with open(file_name, 'r', encoding='utf-8') as file:
    return file.read().splitlines()


CAPTURE_GROUP_REGEX = r'''
  \(
    (?P<alternatives> [1-5|]* )
  \)
'''


def replace_capture_group(group_match_object, group_alternatives_set_list):
  """
  Replace a capture group match object with a back reference.
  Appends the capture group's alternatives (as a set)
  to the supplied list of sets of capture group alternatives.
  """
  
  group_alternatives_string = group_match_object.group('alternatives')
  group_alternatives_set = set(group_alternatives_string.split('|'))
  group_alternatives_set_list.append(group_alternatives_set)
  
  group_index = len(group_alternatives_set_list)
  back_reference = fr'\{group_index}'
  
  return back_reference


BACK_REFERENCE_REGEX = r'''
  \\
  (?P<group_index> [1-9] )
'''


def replace_back_reference(
  back_reference_match_object,
  alternatives_combination
):
  """
  Replace a back reference with the appropriate alternative.
  """
  
  group_index = int(back_reference_match_object.group('group_index'))
  alternative = alternatives_combination[group_index - 1]
  
  return alternative


def to_sequence_set(sequence_regex):
  """
  Convert stroke sequence regex to a stroke sequence set.
  Assumes capture groups:
    1. number at most 9,
    2. are not nested,
    3. contain pure digits separated by pipes, and
    4. are referred to by a backslash followed by
       a positive decimal digit.
  """
  
  group_alternatives_set_list = []
  
  back_referenced_sequence_regex = re.sub(
    CAPTURE_GROUP_REGEX,
    lambda x: replace_capture_group(x, group_alternatives_set_list),
    sequence_regex,
    flags=re.VERBOSE
  )
  
  sequence_set = set()
  
  alternatives_combinations = itertools.product(*group_alternatives_set_list)
  
  for alternatives_combination in alternatives_combinations:
    
    sequence = re.sub(
      BACK_REFERENCE_REGEX,
      lambda x: replace_back_reference(x, alternatives_combination),
      back_referenced_sequence_regex,
      flags=re.VERBOSE
    )
    
    sequence_set.add(sequence)
  
  return sequence_set


CHARACTER_TYPE_TRADITIONAL = '^'
CHARACTER_TYPE_SIMPLIFIED = '*'
COMPLIANT_LINE_REGEX = r'''
  U[+]
  (?P<codepoint_hex> [0-9A-F]{4,5} )
    \t
  (?P<character> \S )
  (?P<character_type> [\^*]? )
    \t
  (?P<sequence_regex> [1-5|()\\]+ )
'''

CODEPOINT_CHARACTER_SEQUENCE_FILE_NAME = 'codepoint-character-sequence.txt'
SEQUENCE_CHARACTERS_FILE_NAME = 'sequence-characters.txt'
CHARACTERS_TRADITIONAL_FILE_NAME = 'characters-traditional.txt'
CHARACTERS_SIMPLIFIED_FILE_NAME = 'characters-simplified.txt'
IGNORED_LINES_FILE_NAME = '.ignored-lines.txt'


STROKE_DATA_NOTICE = (
'''\
# Part of 'Conway Stroke Data',
# see <https://github.com/stroke-input/stroke-input-data>.\
'''
)


CREATIVE_COMMONS_NOTICE = (
'''\
# Copyright 2021 Conway.
# Licensed under Creative Commons Attribution 4.0 International (CC-BY-4.0),
# see <https://creativecommons.org/licenses/by/4.0/>.\
'''
)


PUBLIC_DOMAIN_NOTICE = (
'''\
# Released into the public domain,
# see <https://creativecommons.org/publicdomain/zero/1.0/>.\
'''
)


AUTOMATIC_GENERATION_NOTICE = (
f'''\
# This file is automatically generated by running `generate.py`
# in <https://github.com/stroke-input/stroke-input-data>.
# It should NOT be edited manually.
# Manual edits should be made to `{CODEPOINT_CHARACTER_SEQUENCE_FILE_NAME}`.\
'''
)


SEQUENCE_CHARACTERS_FILE_HEADER = (
f'''\
# # {SEQUENCE_CHARACTERS_FILE_NAME}

{STROKE_DATA_NOTICE}

{CREATIVE_COMMONS_NOTICE}

# Contains tab-separated (stroke sequence, characters) pairs.

{AUTOMATIC_GENERATION_NOTICE}

'''
)


CHARACTERS_TRADITIONAL_FILE_HEADER = (
f'''\
# # {CHARACTERS_TRADITIONAL_FILE_NAME}

{STROKE_DATA_NOTICE}

{PUBLIC_DOMAIN_NOTICE}

# Contains traditional characters.

{AUTOMATIC_GENERATION_NOTICE}

'''
)


CHARACTERS_SIMPLIFIED_FILE_HEADER = (
f'''\
# # {CHARACTERS_SIMPLIFIED_FILE_NAME}

{STROKE_DATA_NOTICE}

{PUBLIC_DOMAIN_NOTICE}

# Contains simplified characters.

{AUTOMATIC_GENERATION_NOTICE}

'''
)


if __name__ == '__main__':
  
  traditional_character_set = set()
  simplified_character_set = set()
  dual_character_set = set()
  
  characters_from_sequence = {}
  
  with open(IGNORED_LINES_FILE_NAME, 'w', encoding='utf-8') \
  as ignored_lines_file:
    
    for codepoint_character_sequence_line \
    in get_lines(CODEPOINT_CHARACTER_SEQUENCE_FILE_NAME):
      
      line_match_object = re.fullmatch(
        COMPLIANT_LINE_REGEX,
        codepoint_character_sequence_line,
        flags=re.VERBOSE
      )
      line_is_not_compliant = line_match_object is None
      
      if line_is_not_compliant:
        ignored_lines_file.write(codepoint_character_sequence_line + '\n')
        continue
      
      codepoint_hex = line_match_object.group('codepoint_hex')
      character = line_match_object.group('character')
      character_type = line_match_object.group('character_type')
      sequence_regex = line_match_object.group('sequence_regex')
      
      if int(codepoint_hex, 16) != ord(character):
        ignored_lines_file.write(codepoint_character_sequence_line + '\n')
        continue
      
      if character_type == CHARACTER_TYPE_TRADITIONAL:
        traditional_character_set.add(character)
      elif character_type == CHARACTER_TYPE_SIMPLIFIED:
        simplified_character_set.add(character)
      else:
        dual_character_set.add(character)
      
      sequence_set = to_sequence_set(sequence_regex)
      
      for sequence in sequence_set:
        
        try:
          existing_characters = characters_from_sequence[sequence]
        except KeyError:
          existing_characters = characters_from_sequence[sequence] = ""
        
        characters_from_sequence[sequence] = existing_characters + character
  
  character_count = len(
    {
      *traditional_character_set,
      *simplified_character_set,
      *dual_character_set,
    }
  )
  print(
    f'Finished parsing `{CODEPOINT_CHARACTER_SEQUENCE_FILE_NAME}` '
    f'({character_count} characters).'
  )
  
  sorted_sequences = sorted(characters_from_sequence.keys())
  
  with open(SEQUENCE_CHARACTERS_FILE_NAME, 'w', encoding='utf-8') \
  as sequence_characters_file:
    
    sequence_characters_file.write(SEQUENCE_CHARACTERS_FILE_HEADER)
    
    for sequence in sorted_sequences:
      characters = characters_from_sequence[sequence]
      sequence_characters_file.write(f'{sequence}\t{characters}\n')
  
  sorted_sequence_count = len(sorted_sequences)
  print(
    f'Finished generating `{SEQUENCE_CHARACTERS_FILE_NAME}` '
    f'({sorted_sequence_count} stroke sequences).'
  )
  
  with open(CHARACTERS_TRADITIONAL_FILE_NAME, 'w', encoding='utf-8') \
  as characters_traditional_file:
    
    characters_traditional_file.write(CHARACTERS_TRADITIONAL_FILE_HEADER)
    for character in sorted(traditional_character_set):
      characters_traditional_file.write(f'{character}\n')
  
  traditional_character_count = len(traditional_character_set)
  print(
    f'Finished generating `{CHARACTERS_TRADITIONAL_FILE_NAME}` '
    f'({traditional_character_count} characters).'
  )
  
  with open(CHARACTERS_SIMPLIFIED_FILE_NAME, 'w', encoding='utf-8') \
  as characters_simplified_file:
    
    characters_simplified_file.write(CHARACTERS_SIMPLIFIED_FILE_HEADER)
    for character in sorted(simplified_character_set):
      characters_simplified_file.write(f'{character}\n')
  
  simplified_character_count = len(simplified_character_set)
  print(
    f'Finished generating `{CHARACTERS_SIMPLIFIED_FILE_NAME}` '
    f'({simplified_character_count} characters).'
  )
