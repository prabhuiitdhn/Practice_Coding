class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        p1 = 0
        p2 = 1
        n = len(nums)

        while p2 < n:
            if nums[p1] == 0 and nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1

            if nums[p1] != 0 and nums[p2] == 0:
                p1 = p2

            p2 += 1


nums = [0,1, 0, 3, 12]
s = Solution()
s.moveZeroes(nums)
print(nums)