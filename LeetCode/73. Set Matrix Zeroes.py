"""
https://leetcode.com/problems/set-matrix-zeroes/description/
"""
import numpy as np


class Solution(object):
    def setZeroes(self, matrix):

        row = len(matrix)
        col = len(matrix[0])
        visited_row = []
        visited_col = []
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    if i not in visited_row:
                        visited_row.append(i)
                    if j not in visited_col:
                        visited_col.append(j)

        # print(visited_col)
        # print(visited_row)

        for required_col in visited_col:
            for required_row in range(row):
                matrix[required_row][required_col] = 0

        for required_row in visited_row:
            for required_col in range(col):
                matrix[required_row][required_col] = 0


matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
# matrix =  [[1,1,1],[1,0,1],[1,1,1]]
# matrix = np.array(matrix)
s = Solution()
s.setZeroes(matrix)
print(matrix)

# array slicing in 2d for column
# how to set all to zero
