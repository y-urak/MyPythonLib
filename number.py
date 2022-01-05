#素数判定
def isPrime(n):
    #どこまでみるか→Nの平方根
    max=int(n**(1/2))
    #1とnでしか割り切れない→素数
    for i in range(2,max):
        if n%i==0:
            return False
    return True
#素数判定→応用例　約数checker
def check_divisor(n):
    # 素数チェックの応用
    max=int(n**(1/2))
    return_list=[]
    for i in range(1,max):
        if not(n%i==0): continue
        # 割り切れたものを追加
        return_list.append(i)
        #ex 21=3*7の時に7の値も一緒に追加する
        if not(i==int(n/i)):
            return_list.append(int(n/i))

    return return_list

print(isPrime(100))
print(check_divisor(100))

#ユークリッドの互除法->最大公約数を求めるのに用いられる方法
def GCD(a,b): #Greatest Common Divisor
    c = max(a,b)
    d = min(a,b)
    while True:
        if d==0:
            return c
        else:
            c=c%d
            tmp=d
            d=c
            c=tmp
    #a==0 or b==0 ->max(a,b)
    #if a>b: a=a%b
    #else: b=b%a でもいいと思った

print("GCD",GCD(24,40))
#三つの場合のGCDの出し方
print("GCD",GCD(GCD(24,40),60))

#期待値->値*確率の総和
def dice_exceptation(dice_list=[1,2,3,4,5,6]):
    probability=1/len(dice_list)
    ex = 0
    for dice in dice_list:
        ex+=dice*probability
    return ex
print(dice_exceptation())
#期待値の線形性->それぞれの試行の期待値の総和が答え
# 2個のサイコロの総和
##2 期待値について
print(dice_exceptation()+dice_exceptation())

import random
#モンテカルロ法->確率がわからないとき実際に試行を繰り返すことで実際の確率を推定することができる
def calc_PI(n=1000):
    cnt=0
    for i in range(n):
        x=random.random()
        y=random.random()
        if x*x + y*y <=1:
            cnt+=1
    return 4*cnt/n
print(calc_PI(100000))

#大きい値の作り方
num1=1e9
num2=(10**9)
##1
num3=float('inf')
print(num1)
print(num2)
print(num3)



#1 https://qiita.com/You-Tarin/items/eebdc39c6f8ffd2770f0
#2 https://mathwords.net/saikorokitaichi