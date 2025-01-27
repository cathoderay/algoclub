# problem: https://leetcode.com/problems/koko-eating-bananas/
# space: O(1) | time: O(n*log(max(piles)))


from math import ceil, inf
from bisect import bisect_left


def min_eating_speed(piles, h):
    get_hours = lambda k: -1 * sum(ceil(pile / k) for pile in piles) if k != 0 else inf
    search_space = range(1, max(piles) + 1)
    return bisect_left(search_space, -h, key=get_hours) + 1
