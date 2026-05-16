import math
import sys


class Solution(object):
    def __init__(self):
        self.min_perfect = sys.maxsize


    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 4:
            return n

        till = int(math.floor(
            math.sqrt(
                n
            )
        ))

        for i in range(till, 0, -1):
            self.min_perfect = min(
                self.min_perfect, 1 + self.numSquares(n - (i * i))
            )

        return self.min_perfect


s = Solution()
print(s.numSquares(77))
