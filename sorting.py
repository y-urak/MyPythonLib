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
def merge_sort(sort_list,start_i,end_i):
    #配列の大きさが2以上で比較と結合した配列を渡すことができる
    if start_i+1<end_i:
        m = int((start_i + end_i)/2)
        #半分に分ける
        merge_sort(sort_list,start_i,m)
        merge_sort(sort_list,m,end_i)
        print("merge: ",start_i,m,end_i)
        #merge ->配列の要素同士の比較とリスト化
        sort_list[start_i:end_i]=merge(sort_list[start_i:m],sort_list[m:end_i])
        print(sort_list)

def merge(list_a,list_b):
    a_i=0
    b_i=0
    merged_list=[]
    for i in range(len(list_a)+len(list_b)):
        if not (a_i<len(list_a)):
            merged_list.append(list_b[b_i])
            b_i+=1
        elif not (b_i<len(list_b)):
            merged_list.append(list_a[a_i])
            a_i+=1
        elif list_a[a_i]>list_b[b_i]:
            merged_list.append(list_b[b_i])
            b_i+=1
        elif not(list_a[a_i]>list_b[b_i]):
            merged_list.append(list_a[a_i])
            a_i+=1
    return merged_list


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
    merge_sort(sort_list,0,len(sort_list))

#1 https://algo-logic.info/permutation/#toc_id_2_2
# https://atcoder.jp/contests/abc232/editorial/3143
# 重複しない条件で確認する場合→チェックした配列の値を変えておくのが割と楽
# https://atcoder.jp/contests/abc065/submissions/28104912