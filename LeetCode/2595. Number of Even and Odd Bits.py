import math


class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        max_bits_to_be_traversed = int(
            math.ceil(
                math.log(n, 2)
            ) + 1
        )

        print(max_bits_to_be_traversed)
        even_index = 0
        odd_index = 0
        for i in range(max_bits_to_be_traversed):
            mask = 1 << i
            # n = n & mask
            if n & mask:
                if i % 2 == 0:
                    even_index += 1
                else:
                    odd_index += 1
        return [even_index, odd_index]


n = 2
s = Solution()
print(s.evenOddBit(n))
