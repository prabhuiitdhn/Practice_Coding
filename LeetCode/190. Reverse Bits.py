"""
Ti reverse the bit to 32bit, each bit have to right shift by 1 bit and this has to be repeat for 32 time bcz
all 32 bit has to be reversed.
n&1: 0 if n is even
    1 if n is odd


"""
class Solution:
    def reverseBits(self, n):
        res = 0 # it is used for adding the
        for _ in range(32):
            # res<<1 is used for adding the number res*2
            res = (res<<1) + (n&1)
            n>>=1 # shifting left shift for reversing the bit
        return res

# n = "00000010100101000001111010011100"
# n =43261596
n = 8
s = Solution()
print(s.reverseBits(n))