"""
needed to find out the distinct triplets which can make sum
0
"""


class Solution(object):
    def threeSum(self, nums):
        # working but time limit exceed
        # o(n^3)
        final_list = []
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (i != j and i != k and j != k) and nums[i] + nums[j] + nums[k] == 0:
                        current_list = [nums[i], nums[j], nums[k]]
                        if sorted(current_list) not in final_list:
                            final_list.append(sorted(current_list))

        return final_list

    def threesum2(self, nums):
        # working but time limit exceed.
        # O(n^2)
        if len(nums) < 3:
            return
        n = len(nums)
        final_list = []
        for i in range(n):
            for j in range(i + 1, n):
                remaining = - (nums[i] + nums[j])
                if remaining in nums[j + 1:]:
                    index = nums.index(remaining, j + 1, n)
                    current_list = [nums[i], nums[j], nums[index]]
                    if sorted(current_list) not in final_list:
                        final_list.append(sorted(current_list))

        return final_list

    def threesum4(self, nums):

        """
        Considered all the corner cases. O(n logn)
        corner cases:
        1. all elements is 0, [0, 0, 0]
        2. no triplets found then []
        @param nums:
        @return:

        Approach:
        1. Sorting the array
        2. negate the array and say that this is the target that we need to find with 2 index.
            start_pointer = i+1
            end_pointer = n-1
        3. check using two point approach. If sorted[start_pointer] + sorted[end_pointer] == target then we finf the triplets but
            if it is less than taget then we need to go higher side so we increase the start_pointer bcz array is in sorted order.
            If it is greater than target then we need to go to lower side then we will decrease the end_pointer bcz this is going lesser value side.
        """
        final_list = []
        if len(nums) < 3:
            return final_list
        if min(nums) == 0 and max(nums) == 0:
            # handles the case where all the elements in the nums is 0
            final_list.append([0, 0, 0])
            return final_list

        sorted_nums = sorted(nums)
        sorted_targets = [-1 * elements for elements in sorted_nums]

        final_list = []
        n = len(nums)
        for i in range(n - 2): # O(n)
            target = sorted_targets[i]
            k = n - 1
            j = i + 1
            while j < k: # worst case O(n)
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


# nums = [1, -1, -1, 0]
nums = [-1, 0, 1, 2, -1, -4]
# nums = [-2,0,1,1,2]
s = Solution()
print(s.threesum4(nums))
