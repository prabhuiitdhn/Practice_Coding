"""
https://leetcode.com/problems/find-peak-element/description/

This problem is about returning the index which will have peak element compared to it's neighbor
there would be many peak elements but needed to return any of it.

if problem is on O(logn): It can be solved using Binary search tree
"""


# class Solution(object):
#     def findPeakElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#         index = 0
#         n = len(nums)
#
#         for i in range(n - 1, 0, -1):
#             if nums[i] > nums[i - 1]:
#                 index = i
#                 break
#         return index


class Solution(object):
    def findPeakElement(self, mountain):
        """
        :type mountain: List[int]
        :rtype: List[int]
        """
        # output = []
        #
        # n = len(mountain)
        # for i in range(n - 1, 0, -1):
        #     if mountain[i] > mountain[i - 1]:
        #         output.append(i)
        #
        # return output


        output = []
        n = len(mountain)
        for i in range(1,n-1):
            if mountain[i-1]<mountain[i]>mountain[i+1]:
                output.append(i)
        return output

# nums = [1, 2, 1, 3, 5, 6, 4]
# nums = [0, 1, 2, 3, 4]
# nums = [1]
# nums = [4, 3, 2, 1]
nums = [1, 4, 3, 8, 5]
# nums = [2, 4, 4]
s = Solution()
print(s.findPeakElement(nums))
