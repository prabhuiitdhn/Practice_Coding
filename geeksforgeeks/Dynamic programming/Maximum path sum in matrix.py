"""
https://practice.geeksforgeeks.org/problems/path-in-matrix3805/1?page=2&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty



"""


def maximumPath(n, matrix):
    """
    The matrix is NxN
    Start from any column from row 0
    possible move:
                {r, c}
                  =
    {{r+1, c-1}, {r+1, c}, {r+1, c+1}}

    @param N:
    @param matrix:
    @return:  highest maximum path sum
    """

    def maximumPathHelper(row, col, n, matrix):
        _max = 0
        if row < 0 or col < 0 or row > n - 1 or col > n - 1:
            return 0

        if 0 <= row < n and 0 <= col < n:
            first = maximumPathHelper(row + 1, col - 1, n, matrix)
            second = maximumPathHelper(row + 1, col, n, matrix)
            third = maximumPathHelper(row + 1, col + 1, n, matrix)
            _max = max(first, second, third)

        return matrix[row][col] + _max

    if n == 0:
        return 0
    if n == 1:
        return matrix[0][0]

    sumList = []
    for col in range(n):
        sumList.append(maximumPathHelper(0, col, n, matrix))
    return max(sumList)


def maximumPathDPRecursive(n, matrix):
    """
    The matrix is NxN
    Start from any column from row 0
    possible move:
                {r, c}
                  =
    {{r+1, c-1}, {r+1, c}, {r+1, c+1}}

    @param N:
    @param matrix:
    @return:  highest maximum path sum
    """

    def maximumPathHelper(row,
                          col,
                          n,
                          matrix,
                          dp):

        if row < 0 or col < 0 or row > n - 1 or col > n - 1:
            return 0

        if col == 0:
            if dp[row + 1][col] == 0:
                dp[row + 1][col] = maximumPathHelper(row + 1, col, n, matrix, dp)
            if dp[row + 1][col + 1] == 0:
                dp[row + 1][col + 1] = maximumPathHelper(row + 1, col + 1, n, matrix, dp)

            if dp[row][col] == 0:
                dp[row][col] = matrix[row][col] + max(dp[row + 1][col], dp[row + 1][col + 1])

        if col == n - 1:
            if dp[row + 1][col - 1] == 0:
                dp[row + 1][col - 1] = maximumPathHelper(row + 1, col - 1, n, matrix, dp)

            if dp[row + 1][col] == 0:
                dp[row + 1][col] = maximumPathHelper(row + 1, col, n, matrix, dp)

            if dp[row][col] == 0:
                dp[row][col] = matrix[row][col] + max(dp[row + 1][col - 1], dp[row + 1][col])

        if 0 <= row < n and 0 < col < n - 1:
            if dp[row + 1][col - 1] == 0:
                dp[row + 1][col - 1] = maximumPathHelper(row + 1, col - 1, n, matrix, dp)

            if dp[row + 1][col] == 0:
                dp[row + 1][col] = maximumPathHelper(row + 1, col, n, matrix, dp)
            if dp[row + 1][col + 1] == 0:
                dp[row + 1][col + 1] = maximumPathHelper(row + 1, col + 1, n, matrix, dp)

            if dp[row][col] == 0:
                dp[row][col] = matrix[row][col] + max(dp[row + 1][col - 1], dp[row + 1][col], dp[row + 1][col + 1])

        return dp[row][col]

    if n == 0:
        return 0
    if n == 1:
        return matrix[0][0]

    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    sumList = []
    for col in range(n):
        sumList.append(maximumPathHelper(0, col, n, matrix, dp))
    return max(sumList)


def maximumPathDPIterative(n, matrix):
    def maximumPathHelper(N, dp):

        for i in range(1, N):
            for j in range(N):
                if j == 0:
                    dp[i][j] += max(dp[i - 1][j], dp[i - 1][j + 1])
                elif j == N - 1:

                    dp[i][j] += max(dp[i - 1][j], dp[i - 1][j - 1])
                else:
                    dp[i][j] += max(dp[i - 1][j], dp[i - 1][j - 1], dp[i - 1][j + 1])

        return max(dp[N - 1])

    return maximumPathHelper(n, matrix)
# N = 2
# matrix = [[348, 391],
#           [618, 193]]
# N = 3
# matrix = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]

N = 4
matrix = [[1, 2, 3, 4],
          [4, 5, 6, 7],
          [8, 9, 10, 11],
          [12, 13, 14, 15]]
print(maximumPath(N, matrix))
print(maximumPathDPRecursive(N, matrix))
print(maximumPathDPIterative(N, matrix))
