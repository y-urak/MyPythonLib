
import sys
# 再帰関数の呼び出し制限 -> 計算数を気にする場合には書いとくべき
sys.setrecursionlimit(10**7) 
h,w = map(int,input().split())
#個別
m = [list(input()) for _ in range(h)]
#一括 -> stringだと気軽に文字列をいじれない
#m = list(input() for _ in range(h))
s=[]
for y in range(h):
    for x in range(w):
        if m[y][x]=="S":
            s.append(x)
            s.append(y)
            break
    if len(s)>0:
        break
print(s)

##1 DFS -> 深さ探索
def dfs(x,y):
    #print(x,y,m[y][x])
    #前提条件→範囲外
    #if y<0 or y>=h or x<0 or x>=w :
    if  not(0 <= y < h) or not(0 <= x < w):
        print("YES")
        sys.exit()
    #前提条件→範囲内
    if m[y][x] == "#": 
        return
    m[y][x]="#"
    #次の場所へ
    dfs(x+1,y)
    dfs(x-1,y)
    dfs(x,y+1)
    dfs(x,y-1)
    
#dfs(*s)
print("NO")

##2 BFS -> 幅優先探索
from collections import deque
def bfs(x,y):
    queue = deque([[x,y]])
    while queue:
        xx,yy = queue.popleft()
        print(xx,yy)
        #前提条件
        if  not(0 <= yy < h) or not(0 <= xx < w):
            print("YES")
            sys.exit()
        #次の場所へ
        if not(m[yy][xx] == "#"): 
            m[yy][xx]="#"
            #1
            queue.append([xx+1,yy])
            #2
            queue.append([xx,yy+1])
            #3
            queue.append([xx-1,yy])
            queue.append([xx,yy-1])
        
bfs(*s)
print("NO")

#1 https://nashidos.hatenablog.com/entry/2020/01/04/234842
#dfs -> 最初のdfs->*dfs(x+1,y)->[**(x+1,y)->[***(x+1,y)...],**(x-1,y),**(x,y+1),**(x,y-1)],*dfs(x-1,y),*dfs(x,y+1),*dfs(x,y-1)

#2 https://qiita.com/takayg1/items/05d33193fbd7f2fc9256
#bfs -> 最初のbfs->*dfs(x+1,y),*dfs(x,y+1),*dfs(x-1,y),*dfs(x,y-1) -> **dfs()....

#入力-> https://paiza.jp/student/challenges/482/retry