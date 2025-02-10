# problem: https://leetcode.com/problems/range-sum-query-2d-immutable
# space: O(mn) | time (initialization): O(mn) | time (queries): O(1)


class NumMatrix:
    def __init__(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        self.p = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                a = self.p[i][j-1] if j >=1 else 0
                b = self.p[i-1][j] if i >= 1 else 0
                c = self.p[i-1][j-1] if i >= 1 and j >= 1 else 0
                self.p[i][j] = matrix[i][j] + a + b - c

    def sumRegion(self, row1, col1, row2, col2):
        a = self.p[row2][col2]
        b = self.p[row2][col1-1] if col1 >= 1 else 0
        c = self.p[row1-1][col2] if row1 >= 1 else 0
        d = self.p[row1-1][col1-1] if row1 >= 1 and col1 >= 1 else 0
        return a - b - c + d