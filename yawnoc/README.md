# stroke-input-data/yawnoc

A stroke data set that I am compiling manually (work in progress).
Will probably take until end of 2021 to complete.


## Contents

### [`codepoint-character-sequence.txt`]

- Tab-separated list of (code point, character, stroke sequence regex) data
- Compiled manually by @yawnoc
- Released into the [Public Domain]

### [`makeblank.py`]

- Script used to generate `codepoint-character-sequence.txt`
  before it was populated with actual data
- Licensed under [MIT-0]

[`codepoint-character-sequence.txt`]: yawnoc/codepoint-character-sequence.txt
[`makeblank.py`]: yawnoc/makeblank.py
[Public Domain]: https://creativecommons.org/publicdomain/zero/1.0/
[MIT-0]: https://spdx.org/licenses/MIT-0


<!--
  CJK Strokes (Unicode block)
  <https://en.wikipedia.org/wiki/CJK_Strokes_(Unicode_block)>
  (`U+31C0` to `U+31E3`)
  ㇀㇁㇂㇃㇄㇅㇆㇇㇈㇉㇊㇋㇌㇍㇎㇏
  ㇐㇑㇒㇓㇔㇕㇖㇗㇘㇙㇚㇛㇜㇝㇞㇟
  ㇠㇡㇢㇣
-->

## How are strokes classified?

Mostly according to [康熙字典], with leniency and some exceptions.

Examples where lenient classification has been applied:

- `U+4E30` 丰 has 1st stroke either ㇐ or ㇒
- `U+4E31` 丱 has 2nd stroke either ㇓ or ㇑
- `U+4E9B` 些 has either 7 strokes or 8 strokes
  (康熙字典 counts only 3 strokes for the component 止; allow counting 4)
- `U+4ECA` 今 has 3rd stroke either ㇐ or ㇔
- `U+5315` 匕 has 1st stroke either ㇐ or ㇒
- `U+53CD` 反 has 1st stroke either ㇐ or ㇒
- `U+5782` 垂 has either 8 strokes or 9 strokes
  (康熙字典 counts only 3 strokes for the component 艹; allow counting 4)
- `U+58EC` 壬 has 1st stroke either ㇐ or ㇒
- `U+7A7A` 空 has 5th stroke either ㇏ or ㇟
  (康熙字典 has ㇏ despite having ㇟ for most occurrences of 穴)

Exceptions where [康熙字典] has been ignored:

- `U+4EE4` 令 has last stroke ㇔ rather than ㇑
- `U+5E1D` 帝 has 1st stroke ㇔ rather than ㇐
- `U+821F` 舟 has last stroke ㇔ rather than ㇑


## How are strokes ordered?

Leniently. Notable examples:

- `U+4E5D` 九 can have ㇓ either 1st or 2nd
- `U+5315` 匕 can have ㇒ either 1st or 2nd
- `U+6208` 戈 can have ㇔ either last or 2nd-last
- `U+65B9` 方 can have ㇒ either 2nd-last or last
- `U+6BCD` 母 can have ㇐ either last or 2nd-last
- `U+821F` 舟 can have ㇐ either last or 2nd-last
- `U+8279` 艹 can have ㇑ either 1st or 2nd
- `U+9577` 長 can have ㇑ either 1st or 2nd
- `U+99AC` 馬 can have ㇑ either 1st or 2nd


## What characters are included?

1. Does the character belong to either
   the [CJK Unified Ideographs block] (`U+4E00` to `U+9FFC`)
   or the [CJK Unified Ideographs Extension A block] (`U+3400` to `U+4DBF`)?
   - YES: go to 2.
   - NO: EXCLUDE the character. ❎

2. Does the character appear in [康熙字典]?
   - YES: INCLUDE the character. ✔️
   - NO: go to 3.

3. Is the character a variant or ancient form of another character?
   - YES: INCLUDE the character. ✔️
   - NO: go to 4.

4. Is the character the simplified form of another character?
   - YES: go to 5.
   - NO: INCLUDE the character. ✔️

5. Is the character used in another context as a non-simplified character?
   - YES: INCLUDE the character. ✔️
   - NO: EXCLUDE the character. ❎

[CJK Unified Ideographs block]:
  https://en.wikipedia.org/wiki/CJK_Unified_Ideographs_(Unicode_block)
[CJK Unified Ideographs Extension A block]:
  https://en.wikipedia.org/wiki/CJK_Unified_Ideographs_Extension_A
[康熙字典]: https://en.wikipedia.org/wiki/Kangxi_dictionary
