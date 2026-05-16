"""
https://practice.geeksforgeeks.org/problems/maximum-sum-combination/1
https://www.geeksforgeeks.org/k-maximum-sum-combinations-two-arrays/


Given two arrays A and B of size N each.
needed to fing the 'k' maximum combinations sum from A and B

Expected time complexity : O(NlogN)
Auxillary space: O(N)

"""

import heapq


# Function prints k maximum possible combinations
def KMaxCombinations(n, k, a, b):
    a.sort()
    b.sort()

    # Using a max-heap.
    pq = []
    heapq.heapify(pq)
    pq.append((-a[n - 1] - b[n - 1], (n - 1, n - 1)))

    sum_list = []  # sum is for adding the maximum sum combinations list.

    my_set = set()  # set is for adding the index position which is already visited.
    my_set.add((n - 1, n - 1))  # initially added the last index of the array bcz It will have the maximum sum.

    for count in range(k):
        temp = heapq.heappop(pq)

        sum_list.append(-temp[0])  # This is the value.

        i = temp[1][0]  # ith index which is already visited.
        j = temp[1][1]  # jth index which is already visited.
        sum = a[i - 1] + b[j]  # Checking the next combinations of sum.

        temp1 = (i - 1, j)

        if temp1 not in my_set:
            # if the index is not in the set [visited set.]
            heapq.heappush(pq, (-sum, temp1))
            my_set.add(temp1)

        sum = a[i] + b[j - 1]  # checking the another combinations of sum.

        temp1 = (i, j - 1)

        if temp1 not in my_set:
            heapq.heappush(pq, (-sum, temp1))
            my_set.add(temp1)

    return sum_list


# # Back-end complete function Template for Python 3
#
# # Class to find the maximum sum of combinations
# import heapq
#
#
# class findMaxSum:
#     def __init__(self, A, B):
#         # Sort the lists in reverse order
#         self.A = sorted(A, reverse=True)
#         self.B = sorted(B, reverse=True)
#         self.sums, self.visited = list(), set()
#         self.__add_element(0, 0)
#
#     def __call__(self):
#         # Pop the element with the maximum sum
#         el_sum, indexes = heapq.heappop(self.sums)
#         iA, iB = indexes
#         # Add the next possible elements to the heap
#         self.__add_element(iA, iB + 1)
#         self.__add_element(iA + 1, iB)
#         return -el_sum
#
#     def __add_element(self, iA, iB):
#         indexes = iA, iB
#         # Check if the indexes are within range and not already visited
#         if iA < len(self.A) and iB < len(self.B) and indexes not in self.visited:
#             # Push the sum and indexes to the heap
#             heapq.heappush(self.sums, (-self.A[iA] - self.B[iB], indexes))
#             self.visited.add(indexes)
#
#
# class Solution:
#     # Function to find the maximum combinations with maximum sum
#     def maxCombinations(self, K, A, B):
#         # Create an instance of findMaxSum class
#         retriver = findMaxSum(A, B)
#         # Call the __call__ method to retrieve the maximum sums
#         return [retriver() for _ in range(K)]


N = 7
K = 4
A = [9, 9, 10, 6, 1, 6, 4]
B = [5, 3, 4, 2, 10, 4, 9]
# print(KMaxCombinations(N, K, A, B))
Sol = Solution()
print(Sol.maxCombinations(K, A, B))
