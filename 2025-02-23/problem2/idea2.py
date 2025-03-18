# problem: https://leetcode.com/problems/triangle/
# extra space: O(m^2) | time: O(m^2)

from math import inf


def minimum_total(triangle):
    m = len(triangle)
    dp = [[inf] + triangle[i] + [inf] for i in range(m)]

    for i in range(1, m):
        for j in range(1, i + 2):
            dp[i][j] += min(dp[i - 1][j], dp[i - 1][j - 1])

    return min(dp[m - 1])