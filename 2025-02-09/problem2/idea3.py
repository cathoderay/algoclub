# problem: https://leetcode.com/problems/range-sum-query-2d-immutable
# space: O(mn) | time (initialization): O(mn) | time (queries): O(1)


class NumMatrix:
   def __init__(self, matrix):
       m = len(matrix)
       n = len(matrix[0])

       self.p = [[0]*(n+1) for _ in range(m+1)]

       for i in range(1, m+1):
           for j in range(1, n+1):
               self.p[i][j] = matrix[i-1][j-1] + self.p[i][j-1] + self.p[i-1][j] - self.p[i-1][j-1]

   def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
       return self.p[row2+1][col2+1] - self.p[row2+1][col1] - self.p[row1][col2+1] + self.p[row1][col1]
