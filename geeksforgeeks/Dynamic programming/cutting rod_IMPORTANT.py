"""
https://practice.geeksforgeeks.org/problems/rod-cutting0840/1?page=1&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty
Please understand this
This contains
1. recursion [native approach]
2. DP recursive
3. DP iterative [2D tabulation]
4. DP iterative more optmised (1D tabulation)
"""


def cutRod(price, n):
    """
    This is native approach
    @param price:
    @param n:
    @return:
    """

    def cuttingRoadHelper(roadIndexStart, n, price):
        if roadIndexStart == 0:
            # this is basically talking about index 0 of road i.e length of 1
            # if the rod length is 1 then we need to have N rod of length 1
            return n * price[0]

        taken = 0
        not_taken = cuttingRoadHelper(roadIndexStart - 1, n, price)
        if roadIndexStart + 1 <= n:
            taken = price[roadIndexStart] + cuttingRoadHelper(roadIndexStart, n - (roadIndexStart + 1), price)

        return max(taken, not_taken)

    roadIndexStart = n - 1
    return cuttingRoadHelper(roadIndexStart, n, price)


def cutRodDPRecursive(price, n):
    def cuttingRoadHelper(roadIndexStart,
                          n,
                          price,
                          dp):
        """
        this is recursive approach for an DP
        @param roadIndexStart:
        @param n:
        @param price:
        @param dp:
        @return:
        """
        if roadIndexStart == 0:
            # this is basically talking about index 0 of road i.e length of 1
            # if the rod length is 1 then we need to have N rod of length 1
            return n * price[0]

        # taken = 0
        if dp[roadIndexStart - 1][n] == -1:
            # this is for not taken
            dp[roadIndexStart - 1][n] = cuttingRoadHelper(roadIndexStart - 1, n, price, dp)
        if roadIndexStart + 1 <= n:
            # this is for taken
            if dp[roadIndexStart][n] == -1:
                dp[roadIndexStart][n - (roadIndexStart + 1)] = cuttingRoadHelper(roadIndexStart,
                                                                                 n - (roadIndexStart + 1), price, dp)
                dp[roadIndexStart][n] = price[roadIndexStart] + dp[roadIndexStart][n - (roadIndexStart + 1)]

        return max(dp[roadIndexStart - 1][n], dp[roadIndexStart][n])

    roadIndexStart = n - 1
    import numpy as np
    dp = np.ones(shape=(n, n + 1), dtype=float) * -1
    for i in range(1, n):
        dp[0][i] = price[i - 1]

    return int(cuttingRoadHelper(roadIndexStart, n, price, dp))


def cutRodDPIterative(price, n):
    """
    This is iterative approch which is faster than memoisation, this is tablulation. Bottom up approach
    @param price:
    @param n:
    @return:
    """

    def cuttingRoadHelper(totalRodLength,
                          price,
                          dp):

        for roadIndexStart in range(1, n):  # this denotes the roadIndexStart
            for N in range(totalRodLength + 1):  # this indicates the rod length
                taken = 0
                notTaken = dp[roadIndexStart - 1][N]  # if it is not taken then It will consider next index
                if roadIndexStart + 1 <= N:  # if it satisfy the condition i.e if the rod length is still remaining then
                    # it will take
                    taken = price[roadIndexStart] + dp[roadIndexStart][N - (roadIndexStart + 1)]
                    # this is taking the current price remaining rod length index price.
                dp[roadIndexStart][N] = max(notTaken, taken)

        return dp[totalRodLength - 1][totalRodLength]

    # import numpy as np
    # dp = np.ones(shape=(n, n + 1), dtype=float) * -1

    dp = [[-1 for i in range(n + 1)] for j in range(n)]
    for i in range(n + 1):
        dp[0][i] = i * price[0]

    return cuttingRoadHelper(n, price, dp)


def cutRodDPIterativeMoreOptimised(price, N):
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(i):
            dp[i] = max(dp[i], price[j] + dp[i - j - 1])
    return dp[N]


# N = 8
# price = [1, 5, 8, 9, 10, 17, 17, 20]

N = 5
price = [2, 5, 7, 8, 10]

print(cutRod(price, N))
print(cutRodDPRecursive(price, N))
print(cutRodDPIterative(price, N))
print(cutRodDPIterativeMoreOptimised(price, N))
