# problem: https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/
# space: O(m * n) | time: O((m * n) * log(m * n))


def count_paths(grid):
    m, n = len(grid), len(grid[0])
    dp = [[1] * n for _ in range(m)]
    topological_order = sorted((grid[i][j], i, j) for i in range(m) for j in range(n))

    for _, i, j in topological_order:
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x + i < m and 0 <= y + j < n and grid[i + x][j + y] < grid[i][j]:
                dp[i][j] += dp[x + i][y + j]

    return sum(map(sum, dp)) % (10**9 + 7)
