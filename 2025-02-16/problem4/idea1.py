# problem: https://leetcode.com/problems/delete-and-earn/
# space: O(n) | time: O(max(numx))


from collections import Counter


def delete_and_earn(nums):
    f = Counter(nums)
    a, b = 0, f[1]

    for i in range(2, max(nums) + 1):
       a, b = b, max(a + f[i] * i, b)

    return b
