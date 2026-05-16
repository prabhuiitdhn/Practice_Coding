"""
https://practice.geeksforgeeks.org/problems/gold-mine-problem2608/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty
given a gold mine Called M [contains the weight of gold in tons] of (nXm) dimensions. Iniatially the miner can start from any row in the first column

from one cell the miner can move:
1. diagonally up towards the right (i-1, j+1)
2. to the right(i, j+1)
3. diagonally down towards the right(i+1, j+1)

"""


def maxGoldNative(n, m, M):
    def maxGoldHelper(start1, start2, n, m, M) -> float:
        # if 0 > start1 > n - 1 or start2 > m - 1:
        #     return 0

        if start1 < 0:
            return 0
        if start2 < 0:
            return 0
        if start1 > n - 1:
            return 0
        if start2 > m - 1:
            return 0
        diagonalUp = maxGoldHelper(start1 - 1, start2 + 1, n, m, M)
        right = maxGoldHelper(start1, start2 + 1, n, m, M)
        diagonalDown = maxGoldHelper(start1 + 1, start2 + 1, n, m, M)
        return M[start1][start2] + max(diagonalUp, right, diagonalDown)

    maximum = []
    for i in range(n):
        maximum.append(maxGoldHelper(i, 0, n, m, M))

    return max(maximum)


def maxGoldRecursiveDP(n, m, M):
    def maxGoldHelper(start1, start2, n, m, M, dp) -> float:
        # if 0 > start1 > n - 1 or start2 > m - 1:
        #     return 0

        if start1 < 0:
            return 0
        if start2 < 0:
            return 0
        if start1 > n - 1:
            return 0
        if start2 > m - 1:
            return 0
        if start1 == 0:
            # if dp[start1 - 1][start2 + 1] == -1:
            #     dp[start1 - 1][start2 + 1] = maxGoldHelper(start1 - 1, start2 + 1, n, m, M, dp)
            if dp[start1][start2 + 1] == -1:
                dp[start1][start2 + 1] = maxGoldHelper(start1, start2 + 1, n, m, M, dp)
            if dp[start1 + 1][start2 + 1] == -1:
                dp[start1 + 1][start2 + 1] = maxGoldHelper(start1 + 1, start2 + 1, n, m, M, dp)
            dp[start1][start2] = M[start1][start2] + max(dp[start1][start2 + 1],
                                                         dp[start1 + 1][start2 + 1])
        else:
            if dp[start1 - 1][start2 + 1] == -1:
                dp[start1 - 1][start2 + 1] = maxGoldHelper(start1 - 1, start2 + 1, n, m, M, dp)
            if dp[start1][start2 + 1] == -1:
                dp[start1][start2 + 1] = maxGoldHelper(start1, start2 + 1, n, m, M, dp)
            if dp[start1 + 1][start2 + 1] == -1:
                dp[start1 + 1][start2 + 1] = maxGoldHelper(start1 + 1, start2 + 1, n, m, M, dp)

            dp[start1][start2] = M[start1][start2] + max(dp[start1 - 1][start2 + 1],
                                                         dp[start1][start2 + 1],
                                                         dp[start1 + 1][start2 + 1])

        return dp[start1][start2]

    maximum = []
    dp = [[-1 for i in range(m + 1)] for j in range(n + 1)]
    for i in range(n):
        dp[i][0] = M[i][0]
    for i in range(n):
        maximum.append(maxGoldHelper(i, 0, n, m, M, dp))

    return max(maximum)


# n = 3
# m = 3
# M = [[1, 3, 3], [2, 1, 4], [0, 6, 4]]

# n = 4
# m = 4
# M = [[1, 3, 1, 5],
#      [2, 2, 4, 1],
#      [5, 0, 2, 3],
#      [0, 6, 1, 2]]

# n = 7
# m = 4
# M = [[77,15,93,35],
#      [86, 92, 49, 21],
#      [62, 27, 90, 59],
#      [63, 26, 40, 26],
#      [72, 36,11, 68],
#      [67, 29,82 ,30],
#      [62,23,67,35]]


n = 4
m = 7
M = [[77, 15, 93, 35, 86, 92, 49],
     [21, 62, 27, 90, 59, 63, 26],
     [40, 26, 72, 36, 11, 68, 67],
     [29, 82, 30, 62, 23, 67, 35]]

print(maxGoldNative(n, m, M))
print(maxGoldRecursiveDP(n, m, M))
