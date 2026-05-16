"""
https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
"""
class Solution(object):
    # this is an bruceforce approach which does not work, Beacause doing all bits to all number in between
    # left to right is a memory error job so, needed to find the smart solution for this.
    def rangeBitwiseAnd_bruteForce(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left == right:
            return left & right

        t = 2**32
        if right >= t:
            return 0
        if right < t:
            output = left
            for i in range(left + 1, right + 1):
                print(i)
                output &= i
                print("Line:", output)
            return output

    def rangeBitwiseAnd(self, left, right):
        """
        Try to find the common bit from left to right
        to find the common bit from left to right, we need to rightshift by 1 bit until both number are same.
        If both number are same meaning that bits from the left and right are same. Keep the track of after how many right shifts
        the left and right number are same.
        return the left shift by the count by 1 bit.
        i.e this was the number which was common between in the range of left to right.
        @param self:
        @param left:
        @param right:
        @return:
        """
        shift_count = 0

        while left<right:
            left >>=1
            right >>=1
            shift_count +=1

        return shift_count<<1

left = 5
right = 7
s = Solution()
print(s.rangeBitwiseAnd(left, right))