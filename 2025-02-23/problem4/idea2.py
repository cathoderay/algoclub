# problem: https://leetcode.com/problems/maximal-square/
# extra space: O(1) | Time: O(m*n)


def maximal_square(matrix):
    m, n = len(matrix), len(matrix[0])

    for i in range(m): matrix[i] = list(map(int, matrix[i]))
    dp = matrix

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1 if dp[i][j] else 0

    return max(map(max, dp)) ** 2
