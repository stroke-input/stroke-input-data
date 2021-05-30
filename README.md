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


## Stuff in the `cns/` directory


### Processed data sets

The processed data sets are obtained from the raw ones
by running the Python script `./cns/process.py`.

First we have (character, stroke sequence) pairs (tab-separated),
sorted by stroke sequence:

- [`cns/stroke-data-all.txt`]: for all characters
- [`cns/stroke-data-bmp.txt`]: for the Basic Multilingual Plane (BMP)

Then we have (code point, character, stroke sequence) triplets (tab-separated),
sorted by code point, even including characters missing in the raw data sets:

- [`cns/stroke-data-triplets.txt`]: U+4E00 to U+9FFF

[`cns/stroke-data-all.txt`]: cns/stroke-data-all.txt
[`cns/stroke-data-bmp.txt`]: cns/stroke-data-bmp.txt


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
