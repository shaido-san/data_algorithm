def levenshtein(s, t):
    dp = [[i+j if i*j == 0 else 0 for j in range(len(t)+1)] for i in range(len(s)+1)]
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            cost = 0 if s[i-1] == t[j-1] else 1
            dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+cost)
    return dp[-1][-1]

print(levenshtein("kitten", "sitting"))