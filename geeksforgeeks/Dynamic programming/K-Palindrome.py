"""
https://practice.geeksforgeeks.org/problems/find-if-string-is-k-palindrome-or-not1923/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty

input: str
K = this value represents number of char needed to be deleted and check whether it is a palindrome or not?
"""


def kPalindrome(str, n, k):
    """
    this is native solution & it worked but time complexity needs to be improved.
    @param str:
    @param n:
    @param k:
    @return:
    """
    def kPalindromeHelper(str, s, e, n, k):
        if s >= e:
            return 0
        if str[s] == str[e]:
            return kPalindromeHelper(str, s + 1, e - 1, n, k)

        return 1 + min(kPalindromeHelper(str, s + 1, e, n, k), kPalindromeHelper(str, s, e - 1, n, k))

    startIndex = 0
    endIndex = n - 1
    p = kPalindromeHelper(str, startIndex, endIndex, n, k)
    if n == 1:
        return 1
    if p == k:
        return 1
    else:
        return 0


def kPalindromeDP(str, n):
    # Code here
    str2 = str[::-1]
    strlength = len(str)
    dp = [[0 for i in range(strlength + 1)] for j in range(strlength + 1)]

    for i in range(1, strlength + 1):
        for j in range(1, strlength + 1):
            if str[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    no_of_deletion_required = strlength - dp[strlength][strlength]
    if strlength == 1:
        return 1
    if no_of_deletion_required <= n:
        return 1
    else:
        return 0

#
# str = "abcdecba"
# n = 8
# k = 1

#
# str = "abcdefcba"
# n = 9
# k = 1

# str = "wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco"
# n= 5

str = "nwnk"
n= 1
print(kPalindromeDP(str, n))
