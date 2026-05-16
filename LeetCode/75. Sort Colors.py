"""
https://leetcode.com/problems/sort-colors/
This problem can be solved using Counting sort.
https://www.geeksforgeeks.org/counting-sort/
"""
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        count_0 = 0
        count_1 = 0
        count_2 = 0

        for element in nums:
            if element == 0:
                count_0 += 1
            if element == 1:
                count_1 += 1
            if element == 2:
                count_2 += 1

        for i in range(count_0):
            nums[i] = 0

        for k in range(count_0, count_0 + count_1):
            nums[k] = 1

        for l in range(count_0 + count_1, count_0 + count_1 + count_2):
            nums[l] = 2


nums = [2, 0, 2, 1, 1, 0]
s = Solution()
s.sortColors(nums)
print(nums)
