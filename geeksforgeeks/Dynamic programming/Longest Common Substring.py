"""

"""

def longestCommonSubstr(s1, s2, a, b):
    dp = [[0 for _ in range(b + 1)] for _ in range(a + 1)]
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:
                dp[i][j] = 0

    _max = -9999

    for i in range(a+1):
        for j in range(b+1):
            _max = max(_max, dp[i][j])

    return _max




# A = 4
# B = 6
# str1 = "adac"
# str2 ="adadac"


str1 = "bbabcbcab"
str2 = str1[::-1]
A = len(str1)
B = len(str2)
print(longestCommonSubstr(str1,str2, A, B))
