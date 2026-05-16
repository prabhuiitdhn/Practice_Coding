"""
https://practice.geeksforgeeks.org/problems/reach-the-nth-point5433/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty
There are N points on the road ,you can step ahead by 1 or 2 . Find the number of ways you can reach at point N.
Input: N = 4
Output: 5
Explanation: Three ways to reach at 4th
point. They are {1, 1, 1, 1}, {1, 1, 2},
{1, 2, 1} {2, 1, 1}, {2, 2}.

Input: N = 5
Output: 8
Explanation: Three ways to reach at 5th
point. They are {1, 1, 1, 1, 1},
{1, 1, 1, 2}, {1, 1, 2, 1}, {1, 2, 1, 1},
{2, 1, 1, 1}{1, 2, 2}, {2, 1, 2}, {2, 2, 1}

"""


def nthPoint(n):
    def nthPointHelper(n):
        dp = [-1 for i in range(n + 2)]
        dp[n] = 1
        dp[n + 1] = 0
        for i in range(n - 1, 0, -1):
            dp[i] = dp[i + 1] + dp[i + 2]

        return dp[1] + dp[2]

    return nthPointHelper(n) % (10 ** 9 + 7)


n = 485
print(nthPoint(n))
