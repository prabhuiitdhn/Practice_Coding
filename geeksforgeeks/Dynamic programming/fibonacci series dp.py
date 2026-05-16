"""
https://www.geeksforgeeks.org/introduction-to-dynamic-programming-data-structures-and-algorithm-tutorials/
https://www.geeksforgeeks.org/what-is-memoization-a-complete-tutorial/

Simple example using DP
1. memoisation [1D memoisation- which will have 1 parameter as variable.]

"""
import numpy as np

def fibbonacci(dp, n):
    """
    memoization approach:
        Stores the result in cache so that It can be used later.
        Which is suitable for smaller set of inputs.
        Recursive implementation
        Used when the subproblems have overlapping subproblems


    @param dp: it is an array which stores the value in the index.
    @param n:
    @return:
    """
    if n == 0:
        return dp[0]
    if n == 1:
        return dp[1]

    if n > 1 and dp[n] == -1:
        dp[n] = fibbonacci(dp, n - 1) + fibbonacci(dp, n - 2)

    return dp[n]

def fibonacci_impproved1(dp, n):
    """
    Tabulation implementation:
        Stores the results of subproblems in a table
        Iterative implementation
        Well-suited for problems with a large set of inputs
        Used when the subproblems do not overlap

    as we already know that dp[0] & dp[1] is already known then I can start calculating using given and proceed further
    until the n which has to be calculated.
    @param dp:
    @param n:
    @return:
    """
    if n<=1:
        return dp[n]
    for i in range(2, n+1):
        """
        we do not have subproblem overlapping bcz we are calculating iteratively so for each loop 
        we are calculating the next and keeping it. 
        """
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

def fibonacci_impproved2(n):
    """
    As we know that fibonaaci is only depending on two previous number then why to store 'n' no of array
    so just to store two previous number.
    Even storage is not required in this case. Just to have prevPrev, prev pointer to store the current value
    @param dp:
    @param n:
    @return:
    """
    prevprev = 0
    prev = 1
    current = 1
    for i in range(2, n+1):
        current = prevprev + prev
        prevprev = prev
        prev = current
    return current

n = 10
dp = np.ones(n+1) * -1
dp[0] = 0
dp[1] = 1
# print(fibbonacci(dp, n))
# print(fibonacci_impproved1(dp, n))
print(fibonacci_impproved2(n))