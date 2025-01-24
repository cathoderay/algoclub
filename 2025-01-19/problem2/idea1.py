from functools import reduce

def xor_all_nums(nums1, nums2):
    solution = 0

    if len(nums1) % 2 == 1:
        solution ^= reduce(lambda a, b: a ^ b, nums2)

    if len(nums2) % 2 == 1:
        solution ^= reduce(lambda a, b: a ^ b, nums1)

    return solution
