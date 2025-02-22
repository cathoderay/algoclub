# problem: https://leetcode.com/problems/house-robber/
# space: O(n) | time: O(n)


import functools


def rob(nums):
    @functools.cache
    def solve(i):
        if i >= len(nums): return 0
        return max(nums[i] + solve(i + 2), solve(i + 1))

    return solve(0)
