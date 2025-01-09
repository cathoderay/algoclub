from collections import Counter


def contains_duplicate(nums):
    return any(freq > 1 for freq in Counter(nums).values())