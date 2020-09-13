# User function Template for python3
def scs(m, n, X, Y):
    def lcs(m, n, X, Y):
        '''
        :param m: length of string X
        :param n: length of string Y
        :param X: string X
        :param Y: string Y
        :return: Integer
        '''
        # code here
        t = [[None for i in range(n + 1)] for i in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 or j == 0:
                    t[i][j] = 0

                elif X[i - 1] == Y[j - 1]:
                    t[i][j] = 1 + t[i - 1][j - 1]

                else:
                    t[i][j] = max(t[i - 1][j], t[i][j - 1])

        return t[m][n]

    return m + n - lcs(m, n, X, Y)


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        X, Y = map(str, input().strip().split())
        print(scs(len(X), len(Y), X, Y))