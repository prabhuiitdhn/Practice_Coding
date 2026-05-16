"""
https://practice.geeksforgeeks.org/problems/minimum-deletitions1648/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty

given a string of S as input, and needed to find out the number of character which can delete and become the palindrome.
"""
# def function(str, s, e):
#     if s>e: return 0
#     if str[s] == str[e]:
#         return 1 + function(str, s+1, e-1)
#     if s==e-1 and str[s] != str[e]:
#         return 0
#     return function(str, s+1, e) + function(str, s, e-1)


def functionHelper(str, s, e):
    """
    This is native solution
    @param str:
    @param s:
    @param e:
    @return:
    """
    if s >= e: return 0
    if str[s] == str[e]:
        functionHelper(str, s + 1, e - 1)
    if str[s] != str[e]:
        return 1 + min(functionHelper(str, s + 1, e), functionHelper(str, s, e - 1))

def functionHelperDPRecursive(str, s, e, dp):
    """
    this is using Rcursive DP solution
    @param str:
    @param s:
    @param e:
    @param dp:
    @return:
    """
    if s >= e:
        return 0
    if str[s] == str[e]:
        dp[s][e] = functionHelperDPRecursive(str, s + 1, e - 1, dp)
    if str[s] != str[e]:
        if dp[s][e] == -1:
            dp[s][e] = 1 + min(functionHelperDPRecursive(str, s + 1, e, dp), functionHelperDPRecursive(str, s, e - 1, dp))

    return dp[s][e]


def functionHelperDPIterative(S, n):
    """
    this is using Rcursive DP solution
    @param str:
    @param s:
    @param e:
    @param dp:
    @return:
    """
    S2 = S[::-1]
    dp = [[0 for i in range(n + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if S[i - 1] == S2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return n - dp[n][n]


def minimumNumberOfDeletions(s):
    startIndex = 0
    endIndex = len(s) - 1

    # return functionHelperDPRecursive(s, startIndex, endIndex, dp)
    return functionHelperDPIterative(s, len(s))


s = "aebcbda"
# s = "geeksforgeeks"
print(minimumNumberOfDeletions(s))
