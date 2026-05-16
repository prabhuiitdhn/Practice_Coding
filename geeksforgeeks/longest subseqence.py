# Function to find length of longest increasing subsequence.
def longestSubsequence(self, a, n):
    lis = [1] * n
    for i in range(n):
        for j in range(i):
            if a[i] > a[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    max = 0
    for i in range(n):
        if lis[i] > max:
            max = lis[i]
    return max
