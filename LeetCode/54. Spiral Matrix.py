"""
https://leetcode.com/problems/spiral-matrix/description/
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
                # it does work for nxn matrix but needed to check for mxn matrix.
        @param matrix:
        @return:
        """

        def helper_up(start, end):
            block_elements = []
            for i in range(start, end + 1):
                block_elements.append(matrix[start][i])

            for j in range(start + 1, end + 1):
                block_elements.append(matrix[j][end])

            return block_elements

        def helper_down(start, end):
            block_elements = []

            for i in range(start, end, -1):
                block_elements.append(matrix[start][i - 1])

            for j in range(start - 1, end, -1):
                block_elements.append(matrix[j][end])

            return block_elements

        l = []
        n = len(matrix[0])
        start_index = 0
        end_index = n - 1

        while start_index <= end_index:
            l.append(helper_up(start_index, end_index))
            l.append(helper_down(end_index, start_index))
            start_index += 1
            end_index -= 1

        return l




matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]
          ]

# matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

# matrix =[[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
print(s.spiralOrder(matrix))
# print(s.spiralOrder2(matrix))
