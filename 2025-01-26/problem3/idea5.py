# problem: https://leetcode.com/problems/koko-eating-bananas/
# space: O(n) | time: O(n*log(max(piles)))


from math import inf
import numpy as np
from bisect import bisect_left


def min_eating_speed(piles, h):
    piles = np.array(piles)
    get_hours = lambda k: -1 * np.sum(np.ceil(piles / k)) if k != 0 else inf
    search_space = range(1, max(piles) + 1)
    return bisect_left(search_space, -h, key=get_hours) + 1
