

def contains_duplicate(nums):
    m = len(nums)
    n = len(set(nums))
    if m == n:
        return False
    else:
        return True
