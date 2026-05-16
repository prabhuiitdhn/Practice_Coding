class Solution(object):
    def integerReplacementUsingRecursion(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0

        def helper(n):
            if n == 1:
                return 1

            if n % 2 == 0:
                return 1 + helper(n / 2)
            else:
                return 1 + min(
                    helper(n - 1), helper(n + 1)
                )

        if n == 1:
            return count
        if n % 2 == 0:
            count += helper(n / 2)
        else:
            count += min(
                helper(n + 1),
                helper(n - 1)
            )

        return count

    # def integerReplacement(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     count = 0
    #
    #     def helper(n):
    #         if n == 1:
    #             return 1
    #
    #         if not (n & 1):
    #             return 1 + helper(n >> 1)
    #         else:
    #             return 1 + min(
    #                 helper(n - 1), helper(n + 1)
    #             )
    #
    #     if n == 1:
    #         return count
    #
    #     return helper(n)


n = 7
s = Solution()
print(s.integerReplacement(n))
