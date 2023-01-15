# Changelog


## [Unreleased]

- Added stroke data for U+21014 𡀔, U+21145 𡅅
  (see <<https://jyutping.org/blog/particles/>>)
- Added stroke data for some mouth-beside characters
  in CJK Unified Ideographs Extension B
  (𠼦𠼻𠽟𠾐𠾶𡂴𡂿𡃏)
- Added phrase 指擬


## [v1.19.0] 落街插蘇 (2022-12-23)

- Added phrase 落街
- Added phrase 插蘇


## [v1.18.0] 軟熟 (2022-11-20)

- Added phrase 器重
- Added phrase 鬥木
- Added phrase 軟熟


## [v1.17.0] 乾透 (2022-10-30)

- Added phrases 大佬, 大堂, 大會, 大禍, 大蒜, 大難
- Added phrases 乾透, 俐落
- Added phrases 凡塵, 凡間
- Added phrase 幹道


## [v1.16.0] 打喊露 (2022-09-23)

- Added phrases 喊露, 打喊露
- Added phrases 七七八八, 七彩
- Added phrases 九十後, 九重
- Added phrase 了結
- Added phrases 二進制, 十進制, 進制
- Added phrases 人事部, 人名, 人均
- Added phrase 兒科
- Added phrases 入伙, 入住, 入味, etc.
- Added phrases 刁蠻, 力度, 叉腰
- Added phrase 幾點


## [v1.15.0] God save the King (2022-09-11)

- Added phrase 英皇壽辰
- Added phrase 保重


## [v1.14.0] 早前騙案 (2022-09-04)

- Raised ranking of 機
- Added phrases 早前, 騙案, 對路
- Added phrases 一旦, 一早, 一時, 一條, 一條龍, 一概, 一概而論, 一模一樣, 一貫, 一連, 一點
- Added phrases 一年 etc., 一日 etc., 一月 etc., 一號 etc.


## [v1.13.1] 莉 fix (2022-08-02)

- Fixed stroke sequence for U+8389 莉 incorrectly that of U+8388 莈


## [v1.13.0] 秋葵起樓 (2022-07-31)

- Fixed inconsistent leniency for 3rd stroke of 亦-above
- Fixed missing leniency for last stroke of U+4F5F 佟
- Fixed missing 衮袞-leniency in U+78D9 磙, U+3665 㙥
- Fixed missing 青靑-leniency in U+775B 睛
- Fixed missing 黄黃-leniency in U+9ECB 黋
- Added phrases 起屋, 起樓, 秋葵


## [v1.12.0] 扵拜 leniencies (2022-07-16)

- Allowed 4th stroke ㇑ for stroke sequence of U+62DC 拜
- Allowed left 才 (123) for stroke sequence of U+6275 扵
- Added phrase 掌上壓
- Added phrase 悉數


## [v1.11.0] 債主清盤 (2022-07-02)

- Added phrases 債主, 清盤


## [v1.10.0] 屋企直程 (2022-06-10)

- Added phrases 屋企, 屋企人
- Added phrases 直程, 直頭
- Added phrases 流感針, 豬流感
- Added phrases 折腰, 緊絀


## [v1.9.0] 好在好彩 (2022-05-21)

- Added phrases 好在, 好彩


## [v1.8.0] 暢順彈牙 (2022-05-16)

- Added phrase 暢順
- Added phrase 彈牙
- Added phrase 避彈衣


## [v1.7.0] 較為爆煲 (2022-04-23)

- Added phrase 較為
- Added phrase 爆煲


## [v1.6.0] 奇難雜症 (2022-03-26)

- Added phrase 奇難雜症
- Added phrase 床下底
- Added phrase 放工
- Added phrases 擺低, 放低, 漏低


## [v1.5.0] 樹熊侍應 (2022-02-26)

- Added phrases 侍應, 樹熊


## [v1.4.1] Meat-beside fixes (2022-02-05)

- Fixed incorrect stroke sequences for meat-beside in `U+8192 膒` to `U+819F 膟`,
  specifically 膒膓膔膕膖膗膘膙膛膜膝膞膟


## [v1.4.0] 安裝功架 (2022-01-31)

- Added phrases 功架, 安裝
- Improved README content listing structure
- Fixed `codepoint-character-sequence.txt` stroke sequence regex comment


## [v1.3.0] Some dialectal terms (2022-01-21)

- Added stroke data for some dialectal Extension B characters
- Added a few phrases for some dialectal Extension B characters
- Fixed `test_sort.py` sorting key name


## [v1.2.1] Small clarifications (2022-01-16)

- Clarify readme parsing of `codepoint-character-sequence.txt`
- Fixed changelog v1.2.0 heading missing date


## [v1.2.0] Non-BMP characters in Tongyong Guifan Hanzi Biao (2022-01-16)

- Added stroke data for non-BMP characters in [通用规范汉字表] (2013),
  or "Table of General Standard Chinese Characters"
  (see [tygfhzb.pdf])
- Fixed missing 防 in rankings
- Fixed missing 嘢 in traditional ranking

[通用规范汉字表]:
  https://en.wikipedia.org/wiki/Table_of_General_Standard_Chinese_Characters
[tygfhzb.pdf]:
  https://www.gov.cn/gzdt/att/att/site1/20130819/tygfhzb.pdf


## [v1.1.0] Professor Panda says... (2022-01-15)

- Added phrases missed from 成語動畫廊
- Added phrases 麥兜, 菠蘿油
- Added phrases 三七二十一, 下一個, 日日, 燶咗
- Added some HK place names
- Allowed variant 鷄 for 雞 in traditional phrases


## [v1.0.1] URL fixes (2022-01-10)

- Fixed diff/unreleased URLs in changelog


## [v1.0.0] First stable (2022-01-10)

- Stroke data and phrase data are now complete.


[Unreleased]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.19.0...HEAD
[v1.19.0]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.18.0...v1.19.0
[v1.18.0]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.17.0...v1.18.0
[v1.17.0]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.16.0...v1.17.0
[v1.16.0]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.15.0...v1.16.0
[v1.15.0]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.14.0...v1.15.0
[v1.14.0]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.13.1...v1.14.0
[v1.13.1]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.13.0...v1.13.1
[v1.13.0]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.12.0...v1.13.0
[v1.12.0]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.11.0...v1.12.0
[v1.11.0]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.10.0...v1.11.0
[v1.10.0]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.9.0...v1.10.0
[v1.9.0]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.8.0...v1.9.0
[v1.8.0]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.7.0...v1.8.0
[v1.7.0]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.6.0...v1.7.0
[v1.6.0]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.5.0...v1.6.0
[v1.5.0]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.4.1...v1.5.0
[v1.4.1]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.4.0...v1.4.1
[v1.4.0]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.3.0...v1.4.0
[v1.3.0]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.2.1...v1.3.0
[v1.2.1]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.2.0...v1.2.1
[v1.2.0]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.1.0...v1.2.0
[v1.1.0]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.0.1...v1.1.0
[v1.0.1]:
  https://github.com/stroke-input/stroke-input-data/compare/v1.0.0...v1.0.1
[v1.0.0]:
  https://github.com/stroke-input/stroke-input-data/releases/tag/v1.0.0
