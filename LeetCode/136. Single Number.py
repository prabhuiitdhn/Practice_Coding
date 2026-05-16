class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique = []
        nums = sorted(nums)
        unique.append(nums[0])

        print(unique)

        for i in range(1, len(nums)):
            if len(unique)>0:
                if unique[-1] == nums[i]:
                    unique.pop()
            else:
                unique.append(nums[i])

        return unique[0]

nums=[4, 1, 2, 1, 2]
s = Solution()
print(s.singleNumber(nums))