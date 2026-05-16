class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        d = []
        # print(trust)
        # print(len(trust))
        # print(trust[0][0])
        for i in range(len(trust)):
            people = trust[i][0]
            trust_ = trust[i][1]
            print(people)
            print(trust)
            if people not in d:
                d.append(people)
        print(d)
        # judge = n*(n+1)/2 - sum(d)
        # return judge if judge<n else -1
        return n

n = 3
trust = [[1,3],[2,3],[3,1]]

s = Solution()
print(s.findJudge(n, trust))