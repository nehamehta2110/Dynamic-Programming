def coin_change(coin, s, n):
    dp = [[0 for i in range(s + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(s + 1):
            dp[i][0] = 1
            if j != 0:
                dp[0][j] = 0
            if coin[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coin[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][s]


if __name__ == '__main__':
    coin = [1, 2, 3]
    s = 4
    n = len(coin)
    print(coin_change(coin, s, n))
