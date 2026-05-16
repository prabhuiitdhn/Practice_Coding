"""
https://leetcode.com/problems/merge-intervals/description/
"""


class Solution(object):
    def merge(self, intervals):
        if len(intervals) == 1:
            return intervals

        intervals = sorted(intervals)
        l = []
        final_list = []
        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if len(l) ==0:
                l.append(start)
                l.append(end)
            else:
                if start>l[-1]:
                    final_list.append(l)
                    l = []
                    l.append(start)
                    l.append(end)
                else:
                    if end>l[-1]:
                        l.pop()
                        l.append(end)

        final_list.append(l)
        return final_list


# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals = [[1, 4], [4, 5]]
# intervals = [[1,4],[2,3]]
S = Solution()
print(S.merge(intervals))

