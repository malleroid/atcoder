# 入力をintにして変数に格納
a, b, c, k = map(int, input().split())

# KとA,Bの大きさに応じて場合分けして最大値計算
if a >= k :
    max = k

elif a+b >= k :
    max = a

elif a+b <= k :
    max = a - ( k - a - b )

# 結果を出力
print(max)