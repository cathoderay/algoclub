
def xor_all_nums(nums1, nums2):
    solution = 0
    if len(nums1) % 2 == 1:
        for num in nums2:
            solution ^= num

    if len(nums2) % 2 == 1:
        for num in nums1:
            solution ^= num
 
    return solution
