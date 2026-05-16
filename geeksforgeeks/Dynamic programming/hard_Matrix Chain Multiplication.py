import numpy as np

"""
NEEDED TO WORK ON IT.
"""


def matrixMultiplication(n, arr):
    dp = [[0 for _ in range(n)] for _ in range(n)]

    final_ans = 0

    for gap in range(1, n - 1):
        steps = 999999999
        for j in range(n - gap - 1):
            if gap == 1:
                steps = min(steps, arr[j] * arr[j + 1] * arr[j + 2])

            if gap == 2:
                steps = min(steps, min(
                    arr[j] * arr[j + gap] * arr[j + gap + 1],
                    arr[j] * arr[j + 1] * arr[j + gap + 1]
                ))
        final_ans += steps
    return final_ans


def matrixMultiplication2(n, arr):
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n - 1, 0, -1):
        for j in range(i + 1, n):
            min_ = 9999999999
            for k in range(i, j):
                steps = arr[i - 1] * arr[k] * arr[j] + dp[i][k] + dp[k + 1][j]
                min_ = min(min_, steps)
            dp[i][j] = min_

    return dp[1][n - 1]


N = 5
arr = [40, 20, 30, 10, 30]
print(matrixMultiplication2(N, arr))
