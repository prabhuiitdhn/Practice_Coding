'''
https://practice.geeksforgeeks.org/problems/smallest-positive-missing-number-1587115621/1
problem: given an unsorted array of size N, needed to find smallest +ve missing number in an array
array might include -ve numbers but we needed to find the smallest +ve number.
array might include 0, But needed to find smallest +ve number greater then 0
'''


def missingNumber(arr, n):
    # Your code here
    # missing_number = 0
    # count_array = [0] * (10 ** 6)
    #
    # for i in range(n):
    #     if arr[i] > -1:
    #         count_array[arr[i]] += 1
    #
    # for i in range(n):
    #     if i != 0 and count_array[i] == 0:
    #         missing_number = i
    #         break
    #
    # if count_array[0] == 1 and missing_number ==0:
    #     missing_number = n
    # if count_array[0] == 0 and missing_number == 0:
    #     missing_number = n+1

    arr=set(arr)

    for i in range(n+1):
        if i+1 not in arr:
            return i+1



arr =[1]
N = len(arr)
p = missingNumber(arr, N)
print(p)