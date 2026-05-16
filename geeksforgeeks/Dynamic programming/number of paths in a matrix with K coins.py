import numpy as np


def numberOfPath1(N, K, arr):
    # basic solution using recursive
    # using recursive but won't work for all the cases.
    def calculate(i, j, N, K, arr):
        if i >= N or j >= N:
            return 0
        if K == arr[i][j] and i == N - 1 and j == N - 1:
            return 1

        return calculate(i + 1, j, N, K - arr[i][j], arr) + calculate(i, j + 1, N, K - arr[i][j], arr)

    return calculate(0, 0, N, K, arr)


def numberOfPath2(N, K, arr):
    # It optimise the code and uses DP but also does not work, bcz It gives memory error and It might be bcz we are using array
    dp = np.ones((N, N, 100000)) * (-1)

    def calculate(i, j, N, K, arr):
        if i >= N or j >= N:
            return 0

        if i == N - 1 and j == N - 1:
            return K == arr[i][j]
        if dp[i][j][K] != -1:
            return dp[i][j][K]

        dp[i][j][K] = calculate(i + 1, j, N, K - arr[i][j], arr) + calculate(i, j + 1, N, K - arr[i][j], arr)
        return dp[i][j][K]

    return int(calculate(0, 0, N, K, arr))


def numberOfPath4(N, K, arr):
    # USing DP but creating with Dictionary
    memo = {}

    def helper(i, j, k):
        # If we are out of bounds or the remaining coins are negative, return 0
        if i >= N or j >= N or k < 0:
            return 0

        # If we have reached the bottom-right cell, return 1 if remaining coins is equal to the cell value,
        # otherwise return 0
        if i == N - 1 and j == N - 1:
            return 1 if k == arr[i][j] else 0

        # If the current state is in the memo dictionary, return the cached result
        if (i, j, k) in memo:
            return memo[(i, j, k)]

        # Calculate the number of ways to collect exactly k coins while moving right or down
        ways = helper(i + 1, j, k - arr[i][j]) + helper(i, j + 1, k - arr[i][j])

        # Store the calculated number of ways in the memo dictionary and return it
        memo[(i, j, k)] = ways
        return ways

    # Call the helper function to compute the number of ways to collect exactly K coins
    return helper(0, 0, K)


# arr = [[1, 2, 3], [4, 6, 5], [9, 8, 7]]
arr = [[1, 2, 3], [4, 6, 5], [3, 2, 1]]
N = 3
K = 12

num = numberOfPath4(N, K, arr)
print(num)
