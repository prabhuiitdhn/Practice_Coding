"""
https://practice.geeksforgeeks.org/problems/subsets-1587115621/1?page=1&difficulty[]=1&company[]=PayPal&company[]=Nvidia&company[]=KLA%20Tencor&sortBy=difficulty

problem statement: given an array and needed to find out the unique subset of the array.
the final subset elements should in lexigorical increasing order.
{} //empty set should also be included.

time complexity: O(2^N): N is number of array length

approch explained: https://www.youtube.com/watch?v=4rGEAgP33gc&ab_channel=GeeksforGeeksPractice
                https://www.youtube.com/watch?v=REOH22Xwdkk&ab_channel=NeetCode
    approach 1: power subset
    approach 2: Back tracking
    approach 3: recursion.

this code is about the backtracking. each iteration the element will included or not included.
"""


def AllSubsets2(arr, n):  # optimal, not by me.

    def helper(arr, start, end, lst, temp):

        if start > n:
            return

        else:
            lst.add(tuple(temp[:]))

        for i in range(start, end):
            temp.append(arr[i])
            helper(arr, i + 1, n, lst, temp)  # including
            temp.pop() # not including.

    arr.sort()

    lst = {()}
    temp = []
    helper(arr, 0, n, lst, temp)
    lst = list(lst)
    lst = list(map(list, lst))
    lst.sort()

    return lst


def AllSubsets(arr, n):  # # THIS IS NOT OPTIMAL; PLease optimise it using dict or anything.
    """
    This approach is about considering element for the set or not to consider for the set.
    once consider the element will be next element to consider or not to consider.
    It is recursive process.
    @param arr:
    @param n:
    @return:
    """
    result = set()
    current_subset = []

    def helper(arr, startIndex, endIndex):
        if startIndex >= endIndex:
            result.add(tuple(current_subset.copy()))
            return

        # Including the elements
        current_subset.append(arr[startIndex])  # including.
        helper(arr, startIndex + 1, endIndex)

        # not including
        # & whatever element is added in will be pop up
        current_subset.pop()
        helper(arr, startIndex + 1, endIndex, )  # including.

    array = sorted(arr)  # sorting the array for sorted subset
    # result = []  # list of all subset which is being calculated.
    helper(array, 0, n)
    return sorted(result)


arr = [1, 2, 2]
N = 3
# to have the set which only consider the unique element, we will be using set.
# to have increasing order, we will sort the given array.
print(AllSubsets(arr, N))
