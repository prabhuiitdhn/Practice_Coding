"""
https://practice.geeksforgeeks.org/problems/express-as-sum-of-power-of-natural-numbers5647/1?page=2&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=KLA%20Tencor&category[]=Recursion&sortBy=difficulty

given the number x = 10 and needed to find the ways for having multiple possible solutions for finding 10 with ^squares  of the natural numbers.

example: 10, which has only one possible ways: 1^ + 3^2
example: 100:
"""

import numpy as np


def numOfWays(x, n):
    dp = np.ones(shape=(1001, 1001)) * (-1)

    def helper(x, n, i):
        # It should return the list which will make sum of combinations 0
        # Stopping conditions
        if x == 0:
            # it shows that after subtracting the power it became 0
            # return count as 1 so that It is going to add the count say one more count we have with this combinations.
            return 1
        if i > x:
            return 0

        if dp[x][i] != -1:
            return dp[x][i] % (10 ** 7)
        # condition for backtracking
        if (i ** n) <= x:
            # backtracking should work
            dp[x][i] = helper(x - (i ** n), n, i + 1) + helper(x, n, i + 1)
        else:
            dp[x][i] = 0
            return dp[x][i] % (10 ** 7)

    helper(x, n, 1)


x = 10
n = 2

print(numOfWays(x, n))  # this should return all possible ways of having the sum x
