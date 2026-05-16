'''
https://practice.geeksforgeeks.org/problems/find-duplicates-in-an-array/1?page=1&company[]=Qualcomm&category[]=Arrays&sortBy=difficulty
1. given an array of size N
2. element contains in an array is 0 to N-1
3. find the elements which occurs more than once in an array
Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).
'''

import numpy as np


def duplicates(arr, n):
    # code here
    arr = sorted(arr)
    l = []
    for i in range(1, n):
        if arr[i - 1] == arr[i]:
            l.append(arr[i])

    if len(l) == 0:
        return [-1]
    else:
        return np.unique(l)


arr = [2, 3, 1, 2, 3]
n = len(arr)
duplicates(arr, n)
