"""
IMPORTANT TO READ:
https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/


https://practice.geeksforgeeks.org/problems/max-sum-without-adjacents2430/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty

this problem is about finding the maximum sum of the sub sequence but the elements in the sequence should not adjacent.
So, basically needed to take the elements in the subsequence which can make the maximum sum.

https://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/
Based on the description & https://www.youtube.com/watch?v=GrMBfJNk_NY

The explaination come into this way

we needed to take care of two things.
1. pickedOne: If we pick the element 'i' in the sequence then we won;t pick the i+1 in the subsequnce and we will pick
    i+2 in the sequence.
2. NotPickedOne: if we are not picking the i then we can definitely pick i+1

so, pick = a[i] + findMaxSum(i+2, array) # if i is considered then i+1 will not be consider and needed to check the maximum sum between (i+2 to all)
    not_picked = findMaxSum(i+1, array) # if we are not considering i then we will finding the maximum sum from (i+1 to all)

    return max(pick, not_picked.)

"""


def findMaxSum(arr, index):
    """
    This is naive solution.
    @param arr: elements in the array of length n
    @param n: n is length of the array
    @return: maximum sum of subsequence without adjacent elements.
    """
    if index > len(arr) - 1:
        return 0

    if index < 0:
        return 0

    pick = arr[index] + findMaxSum(arr, index + 2)
    notPicked = findMaxSum(arr, index + 1)

    return max(pick, notPicked)


def findMaxSumUsingRecursive(arr, dp, index):
    """
    this is based on recursive calculation: Bcz findMaxSum is recursively calculating the value and putting into the DP
    This is using dynamic programming. using the memoisation, storing the value which is already being calculated.
    @param arr: elements in the array of length n
    @param n: n is length of the array
    @return: maximum sum of subsequence without adjacent elements.
    """
    if index > len(arr) - 1:
        return 0

    if index < 0:
        return 0

    if dp[index] != -1:
        return dp[index]
    pick = arr[index] + findMaxSumUsingRecursive(arr, dp, index + 2)
    notPicked = findMaxSumUsingRecursive(arr, dp, index + 1)
    dp[index] = max(pick, notPicked)
    return dp[index]

def findmaxSumIterative(arr, n):
    """
    This appraoch is based on Iterative calculation the current will depend on the previous calculated value.
    Approach:
    If we are into the ith Index then two possibilities
    1. The maximum sum will be until ith Index is maxSum + arr[i]  [Including arr[i]]//Bcz it is being picked.
    2. the maximum sum will be until ith Index is maxSum excluding arr[i]
    So, we have Storage DP[N][2]
    DP[i][0]: this is to store maximum sum without ith Index.
    DP[i][1]: this is to store maximum sum with ith Index.

    DP[i][0] = max(DP[i-1][0], dp[i-1][1]) # THIS IS FINDING THE MAXIMUM SUM WHICH CAME PREVIOUSLY WITH THE INC
    DP[i][1] = DP[i-1][0] + arr[i] # IT IS INCLUDING THE MAXSUM TILL iTH INDEX WITH ARR[INDEX]

    @param arr: the array which contains the element.
    @param n: length of array
    @return: the maximum sum of subsequence which has length n
    """

    # assigning the DP with NX2
    dp = [[0 for i in range(2)] for j in range(n)]

    # initialisation of dp[0][0]
    dp[0][0] = 0 # bcz it does not exit dp[-1]
    dp[0][1] = arr[0] # if dp[-1] does not exist then we just to include the arr[0]; bcz this will the maximum value

    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]) # it is giving just the maximum sum until the last index
        dp[i][1] = dp[i-1][0] + arr[i] # dp[i-1] has the maximum sum and adding arr[index] for next maximum sum.

    return max(dp[n-1][0], dp[n-1][1])


def findMaxSumDPPointer(arr):
    """
    we only care about the maximum value until the last index. then If we all current value If are including in the maximum sum
    or If not then currentMaximumSum will be the maximumSum from the last index.
    @param arr:
    @return:
    """
    incl = 0 # THis is including the current array value
    excl = 0 # this is not including the current array value
    for i in arr:
        # Current max excluding i
        new_excl = max(excl, incl) # It is finding the maximum value (including array value, excluding array value)

        # Current max including i
        incl = excl + i # each time we add the current array value if we including the current index value
        excl = new_excl # other wise last will the maximum valye

    # Return max of incl and excl
    return max(excl, incl)

arr = [5, 5, 10, 100, 10, 5]
# n = len(arr)
# print(findMaxSum(arr, 0)) # using naive approach
dp = [-1] * len(arr)
print(findmaxSumIterative(arr, len(arr)))
