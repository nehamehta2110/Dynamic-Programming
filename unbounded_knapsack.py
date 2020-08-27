def unbounded_knapsack(wt, val, n, w):
    dp = [[0 for i in range(w + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(w + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            if wt[i - 1] <= w:
                dp[i][j] = max(dp[i - 1][j], val[i - 1] + dp[i][j - wt[i - 1]])
            elif wt[i - 1] > w:
                dp[i][j] = dp[i - 1][j]

    return dp[n][w]


W = 100
val = [10, 30, 20]
wt = [5, 10, 15]
n = len(val)

print(unbounded_knapsack(wt, val, n, W))
