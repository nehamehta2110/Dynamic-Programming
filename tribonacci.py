"""
The Tribonacci sequence Tn is defined as follows:
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Input: n = 4
Output: 4
Explanation: T_3 = 0 + 1 + 1 = 2
             T_4 = 1 + 1 + 2 = 4
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        if n == 2:
            return 1
        t = [0 for x in range(n + 1)]

        t[0] = 0
        t[1] = 1
        t[2] = 1

        for i in range(3, n + 1):
            t[i] = t[i - 1] + t[i - 2] + t[i - 3]

        return t[n]


def main():
    s = Solution()
    print(s.tribonacci(4))


if __name__ == '__main__':
    main()
