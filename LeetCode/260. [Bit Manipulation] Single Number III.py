class Solution(object):
    def singleNumber(self, nums):
        """
        Approach:
        1. Xor all the result which can find the two different elements which occurs once.
        2. Find the right most set bit in xor results. [result & (2s complement of results)]//mask
        3. Iterate through the array and separate the elements into two groups:
            one groups with elements having the bit as 1 at the masked position
            other group with elements having the bit at the masked position as 0
            note: if an element is occurs once then definetely the bit of this will be different from others.
            so assume element 'a', 'b' are two different element is being used then these two will also have different bit
            value at some position.
        4. iterate all the number in each group. and find the element which occurs once
        :type nums: List[int]
        :rtype: List[int]
        """
        xor= 0
        for i in nums:
            xor ^= i
        rmsb = xor & (-xor)
        # print(rmsb)
        group1 = 0
        group2 =0

        # group1 = []
        # group2 = []
        for num in nums:
            if num & rmsb:
                group1 ^= num
                # group1.append(num)
            else:
                group2 ^= num
                # group2.append(num)

        # a = group1[0]
        # for i in range(1, len(group1)):
        #     a ^= group1[i]

        # b= group2[0]
        # for j in range(1, len(group2)):
        #     b ^=group2[j]

        # return [a, b]
        return [group1, group2]

nums = [1, 2, 1, 3, 2, 5]
s = Solution()
print(s.singleNumber(nums))