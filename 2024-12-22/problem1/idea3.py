

def contains_duplicate(nums):
    m = len(nums)
    n = len(set(nums))
    return m != n
