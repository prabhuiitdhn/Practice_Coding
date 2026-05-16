import sys
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        d = {}
        int_max = sys.maxsize
        n = len(points)
        for i in range(n):
            for j in range(i+1, n):
                p1 = points[i]
                p2 = points[j]
                # if p2[1] - p2[0] == 0:
                nem = p2[1] - p1[1]
                dem  = p2[0] - p1[0]
                if nem ==0:
                    nem = int_max
                if dem == 0:
                    dem = int_max
                slope = nem / dem

                if slope not in d:
                    d[slope] = [p1, p2]
                    # d[slope].append(p2)
                else:
                    d[slope].append(p1)
                    d[slope].append(p2)

        ans = 1
        print("d:", d)
        for i in d:
            points =  d[i]
            count = []
            print("D[i]:", d[i])
            for p in points:
                if p not in count:
                    count.append(p)
            print("count:", count)
            ans = max(
                ans, len(count)
            )

        return ans



# points = [[1,1],[2,2],[3,3]]
#
points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
s = Solution()
print(s.maxPoints(points))
