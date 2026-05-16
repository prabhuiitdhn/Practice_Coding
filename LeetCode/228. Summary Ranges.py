class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []

        final_list = []
        p = []

        p.append(nums[0])
        for i in range(1, len(nums)):
            if p[-1] + 1 == nums[i]:
                p.append(nums[i])
            else:
                final_list.append(p)
                p = []
                p.append(nums[i])

        final_list.append(p)

        output = []
        for list_ in final_list:
            p = list_
            if len(p)==1:
                output.append(str(p[0]))
            else:
                string = str(p[0]) + str("->") + str(p[-1])
                output.append(string)

        return output

nums = [0,1,2,4,5,7]
s = Solution()
print(s.summaryRanges(nums))

