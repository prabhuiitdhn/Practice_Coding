class Solution(object):
    def totalHammingDistance_bruteForce(self, nums):
        # THIS SOLUTION WORKS BUT UNTIL INTEGER VALUE
        # BUT IF IT EXCEEDS THE LIMIT THEN IT GIVES AN ERROR.
        """
        :type nums: List[int]
        :rtype: int
        """

        def countBits(n):
            count = 0
            while n:
                count += 1
                n &= n - 1
            return count

        n = len(nums)
        total = 0
        for i in range(n):
            for j in range(i + 1, n):
                total += countBits(
                    nums[i] ^ nums[j]
                )

        return total

    def totalHammingDistance(self, nums):
        """
        To make it optimal.
        Check all bits of the number that how many bits are 0s and 1s and multiply with no of 1s with no of 0s
        example: [4, 14, 2]
        4:  0100
        14: 1110
        2:  0010
        so, oth bit: # of zeros bit: 3, # of 1s: 0
            1st bit: # of zeros bit: 1, # of 1s: 2
            2nd bit: # of zeros bit: 1 # of 1s: 2
            3rd bit: # of zeros bit: 2, # of 1s : 1

            So total : 3*0 + 1 *2 + 1*2 +2*1 = 6
        @param nums:
        @return:
        """

        import math
        total_sum = 0
        max_bit_to_be_traversed = int(math.ceil(math.log(max(nums),2))+1)
        for i in range(max_bit_to_be_traversed):
            mask = 1 << i
            zeros_bit = 0
            ones_bit = 0
            for num in nums:
                num = num & mask
                if num == 0:
                    zeros_bit += 1
                else:
                    ones_bit += 1
            total_sum += zeros_bit * ones_bit
        return total_sum

nums = [4, 14, 2]
s = Solution()
print(s.totalHammingDistance(nums))
