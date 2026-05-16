"""
https://leetcode.com/problems/two-sum/

Given a array list and needed to find the two indices of the array which can sum to target.

"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        This appraoch is on o(n2)
        @param nums:
        @param target:
        @return:
        """
        # boundaries
        # it is O(N^2)
        if len(nums)==2:
            if nums[0] + nums[1] == target:
                return [0, 1]
        else:
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i]+nums[j]==target:
                        return [i, j]

    def twosum2(self, nums, target):
        # O(N)
        for i in range(len(nums)):
            remaining = target-nums[i]
            if remaining in nums[i+1:]:
                # Searching in O(1) hash tables.
                # nums.index(element, start, end)
                index_of_remaining = nums.index(remaining, i+1)
                return [i, index_of_remaining]

        return []

# nums = [2, 7, 11, 15]
# target = 9
# nums = [3, 2, 4]
# target= 6

nums = [3, 3]
target=6

S = Solution().twosum2(nums, target)
print(S)

