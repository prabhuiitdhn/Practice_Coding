class Solution(object):
    def maximumXorProduct2(self, a, b, n):
        """
        Working code but not optimal.
        :type a: int
        :type b: int
        :type n: int
        :rtype: int
        """
        max_ = 1
        if n == 0:
            return (a ^ 0) * (b ^ 0)
        until = 2 ** n
        m = 10 ** 9 + 7
        # a = a%m
        # b = b%m
        for i in range(until):
            max_ = max(
                max_, (
                        ((a ^ i) % m * (b ^ i) % m) % m
                )
            ) % m
        return max_

    def maximumXorProduct(self, a, b, n):
        """
        So approach is to find the max product that means If the a and b is as large as possible then product is going to be higher.
        So, or a and should be equal or closer and higher.
        brute force approach is not going to work so, needed to work with Bit Manipulation approach.
        1. SO we are iterating through MSB to LSB
        2. TO get the maximum product we have to make a and b are close to equal or equal if possible.
        3. hence, If we have a>b then reduce a and increase b so that a & b will be closer as possible.
        4. if a<b: the increase a and reduce b so that a & b will be closer as possible.

        @param a:
        @param b:
        @param n:
        @return:
        """
        m = (10 ** 9) + 7

        # Iterating each bit from MSB to LSB
        for i in range(n - 1, -1, -1):
            # the range is going to upto 2**n i.e. total n bits.
            mask = 1 << i
            # mask is being found the right most significant bit of the index.
            a_bit = a & mask
            b_bit = b & mask

            if a_bit and b_bit:
                # If a_bit and b_bit are set then both bit are equal i.e both are at maximum
                continue

            elif not a_bit and not b_bit:
                # if a_bit and b_bit are not set i.e. It has to be set to give the maximum products.
                a |= mask # used for setting the bit.
                b |= mask
            else:
                if a_bit and a > b:
                    # if abit is set and a>b then a has to be reduced
                    # and b has be increased
                    a ^= mask #Reduced using Xor
                    b |= mask # increased by OR [OR is basically used for adding an integers.]

                elif b_bit and b > a:
                    # if b_bit is set and b>a then b is to reduced and a hs to be increased.
                    a |= mask
                    b ^= mask

        a %= m
        b %= m
        return (a * b)%m



"""
# contraints:
# 0<=a, b<2**50
# 0<=n<=50

in this contraints if b is 2**50 and a is a**50 then multiplication would be 2**10 
which is be never possible in brute force approach. It exceeds the integer limits.
So, needed to think in such a way that can be easily run in the memory.


"""

# a = 53449611838892
# b = 712958946092406
# n = 6

a = 12
b = 5
n = 4
# for this example the maximum product is 14*7
s = Solution()
print(s.maximumXorProduct(a, b, n))
