"""
Given two strings text1 and text2, return the length of their longest common subsequence.
Input: text1 = "abcde", text2 = "ace"
Output: 3
"""


class Solution:
    @staticmethod
    def longestCommonSubsequence(text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        table = [[None] * (n + 1) for i in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    table[i][j] = 0
                elif text1[i - 1] == text2[j - 1]:
                    table[i][j] = table[i - 1][j - 1] + 1
                else:
                    table[i][j] = max(table[i - 1][j], table[i][j - 1])

        return table[m][n]


def main():
    s = Solution()
    print(s.longestCommonSubsequence('abcde', 'ace'))


if __name__ == '__main__':
    main()



