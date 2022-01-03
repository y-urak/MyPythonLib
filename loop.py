##1 逆順に見ていくループ
def inverseLoop(l):
    #range
    for i in range(len(l)-1,-1,-1):
        print(l[i])
    #リスト
    for ll in l[::-1]:
        print(ll)

##2 loop内である値が見つかった時に終了->これ以降実行しない
# 競プロ用
def exitLoop(l):
    for i in l:
        if i == 3:
            print("found")
            exit()
# returnの場合はその後の関数も実行してくれる
def returnLoop(l):
    for i in l:
        if i == 3:
            print("ffound")
            return

if __name__ == '__main__':
    inverseLoop([0,1,2,3,4,5])
    print("")
    returnLoop([1,2,3,4])
    exitLoop([1,2,3,4,4,4])
    returnLoop([1,2,3,4])




#1 https://www.python.ambitious-engineer.com/archives/1757
#2 https://www.sejuku.net/blog/24331