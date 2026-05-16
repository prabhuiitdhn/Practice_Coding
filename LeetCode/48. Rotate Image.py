"""
https://leetcode.com/problems/rotate-image/
Rotating image. given nxn matrix which would be rotating by 90.
"""


class Solution(object):
    def rotate(self, matrix):
        n = len(matrix[0])
        # Transposing the matrix and swapping the columns
        # Using numpy or using indexing.

        # using indexing for swapping the columns for rotating the matrix.

        # print("Before:", matrix)
        # Transposing the matrix.
        for i in range(n):
            for j in range(i, n):
                if i != j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Swapping the columns

        for i in range(n // 2):
            for j in range(n):
                matrix[j][i], matrix[j][n - i - 1] = matrix[j][n - i - 1], matrix[j][i]

        print(matrix)

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

s = Solution()
s.rotate(matrix)
print(matrix)
