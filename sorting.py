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

# [1,2,3,4,5]
def select_sort(sorting_list):
    for i in range(len(sorting_list)):
        for j in range(i,len(sorting_list)):
            if sorting_list[i]>sorting_list[j]:
                tmp=sorting_list[i]
                sorting_list[i]=sorting_list[j]
                sorting_list[j]=tmp
    return sorting_list
#TODO
def merge_sort(start_i,end_i):
    global sort_list
    if end_i==start_i:
        return 
    merge_sort()
    

#range(n)->[0,.......,n-1]
if __name__ =='__main__':
    permutation(range(4))
    #4!
    print(permutation_num(4))
    #4P2
    print(permutation_num(4)/permutation_num(2))
    #4C2 ->n/r*n-r
    print(permutation_num(4)/permutation_num(2)/permutation_num(2))
    
    print([4,3,2,44,1],select_sort([4,3,2,44,1]))

    sort_list=[6,2,66,9,0,3,8,11]

#1 https://algo-logic.info/permutation/#toc_id_2_2
# https://atcoder.jp/contests/abc232/editorial/3143
# 重複しない条件で確認する場合→チェックした配列の値を変えておくのが割と楽
# https://atcoder.jp/contests/abc065/submissions/28104912