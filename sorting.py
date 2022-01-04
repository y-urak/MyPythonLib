import itertools
#別のPCテスト
##1 順列の中身
def permutation(list):
    sum=0
    #中身の出力
    output_list=[]
    for p in itertools.permutations(list):
        #中身の出力
        print(p)
        output_list.append(p)
        #for a in p:
        #    output_list.append(a)
        sum+=1
    print(sum)

#1 順列の総数
def permutation_num(n):
    retval=1
    for i in range(1,n+1):
        retval*=i
    return retval

    

#range(n)->[0,.......,n-1]
if __name__ =='__main__':
    permutation(range(4))
    #4!
    print(permutation_num(4))
    #4P2
    print(permutation_num(4)/permutation_num(2))
    #4C2 ->n/r*n-r
    print(permutation_num(4)/permutation_num(2)/permutation_num(2))


#1 https://algo-logic.info/permutation/#toc_id_2_2
# https://atcoder.jp/contests/abc232/editorial/3143
# 重複しない条件で確認する場合→チェックした配列の値を変えておくのが割と楽
# https://atcoder.jp/contests/abc065/submissions/28104912