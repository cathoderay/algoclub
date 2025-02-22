# problem: https://leetcode.com/problems/house-robber/
# space: O(n) | time: O(n)


def rob(nums):
    memo = {}
    def solve(i):
        if i >= len(nums): return 0
        if i in memo: return memo[i]

        a = memo[i + 2] = solve(i + 2)
        b = memo[i + 1] = solve(i + 1)

        return max(nums[i] + a, b)
    return solve(0)
