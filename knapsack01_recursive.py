def knapsack(wt, val, w, n):
    if n == 0 or w == 0:
        return 0

    if wt[n - 1] <= w:
        return max(val[n - 1] + knapsack(wt, val, w - wt[n - 1], n - 1), knapsack(wt, val, w, n - 1))

    elif wt[n - 1] > w:
        return knapsack(wt, val, w, n - 1)


t = int(input())
for i in range(t):
    n = int(input())
    w = int(input())
    val = list(map(int, input().split()))
    wt = list(map(int, input().split()))
    s = knapsack(wt, val, w, n)
    print(s)