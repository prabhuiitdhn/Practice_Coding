"""
https://practice.geeksforgeeks.org/problems/shortest-common-supersequence0322/1?page=2&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty
So basically we will have two strings and needed to findout how many substring can be created using the strings's substrings.

In this approach, we are calculating the common subsequence between 2 string and while creating the full string combination of two strings. reming the common substring and return the length of substring.
"""


# def shortestCommonSupersequence(s1, s2, m, n):
#     def helper(s1, s2, m, n,
#                p1,
#                p2,
#                dp):
#         if p1 < 0 or p2 < 0:
#             return 0
#         if dp[p1][p2] != -1:
#             return dp[p1][p2]
#
#         if s1[p1] == s2[p2]:
#             dp[p1][p2] = 1 + helper(s1, s2, m, n, p1 - 1, p2 - 1, dp)
#             return dp[p1][p2]
#
#         if dp[p1 + 1][p2] == -1:
#             dp[p1 + 1][p2] = helper(s1, s2, m, n, p1 - 1, p2, dp)
#         if dp[p1][p2 + 1] == -1:
#             dp[p1][p2 + 1] = helper(s1, s2, m, n, p1, p2 - 1, dp)
#
#         dp[p1][p2] = max(dp[p1 + 1][p2], dp[p1][p2 + 1])
#         return dp[p1][p2]
#
#     p1 = m - 1
#     p2 = n - 1
#     dp = [[-1 for i in range(m + 1)] for j in range(n + 1)]
#     return (m + n) - helper(s1, s2, m, n, p1, p2, dp)


def shortestCommonSupersequenceOptimised(s1, s2, m, n):
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]

    # Base case : covered in dp, if i==0 or j==0: return 0
    # for i in range(n+1):
    #     for j in range(m+1):
    #         dp[i][j]=0

    for i1 in range(1, m + 1):
        for i2 in range(1, n + 1):
            if s1[i1 - 1] == s2[i2 - 1]:
                dp[i1][i2] = 1 + dp[i1 - 1][i2 - 1]
            else:
                dp[i1][i2] = 0 + max(dp[i1 - 1][i2], dp[i1][i2 - 1])

    lcs = dp[m][n]
    # adding the common subsequence once
    mini = (len(s1) - lcs) + (len(s2) - lcs) + (lcs)
    return mini


#
# s1 = "hxmngqmf"
# s2 = "gnapcnty"

s1 = "abcd"
s2 = "xycd"
m = len(s1)
n = len(s2)
# needed to find out the string which is combinations of subsequence of s1 and s2
print(shortestCommonSupersequenceOptimised(s1, s2, m, n))
