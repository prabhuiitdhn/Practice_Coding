"""
https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1?page=1&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=KLA%20Tencor&category[]=Greedy&sortBy=difficulty
given an array denoting heights of N towers and positive number k
for each tower, increase the height by K or decrease the height by k (exaclty once)
condition:
1. increasing and decreasing by k is must
2. it should perform
3. array should not contain any -ve integer.
"""


def getMinDiff(arr, n, k):
    """
    the minimum difference between tallest and smallest tower can be found using (max_of_array - k ) - (min_of_array +k)
    @param arr:
    @param n:
    @param k:
    @return:
    """
    sorted_array = sorted(arr)
    # this could be maximum distance between the tower
    difference = (sorted_array[-1]) - (sorted_array[0])
    # it is maximum distance between the tallest and smallest tower
    for i in range(1, n):
        # partition the data into two part
        # 0 (first part) | [second part] 1 2 3 4 5  7 8
        if sorted_array[i] - k < 0:
            # if value is less than K then min will be in negative and later It subtraction will become addition
            continue
        min_ = min(sorted_array[0] + k, sorted_array[i] - k)
        # finding the min between 0th element in the sorted array and next element with -k
        # +k will give the minimum difference between tallest tower and smallest.
        max_ = max(sorted_array[-1] - k, sorted_array[i - 1] + k)
        # finding the max between tallest tower and started from first elements.
        difference = min(difference, max_ - min_)

    return difference


K = 5
N = 10
arr = [8, 1, 5, 4, 7, 5, 7, 9, 4, 6]
print(getMinDiff(arr, N, K))
