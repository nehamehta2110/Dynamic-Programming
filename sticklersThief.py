def FindMaxSum(a, n):
    '''
    :param a:  given list of values
    :param n: size of a
    :return: Integer
    '''
    # code

    if n == 0:
        return 0

    if n == 1:
        return a[0]

    if n == 2:
        return max(a[0], a[1])

    dp = [0 for i in range(n)]

    dp[0] = a[0]
    dp[1] = max(a[0], a[1])

    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + a[i])

    return dp[-1]


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        print(FindMaxSum(a, n))