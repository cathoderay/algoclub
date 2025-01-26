from math import ceil


def min_eating_speed(piles, h):
    def is_enough(k):
        return sum(ceil(pile / k) for pile in piles) <= h

    def binary_search(r):
        l = 1
        while l <= r:
            mid = (l + r) // 2
            if is_enough(mid):
                r = mid - 1
            else:
                l = mid + 1
        return r + 1
    return binary_search(max(piles))
