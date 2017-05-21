# 一種動態路徑規劃算法

## 情景
![情景示意圖](https://cdn.rawgit.com/axionl/bikonochikan/a9a3ce83/fig/Planning_plans.svg)
B 爲主動點，A、K爲從動點，C、D、E 爲障礙物，搜遊的點都有自己的障礙範圍，也即所有模型爲剛體模型。

## 條件
已知各剛體體積，以及中心座標，在不發生碰撞的情況下尋求最短跟隨主動點的路徑。
