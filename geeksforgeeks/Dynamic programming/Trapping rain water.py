"""
https://practice.geeksforgeeks.org/problems/trapping-rain-water-1587115621/1?page=1&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty
https://www.interviewbit.com/blog/trapping-rain-water/

This is about the problem where we need to find the maximum water we can collect between the blocks we have.The empty
space will collect the water.
So assume, the left side is 2 and immediate right side is 3 the 2,3[we plot the block] then we con't store the water bcz it is flow at 2 block
another example:
2, 0, 3, in this case, we can only collect two unit of water in between 2 block and 3 block
      --
--    --
-- -- --
So, basically would be approach to find the left side biggest block and right side biggest block, once we find out the
block then we can calculate how much blocks we can have water trapped.
"""


def trappingWater(A, N):
    """
    This is a native approach to solve the problem.
    So, basically we are finding the leftSideBiggest block, and rightSideBiggest block and between that we can calculate the trapped water.
    @param A:
    @param N:
    @return:
    """
    res = 0
    for i in range(1, N - 1):  # starting from 1 index.
        left_max = A[i]
        for j in range(i):  #
            # finding the left side bigger blocks before ith block
            left_max = max(left_max, A[j])

        right_max = A[i]

        for j in range(i + 1, n):  # it finds the rightSideBiggest Block after ith index
            right_max = max(right_max, A[j])

        # after finding the leftSideBiggestBlock and rightSideBiggestBlock.
        # We are calculating how much empty blocks we have which can trap the water.
        res = res + (min(left_max, right_max) - A[i])

    return res


def trappingWaterDp(A, N):
    """
    This is based on dynamic programming.
    If we look aur analyse the native approach recursively then we are able to find that
    1. left max= it is finding the max until the current index including current to save into storage
    2. rightmax: it calculating the max from the current index to last index, so in this case we are storing reversively the max to avoid to calculate each time max from current to end index.

    So, once we will have left_max and right_max being calculated beforehand then It will be easy to just calculate the
    trapping water index recursively and easily.
    @param A:
    @param N:
    @return:
    """
    left_max = N * [0]
    right_max = N * [0]
    ans = 0
    for i in range(N):
        if i == 0:
            left_max[i] = A[i]
            right_max[N - 1 - i] = A[N - 1 - i]
        else:
            left_max[i] = max(left_max[i - 1], A[i])
            right_max[N - 1 - i] = max(right_max[N - i], A[N - 1 - i])

    for i in range(N):
        ans += (min(left_max[i], right_max[i]) - A[i])

    return ans


# n = 6
# arr = [3, 0, 0, 2, 0, 4]

arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
n = len(arr)
# print(trappingWater(arr, n))
print(trappingWaterDp(arr, n))
