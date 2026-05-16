"""
https://practice.geeksforgeeks.org/problems/edit-distance3702/1?page=2&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty

this problem is about know what is minimu number of operation [insertion, deletion, replacement] needed to convert string S to T
so, S and T two string is being given and needed to find out min no of operation required to convert S to T

so, basically If size(S)< size(T): insertion needed
              if size(S)> size(T): deletion needed in string S
              but If size(s)==Size(T) but some both strings are not matching then definitely needed to replace the elements.
approach:
1. traverse each string and check what operation needed to do it. nased on native concepts.
2. using dynamic programming.

"""

#
# def editDistanceDPRecursive(s, t):
#     def solve(s1, s2, i, j, dp):
#         if i == len(s1):
#             return (len(s2) - j)
#         if j == len(s2):
#             return (len(s1) - i)
#         if dp[i][j] != -1:
#             return dp[i][j]
#
#         ans = 0
#         if s1[i] == s2[j]:
#             return solve(s1, s2, i + 1, j + 1, dp)
#         else:
#             ins = 1 + solve(s1, s2, i, j + 1, dp)
#             delt = 1 + solve(s1, s2, i + 1, j, dp)
#             repl = 1 + solve(s1, s2, i + 1, j + 1, dp)
#             ans = min(ins, min(delt, repl))
#         dp[i][j] = ans
#         return dp[i][j]
#
#     i = 0
#     j = 0
#     dp = [[-1 for i in range(len(t) + 1)] for j in range(len(s) + 1)]
#     return solve(s, t, i, j, dp)
#
# def editDistanceDPIterative(s, t):
#     """
#     Please solve it.
#     @param s:
#     @param t:
#     @return:
#     """
#     return
#
# # s = "dbb"
# # t = "fdfaccddfac"


class Solution(object):
    def minDistance(self, word1, word2):
        def solve(s1, s2, i, j, dp):
            if i == len(s1):
                return (len(s2) - j)
            if j == len(s2):
                return (len(s1) - i)

            if dp[i][j] != -1:
                return dp[i][j]

            ans = 0
            if s1[i] == s2[j]:
                return solve(s1, s2, i + 1, j + 1, dp)
            else:
                ins = 1 + solve(s1, s2, i, j + 1, dp)
                delt = 1 + solve(s1, s2, i + 1, j, dp)
                repl = 1 + solve(s1, s2, i + 1, j + 1, dp)
                ans = min(ins, min(delt, repl))
            dp[i][j] = ans
            return dp[i][j]

        i = 0
        j = 0
        dp = [[-1 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
        return solve(word1, word2, i, j, dp)


word1 = "horse"
word2 = "ros"
# print(editDistanceDPRecursive(word1, word2))
# print(editDistanceDPIterative(s, t))


s = Solution().minDistance(word1, word2)
print(s)