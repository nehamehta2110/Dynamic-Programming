"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        s = [0 for i in range(n + 1)]
        if n < 2:
            return n
        s[1] = 1
        s[2] = 2

        for i in range(3, n + 1):
            s[i] = s[i - 1] + s[i - 2]

        return s[n]


def main():
    s = Solution()
    print(s.climbStairs(3))


if __name__ == '__main__':
    main()
