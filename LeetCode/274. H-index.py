class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """

        n = len(citations)
        count = [0] * n
        sorted_cit = sorted(citations)

        def count_citations(number):
            count = 0
            for j in range(n):
                if sorted_cit[j] >= number:
                    count += 1
            return count

        for i in range(n):
            count[i] = count_citations(i + 1)

        h_index = 0
        print(count)

        for k in range(n):
            h_index = max(h_index,
                          min(k + 1, count[k])
                          )
            print(h_index)

        return h_index



# citations = [1, 3, 1]
citations = [3,0,6,1,5]
s = Solution()
print(s.hIndex(citations))
