class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        for i in range(1, 32):
            # if (i-1)<<2 == n:
            #     return True
            if 2 << (i - 1) == n:
                return True
        return False

n = 12
s = Solution()
print(s.isPowerOfTwo(n))