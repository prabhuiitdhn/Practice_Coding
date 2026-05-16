"""
https://practice.geeksforgeeks.org/problems/form-a-palindrome2544/1?page=2&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty

https://practice.geeksforgeeks.org/problems/form-a-palindrome1455/1?page=2&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty

"""


def countMin(str):
    def helper(str, n, i, j):
        if i < n and j >= 0:
            if str[i] == str[j]:
                return helper(str, n, i + 1, j - 1)
            else:
                return 1 + min(helper(str, n, i + 1, j), helper(str, n, i, j - 1))
        return 0

    n = len(str)
    return helper(str, n, 0, n - 1)


def countMinDPIterative(str):
    n = len(str)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i_ in range(n):
        dp[i_][i_] = 0

    for gap in range(1, n):
        for i in range(n - gap):
            if str[i] == str[i + gap]:
                dp[i][i + gap] = dp[i + 1][i + gap - 1]
            else:
                dp[i][i + gap] = 1 + min(dp[i+1][i + gap], dp[i][i + gap - 1])

    return dp[0][n-1]


str = "babaab"
n = len(str)
print(countMin(str))
print(countMinDPIterative(str))
