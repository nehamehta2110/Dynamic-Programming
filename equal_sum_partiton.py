def subset_sum(arr, n, s):
    dp = [[False for i in range(s + 1)] for i in range(n + 1)]

    for i in range(n + 1):
        for j in range(s + 1):

            dp[i][0] = True
            if j != 0:
                dp[0][j] = False

            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] or dp[i - 1][j]

            elif arr[i - 1] > j:
                dp[i][j] = dp[i - 1][j]

    return dp[n][s]


def equal_sum(arr, n):
    s = sum(arr)
    if s % 2 != 0:
        return False
    else:
        return subset_sum(arr, n, s // 2)


if __name__ == '__main__':
    arr = [3, 1, 5, 9, 12]
    n = len(arr)
    if equal_sum(arr, n):
        print("Can be divided into two subsets of equal sum")
    else:
        print("Can not be divided into two subsets of equal sum")
