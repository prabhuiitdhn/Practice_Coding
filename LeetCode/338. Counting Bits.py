import math as math


class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        output = [0]
        max_bit_to_be_traverse = int(math.ceil(abs(math.log(n, 2)))) + 1
        for i in range(1, n + 1):
            count = 0
            for j in range(max_bit_to_be_traverse):
                if (i >> j) % 2 == 1:
                    # this is for checking If jth bit of ith number.
                    count += 1
            output.append(count)
        return output


n =5
s = Solution()
print(s.countBits(n))


