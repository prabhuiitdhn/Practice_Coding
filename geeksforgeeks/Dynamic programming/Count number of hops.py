"""
https://practice.geeksforgeeks.org/problems/count-number-of-hops-1587115620/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty

"""
def countWays(s, n):
    if s > n:
        return 0
    if s == n:
        return 1
    return countWays(s + 1, n) + countWays(s + 2, n) + countWays(s + 3, n)


def countWaysDPIterative(n):
    """
    The approach is iterative, to reach to BR(nXn index) we will start from 0th index, and each will have 3 possibilities
    to reach nxn index.
    if startIndex = 0, 3 chances: (startindex+1, n) + (startIndex+2, n)+ (startIndex+3, n)
    & it can call recursively upto maximum is (n, n) + (n+1,n) + (n+2, n)
    where: (n, n) = 1: which shows that reached to the destination
    (n+1, n) = 0 because It is not possible
    (n+2, n) =0 because it is also not possible.

    once it find (n, n)=1 , (n+1, n)=0 and (n+2, n) = 0 then recursively is coming back upto the 0th index.
    @param n:
    @return:
    Tabulation approach:
    Bottom-up approach.
    """
    dp = [-1] * (n + 3)
    dp[n], dp[n+1], dp[n+2] = 1, 0, 0 # assigning the final three possible.

    for j in range(n-1, -1, -1):
        # Iteratively coming back from bottom to top
        # (4, n) = (5, n)+(6, n)+(7, n)
        dp[j] = dp[j + 1] + dp[j + 2] + dp[j + 3]
    return dp[0] % (10**9+7)


n = 54
s = 0
# print(countWays(s, n))

print(countWaysDPIterative(n))
