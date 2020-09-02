def longest_common_substring(X, Y, n, m):

    dp = [[0 for i in range(n + 1)] for i in range(m + 1)]

    result = 0

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif Y[i - 1] == X[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                result = max(result, dp[i][j])
            else:
                dp[i][j] = 0

    index = dp[m][n]

    lcs = [""] * (index + 1)
    lcs[index] = ""

    while n > 0 and m > 0:


        if X[n - 1] == Y[m - 1]:
            lcs[index - 1] = X[n - 1]
            n -= 1
            m -= 1
            index -= 1

        elif dp[m - 1][n] > dp[m][n - 1]:
            m -= 1
        else:
            n -= 1

    print(lcs)

def main():
    X = 'MynameisNeha'
    Y = 'HernameisNaina'
    print('Length of Longest Common Substring is', longest_common_substring(X, Y, len(X), len(Y)))


if __name__ == '__main__':
    main()




