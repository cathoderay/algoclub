# problem: https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/
# space: O(m * n) | time: O((m * n))


import functools


def count_paths(grid):
    m, n = len(grid), len(grid[0])

    @functools.cache
    def dfs(x, y):
        acc = 1
        for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= x + i < m and 0 <= y + j < n and grid[x + i][y + j] < grid[x][y]:
                acc += dfs(x + i, y + j)
        return acc

    return sum(dfs(i, j) for i in range(m) for j in range(n)) % (10**9 + 7)
