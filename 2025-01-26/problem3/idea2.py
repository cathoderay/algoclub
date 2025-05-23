# problem: https://leetcode.com/problems/koko-eating-bananas/
# space: O(1) | time: O(n*log(max(piles)))


from math import ceil


def min_eating_speed(piles, h):
    l, r = 1, max(piles)

    while l < r:
        mid = (l + r) // 2
        if sum(ceil(pile/mid) for pile in piles) <= h:
            r = mid
        else:
            l = mid + 1
    return r
