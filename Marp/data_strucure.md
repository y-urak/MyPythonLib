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
# data_structure.pyの忘備録

---
<!-- class: normal -->
<!-- footer: 2022 1/9 https://qiita.com/ell/items/fe52a9eb9499b7060ed6 -->
# 優先度付きキュー
最小値と最大値を簡単に出せるすごいやつ
追加した要素も勝手に並び替えてくれる

- 作り方 ```heaqp.heapify(List)``` 
    これを行うとlistの中身が木構造になっている
- 追加 ```heaqp.heaqqush(List, 要素)```
    List内では並び替えが行われて追加される
- 最小値の取り出し ```heaqp.heappop(List)```
- 最大値の取り出し(要素すべてに-1をかけて並び替え)
```
A=list(map(lambda x: x*(-1), A))  # 各要素を-1倍
heapq.heapify(A)
print(heapq.heappop(A)*(-1)) #最大値が最小値になる
```


---
<!-- class: normal -->
<!-- footer: 2022 1/8 -->
# 累積和
- 累積して足し合わせるための配列を用意する
- 順に配列を見ていき条件に適した値と一つ前の累積和を足し合わせて今の累積和を作成していく
```
A = [3,1,4,1,5,9,2,6] 
N=len(A)

T = [0] * N
# 初期値を定める (T[0] は 0 に設定済み)
# 確定で決まる部分は値を入れる
T[1] = A[1]

# 順に計算していく -> 今回は二パターンのやつで小さい方を入れる
for i in range(2, N):
    T[i] = min(T[i-1] + A[i], T[i-2] + A[i] * 2)
print(T[-1])
```
---
## 参考
https://nashidos.hatenablog.com/entry/2020/01/04/234842

---
# 再帰関数の呼び出し制限
- dfs,bfsでつかう再帰関数で適用させておく
- 計算数を気にする場合には書いとくべき
```
import sys
sys.setrecursionlimit(10**7) 
```
---
## DFS(深さ探索)
- 先に深くまで探索する
- 再帰関数なので先に終了条件を書いて処理
- 探索済みに書き込み
```
def dfs(x,y):
    #前提条件→範囲外
    if  not(0 <= y < h) or not(0 <= x < w):
        print("YES")
        sys.exit()
    #前提条件→範囲内
    if m[y][x] == "#": 
        return
    m[y][x]="#"
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
```

---
#### BFS(幅優先探索)
- 先に浅瀬を探索する
- queueを使って浅瀬から順に見ていくことができる
```
from collections import deque
def bfs(x,y):
    queue = deque([[x,y]])
    while queue:
        xx,yy = queue.popleft()
        #前提条件
        if  not(0 <= yy < h) or not(0 <= xx < w):
            print("YES")
            sys.exit()
        #次の場所へ
        if not(m[yy][xx] == "#"): 
            m[yy][xx]="#"
            queue.append([xx+1,yy])
            queue.append([xx,yy+1])
            queue.append([xx-1,yy])
            queue.append([xx,yy-1])
        
```

---
## 参考

1. https://nashidos.hatenablog.com/entry/2020/01/04/234842
    dfs -> 最初のdfs->*dfs(x+1,y)->[**(x+1,y)->[***(x+1,y)...],**(x-1,y),**(x,y+1),**(x,y-1)],*dfs(x-1,y),*dfs(x,y+1),*dfs(x,y-1)
2. https://qiita.com/takayg1/items/05d33193fbd7f2fc9256
    bfs -> 最初のbfs->*dfs(x+1,y),*dfs(x,y+1),*dfs(x-1,y),*dfs(x,y-1) -> **dfs()....
3. https://paiza.jp/student/challenges/482/retry