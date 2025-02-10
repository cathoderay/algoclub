# problem: https://leetcode.com/problems/subarray-sum-equals-k/
# space: O(n) | time: O(n)


def subarray_sum(nums, k):
    n = len(nums)
    m = {0 : 1}
    p = count = 0
    for i in range(n):
        p += nums[i]
        count += m.get(p - k, 0)
        m[p] = m.get(p, 0) + 1
    return count