import itertools
#別のPCテスト
##1 順列の例
def permutation(list):
    for p in itertools.permutations(list):
        for a in p:
            print(a)
        print("next")
    

#range(n)->[0,.......,n-1]
if __name__ =='__main__':
    permutation(range(4))

#1 https://algo-logic.info/permutation/#toc_id_2_2
# https://atcoder.jp/contests/abc232/editorial/3143
# 重複しない条件で確認する場合→チェックした配列の値を変えておくのが割と楽
# https://atcoder.jp/contests/abc065/submissions/28104912