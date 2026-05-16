"""
https://practice.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1?page=2&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty
needed to find minimum character which are matching on both string/

"""

def lcs(s1, s2, a,b): # optimised way using Iterative [DP]

    dp =[[0 for _ in range(a+1)] for _ in range(b+1)]
    for i in range(1, a+1):
        for j in range(1, b+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]

            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[i][j]

A=6
B=6

str1 = "ABCDGH"
str2 = "ACDGHR"
#
#
# # str1 = "ABC"
# # str2 = "ACB"
# A = len(str1)
# B= len(str2)

# str1 = "abcd"
# str2 = str1[::-1]
# A = len(str1)
# B = len(str2)
print(lcs(str1, str2, A, B))

