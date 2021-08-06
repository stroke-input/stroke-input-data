#!/usr/bin/env python3

"""
# generate.py

Parse the lines of `codepoint-character-sequence.txt`,
which are (code point, character, stroke sequence regex) triplets,
and generate `sequence-characters.txt`,
whose lines shall be (stroke sequence, characters) pairs,
and the subsidiary `abomination.txt`, whose lines shall be abominations.

Licensed under "MIT No Attribution" (MIT-0),
see <https://spdx.org/licenses/MIT-0>.
"""


import itertools
import os
import re


SCRIPT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))


def absolute_path(file_name):
  """
  Return the absolute path for a file name.
  Reckoned relative to the script directory.
  """
  
  return os.path.join(SCRIPT_DIRECTORY, file_name)


def sequence_set_from_regex(sequence_regex):
  """
  Return the set of stroke sequences for a stroke sequence regex.
  Assumes capture groups number at most 9, are not nested,
  contain pure digits separated by pipes, and are referred to
  by a backslash followed by a positive decimal digit.
  """
  
  sequence_regex_no_groups, group_alternatives_set_list = (
    parse_sequence_regex_groups(sequence_regex)
  )
  
  sequence_set = set()
  
  cartesian_product = itertools.product(*group_alternatives_set_list)
  for group_alternatives_combination in cartesian_product:
    
    sequence = re.sub(
      r'''
        \\
        (?P<group_index> [1-9] )
      ''',
      lambda back_reference_match_object:
        replace_back_reference_match_object(
          back_reference_match_object,
          group_alternatives_combination
        ),
      sequence_regex_no_groups,
      flags=re.VERBOSE
    )
    
    sequence_set.add(sequence)
  
  return sequence_set


def replace_back_reference_match_object(
  back_reference_match_object,
  group_alternatives_combination
):
  """
  Replace a back reference with the appropriate alternative.
  """
  
  group_index = int(back_reference_match_object.group('group_index'))
  
  return group_alternatives_combination[group_index - 1]


def parse_sequence_regex_groups(sequence_regex):
  """
  Parse the capture groups of a stroke sequence regex.
  Returns a tuple of
  1. the regex with capture groups replaced by back references, and
  2. a list of sets for the capture groups' alternatives.
  """
  
  group_alternatives_set_list = []
  
  sequence_regex_no_groups = re.sub(
    r'''
      \(
        (?P<alternatives> [1-5|]* )
      \)
    ''',
    lambda group_match_object:
      replace_group_match_object(
        group_match_object,
        group_alternatives_set_list
      ),
    sequence_regex,
    flags=re.VERBOSE
  )
  
  return sequence_regex_no_groups, group_alternatives_set_list


def replace_group_match_object(
  group_match_object,
  group_alternatives_set_list
):
  """
  Replace a capture group match object with a back reference.
  Appends the capture group's alternatives (as a set)
  to the supplied list of sets of alternatives.
  """
  
  group_alternatives_string = group_match_object.group('alternatives')
  group_alternatives_set = set(group_alternatives_string.split('|'))
  group_alternatives_set_list.append(group_alternatives_set)
  
  group_index = len(group_alternatives_set_list)
  back_reference = fr'\{group_index}'
  
  return back_reference


if __name__ == '__main__':
  
  INPUT_FILE_NAME = absolute_path('codepoint-character-sequence.txt')
  OUTPUT_FILE_NAME = absolute_path('sequence-characters.txt')
  ABOMINATION_FILE_NAME = absolute_path('abomination.txt')
  
  with open(INPUT_FILE_NAME, 'r', encoding='utf-8') as input_file:
    input_lines = input_file.read().splitlines()
  
  character_set_from_sequence = {}
  abomination_list = []
  
  for line in input_lines:
    
    line_match_object = re.fullmatch(
      r'''
        U[+][0-9A-F]{4,5}
          \t
        (?P<character> \S )
        (?P<abomination_asterisk> [*]? )
          \t
        (?P<sequence_regex> [1-5|()\\]+ )
      ''',
      line,
      flags=re.VERBOSE
    )
    
    if line_match_object is None:
      continue
    
    character = line_match_object.group('character')
    abomination_asterisk = line_match_object.group('abomination_asterisk')
    sequence_regex = line_match_object.group('sequence_regex')
    
    sequence_set = sequence_set_from_regex(sequence_regex)
    for sequence in sequence_set:
      if sequence not in character_set_from_sequence:
        character_set_from_sequence[sequence] = set()
      character_set_from_sequence[sequence].add(character)
    
    if abomination_asterisk != '':
      abomination_list.append(character)
  
  sorted_sequences = sorted(character_set_from_sequence.keys())
  
  with open(OUTPUT_FILE_NAME, 'w', encoding='utf-8') as output_file:
    
    output_file.write(
      '# # sequence-characters.txt\n'
      '\n'
      '# Copyright 2021 Conway.\n'
      '# Licensed under Creative Commons Attribution 4.0 International '
        '(CC-BY-4.0),\n'
      '# see <https://creativecommons.org/licenses/by/4.0/>.\n'
      '\n'
      '# Contains tab-separated (stroke sequence, characters) data.\n'
      '\n'
      '# This file is automatically generated by running `generate.py`\n'
      '# in <https://github.com/stroke-input/stroke-input-data>.\n'
      '# It should NOT be edited manually.\n'
      '# Manual edits should be made to `codepoint-character-sequence.txt`.\n'
      '\n'
    )
    
    for sequence in sorted_sequences:
      sorted_character_set = sorted(character_set_from_sequence[sequence])
      sorted_characters = ''.join(sorted_character_set)
      output_file.write(f'{sequence}\t{sorted_characters}\n')
  
  with open(ABOMINATION_FILE_NAME, 'w', encoding='utf-8') as abomination_file:
    
    abomination_file.write(
      '# # abomination.txt\n'
      '\n'
      '# Released into the public domain,\n'
      '# see <https://creativecommons.org/publicdomain/zero/1.0/>.\n'
      '\n'
      '# Contains abominations.\n'
      '\n'
      '# This file is automatically generated by running `generate.py`\n'
      '# in <https://github.com/stroke-input/stroke-input-data>.\n'
      '# It should NOT be edited manually.\n'
      '# Manual edits should be made to `codepoint-character-sequence.txt.`\n'
      '\n'
    )
    
    for character in abomination_list:
      abomination_file.write(f'{character}\n')
