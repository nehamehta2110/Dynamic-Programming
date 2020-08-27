def subset_diff(arr, n):
    s = sum(arr)

    dp = [[False for i in range(s + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(s + 1):

            dp[i][0] = True
            if j != 0:
                dp[0][j] = False

            if j >= arr[i - 1]:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]
            elif j < arr[i - 1]:
                dp[i][j] = dp[i - 1][j]

    diff = 99999

    for i in range(s // 2, -1, -1):
        if dp[n][i]:
            diff = min(diff, s - 2 * i)

    return diff


a = [3, 1, 4, 2, 2, 1]
n = len(a)

print("The minimum difference between 2 subsets is ", subset_diff(a, n))

