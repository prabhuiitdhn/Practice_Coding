class Solution:
    def kthSmallest(self, arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        arr.sort()
        return arr[k - 1]


# {
#  Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    import random

    # t = int(input())1234
    t = 1
    import numpy as np
    for tcs in range(t):
        # n = int(input())
        n =5
        # arr = list(map(int, input().strip().split()))
        arr = np.array([7, 10, 4, 20, 15])
        # k = int(input())
        k =4
        ob = Solution()
        print(ob.kthSmallest(arr, 0, n - 1, k))

# } Driver Code Ends
