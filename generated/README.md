# generated/

This directory contains data __generated automatically__
by the scripts in the root directory.


## Contents


### Text

#### [`characters-traditional.txt`], [`characters-simplified.txt`]

- Lists of traditional-only and simplified-only characters
- Automatically generated from `../make_txt.py`
- Released into the [public domain]

#### [`sequence-characters.txt`]

- Tab-separated (stroke sequence, characters) pairs
- Automatically generated from `../make_txt.py`
- Licensed under [CC-BY-4.0]


### Serial (ignored by Git)

#### `characters-traditional.ser`, `characters-simplified.ser`

- `Set<Integer>`: sets of integer code points
  for traditional-only and simplified-only characters
- Automatically generated from `../MakeSer.java`
- Released into the [public domain]

#### `common-traditional.ser`, `common-simplified.ser`

- `Set<Integer>`: sets of integer code points
  for commonly used traditional and simplified characters
- Automatically generated from `../MakeSer.java`
- Released into the [public domain]

#### `phrases-traditional.ser`, `phrases-simplified.ser`

- `Set<String>`: sets of traditional and simplified phrases
- Automatically generated from `../MakeSer.java`
- Released into the [public domain]

#### `ranking-traditional.ser`, `ranking-simplified.ser`

- `Map<Integer, Integer>`: maps from integer code point to integer rank
- Automatically generated from `../MakeSer.java`
- Released into the [public domain]

#### `sequence-characters.ser`

- `Map<String, String>`: map from stroke digit sequence to characters
- Automatically generated from `../MakeSer.java`
- Licensed under [CC-BY-4.0]

[`characters-traditional.txt`]: characters-traditional.txt
[`characters-simplified.txt`]: characters-simplified.txt
[`sequence-characters.txt`]: sequence-characters.txt
[CC-BY-4.0]: https://creativecommons.org/licenses/by/4.0/
[public domain]: https://creativecommons.org/publicdomain/zero/1.0/
