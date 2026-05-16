class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        freq = {}
        for i in range(len(nums)):
            if nums[i] not in freq.keys():
                freq[nums[i]] = 1
            else:
                freq[nums[i]] += 1

        # sort the freq with their values
        dict(sorted(freq.items(), key=lambda item: item[1]))
        print(freq)
        output = []

        count = 0
        for key in freq.keys():
            if count<k:
                output.append(key)
                count += 1
            else:
                break

        print(output)


nums = [4,1,-1,2,-1,2,3]
k = 2
s = Solution()
print(s.topKFrequent(nums, k))
