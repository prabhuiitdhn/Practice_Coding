"""

"""

def maxProfit(n, share):
    dp = [0 for i in range(n)]
    dp[0] = 0
    _min = share[0]
    for i in range(1, n):
        _min = min(_min, share[i])
        dp[i]= max(dp[i-1], share[i]-_min)

    _max = share[n-1]
    for i in range(n-2, -1, -1):
        _max = max(_max, share[i])
        dp[i]=max(dp[i+1], dp[i]+_max-share[i])

    return dp[0]

n = 6
share = [10, 22, 5, 75, 65, 80]
print(maxProfit(n, share))
