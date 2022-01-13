# 3.7.1 
def solv1():
    li =[0]*10
    li[0]=1
    for i in range(1,10):
        li[i]=2*li[i-1]
    return li
print(solv1())

def solv2():
    li =[0]*10
    li[0]=1
    li[1]=1
    li[2]=1
    for i in range(3,10):
        li[i]=li[i-1]+li[i-2]+li[i-3]
    return li
print(solv2())

#3.7.2
# つながっている先の情報を足す
# スタートを1にする
def solv3():
    li=[[],[0],[0,1],[2],[3,1],[4,3]]
    ans=[0]*(len(li)+1)
    ans[0]=1
    for i in range(1,len(li)):
        ll = li[i]
        for j in ll:
            ans[i]+=ans[j]
        print(i,ans[i])
    print(ans[5])
solv3()

def solv4():
    n=6
    dp=[[-1]*n for _ in range(n)]
    dp[0][0]=1
    dp[2][2]=0
    dp[1][5]=0
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if dp[i][j]==-1:
                dp[i][j]=0
                if j-1>=0:
                    dp[i][j]+=dp[i][j-1]
                if i-1>=0:
                    dp[i][j]+=dp[i-1][j]
        print(dp[i])
solv4()

# https://github.com/E869120/math-algorithm-book/blob/main/editorial/chap3-7/chap3-7.pdf