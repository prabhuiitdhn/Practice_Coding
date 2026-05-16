
class LargerNumKey(str):
    def __lt__(x, y):
        # Compare x+y with y+x in reverse order to get descending order
        return x+y > y+x

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(num) for num in nums]
        nums.sort(key=LargerNumKey)
        print(nums)
        empty_str = ""
        for sorted_num in nums:
            empty_str += sorted_num

        if max(nums) == '0':
            return '0'
        else:
            return empty_str

nums = [3, 30, 34, 5, 9]

s = Solution()
print(s.largestNumber(nums))