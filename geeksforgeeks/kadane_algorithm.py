'''
# the problem is to find the maximum contigous sum of an array
input:
[1, 2, 3, -2, 5]
output: 9

'''

# #
# def maxSumOfArray(array, length, maxsum):
#
#
# class Solution:
#     ##Complete this function
#     # Function to find the sum of contiguous subarray with maximum sum.
#     def maxSum(arr, length, maxsum):
#         if length == 0:
#             return maxsum
#         else:
#             max_sum = maxsum
#             current_sum = 0
#             for i in range(length):
#                 current_sum += arr[i]
#                 if current_sum > max_sum:
#                     max_sum = current_sum
#             length = length - 1
#             return Solution.maxSum(arr, length, max_sum)
#
#     def maxSubArraySum(self, arr, N):
#         return Solution.maxSum(arr, N, -9999)
#
#
# # input = [1, 2, 3, -2, 5]
# # input = [1, 2, 3, -2, -5]



def maxSumOfArray(arr, n):
    best = -99999
    sum=0
    for i in range(n):
        sum = max(arr[i], sum+arr[i])
        best =max(best, sum)
    return best

input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

length = len(input)
# s = Solution()
# final_sum = s.maxSubArraySum(input, length)
final_sum = maxSumOfArray(input, length)
print(final_sum)
