# problem: https://leetcode.com/problems/koko-eating-bananas/
# space: O(1) | time: O(n*log(max(piles)))


from math import ceil, inf
from bisect import bisect_right 


def min_eating_speed(piles, h):
    get_hours = lambda k: sum(ceil(pile / k) for pile in piles) if k != 0 else inf
    search_space = range(max(piles) + 1, -1, -1)
    return search_space[bisect_right(search_space, h, key=get_hours)] + 1
