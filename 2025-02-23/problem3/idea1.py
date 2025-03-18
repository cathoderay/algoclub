# problem: https://leetcode.com/problems/minimum-falling-path-sum/
# extra space: O(1) | time: O(m*n)


from math import inf


def min_falling_path_sum(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = matrix
    for i in range(1, m):
        for j in range(n):
            dp[i][j] += min(
                dp[i - 1][j - 1] if j - 1 >= 0 else inf,
                dp[i - 1][j],
                dp[i - 1][j + 1] if j + 1 < n else inf)
    return min(dp[m - 1])
