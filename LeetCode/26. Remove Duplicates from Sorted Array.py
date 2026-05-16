"""
this is inplace removing duplicates element in the array.
Where the first K (if the total number of unique elements in k) would be unique element in array and remaining would anything which does not matter.
"""

class Solution:
    def removeDuplicates(self, nums):
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
S = Solution()
print(S.removeDuplicates(nums))