# problem: https://leetcode.com/problems/triangle/
# extra space: O(1) | time: O(m^2)


from math import inf


def minimum_total(triangle):
    m = len(triangle)
    dp = triangle
    for i in range(1, m):
        for j in range(i + 1):
            dp[i][j] += min(
                dp[i - 1][j] if j != i else inf,
                dp[i - 1][j - 1] if j - 1 >= 0 else inf)
    return min(dp[m - 1])
