# problem: https://leetcode.com/problems/range-sum-query-2d-immutable
# space: O(1) | time (initialization): O(mn) | time (queries): O(1)

class NumMatrix:
    def __init__(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                a = matrix[i][j-1] if j >= 1 else 0
                b = matrix[i-1][j] if i >= 1 else 0
                c = matrix[i-1][j-1] if i >= 1 and j >= 1 else 0
                matrix[i][j] = matrix[i][j] + a + b - c

        self.matrix = matrix

    def sumRegion(self, row1, col1, row2, col2):
        a = self.matrix[row2][col2]
        b = self.matrix[row2][col1-1] if col1 >=1 else 0
        c = self.matrix[row1-1][col2] if row1 >= 1 else 0
        d = self.matrix[row1-1][col1-1] if row1 >= 1 and col1 >= 1 else 0
        return a - b - c + d
