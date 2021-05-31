# stroke-input-data

Data sets for the [Stroke Input Method (筆畫輸入法)] in Chinese.

(For when I get around to writing a Stroke Input Method app some day.)


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
[dumbphone]: dumbphone-stroke-input.jpg


## Stuff in the `yawnoc/` directory

A set of (code point, character, stroke sequence) triplets (tab-separated),
manually compiled by @yawnoc with strokes according to his liking,
and released into the [Public Domain]:

- [`yawnoc/codepoint-character-sequence.txt`]: for yawnoc-relevant characters

[Public Domain]: https://creativecommons.org/publicdomain/zero/1.0/
[`yawnoc/codepoint-character-sequence.txt`]:
  yawnoc/codepoint-character-sequence.txt


### How are strokes classified?

According to [康熙字典]. Notable examples:

- `U+4E0E` 与 has 4 strokes (consistent with the upper-middle component of 與).
- `U+4ECA` 今 has 3rd stroke horizontal.
- `U+53CD` 反 has 1st stroke horizontal.
- `U+58EC` 壬 has 1st stroke horizontal.

Exceptions where lenient classification has been applied:

- `U+4E30` 丰 has 1st stroke either horizontal or left-slash.
- `U+4E31` 丱 has 2nd stroke either left-slash or vertical.


### What is a yawnoc-relevant character?

Very poorly defined:

1. Does the character belong to either
   the [CJK Unified Ideographs block] (`U+4E00` to `U+9FFC`)
   or the [CJK Unified Ideographs Extension A block] (`U+3400` to `U+4DBF`)?
   - YES: go to 2.
   - NO: the character is NOT a yawnoc-relevant character. ❎

2. Does the character appear in [康熙字典]?
   - YES: the character is a yawnoc-relevant character. ✔️
   - NO: go to 3.

3. Is the character a Japanese 国字 (kokuji), a Korean 國字 (gukja),
   or a Vietnamese 字喃 (chữ Nôm) that has no usage in Chinese?
   - YES: the character is NOT a yawnoc-relevant character. ❎
   - NO: go to 4.

4. Is the character a variant or ancient form of another character?
   - YES: the character is a yawnoc-relevant character. ✔️
   - NO: go to 5.

5. Is the character the simplified form of another character?
   - YES: go to 6.
   - NO: the character is a yawnoc-relevant character. ✔️

6. Is the character used in another context as a non-simplified character?
   - YES: the character is a yawnoc-relevant character. ✔️
   - NO: the character is NOT a yawnoc-relevant character. ❎

[CJK Unified Ideographs block]:
  https://en.wikipedia.org/wiki/CJK_Unified_Ideographs_(Unicode_block)
[CJK Unified Ideographs Extension A block]:
  https://en.wikipedia.org/wiki/CJK_Unified_Ideographs_Extension_A
[康熙字典]: https://en.wikipedia.org/wiki/Kangxi_dictionary


## Stuff in the `cns/` directory


### Processed data sets

The processed data sets are obtained from the raw ones
by running the Python script `./cns/process.py`.

First we have (character, stroke sequence) pairs (tab-separated),
sorted by stroke sequence:

- [`cns/stroke-data-all.txt`]: for all characters
- [`cns/stroke-data-bmp.txt`]: for the Basic Multilingual Plane (BMP)

Then we have (code point, character, stroke sequence) triplets (tab-separated),
even including characters missing in the raw data sets:

- [`cns/stroke-data-triplets.txt`]

[`cns/stroke-data-all.txt`]: cns/stroke-data-all.txt
[`cns/stroke-data-bmp.txt`]: cns/stroke-data-bmp.txt
[`cns/stroke-data-triplets.txt`]: cns/stroke-data-triplets.txt


### Raw data sets

The raw data sets were obtained by:

1. Navigating to <<https://data.gov.tw/dataset/5961>>
2. Downloading `Open_Data.zip` and extracting it
3. Copying the following to `cns/raw/`:
   - `Properties/CNS_strokes_sequence.txt`: (CNS code, stroke sequence) pairs
   - `MapingTables/Unicode/*` [sic]: (CNS code, unicode) pairs
4. Fixing the missing newline at the end of each file


### Data licensing

1. The data sets (both raw and processed) in `cns/` are licensed
   under the Open Government Data License, version 1.0,
   with the raw data sets being sourced from:

   國家發展委員會 (2015), CNS11643中文標準交換碼全字庫(簡稱全字庫) 110年3月30日更新. <br>
   <<https://data.gov.tw/dataset/5961>>

2. The "Open Data" is published under the Open Government Data License;
   "Users" can make use of it when complying with its terms.

3. The Open Government Data License can be viewed
   at <<https://data.gov.tw/license>>.
