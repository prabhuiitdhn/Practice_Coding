from collections import deque
import sys


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = deque(maxlen=k)

        output = []
        max_value = -sys.maxsize

        for i in range(len(nums)):
            if len(d)<k:
                d.append((nums[i], i))
                max_value = max(
                    max_value, nums[i]
                )
            else:
                max_value = max(
                    max_value, nums[i]
                )
                if (i-k)>0 and max_value == nums[i-k]:
                    d.popleft()
                    d.append((nums[i], i))
                    max_value = max(d)
                    output.append(max_value)
                else:
                    output.append(max_value)
                    d.popleft()
                    d.append((nums[i], i))

        max_value = max(
            max_value, nums[-1]
        )
        output.append(max_value)
        # output.append(max(d)[0])

        return output


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
S = Solution()
print(S.maxSlidingWindow(nums, k))


# d = deque()
# d.append((1, 0))
# d.append((3, 1))
# d.append((-1, 2))
# d.append((-7, 8))
# d.append((17, -2))
# print(max(d))
# print(sorted(d))
#
# p_d = deque(maxlen=3)
# p_d.append((1, 0))
# p_d.append((3, 1))
# p_d.append((-1, 2))
# p_d.append((-7, 8))
# p_d.append((17, -2))
# print(max(p_d))
# print(sorted(p_d))