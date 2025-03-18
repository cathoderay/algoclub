# problem: https://leetcode.com/problems/unique-paths/
# space: O(m*n) | time: O(m*n)


import functools


def unique_paths(m, n):
    @functools.cache
    def solve(x, y):
        if x == 0 or y == 0: return 1
        return solve(x - 1, y) + solve(x, y - 1)

    return solve(m - 1, n - 1)