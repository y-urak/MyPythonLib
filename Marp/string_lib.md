---
marp: true
size: 4:3
style: |
  section.normal {
    justify-content: normal;
    background-color: #F5F0F6;
    color:#2B4162;
  }
  section.lead {
    justify-content: center;
    text-align: center;
  }
---
<!-- class: lead -->
<!-- paginate: true -->
# string_lib.pyの忘備録

---
<!-- class: normal -->
# asciiコード変換 
- コンピュータは文字も数字で表している
- asciiコードは文字と数字の対応表
#### char→int
```
# cが文字
i=ord(c)
```
#### int→char
```
# iは整数値
c=chr(i)
```

<!-- footer: 2022 1/8 -->
---
## 参考
1. https://qiita.com/ell/items/6eb48e934a147898d823

---
# 文字長が決まっている文字列のパディング
#### zfill()
```
"223".zfill(8)
#22300000
```
#### format()
```
print(format(4,"06"))
#000004
print(format(4,"06f"))
#4.000000
```
---
## 参考
1. https://it-engineer-info.com/language/python/5664/
2. https://itips.krsw.biz/python-how-to-do-zero-padding/

---
# 文字列の部分一致
- めっちゃ簡単に部分一致できる
- 調べたい文字列 in 元の文字列
```
s="abcdddxxxd"
print('cdd' in s,'dxx' in s,'aci' in s)
```
## 参考
1. https://note.nkmk.me/python-str-compare/#:~:text=source%3A%20str_compare.py-,%E9%83%A8%E5%88%86%E4%B8%80%E8%87%B4%3A%20in%2C%20not%20in,%E3%81%A8%20False%20%E3%81%8C%E8%BF%94%E3%81%95%E3%82%8C%E3%82%8B%E3%80%82

---
# 文字列の繰り返し

```
n=3
s="strings"
print(s*n)
```


---
# 文字列の一部変更
- 文字列の参照はできる
- 文字列の一部を書き換えたりはできない eg. s[1]='a'
- 文字列の結合を使って書き換える
```
start=3
s="abbbbbs"
subs="ooo"
s[0:start]+ subs + s[start+len(subs):len(s)]
```
後で結合する文字列の始まりを挿入したい文字列分ずらす
#### 参考
https://minus9d.hatenablog.com/entry/20130528/1369745960

