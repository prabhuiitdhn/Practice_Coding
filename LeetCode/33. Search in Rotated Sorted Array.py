"""
nums are in sorted (ascending order, with distinct value)
Also rotated after some index.
if target is not found then It is -1
else the index of target

complexity : O(logn) i.e all elements in the array should not be traverse.
1. Divide and conquer
2. two pointer approach which help us not to trasverse all the elements in the array
3. Binary search.

"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 2:
            if nums[0] == target:
                return 0
            else:
                return -1

        n = len(nums)
        start = 0
        endIndex = n - 1

        while start < endIndex:
            if target < nums[start] and target > nums[endIndex]:
                return -1
            if target > nums[start]:
                start += 1
            if target < nums[endIndex]:
                endIndex -= 1

            if target == nums[start]:
                return start

            if target == nums[endIndex]:
                return endIndex

        return -1


# nums = [4, 5, 6, 7, 0, 1, 2, 3]
# target = 3

nums = [16, 18, 20, 5, 7, 8]
target= 5
S = Solution()
print(S.search(nums, target))
