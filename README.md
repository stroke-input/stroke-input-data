# Conway Stroke Data

A data set that I am compiling manually (work in progress)
for the [Stroke Input Method (筆畫輸入法)] in Chinese.

Will probably take until end of 2021 to complete.

To be used in [stroke-input-android].


## Stroke Input Method

The stroke input method is found on all dumbphones in HK and surrounds.

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

[Stroke Input Method (筆畫輸入法)]: https://zh.wikipedia.org/wiki/筆畫輸入法
[stroke-input-android]: https://github.com/stroke-input/stroke-input-android
[dumbphone]: dumbphone-stroke-input.jpg


## Contents

### [`codepoint-character-sequence.txt`]

- Tab-separated (code point, character, stroke sequence regex) triplets
- Compiled manually by Conway (@yawnoc)
- Licensed under [CC-BY-4.0]

### [`generate.py`]

- Script used to generate `sequence-characters.txt`
- Licensed under [MIT-0]

### [`phrases-traditional.txt`], [`phrases-simplified.txt`]

- List of common phrases
- Released into the [public domain]

### [`ranking-traditional.txt`], [`ranking-simplified.txt`]

- Ranking of commonly used characters
- Compiled manually by Conway (@yawnoc)
- Released into the [public domain]

### [`sequence-characters.txt`]

- Tab-separated (stroke sequence, characters data) pairs
- Automatically generated from `generate.py`
- Licensed under [CC-BY-4.0]

### [`test_generate.py`]

- Unit tests for `generate.py`
- Licensed under [MIT-0]

[`codepoint-character-sequence.txt`]: codepoint-character-sequence.txt
[`generate.py`]: generate.py
[`phrases-traditional.txt`]: phrases-traditional.txt
[`phrases-simplified.txt`]: phrases-simplified.txt
[`ranking-traditional.txt`]: ranking-traditional.txt
[`ranking-simplified.txt`]: ranking-simplified.txt
[`sequence-characters.txt`]: sequence-characters.txt
[`test_generate.py`]: test_generate.py
[CC-BY-4.0]: https://creativecommons.org/licenses/by/4.0/
[MIT-0]: https://spdx.org/licenses/MIT-0
[public domain]: https://creativecommons.org/publicdomain/zero/1.0/


## Unicode strokes

[CJK Strokes (Unicode block)] (`U+31C0` to `U+31E3`),
for convenient reference:

````
㇀㇁㇂㇃㇄㇅㇆㇇㇈㇉㇊㇋㇌㇍㇎㇏
㇐㇑㇒㇓㇔㇕㇖㇗㇘㇙㇚㇛㇜㇝㇞㇟
㇠㇡㇢㇣
````

[CJK Strokes (Unicode block)]:
  https://en.wikipedia.org/wiki/CJK_Strokes_(Unicode_block)
