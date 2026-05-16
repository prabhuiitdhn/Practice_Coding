"""
https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1?page=1&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=KLA%20Tencor&category[]=Greedy&sortBy=difficulty
problem: given an array of size N
each elements in the array will say that from that particular point 'given no of time it can jump(if 3 then It can jump by 1, 2, 3) so, needed to find the minimum no of jumps to reach final element of the array

example:
N = 11
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
if arr[0] = 1; means from 0th index, 1 jumps can be possible and it will reach 3
arr[1] = 3 i.e. from 1st index of array it can jump to 1 more step, 2 or 3 more steps and can reach to arr[3index], arr[4th index], and arr[5th index]
so, to reach the last element of array, min required is 3

1->3->9
1->3 i.e. 3 steps jumps 9 then after 6th jump it will reach to last elements of array

"""


def minJumps(arr, n):
    """
    @param arr: array which contains the element which might take next jumps from the current index
    @param n: number of elements in the arra
    @return: minimum no of jumps required to reach to the last of index.
    It is being solved using greedy approach:
    1. bcz in each steps it tries to find the best by cosidering the element as maximum no of jumps.

    """

    curr, max_jumps, num_jumps = 0, 0, 0
    # current will take care where the pointer is currently
    # max_jumps shows from the current index what is possible maximum distance can be jumped from current pointer.
    # num_jumps say to reach to the end of the array no of jumps required for this.
    for i in range(n):
        max_jumps = max(max_jumps, arr[i] + i)
        # at each time of trasversing elements, it find what is max_jumps possible from ith index.
        if curr == i:
            # if current pointer  is equal to current index then it is considered as max_jumps bcz if 5 possible can be
            # made then current has to pass the 5 index to track the jumps
            curr = max_jumps
            if n - 1 != i:
                # until it did not reach to the end of the array num_jumps would be increment by 1.
                num_jumps += 1

    if curr < n - 1:
        # this is condition where traversing the elements is finished but current is still did not reahc to the end
        # of the array so, it retursn -1 i.e. it works with the condition where 0 comes in the array elements.
        return -1
    else:
        return num_jumps


N = 11
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(minJumps(arr, N))