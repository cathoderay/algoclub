# problem: https://leetcode.com/problems/unique-paths/
# space: O(n) | time: O(m*n)


def unique_paths(m, n):
    a, b = [1] * n, [1]

    for i in range(1, m):
        for j in range(1, n):
            b.append(a[j] + b[j - 1])
        a, b = b, [1]

    return a[-1]
