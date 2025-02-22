# problem: https://leetcode.com/problems/climbing-stairs/
# space: O(n) | time: O(n)


def climb_stairs(n):
    memo = {}
    def solve(n):
        if n <= 1: return 1
        if n in memo: return memo[n]

        a = memo[n - 1] = solve(n - 1)
        b = memo[n - 2] = solve(n - 2)

        return a + b
    return solve(n)
