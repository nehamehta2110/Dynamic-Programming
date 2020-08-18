"""
Here we are given an array S = [1, 2, 3] and N = 4, we have to find number of ways by which we can use the given coins
in S to return total sum as N, example: [1,1,1,1], [2,2], [1,3] and [1,1,2] so output=4
"""


def count_change_coin(S, n, size):

    table = [0 for i in range(n + 1)]
    table[0] = 1

    for i in range(0, size):
        for j in range(S[i], n + 1):
            table[j] += table[j - S[i]]

    return table[n]


if __name__ == '__main__':
    S = [1, 2, 3]
    n = 4
    size = len(S)
    print(count_change_coin(S, n, size))
