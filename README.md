# Conway Stroke Data

A data set compiled manually by Conway ([@yawnoc]),
used in the Android keyboard app [Stroke Input Method (Chinese keyboard)][app].


## Stroke input method (筆畫輸入法)

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
[dumbphone]: images/dumbphone-stroke-input.jpg
[@yawnoc]: https://github.com/yawnoc


## Directories

### [`compiled/`]

Contains data __compiled manually__ by Conway ([@yawnoc]).

### [`generated/`]

Contains data __generated automatically__ by the scripts in the root directory.

[`compiled/`]: compiled/
[`generated/`]: generated/


## Scripts

### [`make_txt.py`]

- Script used to generate `generated/*.txt` (text files)
- Licensed under [MIT-0]

### [`MakeSer.java`]

- Script used to generate `generated/*.ser` (serial files)
- Licensed under [MIT-0]

### [`sort_phrases.py`]

- Script used to sort certain sections of `compiled/phrases-*.txt`.
- Licensed under [MIT-0]

### [`test_make_txt.py`]

- Unit tests for `make_txt.py`
- Licensed under [MIT-0]

### [`test_sort_phrases.py`]

- Unit tests for `sort_phrases.py`
- Licensed under [MIT-0]

[`make_txt.py`]: make_txt.py
[`MakeSer.java`]: MakeSer.java
[`sort_phrases.py`]: sort_phrases.py
[`test_make_txt.py`]: test_make_txt.py
[`test_sort_phrases.py`]: test_sort_phrases.py
[MIT-0]: https://spdx.org/licenses/MIT-0
