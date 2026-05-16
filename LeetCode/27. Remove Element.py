class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        index_of_val = []
        count = 0
        for i in range(len(nums)):
            if nums[i] == val:
                index_of_val.append(i)
            else:
                count += 1

        for j in range(len(index_of_val)):
            # nums of times the val is being removed.
            nums.remove(val)

        return count


nums = [3, 2, 2, 3]
val = 3

s= Solution()
print(s.removeElement(nums, val))
print(nums)

nums.remove()

