class Solution(object):
    def searchMatrix(self, matrix, target):

        """
        # It worked but needed to improve time complexity.
        # Use binary search tree for improving the code.
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        rows = len(matrix)
        cols = len(matrix[0])

        finding_row = 0

        if rows == 1:
            finding_row = 0
        else:
            for i in range(rows-1):
                if target < matrix[i + 1][0]:
                    finding_row = i
                    break
                if target == matrix[i+1][0]:
                    finding_row = i+1
        current_row = matrix[finding_row]
        middle_index = cols // 2
        if target == current_row[middle_index]:
            return True
        if target > current_row[middle_index]:
            middle_index_ = middle_index + 1
            while middle_index_ < cols:
                if target == current_row[middle_index_]:
                    return True
                middle_index += 1

        if target < current_row[middle_index]:
            middle_index__ = middle_index - 1
            while middle_index__ > -1:
                if target == current_row[middle_index__]:
                    return True

                middle_index__ -= 1

        return False

    def searchMatrix2(self, matrix, target): # accepted.
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        rows = len(matrix)
        cols = len(matrix[0])
        top_row = 0
        bottom_row = rows - 1

        # find the row where we can find the target.
        # it finds the row using Binary search search.
        while top_row <= bottom_row:
            middle_row = (top_row + bottom_row) // 2
            if target > matrix[middle_row][0]:
                top_row = middle_row + 1
            elif target < matrix[middle_row][0]:
                bottom_row = middle_row - 1
            else:
                break

        # It found the middle row where we can find the target in the row.
        middle_row = (top_row + bottom_row) // 2
        left_col = 0
        right_col = cols - 1

        while left_col <= right_col:
            middle_col = (left_col + right_col) // 2
            if target == matrix[middle_row][middle_col]:
                return True
            if target > matrix[middle_row][middle_col]:
                left_col = middle_col + 1
            if target < matrix[middle_row][middle_col]:
                right_col = middle_col - 1
        return False


# matrix = [[1, 3]]
# matrix = [[1],[3]]
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 11
s = Solution()
print(s.searchMatrix2(matrix, target))
