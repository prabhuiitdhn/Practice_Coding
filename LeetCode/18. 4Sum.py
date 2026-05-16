"""
https://leetcode.com/problems/4sum/description/

this problem is about given a nums as array of n integer and return all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that it will have sum as target.

* return unique quadruplets

Corner cases:
1. if len(num)<4:
    return []
2. if all the element of nums as 0
    return [0, 0, 0, 0]
3. if no quadruplets found then
    return []
# Approach
1. bruteforce approach O(n^4)
2. iterate 0 to n-4 and remaining find triplets using two point algorithm
"""


class Solution(object):
    def threeSum(self, nums, target):
        final_list = []
        if len(nums) < 3:
            return final_list
        if min(nums) == 0 and max(nums) == 0:
            # handles the case where all the elements in the nums is 0
            final_list.append([0, 0, 0])
            return final_list

        sorted_nums = nums
        sorted_targets = [(target - element) for element in sorted_nums]

        final_list = []
        n = len(nums)
        for i in range(n - 2):  # O(n)
            target = sorted_targets[i]
            k = n - 1
            j = i + 1
            while j < k:  # worst case O(n)
                if j != k and sorted_nums[j] + sorted_nums[k] == target:
                    current_list = [sorted_nums[i], sorted_nums[j], sorted_nums[k]]
                    if sorted(current_list) not in final_list:
                        final_list.append(sorted(current_list))
                        j += 1
                    else:
                        j += 1
                elif sorted_nums[j] + sorted_nums[k] > target:
                    k -= 1
                else:
                    j += 1

        return final_list

    def fourSum(self, nums, target):
        final_list = []
        if len(nums) < 0:
            return final_list
        if min(nums) == 0 and max(nums) == 0:
            final_list.append([0, 0, 0, 0])
            return final_list

        n = len(nums)
        sorted_nums = sorted(nums)
        sorted_target = [(target - element) for element in sorted_nums]
        for i in range(n - 3):
            # find target with triplet on remaining array
            return_list = self.threeSum(sorted_nums[i + 1:], sorted_target[i])
            # print("Line no71:", return_list)
            if len(return_list) > 0:
                for element in return_list:
                    # returning no of list from threeSum and adding current element to the list
                    sorted_nums_as_list = [sorted_nums[i]]
                    # extending the current_element as list with returned list.
                    sorted_nums_as_list.extend(element)
                    if sorted_nums_as_list not in final_list:
                        # this is for finding the unique list.
                        final_list.append(sorted_nums_as_list)

        return final_list


# nums = [1, 0, -1, 0, -2, 2]
# targets = 0

# nums = [2, 2, 2, 2, 2]
# targets = 8

# nums = [2,1,0,-1]
# targets=2

nums = [2, 2, 2, 2, 2]
targets = 8

s = Solution()
print(s.fourSum(nums, targets))


