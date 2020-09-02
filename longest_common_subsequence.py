def longest_common_subsequence(x, y, n, m):
    if n == 0 or m == 0:
        return 0

    dp = [[-1 for i in range(n + 1)] for i in range(m + 1)]

    if dp[m][n] != -1:
        return dp[m][n]

    if x[n - 1] == y[m - 1]:
        dp[m][n] = 1 + longest_common_subsequence(x, y, n - 1, m - 1)
        return dp[m][n]

    else:
        dp[m][n] = max(longest_common_subsequence(x, y, n - 1, m), longest_common_subsequence(x, y, n, m - 1))
        return dp[m][n]


def main():
    X = "Manav"
    Y = "Naina"
    print("Length of LCS is", longest_common_subsequence(X, Y, len(X), len(Y)))


if __name__ == '__main__':
    main()
