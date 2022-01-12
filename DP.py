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

# https://github.com/E869120/math-algorithm-book/blob/main/editorial/chap3-7/chap3-7.pdf