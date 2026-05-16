from collections import OrderedDict


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = OrderedDict()
        for i in range(len(s)):
            char = s[i]
            if char not in d.keys():
                d[char] = [i, 1]
            else:
                d[char][1] += 1

        for key in d.keys():
            if d[key][1] == 1:
                return d[key][0]

        return -1


s = "leetcode"
p = Solution()
print(p.firstUniqChar(s))
