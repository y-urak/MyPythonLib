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
# loop.pyの忘備録

---
<!-- class: normal -->
# for文で逆から参照する(1)
#### range()を用いた書き方
1. 逆に参照する → **第三引数を-1にする**
2. 配列の範囲 → 第一、第二引数 

```
for i in range(len(l)-1,-1,-1):
    print(l[i])
```
- 配列の長さから０までの整数値を順番に出力して元の配列の引数に利用する
- 第二引数は **-1**であることに注意
→生成したい値-1

<!-- footer: 2022 1/8 -->

---
# for文で逆から参照する(2)
#### リストを用いた書き方
1. スライス構文の三番目に **-1**を入れる
2. 全範囲の場合は特に値を入れる必要はないが範囲指定をしたい場合には一番目と二番目を利用する
```
for ll in l[::-1]:
    print(ll)
```
- lのリストを逆順で値を見ていく
- ちなみにメソッド```eg : l.reverse()```を使うことで逆順のリストを得ることができるが元のオブジェクトを破壊してしまう
---
## まとめ
- 第三引数がいい味出してる
- 範囲指定に注意
<br />

## 参考
1. https://www.python.ambitious-engineer.com/archives/1757
2. https://kuma-server.com/python-for-reversed/

---
# Loopの抜け方について ***return***
- いつも利用するやつで関数の処理が終わった後に変数を返すこともできる
- 関数が実行し終わった後も処理が続く
```
def exitLoop(l):
    for i in l:
        if i == 3:
            print("found")
            exit()
```

---
# Loopの抜け方について ***exit()***
- プログラムの処理を終了する
- 競プロ用でループ時に欲しい値が見つかった時に利用したりする
```
def exitLoop(l):
    for i in l:
        if i == 3:
            print("found")
            exit()
```
---
## まとめ
- exit()の紹介
- 途中でプログラムを終了できる

<br />

## 参考
1. https://www.sejuku.net/blog/24331