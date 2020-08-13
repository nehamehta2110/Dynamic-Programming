def calculateFib(n):
    dp = [0, 1]

    while len(dp) < n + 1:
        dp.append(0)

    if n <= 1:
        return n
    else:
        if dp[n - 1] == 0:
            dp[n - 1] = calculateFib(n - 1)
        if dp[n - 2] == 0:
            dp[n - 2] = calculateFib(n - 2)

    dp[n] = dp[n - 1] + dp[n - 2]

    return dp[n]


if __name__ == '__main__':
    print(calculateFib(9))
