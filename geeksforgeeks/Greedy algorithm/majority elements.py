"""
https://practice.geeksforgeeks.org/problems/majority-element-1587115620/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=KLA%20Tencor&category[]=Greedy&sortBy=difficulty

Given an array A of N elements. Find the majority element in the array. A majority element in an array A of size N is an element that appears more than N/2 times in the array.
approach:
using dictionry
"""


def majorityElement(A, N):
    d = {} # initialising the dictionary
    for i in range(N):
        if A[i] not in d.keys():
            # checking if the A[i] is available in the dictionary or not If not then initialise and make value =1
            d[A[i]] = 1
        else:
            d[A[i]] += 1
            # if already existed then add the value by 1

    for key, value in d.items():
        if value > N / 2:
            # check the majority of elements.
            return key

    # if not elements in majority elements then it return -1
    return -1


A = [3, 1, 3, 3, 2]
N = 5
print(majorityElement(A, N))
