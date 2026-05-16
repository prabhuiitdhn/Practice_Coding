#Triplet sum in an array?

from itertools import combinations_with_replacement, combinations, permutations

# def triplet_sum_array_1(arr, n, X):
#     # this approach using combinations
#     return_bool = False
#     for combinations_ in combinations(arr, 3):
#         # print(combinations_)
#         if sum(combinations_) == X:
#             return_bool = True
#             break
#
#     return return_bool


def triplet_sum_array_2(A, n, X):
    # using two pointer based approach
    arr =sorted(A)
    for i in range(n):
        l = i+1
        r = n-1

        while(l<r):
            if arr[i] + arr[l]+arr[r] == X:
                return True
            elif arr[i]+arr[l]+arr[r]<X:
                l = l+1
            else:
                r= r+1
        return False

def triplet_sum_arr_3(A, n, X):
    # using set structure in python
    # but when the array elements is not duplicates.
    s = set(A)
    for i in range(n):
        current_sum = X - A[i]

        for j in range(i+1, n):
            current_sum = current_sum - A[j]
            if current_sum in s:
                return True
    return False
X = 10
arr = [1, 2, 4, 3, 6]
n = len(arr)
p = triplet_sum_array_2(arr, n, X)
print(p)

