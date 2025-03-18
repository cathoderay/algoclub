# problem: https://leetcode.com/problems/minimum-falling-path-sum/
# space: O(m*n) | time: O(m*n)


from math import inf


def min_falling_path_sum(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[inf] + matrix[i] + [inf] for i in range(m)]

    for i in range(1, m):
        for j in range(1, n + 1):
            dp[i][j] += min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1])

    return min(dp[m - 1])
