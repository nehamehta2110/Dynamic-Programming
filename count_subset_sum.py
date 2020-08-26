def subset_sum(arr, n, sum):
    if sum == 0:
        return 1
    if n == 0:
        return 0

    dp = [[0 for i in range(sum + 1)] for i in range(n + 1)]

    if arr[n - 1] <= sum:
        dp[n][sum] = subset_sum(arr, n - 1, sum - arr[n - 1]) + subset_sum(arr, n - 1, sum)
        return dp[n][sum]

    else:
        dp[n][sum] = subset_sum(arr, n - 1, sum)
        return dp[n][sum]


arr = [3, 34, 4, 12, 5, 2]
sum = 9
n = len(arr)
print(subset_sum(arr, n, sum))
