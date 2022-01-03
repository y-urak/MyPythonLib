## 1 二次配列に情報を格納しておくのがポイント
#[] -> [[]] ->[[],[]] 横に入れていくパターン
#文字列であれば一次配列に入れておけば参照は楽 A=["abb","bba"] -> A[0][1]="b"
def no1(N,A,B,s):
    # 入力
    N, A ,B = map(int, input().split())
    G = []
    for i in range(N):
        s=input()
        l=[]
        for c in s:
            if c=='x':
                l.append(False)
            else:
                l.append(True)
        G.append(l)
    #print(G)
    if G[A][B]:
        print("Yes")
    else:
        print("No")

#予め用意しておくversion
def no2():
    N, M = map(int, input().split())
    #二次行列の空白行列の作り方
    G = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        # appendで追加する→順不同にlistに追加
        G[A].append(B)

    for i in range(N):
        ans=""
        #並べるためのソート
        G[i].sort()
        for xx in range(N):
            if ans=="":
                ans+=str(xx)
            else:
                ans+=" "+str(xx)
        print(ans)


#1 https://algo-method.com/tasks/411/editorial
# https://algo-method.com/lecture_groups/19

## 2 根→葉　→葉のスタートから根にもどるのは簡単　=> 深さは割と簡単に出せる
def depthcalc(x,a_list):
    #0番目がないので作っておく（大事）->0が根
    a_list.insert(0,1)
    depth=0
    while True:
        if x==0:
            break
        x=a_list[x]
        depth+=1
    return depth
