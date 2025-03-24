# 計算対象の行列
x = [[0, 1, 0, 0],
     [1, 0, 0, 1],
     [0, 1, 0, 0],
     [0, 1, 1, 0]
     ]

# 結果格納用
result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]
          ]

N = len(x)

# 以下A^2を計算する

# 行方向にループ
for i in range(N):
    # 列方向にループ
    for j in range(N):
        # 要素績を足し上げてi行j列の要素を計算する
        for k in range(N):
            result[i][j] += x[i][k] * x[k][j]

# 結果を表示
for r in result:
    print(r)