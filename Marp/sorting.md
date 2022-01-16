---
marp: true
size: 4:3
style: |
  section.normal {
    justify-content: normal;
    background-color: #F5F0F6;
    color:#2B4162;
  }
  section.lead {
    justify-content: center;
    text-align: center;
  }
---
<!-- class: lead -->
<!-- paginate: true -->
# sorting.pyの忘備録

---
<!-- class: normal -->
# 順列について
- 順列とはn個のものを一列に並びかえること
- n! = n * n-1 * n-2 * ..... * 1
- 順列の組み合わせすべてを簡単に表示することが可能
```
import itertools
for p in itertools.permutations(list):
        #中身の出力
        print(p)
```

---
# Select Sort
- 前から順に並び替えていくsort
- 一番簡単に実装できる
- 二重ループを用いることで簡単に実装できるか計算量が大きめ


---
# Merge Sort
- Merge操作を用いたsort
    - Merge操作：二つのリストの要素を前から見て小さい方を新しいリストに追加していき並び替えた一つのリストを出力する
- Merge Sortでは始めと中央の値のリスト(1)と中央と最後までのリスト(2)の二つに分割する
    - できるだけ細かく分割していく
        - (1)と(2)のリストの要素が一つになるまで分割
            - つまりstart, m=start+1, end=start+2 
            - -> end -start >= 2
- 分割したそれぞれのリストにMerge操作をして並び替え

