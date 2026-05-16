"""
https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/diagonal-traversal-of-matrix?page=0&pageSize=10
"""
class DiagonalTraverse(object):
    def function(self, n, mat):
        """
        to track the index, I am using jump which jump each time its step,
        the index is from top-right. Trying to find out the diagonal from the top-right to bottom right.
        @param n:
        @param mat:
        @return:
        """
        jump = (n - 1)
        start = 0
        end = n - jump
        while jump > -(n):
            index = []
            if jump < 0:
                start += 1
                end = n
            for i in range(start, end):
                index.append(mat[i][i + jump])

            end += 1
            jump -= 1

            print(sum(index), end= ' ')

# n = 3
# mat = [[-5, 0, 4], [2, 8, -6], [3, 7, 1]]

n = 6
mat = [[-2, -3, -6, -5, 50, 3],
       [8, 7, 10, -5, -3, 30],
       [6, 3, 70, 9, -20, -7],
       [-9, 9, -6, 7, 3, 2],
       [-1, 7, 7, 6, -4, 3],
       [8, 5, 6, -9, 40, 8]
       ]

s = DiagonalTraverse()
s.function(n, mat)
