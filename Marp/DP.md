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
# DP.pyの忘備録

---
<!-- class: normal -->
# DP: 動的計画法について
- 数列漸化式のように、小さい問題の結果を利用して解くアルゴリズム
- 漸化式を組み立てられるかが課題
    - 組み立て方としては前から順に組み立てていく例
    - 最初の値とその次の値を設定
        - 結構ミスりがちなので注意する
    - その後の値は規則に沿って値を計算