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


def join_sorted(string_set):
  """
  Join a set of strings with lexicographic sorting.
  """
  
  return ''.join(sorted(string_set))


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


class CharactersData:
  """
  Class for characters data.
  """
  
  def __init__(self):
    self.goodly_set = set()
    self.abomination_set = set()
  
  def add_goodly(self, character):
    self.goodly_set.add(character)
  
  def add_abomination(self, character):
    self.abomination_set.add(character)
  
  def add_data(self, characters_data):
    for character in characters_data.goodly_set:
      self.add_goodly(character)
    for character in characters_data.abomination_set:
      self.add_abomination(character)
  
  def to_string(self):
    goodly_string = join_sorted(self.goodly_set)
    abomination_string = join_sorted(self.abomination_set)
    if len(abomination_string) == 0:
      return goodly_string
    else:
      return f'{goodly_string},{abomination_string}'


COMPLIANT_LINE_REGEX = r'''
  U[+]
  (?P<codepoint_hex> [0-9A-F]{4,5} )
    \t
  (?P<character> \S )
  (?P<abomination_asterisk> [*]? )
    \t
  (?P<sequence_regex> [1-5|()\\]+ )
'''


SEQUENCE_CHARACTERS_FILE_HEADER = (
'''\
# # sequence-characters.txt

# Part of 'Conway Stroke Data',
# see <https://github.com/stroke-input/stroke-input-data>.

# Copyright 2021 Conway.
# Licensed under Creative Commons Attribution 4.0 International (CC-BY-4.0),
# see <https://creativecommons.org/licenses/by/4.0/>.

# Contains tab-separated (stroke sequence, characters data) pairs,
# where characters data consists of
# comma-separated (goodly characters, abominable characters) pairs.

# This file is automatically generated by running `generate.py`
# in <https://github.com/stroke-input/stroke-input-data>.
# It should NOT be edited manually.
# Manual edits should be made to `codepoint-character-sequence.txt`.

'''
)


if __name__ == '__main__':
  
  characters_data_from_sequence = {}
  
  with open('.ignored-lines.txt', 'w', encoding='utf-8') \
  as ignored_lines_file:
    
    for codepoint_character_sequence_line \
    in get_lines('codepoint-character-sequence.txt'):
      
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
      abomination_asterisk = line_match_object.group('abomination_asterisk')
      sequence_regex = line_match_object.group('sequence_regex')
      
      if int(codepoint_hex, 16) != ord(character):
        ignored_lines_file.write(codepoint_character_sequence_line + '\n')
        continue
      
      is_abomination = len(abomination_asterisk) > 0
      sequence_set = to_sequence_set(sequence_regex)
      
      for sequence in sequence_set:
        
        try:
          characters_data = characters_data_from_sequence[sequence]
        except KeyError:
          characters_data = \
            characters_data_from_sequence[sequence] = CharactersData()
        
        if is_abomination:
          characters_data.add_abomination(character)
        else:
          characters_data.add_goodly(character)
  
  sorted_sequences = sorted(characters_data_from_sequence.keys())
  
  with open('sequence-characters.txt', 'w', encoding='utf-8') \
  as sequence_characters_file:
    
    sequence_characters_file.write(SEQUENCE_CHARACTERS_FILE_HEADER)
    
    for sequence in sorted_sequences:
      
      characters_data = characters_data_from_sequence[sequence]
      characters_data_string = characters_data.to_string()
      sequence_characters_file.write(f'{sequence}\t{characters_data_string}\n')
