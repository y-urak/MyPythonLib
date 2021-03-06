##10 defaultdict
from collections import defaultdict
s = 'mississippi'
# mのdict内で返す形の指定？
# defaultdict(int) -> intを返す
# defaultdict(list) -> listを返す
ddi = defaultdict(int)
ddl = defaultdict(list)
#print(d.default_factory)
iter_int=0
for k in s:
    ddi[k] += 1
    ddl[k].append(iter_int)
    iter_int+=1
#print(d.items(),d)
print("int",ddi)
print("list",ddl)
#該当しない内容の場合 int -> 0回出てきた, list -> 要素のないリストを返す
print(ddi['a'],ddl['a'])

n=5

##1 _ は使わない変数として定義されることが多い
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

##7 reverse、配列の反転
rev=[0]*2+[3]*5
#今ある配列の反転であることに注意
rev.reverse()
##8 ついでに並び替え→sortedは返す
print(sorted(rev),rev)
#今ある配列の反転...
rev.sort()
print(rev,rev.sort())


##9 insert 好きなところに好きなものを入れれる,置き換えではない
rev.insert(5,-1)
rev.insert(2,-1)
print(rev)

#--------------------------------------------------------------------
#1 https://blog.pyq.jp/entry/Python_kaiketsu_180420

#2 https://www.sejuku.net/blog/24122
#2 https://www.w3schools.com/python/python_dictionaries.asp

#3 https://memoribuka-lab.com/?p=2203

#4 https://flytech.work/blog/21452/#sum-2

#5 https://note.nkmk.me/python-list-clear-pop-remove-del/

#6 https://qiita.com/eumesy/items/dda85b70d28da61663cb

#7 https://note.nkmk.me/python-reverse-reversed/

#8 https://www.javadrive.jp/python/list/index7.html

#9 https://www.javadrive.jp/python/list/index7.html

#10 https://stackoverflow.com/questions/5900578/how-does-collections-defaultdict-work

# https://atcoder.jp/contests/abc232/editorial/3143