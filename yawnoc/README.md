# stroke-input-data/yawnoc

A stroke data set that I am compiling manually (work in progress).
Will probably take until end of 2021 to complete.


## Contents

### [`abomination.txt`]

- Abomination data
- Automatically generated from `generate.py`
- Released into the [public domain]

### [`codepoint-character-sequence.txt`]

- Tab-separated (code point, character, stroke sequence regex) data
- Compiled manually by @yawnoc
- Licensed under [CC-BY-4.0]

### [`generate.py`]

- Script used to generate `sequence-characters.txt`
- Licensed under [MIT-0]

### [`sequence-characters.txt`]

- Tab-separated (stroke sequence, characters) data
- Automatically generated from `generate.py`
- Licensed under [CC-BY-4.0]

### [`test_generate.py`]

- Unit tests for `generate.py`
- Licensed under [MIT-0]

[`abomination.txt`]: abomination.txt
[`codepoint-character-sequence.txt`]: codepoint-character-sequence.txt
[`generate.py`]: generate.py
[`sequence-characters.txt`]: sequence-characters.txt
[`test_generate.py`]: test_generate.py
[public domain]: https://creativecommons.org/publicdomain/zero/1.0/
[CC-BY-4.0]: https://creativecommons.org/licenses/by/4.0/
[MIT-0]: https://spdx.org/licenses/MIT-0


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
