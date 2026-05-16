"""
Given two integer dividend and divisor, needed to find out the quotient after dividing dividend by divisior
without using mulitplication, division and mod operator.
so, we can using logical operator, + and -
"""


class Solution(object):
    def divide(self, act_dividend, act_divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        dividend = abs(act_dividend)
        divisor = abs(act_divisor)
        count = 0
        while dividend >= divisor:
            inner = 1
            # while dividend>=divisor:
            while dividend >= (divisor << 1):
                divisor <<= 1
                # count += 1
                inner <<= 1
            dividend = dividend - (divisor)
            count += inner
            divisor = act_divisor
        if (act_dividend > 0 and act_divisor < 0) or (act_dividend < 0 and act_divisor > 0):
            return -1 * count

        return count


dividend = -7
divisor = 3
S = Solution()
print(S.divide(dividend, divisor))
