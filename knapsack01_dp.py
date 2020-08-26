def knapsack(wt, val, w, n):
    dp = [[-1 for x in range(w + 1)] for y in range(n + 1)]
    if n == 0 or w == 0:
        return 0

    if dp[n][w] != -1:
        return dp[n][w]

    if wt[n - 1] <= w:
        dp[n][w] = max(val[n - 1] + knapsack(wt, val, w - wt[n - 1], n - 1), knapsack(wt, val, w, n - 1))
        return dp[n][w]

    elif wt[n - 1] > w:
        dp[n][w] = knapsack(wt, val, w, n - 1)
        return dp[n][w]


t = int(input())
for i in range(t):
    n = int(input())
    w = int(input())
    val = list(map(int, input().split()))
    wt = list(map(int, input().split()))
    s = knapsack(wt, val, w, n)
    print(s)