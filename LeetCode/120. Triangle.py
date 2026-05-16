"""
https://leetcode.com/problems/triangle/description/
"""


class Solution(object):
    def minimumTotal(self, triangle):
        # IT WORKED BUT NEED TO OPTIMIZE IT for O(n) Space
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        total_rows = len(triangle)
        max_cols = len(triangle[total_rows - 1])
        min_sum = 0

        def helper(triangle, row, col, min_sum):
            if row == total_rows or col > max_cols:
                return 0
            min_sum += triangle[row][col] + min(
                helper(triangle, row + 1, col, min_sum),
                helper(triangle, row + 1, col + 1, min_sum)
            )
            return min_sum

        if total_rows == 1:
            min_sum = triangle[0][0]
        else:
            min_sum = helper(triangle, 0, 0, min_sum)
        return min_sum

    def minimumTotal2(self, triangle):  # WORKED & OPTIMISED, DP
        # 1D memoisation
        rows = len(triangle)
        cols = len(triangle[rows - 1])
        dp = [0] * rows

        if rows == 1:
            return triangle[0][0]

        for p in range(cols):
            dp[p] = triangle[rows - 1][p]

        for row in range(rows - 2, -1, -1):
            for j in range(row + 1):
                dp[j] = triangle[row][j] + min(
                    dp[j], dp[j + 1]
                )

        return dp[0]


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
s = Solution()
print(s.minimumTotal2(triangle))
