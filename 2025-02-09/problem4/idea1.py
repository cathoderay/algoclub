# problem: https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
# space: O(m*n) | time: O(m^2*n)


from collections import defaultdict


def num_submatrix_sum_target(matrix, target):
    m = len(matrix)
    n = len(matrix[0])

    p = [[0]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            a = p[i][j-1] if j >=1 else 0
            b = p[i-1][j] if i >= 1 else 0
            c = p[i-1][j-1] if i >= 1 and j >= 1 else 0
            p[i][j] = matrix[i][j] + a + b - c

    count = 0
    for r1 in range(m):
        for r2 in range(r1, m):
            t = defaultdict(int)
            t[0] = 1
            for c in range(n):
                cur = p[r2][c] - (p[r1-1][c] if r1 - 1 >= 0 else 0)
                count += t[cur - target]
                t[cur] += 1
    return count
