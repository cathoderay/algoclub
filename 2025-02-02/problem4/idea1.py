# problem: https://leetcode.com/problems/subarray-sums-divisible-by-k/
# space: O(n) | time: O(n)


def subarrays_div_by_k(nums, k):
    n = len(nums)
    m = [1] + [0]*k
    p = count = 0
    for i in range(n):
        p += nums[i]
        count += m[p % k]
        m[p % k] += 1
    return count
