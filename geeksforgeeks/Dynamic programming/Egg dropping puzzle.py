"""
https://practice.geeksforgeeks.org/problems/egg-dropping-puzzle-1587115620/1?page=3&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty

Actually we needed to find the minimum trails which said the "maximum floor" where the egg can be dropped without breaking
intuition: https://www.youtube.com/watch?v=uBhSIKLlvdk
wikipage: https://en.wikipedia.org/wiki/Dynamic_programming#Egg_dropping_puzzle


dp(n, k): where n is no of eggs; k is the floor
dp(n, 0) = 0 # if n no of eggs are left but floor is none then "No" experiment will be left
dp(n, 1) = 1 # if n no of eggs are left but floor is 1 then only one experiment will tell that eggs breaks or not.
dp(1, k) = k # if only one egg is left to experiment from the kth floor then highest floor would be 'k'

dp(n, k) = 1 + min [this minimum will give the minimum of attempt for an egg experiment]
                (
                  max
                  (
                    dp[n-1][x-1], # this will give the maximum number of floor where the egg can be dropped without breaking.
                    dp[n][k-x]
                    NOTE: x is floor where the experiment have started, starts from x: 1, 2....k
                  )
                )
we do use x=1, 2, ...k which will determine what is maximum from bottom that egg can be dropped but it will not break.
bcz If we dropped the egg from kth floor then 2 possibilities:
1. Egg drops and breaks from the 10th floor then worst case of highest floor is 10th floor we have not experimented from less number of floor, It might break from the 9, 8, 7th floor
2. Egg drops but did not break then It is good news that we still can go to the next lower floor and experiment the same with same no of eggs

strong condition:
1. If egg drops and breaks from the kth floor then It would also break from k+1, k+2....k+infinite floor.
2. if egg dropps from k-1, k-2, ...k-k th floor and it break then it will also break from kth floor
so to find out the minimum floor where eggs can be dropped and it break would be starts from 0/1th floor to kth

dp(n, k) = 1 + min (dp[n-1][x-1]: this will start from 0th floor & check if eggs break , dp[n][k-x]: this will check if egg does not break from the k-x floor)
"""
import  sys

def eggDrop(n, k):
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(1, k + 1):
        dp[1][i] = i

    for j in range(1, n + 1):
        dp[j][1] = 1
        dp[j][0] = 0

    for nth in range(2, n + 1):
        for kth in range(2, k + 1):
            maxx = sys.maxsize
            for x in range(1, kth + 1):
                eggbreak = dp[nth - 1][x - 1]
                eggDidNotBreak = dp[nth][kth - x]
                min_ = min(maxx, 1 + max(eggbreak, eggDidNotBreak))
                maxx = min_
            dp[nth][kth] = maxx
    return dp[n][k]


n = 2
k = 4
print(eggDrop(n, k))
