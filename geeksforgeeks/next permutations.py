'''
https://practice.geeksforgeeks.org/problems/next-permutation5226/1?page=1&company[]=Qualcomm&category[]=Arrays&sortBy=difficulty
problem: Given an array and needed to find the next permutations of an given array
approach 1: using itertools.permutations but much memory is needed for this so needed to look for an other approach
approach 2: 
'''
from itertools import permutations


def nextPermutation(N, arr):
    # code here
    array_to_list = []
    for i in range(N):
        array_to_list.append(arr[i])
    arr_to_list_sorted = sorted(array_to_list)

    p = sorted(permutations(arr))

    index_in_permutation_list = p.index(tuple(array_to_list))
    # print(index_in_permutation_list)

    if index_in_permutation_list < len(p):
        # remining_indexes = len(p) - index_in_permutation_list
        # # i = 1
        while ((index_in_permutation_list + 1) < len(p) and (
                p[index_in_permutation_list] == p[index_in_permutation_list + 1])):
            index_in_permutation_list += 1
        # i= i-1
        if index_in_permutation_list == len(p) - 1:
            return p[0]
        else:
            return p[index_in_permutation_list + 1]
    else:
        return p[index_in_permutation_list + 1]


def nextPermutation2(arr, N):
    start_index = 0

    for i in range(N - 1, -1, -1):

        if arr[i] > arr[i - 1]:
            # find the start_index where the number should be swapped.
            start_index = i - 1
            break

    # this satisfy 2 conditions:
    #1. If number are already biggest then swap the whole number
    #2. the remaining element after start_index, number should be swapped.
    arr[start_index + 1:] = sorted(arr[start_index + 1:])

    for i in range(len(arr[start_index + 1:])):
        # checking the immediate largest number from the start_index which has be swapped.
        if arr[start_index + 1 + i] > arr[start_index]:
            arr[start_index], arr[start_index + 1 + i] = arr[start_index + 1 + i], arr[start_index]

            break

    return arr


# arr = [1, 2, 3, 6, 5, 4]
arr = [5, 1,1 ]
q = nextPermutation2(arr, len(arr))

print(q)
