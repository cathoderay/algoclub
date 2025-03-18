# problem: https://leetcode.com/problems/maximal-square/
# space: O(m*n) | time: O(m*n)


def maximal_square(matrix):
    m, n = len(matrix), len(matrix[0])

    dp = [list(map(int, i)) for i in matrix]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1 if dp[i][j] else 0

    return max(map(max, dp)) ** 2
