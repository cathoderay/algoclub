# problem: https://leetcode.com/problems/climbing-stairs/
# space: O(1) | time: O(n)

import functools


@functools.lru_cache(maxsize=3)
def climb_stairs(n):
       if n <= 1: return 1
       return climb_stairs(n - 1) + climb_stairs(n - 2)
