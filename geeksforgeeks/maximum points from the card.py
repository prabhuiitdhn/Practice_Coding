'''
https://practice.geeksforgeeks.org/problems/maximum-point-you-can-obtain-from-cards/1?page=1&sortBy=newest&query=page1sortBynewest
https://www.youtube.com/watch?v=1DkVU2i3sOA

Problem statement:
we need to obtain the maximum k cards summation over given n cards.
we can use sliding window technique to fix it.
condition: we can take one card from the start or from the end at one step.
'''


def maximumSumOfArray(arr, n, k):
    # this approach works but needs to optimise.
    # approach 1: not needed to sum of cards points again and again.
    start_sum = 0

    # initial max_sum.
    max_sum = sum(arr[-k:])  # to check this value which is maximum or not? We should be keeping track of it.

    for i in range(k):
        # current_sum = sum(arr[:i+1]) + sum(arr[-(k - i-1):])
        current_sum = sum(arr[:i + 1]) + sum(arr[n-k+i+1:n])
        max_sum = max(max_sum, current_sum)
    return max_sum


def maximumSumOfArray_approach2(arr, n, k):
    # this approach works but needs to optimise.
    # approach 1: not needed to sum of cards points again and again.
    start_sum = 0

    # initial max_sum.
    end_sum = sum(arr[-k:])  # to check this value which is maximum or not? We should be keeping track of it.
    max_sum = end_sum
    for i in range(k):
        start_sum = start_sum + arr[i]
        end_sum = end_sum - arr[n - k + i]
        current_sum = start_sum + end_sum
        max_sum = max(max_sum, current_sum)
    return max_sum


# arr = [1, 2, 4, 3, 2, 1, 7, 10, 11]  # card values.
arr= [8, 6, 2, 4, 5]
length_of_array = len(arr)
k = 5  # out of the n cards, we need to choose 4 card which will have maximum value. we should collect the cards from start & and ends.
max_sum = maximumSumOfArray_approach2(arr, length_of_array, k)
print(max_sum)