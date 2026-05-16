class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = max(nums)
        count = [0] * (maximum + 1)
        for i in range(len(nums)):
            count[nums[i]] += 1

        print(count)
        for j in range(1, len(count)):
            if count[j] > 1:
                return j

nums = [1,1]
s = Solution()
print(s.findDuplicate(nums))