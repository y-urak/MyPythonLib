n=5

#1 _ は使わない変数として定義されることが多い
##一次配列
z = [True]*n
print(z)

##二次配列
zz = [[True]*n]
a = [[False] * n for _ in range(n)]
b = [[False] * n for _ in range(n)]
print(zz,a)

##2 辞書型配列
dict={"apple":0}
print(dict["apple"])
dict_key="banana"
# 新しく辞書の追加
if dict_key not in dict.keys():
    dict[dict_key]=1
# 辞書一覧の表示
for key in dict.keys():
    print(key,dict[key])

##3 重複を許さずにカウントしてくれる関数Counter
from collections import Counter
# リストの作成
alist =['a']*3
blist =['b']*2
ablist=alist+blist
# 順番にならべてカウントする
cnter = Counter(ablist)
# もしcがあればcのカウントをプラス1する、そうでなければ新しく項目を作ってプラス1
cnter["c"] += 1 

##4 sum -> リストやタプルの合計
totalab=sum(cnter.values())
print(ablist,cnter,"->",totalab)
# カウントした数字がいらない人向け
print(list(cnter),set(ablist),list(set(ablist)))

##5 pop ->　pop連続して使う場合に注意
print(ablist.pop(0),ablist.pop(0),ablist)

##6 *演算子(iterable unpacking operator) -> 表示するものをまとめたものを小分けにする
print(type(range(4)),range(4),*range(4))
print(*"iterable")
print(*[1,2,3,10],*(11,12,13))

#--------------------------------------------------------------------
#1 https://blog.pyq.jp/entry/Python_kaiketsu_180420

#2 https://www.sejuku.net/blog/24122
#2 https://www.w3schools.com/python/python_dictionaries.asp

#3 https://memoribuka-lab.com/?p=2203

#4 https://flytech.work/blog/21452/#sum-2

#5 https://note.nkmk.me/python-list-clear-pop-remove-del/

#6 https://qiita.com/eumesy/items/dda85b70d28da61663cb

# https://atcoder.jp/contests/abc232/editorial/3143