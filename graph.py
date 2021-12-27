#1 二次配列に情報を格納しておくのがポイント
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







#1 https://algo-method.com/tasks/411/editorial
# https://algo-method.com/lecture_groups/19