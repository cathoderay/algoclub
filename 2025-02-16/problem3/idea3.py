# problem: https://leetcode.com/problems/house-robber/
# space: O(1) | time: O(n)


def rob(nums):
    a, b = 0, nums[0]

    for i in range(1, len(nums)):
        a, b = b, max(nums[i] + a, b)

    return b
