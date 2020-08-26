def subset_sum(arr, n, sum):
    if sum == 0:
        return True
    if n == 0:
        return False

    dp = [[False for i in range(sum + 1)] for i in range(n + 1)]

    if arr[n - 1] <= sum:
        dp[n][sum] = subset_sum(arr, n - 1, sum - arr[n - 1]) or subset_sum(arr, n - 1, sum)
        return dp[n][sum]

    else:
        dp[n][sum] = subset_sum(arr, n - 1, sum)
        return dp[n][sum]


arr = [3, 34, 4, 12, 5, 2]
sum = 9
n = len(arr)
if subset_sum(arr, n, sum):
    print("Found a subset with given sum")
else:
    print("No subset with given sum")
