#つくった関数などの情報まとめ
import string_lib as slib

def solv1(INPUT):
    strs = INPUT
    print(int(strs[0])*int(strs[2]))

def solv2(INPUT):
    strs=INPUT
    flag=False
    for i in range(26):
        test=""
        for c in strs[0]:
            #変化量が0~26になるようにする->%
            #基準が'a'であることに注意
            test+=chr((ord(c)-ord('a')+i)%26+ord('a'))
            if test==strs[1]:
                flag=True
                break
        #if flag:
        #	break
    if flag:
        print('Yes') 
    else:
        print('No')   

def solv3(INPUT):
    pass


if __name__ =='__main__':
    #solv1("3*3")
    #slib.changeCharToAscii('a')
    solv2(["atcoder","atcoder"])    

#入力　二列それぞれにinput()入れる,改行そのままだとlistになる？
#入力参考 https://qiita.com/zenrshon/items/c4f3849552348b3dbe67
