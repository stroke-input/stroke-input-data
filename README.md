# Conway Stroke Data

A data set compiled manually by Conway ([@yawnoc]),
used in the Android keyboard app [Stroke Input Method (筆畫輸入法)][app].


## Stroke input method (generic, not the app)

The (generic) stroke input method is found on all dumbphones
in HK and surrounds.

It is the simplest Chinese input method in existence.
All strokes are classified into 5 types, entered via keypad:

| \# | Stroke | Type | Comment |
| -: | :-: | - | - |
| 1 | ㇐ | 橫 Horizontal | Includes rises (提) etc. |
| 2 | ㇑ | 豎 Vertical | |
| 3 | ㇒ | 撇 Throw | |
| 4 | ㇔ | 點 Dot | Includes presses (捺) |
| 5 | ㇖ | 折 Break | Basically everything else |

![Picture of a dumbphone with stroke input method on keys 1 to 5.][dumbphone]

[app]: https://github.com/stroke-input/stroke-input-android
[dumbphone]: dumbphone-stroke-input.jpg
[@yawnoc]: https://github.com/yawnoc


## Contents of this repository


### A. Manually compiled data

The following files contain data manually compiled by Conway ([@yawnoc]):

#### [`codepoint-character-sequence.txt`]

- Tab-separated (code point, character, stroke sequence regex) triplets.
- There are 28k+ entries. Because Conway ([@yawnoc]) is human,
  it is highly likely that there are some mistakes; **please report these**.
- Licensed under [CC-BY-4.0].

#### [`phrases-traditional.txt`], [`phrases-simplified.txt`]

- Lists of common phrases.
- To be sorted by running `sort.py`.
- Released into the [public domain].

#### [`ranking-traditional.txt`], [`ranking-simplified.txt`]

- Rankings of commonly used characters.
- Released into the [public domain].


### B. Automatically generated data

The following files contain data automatically generated
by running `generate.py`, which parses `codepoint-character-sequence.txt`:

#### [`characters-traditional.txt`], [`characters-simplified.txt`]

- Lists of traditional-only and simplified-only characters.
- Released into the [public domain].

#### [`sequence-characters.txt`]

- Tab-separated (stroke sequence, characters) pairs.
- Licensed under [CC-BY-4.0].


### C. Scripts

#### [`.bash_aliases`]

- Defines shell functions `s` (search), `sp` (search prefix),
  `ss` (search suffix).

#### [`generate.py`]

- Script used to generate `sequence-characters.txt` and `characters-*.txt`
  (by parsing `codepoint-character-sequence.txt`).
- Licensed under [MIT-0].

#### [`sort.py`]

- Script used to sort certain sections of `phrases-*.txt`.
- Licensed under [MIT-0].


### D. Tests

#### [`test_generate.py`]

- Unit tests for `generate.py`.
- Licensed under [MIT-0].

#### [`test_sort.py`]

- Unit tests for `sort.py`.
- Licensed under [MIT-0].

[`.bash_aliases`]: .bash_aliases
[`characters-traditional.txt`]: characters-traditional.txt
[`characters-simplified.txt`]: characters-simplified.txt
[`codepoint-character-sequence.txt`]: codepoint-character-sequence.txt
[`generate.py`]: generate.py
[`phrases-traditional.txt`]: phrases-traditional.txt
[`phrases-simplified.txt`]: phrases-simplified.txt
[`ranking-traditional.txt`]: ranking-traditional.txt
[`ranking-simplified.txt`]: ranking-simplified.txt
[`sort.py`]: sort.py
[`sequence-characters.txt`]: sequence-characters.txt
[`test_generate.py`]: test_generate.py
[`test_sort.py`]: test_sort.py
[CC-BY-4.0]: https://creativecommons.org/licenses/by/4.0/
[MIT-0]: https://spdx.org/licenses/MIT-0
[public domain]: https://creativecommons.org/publicdomain/zero/1.0/


## Miscellanea for convenient reference (in comments)


### Unicode strokes

[CJK Strokes (Unicode block)] (`U+31C0` to `U+31E3`):

````
㇀㇁㇂㇃㇄㇅㇆㇇㇈㇉㇊㇋㇌㇍㇎㇏
㇐㇑㇒㇓㇔㇕㇖㇗㇘㇙㇚㇛㇜㇝㇞㇟
㇠㇡㇢㇣
````

### Unicode composition

[Ideographic Description Characters (Unicode block)] (`U+2FF0` to `U+2FFB`):

````
⿰⿱⿲⿳⿴⿵⿶⿷⿸⿹⿺⿻
````


[CJK Strokes (Unicode block)]:
  https://en.wikipedia.org/wiki/CJK_Strokes_(Unicode_block)
[Ideographic Description Characters (Unicode block)]:
  https://en.wikipedia.org/wiki/Ideographic_Description_Characters_(Unicode_block)
