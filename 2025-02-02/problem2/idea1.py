# problem: https://leetcode.com/problems/find-pivot-index/
# space: O(n) | time: O(n)


def pivot_index(nums):
    n = len(nums)
    p = [0]*n
    p[0] = nums[0]
    for i in range(1, n): 
        p[i] = p[i-1] + nums[i]
    for i in range(n):
        left = p[i-1] if i > 0 else 0
        right = p[-1] - p[i]
        if left == right: return i
    return -1
