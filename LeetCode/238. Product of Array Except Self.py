import numpy as np
class Solution(object):
    def productExceptSelf1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        output = []
        for i in range(len(nums)):
            output.append(
                int(np.prod(nums[:i]) * np.prod(nums[i+1:]))
            )
        return output

    def productExceptSelf2(self, nums):
        # it is Optimised and Working.
        forward = [1] * len(nums)
        backward = [1] * len(nums)
        forward[0] = nums[0]
        backward[len(nums)-1] = nums[-1]
        for i in range(1, len(nums)):
            forward[i] = forward[i-1] * nums[i]

        for j in range(len(nums)-2, -1, -1):
            backward[j] = backward[j+1] * nums[j]

        output = []
        for i in range(len(nums)):
            if i == 0:
                output.append(backward[i+1])
            elif i == len(nums)-1:
                output.append(forward[i-1])
            else:
                output.append(
                    forward[i-1] * backward[i+1]
                )

        return output

# nums = [2, 3, 4, 5, 6]
nums = [-1,1,0,-3,3]
s = Solution()
print(s.productExceptSelf2(nums))
