"""Tiling Problem
Given a “2 x n” board and tiles of size “2 x 1”, count the number of ways to tile the given board using
the 2 x 1 tiles. A tile can either be placed horizontally i.e., as a 1 x 2 tile or vertically i.e.,
as 2 x 1 tile
Input n = 4
Output: 5
Explanation: For a 2 x 4 board, there are 5 ways
1) All 4 vertical
2) All 4 horizontal
3) First 2 vertical, remaining 2 horizontal
4) First 2 horizontal, remaining 2 vertical
5) Corner 2 vertical, middle 2 horizontal
"""


def calculateFib(n):
    dp = [0, 1]

    while len(dp) < n + 1:
        dp.append(0)

    if n <= 1:
        return n
    else:
        if dp[n - 1] == 0:
            dp[n - 1] = calculateFib(n - 1)
        if dp[n - 2] == 0:
            dp[n - 2] = calculateFib(n - 2)

    dp[n] = dp[n - 1] + dp[n - 2]

    return dp[n]


if __name__ == '__main__':
    print(calculateFib(9))
