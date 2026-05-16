class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        threshold = n // 3
        sort_nums = sorted(nums)
        # print(sort_nums)
        output = []
        count = 1
        for i in range(1, n):
            if sort_nums[i - 1] == sort_nums[i]:
                count += 1
                if count>threshold:
                    if sort_nums[i-1] not in output:
                        output.append(sort_nums[i-1])
            else:
                print(count)
                if count > threshold:
                    output.append(sort_nums[i - 1])
                    count = 1
                count=1

        if count> threshold:
            output.append(sort_nums[n-1])

        return list(set(output))


s = Solution()
nums = [4,1,3,1,3,3,1,2,3,2,4,2,1,4,4,4,4,4]
print(s.majorityElement(nums))



