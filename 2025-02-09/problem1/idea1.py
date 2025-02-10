# problem: https://leetcode.com/problems/special-array-ii
# space: O(n) | time: O(n)


def is_array_special(nums, queries):
    p = [0]

    for i in range(1, len(nums)):
        p.append(p[i-1] + (1 if nums[i] % 2 == nums[i-1] % 2 else 0))

    return [p[r] - p[l] == 0 for l, r in queries]