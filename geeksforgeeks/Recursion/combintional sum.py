"""
https://practice.geeksforgeeks.org/problems/combination-sum-1587115620/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=KLA%20Tencor&category[]=Recursion&sortBy=difficulty
"""

import copy
def combinationalSum(arr, B):
    final_list = [] # which will store the total list
    currenlist = [] # this is storing the list which will have all the elements which could give the sum of B
    arr = sorted(list(set(arr))) # this is unique distinct elements

    def helper(arr, sum, index):
        if sum ==0:
            final_list.append(copy.copy(currenlist))
            return final_list

        for i in range(index, len(arr)):
            if sum-arr[i] >= 0:
                currenlist.append(arr[i])
                helper(arr, sum-arr[i], i)
                currenlist.remove(arr[i])
        # return

    helper(arr, B, 0)
    return final_list


N = 4
arr = [7, 2, 6, 5]
B = 16
print(combinationalSum(arr, B))
