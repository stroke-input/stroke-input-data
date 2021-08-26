#!/usr/bin/env python3

"""
# generate.py

Parse `codepoint-character-sequence.txt`
and generate `sequence-characters.txt`.

Licensed under "MIT No Attribution" (MIT-0),
see <https://spdx.org/licenses/MIT-0>.
"""


import re


def get_lines(file_name):
  """
  Get the lines in a file.
  """
  
  with open(file_name, 'r', encoding='utf-8') as file:
    return file.read().splitlines()


COMPLIANT_LINE_REGEX = r'''
  U[+][0-9A-F]{4,5}
    \t
  (?P<character> \S )
  (?P<abomination_asterisk> [*]? )
    \t
  (?P<sequence_regex> [1-5|()\\]+ )
'''


if __name__ == '__main__':
  
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
      
      character = line_match_object.group('character')
      abomination_asterisk = line_match_object.group('abomination_asterisk')
      sequence_regex = line_match_object.group('sequence_regex')
      
      is_abomination = len(abomination_asterisk) > 0
