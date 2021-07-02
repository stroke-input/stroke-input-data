# stroke-input-data/cns

ROC stroke data sets that I probably won't use,
but which are nevertheless useful for reference.


## Contents

### [`raw/`]

- Raw data sets obtained by:

  1. Navigating to <<https://data.gov.tw/dataset/5961>>
  2. Downloading `Open_Data.zip` and extracting it
  3. Copying the following to `cns/raw/`:
     - `Properties/CNS_strokes_sequence.txt`
     - `MapingTables/Unicode/*` [sic]
  4. Fixing the missing newline at the end of each file

### [`process.py`]

- Script used to generate `stroke-data-*.txt` from the raw data sets
- Licensed under [MIT-0]

### [`stroke-data-all.txt`]

- Tab-separated list of (character, stroke sequence) data,
  for characters in the raw data sets

### [`stroke-data-bmp.txt`]

- Tab-separated list of (character, stroke sequence) data,
  for characters in the raw data sets
  that lie in the Basic Multilingual Plane (BMP)

### [`stroke-data-triplets.txt`]

- Tab-separated list of (code point, character, stroke sequence) data,
  for all characters (with blanks for those missing in the raw data sets)

[`raw/`]: cns/raw
[`process.py`]: cns/process.py
[`stroke-data-all.txt`]: cns/stroke-data-all.txt
[`stroke-data-bmp.txt`]: cns/stroke-data-bmp.txt
[`stroke-data-triplets.txt`]: cns/stroke-data-triplets.txt
[MIT-0]: https://spdx.org/licenses/MIT-0


## Data licensing

1. All data sets in this directory (`cns/`) are licensed
   under the Open Government Data License, version 1.0,
   with the raw data sets being sourced from:

   國家發展委員會 (2015), CNS11643中文標準交換碼全字庫(簡稱全字庫) 110年3月30日更新. <br>
   <<https://data.gov.tw/dataset/5961>>

2. The "Open Data" is published under the Open Government Data License;
   "Users" can make use of it when complying with its terms.

3. The Open Government Data License can be viewed
   at <<https://data.gov.tw/license>>.
