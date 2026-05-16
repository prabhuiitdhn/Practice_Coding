"""
https://practice.geeksforgeeks.org/problems/longest-arithmetic-progression1019/1?page=1&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty
given an array called arr[] of sorted integers having no duplicates, find the length of longest arithmentics progression in it.

example:
a = [1, 7, 10, 13, 14, 19]
output: 4
because the longest is [1, 7, 13, 19]
time complexity: O(N^2)
space: O(N^2)

1. sorted
2. +ve/-ve/0 could be there.


approach:
It is so simple: follow this https://www.youtube.com/watch?v=YaMcX7sem70
for more understanding and concepts: create a nxn distance matrxi and store the distance in each block which will say difference between i and jindex.

all the difference put into the dict and check whether the current distance is already in the dict or not? if already there then increase the count by 1 if not the put it as 2: bcz it is atleast one pair of llp we can found

note:
we will at least get 2 as llp bcz we are trying to calculate the AP between 2 number which is at least possible
so if n==1
the AP is 1
if n==2
then AP is 2 bcz AP defines between the 2 numbers.


"""

def lengthOfLongestAP(A, n):

    a = A
    if n <= 2:
        return n

    ans = 0
    dp = [{} for i in range(n + 1)]
    for i in range(1, n):
        for j in range(0, i):
            diff = a[i] - a[j]
            cnt = 1
            if diff in dp[j]:
                cnt = dp[j][diff]
            dp[i][diff] = 1 + cnt
            ans = max(ans, dp[i][diff])
    return ans


arr=[1, 7, 10, 13, 14, 19]
n= len(arr)
print(lengthOfLongestAP(arr, n))