#!/usr/bin/env python3

"""
# sort.py

Sort (in-place) certain sections of `phrases-traditional.txt` and `phrases-simplified.txt`.

Licensed under "MIT No Attribution" (MIT-0), see <https://spdx.org/licenses/MIT-0>.
"""

import re

CJK_UNIFIED_IDEOGRAPHS_START = 0x4E00
CJK_UNIFIED_IDEOGRAPHS_END = 0x9FFF

PHRASE_FILE_NAMES = [
  'phrases-traditional.txt',
  'phrases-simplified.txt',
]


def character_sorting_key(character):
    """
    Return a key for simple sorting of Chinese characters.

    Puts characters in the main CJK Unified Ideographs block (U+4E00 to U+9FFF) first,
    but otherwise sorts by code point.
    """
    code_point = ord(character)

    if CJK_UNIFIED_IDEOGRAPHS_START <= code_point <= CJK_UNIFIED_IDEOGRAPHS_END:
        block_rank = 0
    else:
        block_rank = 1

    return block_rank, code_point


def phrase_sorting_key(phrase):
    """
    Return a key for simple sorting of Chinese phrases.
    """
    return tuple(character_sorting_key(character) for character in phrase)


def sort_variant_sections(text):
    """
    Sort the variant sections of the supplied text.
    """
    return re.sub(
        r'(?<=^# <variants>\n)[\s\S]+?(?=\n# </variants>)',
        lambda match: '\n'.join(
            sorted(
                set(sort_variants(line) for line in match.group().splitlines()),  # intra-line sorting
                key=phrase_sorting_key,  # inter-line sorting
            )
        ),
        text,
        flags=re.MULTILINE,
    )


def sort_variants(line):
    """
    Sort variants within the supplied line.
    """
    return re.sub(
        r'(?<=^# )\S+',
        lambda match: ''.join(sorted(set(match.group()), key=character_sorting_key)),
        line,
    )


def sort_phrase_sections(text):
    """
    Sort the phrase sections of the supplied text.
    """
    return re.sub(
        r'(?<=^# <phrases>\n)[\s\S]+?(?=\n# </phrases>)',
        lambda match: '\n'.join(
            sorted(
                set(match.group().splitlines()),
                key=phrase_sorting_key,
            )
        ),
        text,
        flags=re.MULTILINE,
    )


def main():
    for phrase_file_name in PHRASE_FILE_NAMES:
        with open(phrase_file_name, 'r', encoding='utf-8') as phrase_file:
            old_text = phrase_file.read()

        new_text = sort_variant_sections(old_text)
        new_text = sort_phrase_sections(new_text)

        if old_text == new_text:
            continue

        with open(phrase_file_name, 'w', encoding='utf-8') as phrase_file:
            phrase_file.write(new_text)


if __name__ == '__main__':
    main()
