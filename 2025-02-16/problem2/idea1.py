# problem: https://leetcode.com/problems/n-th-tribonacci-number/
# space: O(1) | time: O(n)


def tribonacci(n):
    if n == 0: return 0

    a, b, c = 0, 1, 1

    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c

    return c