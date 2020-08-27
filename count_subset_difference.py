def subset_diff(arr, n, s):
    dp = [[0 for i in range(s + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(s + 1):

            dp[i][0] = 1
            if j != 0:
                dp[0][j] = 0

            if j >= arr[i - 1]:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j]
            elif j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]

    return dp[n][s]


def count_subset(arr, n, diff):
    s = (diff + sum(arr)) / 2
    return subset_diff(arr, n, s)


a = [3, 1, 4, 2, 2, 1]
n = len(a)

print("The number of subset is ", subset_diff(a, n, 3))
