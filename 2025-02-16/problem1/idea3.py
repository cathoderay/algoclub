# problem: https://leetcode.com/problems/climbing-stairs/
# space: O(n) | time: O(n)


def climb_stairs(n):
    a, b = 1, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b