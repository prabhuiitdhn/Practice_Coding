"""
this problem is about finding the first and last index of the target in the array.
array is sorted in non-decreasing order.y
Algorithm can be implemented in O(logn)

1. Boundary conditions len(nums)<2
2. no target will be found
3. only one target would be found.
4. If all the elements are targets.
"""


class Solution(object):
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]

        if len(nums) < 2:
            if nums[0] == target:
                return [0, 0]
            if nums[0] != target:
                return [-1, -1]

        n = len(nums)
        find_middle_element = (n // 2)

        if (target < nums[0]) or (target > nums[-1]):
            return [-1, -1]

        if target > nums[find_middle_element]:
            # find the element in the right side of the array
            matchingIndex = []
            for i in range(find_middle_element + 1, n):
                if nums[i] == target:
                    matchingIndex.append(i)

            if len(matchingIndex) == 0:
                return [-1, -1]
            else:
                return [matchingIndex[0], matchingIndex[-1]]

        if target < nums[find_middle_element]:
            # find the elements in left side of the array
            matchingIndex = []
            for j in range(find_middle_element - 1, -1, -1):
                if nums[j] == target:
                    matchingIndex.append(j)
            if len(matchingIndex) == 0:
                return [-1, -1]
            else:
                return [matchingIndex[-1], matchingIndex[0]]

        if target == nums[find_middle_element]:
            startIndex = find_middle_element

            endIndex = find_middle_element

            while startIndex > -1:
                if nums[startIndex] == target:
                    startIndex -= 1
                else:
                    break

            while endIndex < n:
                if nums[endIndex] == target:
                    endIndex += 1
                else:
                    break

            return [startIndex + 1, endIndex - 1]
            # check both side for the first and last index of an elements in the nums
        return [-1, -1]


#
# nums = [5, 7, 7, 8, 8, 10]
# target = 5

nums = [2, 2]
target = 2
S = Solution()
print(S.searchRange(nums, target))
