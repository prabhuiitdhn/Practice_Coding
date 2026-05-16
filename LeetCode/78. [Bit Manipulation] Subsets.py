class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums) # length of num
        total_subset = 2**n # total number of subset will be 2^3
        subsets = []

        for i in range(total_subset): # it will be giving the bit position.
            set_ = []
            for j in range(n): # this should give the binary representation
                if i & (1<<j) != 0: # check which bit is set to place the bit index.
                    set_.append(
                        nums[j]
                    )
            if set_ not in subsets:
                subsets.append(set_)
        print(sorted(subsets))




# nums = [1, 2, 3]
# nums = [1,2,2]
nums =[4,4,4,1,4]
s = Solution()
print(s.subsets(nums))
