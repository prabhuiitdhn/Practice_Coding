class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if nums.count(0)==2:
            return True

        nums=list(filter(lambda nums: nums != 0, nums))

        if sum(nums)!=sum(set(nums)):
            return True
        else:
            return False

nums = [1,1,1,3,3,4,3,2,4,2]
s = Solution()
print(s.containsDuplicate(nums))