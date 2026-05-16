

class Solution(object):
    def groupAnagrams(self, strs):
        sorted_string_list = []
        for element in strs:
            string = sorted(element)
            s= ''
            for i in string:
                s += i
            sorted_string_list.append(s)

        d = {}

        for i in range(len(sorted_string_list)):
            if sorted_string_list[i] not in d:
                d[sorted_string_list[i]] = [strs[i]]
            else:
                d[sorted_string_list[i]].append(strs[i])

        final_list = []
        for value in d.values():
            final_list.append(value)

        return final_list

strs = ["eat","tea","tan","ate","nat","bat"]
s = Solution()
s.groupAnagrams(strs)
