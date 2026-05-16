"""
https://practice.geeksforgeeks.org/problems/longest-palindromic-subsequence-1612327878/1?page=2&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty
Given a String, find the longest palindromic subsequence.
given a string needed to find out the longest subsequence can be found which are palindrome.

"""



def longestPalinSubseq(S):
    # code here
    def helper(s1, s2, a, b):
        dp = [[0 for _ in range(a + 1)] for _ in range(b + 1)]
        for i in range(1, a + 1):
            for j in range(1, b + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]

                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[i][j]

    str1 = S
    str2 = S[::-1]
    a = len(str1)
    return helper(str1, str2, a, a)


str1 = "bbabcbcab"
str2 = str1[::-1]
A = len(str1)
B = len(str2)
print(longestPalinSubseq(str1))
