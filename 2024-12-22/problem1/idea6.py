

def contains_duplicate(nums):
    items = set()
    for num in nums:
        if num in items:
            return True
        items.add(num)
    return False