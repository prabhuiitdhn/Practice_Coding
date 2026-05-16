"""
https://practice.geeksforgeeks.org/problems/count-all-possible-paths-from-top-left-to-bottom-right3011/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty
https://practice.geeksforgeeks.org/problems/number-of-paths0926/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty

reaching topleft to bottom right, find the number of ways to reach from TL to BR
"""
def numberOfPaths(m, n, s, e, dp):
    if s > m - 1 or e > n - 1:
        return 0
    if s == m - 1 and e == n - 1:
        dp[s][e] = 1
    if dp[s][e] == -1:
        dp[s][e] = numberOfPaths(m, n, s + 1, e, dp) + numberOfPaths(m, n, s, e + 1, dp)
    return dp[s][e] % (10**9+7)


def numberOfPathsNativeAlgo(m, n, s, e):
    if s > m - 1 or e > n - 1:
        return 0
    if s == m - 1 and e == n - 1:
        return 1
    return numberOfPathsNativeAlgo(m, n, s + 1, e) + numberOfPathsNativeAlgo(m, n, s, e + 1)


m = 3
n = 4
startIndex = 0
endIndex = 0
dp = [[-1 for i in range(n + 1)] for j in range(m + 1)]
# print(numberOfPathsNativeAlgo(m, n, startIndex, endIndex))
print(numberOfPaths(m, n, startIndex, endIndex, dp))
