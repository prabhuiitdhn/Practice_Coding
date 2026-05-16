class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        total = 0

        length = 1
        while length < len(arr) + 1:

            for i in range(len(arr) - length + 1):
                print(arr[i:i+length])
                total += sum(arr[i:i+length])
            length += 2
        return total

arr = [1,4,2,5,3]
s = Solution()
print(s.sumOddLengthSubarrays(arr))