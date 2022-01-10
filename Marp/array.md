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
# array.pyの忘備録

---
<!-- class: normal -->
# 配列の初期化
#### 一次配列
- [初期化したい要素] * 要素数
```
n = 10
z = [True]*n
```
#### 二次配列
- n*n行列をつくる
- [一次配列(横) for _ in range(n)] → in range(n)が縦
```
a = [[False] * n for _ in range(n)]
```

<!-- footer: 2022 1/8 -->
---
## TIPS
- _ は要素を利用しない時に使われる書き方
- 他人のコードを読むときに必要な知識

https://blog.pyq.jp/entry/Python_kaiketsu_180420

---
# 辞書型配列
文字列を引数として利用できる配列
##### 引数と中身の代入(1): ```dict={"apple":0}```
##### 引数と中身の代入(2): ```dict["banana"]=1```
##### 中身の取得: ```dict["apple"]         #0を返す```
##### 引数の文字列一覧: ```dict.keys()```
##### すべての中身表示
```
for key in dict.keys():
    print(key,dict[key])
```
---
## 参考
1. https://memoribuka-lab.com/?p=2203
---

# Counter
重複をカウントしてまとめてくれる
- ex ```l='aaabb' → Counter(l) → {'a': 3, 'b': 2}```
- 使う : ```from collections import Counter```
- 新しい要素、今ある要素の追加 : ```cnter["c"] += 1``` 
- すべての要素数のカウント : ```total=sum(cnter.values()) ```
- 圧縮(カウントなし)``` list({'a': 3, 'b': 2})->{a,b}```
- 最初から ***カウント必要ない人***は```set("bbbaaaa")```
#### 参考
https://memoribuka-lab.com/?p=2203

---
# pop()
- listであればi番目の要素を取り出すことができる
- 取り出された要素はlistからなくなる点に注意
- ```[0,1,2,3,4].pop(0) #0が取り出される```

## 参考
https://note.nkmk.me/python-list-clear-pop-remove-del/

---
# *演算子
- iterable unpacking operator
- listなどまとめられているものを分解する

example
```
print(type(range(4)),range(4),*range(4))
print(*"iterable")
print(*[1,2,3,10],*(11,12,13))
```
output
```
<class 'range'> range(0, 4) 0 1 2 3
i t e r a b l e
1 2 3 10 11 12 13
```
---
## 参考
https://qiita.com/eumesy/items/dda85b70d28da61663cb

---
## 配列の反転
ex 配列:list
- もとある配列を壊してしまうことに注意
- ```list.reverse()```
## 配列の並び替え
- 返り値で返す : ```sorted(list)```
- 今ある配列の並び替え : ```list.sort()```
#### 参考
反転 https://note.nkmk.me/python-reverse-reversed/
並び替え https://www.javadrive.jp/python/list/index7.html

---
# 配列内に一つの要素を挿入する
置き換えではなく挿入であることに注意
<br />
ex 配列:list
- listのi番目にxを挿入する 
- ```list.insert(i,x)```

#### 参考
https://www.javadrive.jp/python/list/index7.html
