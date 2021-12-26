##1 逆順に見ていくループ
def inverseLoop(l):
    #range
    for i in range(len(l)-1,-1,-1):
        print(l[i])
    #リスト
    for ll in l[::-1]:
        print(ll)



if __name__ == '__main__':
    inverseLoop([0,1,2,3,4,5])


#1 https://www.python.ambitious-engineer.com/archives/1757