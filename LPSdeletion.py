# code

def lcs(a, b):
    m = len(a)
    n = len(b)
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0

            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


for _ in range(int(input())):
    n = int(input())
    a = str(input())
    print(n - lcs(a, a[::-1]))
