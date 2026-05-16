class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # this is using sorting but needed to solve without using soorting i.e. priority queue.
        # return sorted(nums)[::-1][k-1]

        import heapq as hq
        # Using priority queue.
        h = []
        for i in range(len(nums)):
            hq.heappush(h, nums[i])

        hq.heapify(h)
        return hq.nlargest(k, h)[-1]


nums = [3,2,1,5,6,4]
k =2
s = Solution()
print(s.findKthLargest(nums, k))