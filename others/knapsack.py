def knapsack(w, v, W):
    n = len(w)
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(W+1):
            if j >= w[i]:
                dp[i+1][j] = max(dp[i][j], dp[i][j-w[i]] + v[i])
            else:
                dp[i+1][j] = dp[i][j]
    return dp[n][W]

w = [2, 3, 4]
v = [4, 5, 6]
W = 5

print(knapsack(w, v, W))  