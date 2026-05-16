import copy
from itertools import permutations

def permutation_1(arr):
    p = permutations(arr)
    l = []
    for i in p:
        ans = ''.join(i)
        if ans not in l:
            l.append(ans)
    print(l)
# approach 1 using swapping methods
def permutation_2(index, arr, ans_list):
    if index == len(arr):
        appending_list = copy.copy(arr)
        ans_list.append(appending_list)
        # appending_list = []
        return ans_list
    else:
        for i in range(index, len(arr)):
            arr[index], arr[i] = arr[i],arr[index]
            permutation_2(index+1, arr, ans_list)
            arr[i], arr[index] = arr[index], arr[i]

    print(ans_list)
arr = [1, 2, 3]
s = "ABC"
ans_list_s = " "
ans_list = []
permutation_2(0, arr, ans_list)
# permutation_2(s)

