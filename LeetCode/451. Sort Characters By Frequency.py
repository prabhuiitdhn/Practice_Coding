class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = [0] * (122 - 48 + 1)
        for i in s:
            count[ord(i) - 48] += 1

        sorted_str = ''
        maximum = 999
        while maximum > 0:
            maximum = max(count)
            index = count.index(maximum)
            for i in range(maximum):
                sorted_str += chr(index + 48)
            count[index] = 0
        return sorted_str

p = Solution()
s = "2a554442f544asfasssffffasss"
print(p.frequencySort(s))