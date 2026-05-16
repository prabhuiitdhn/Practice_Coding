"""
https://practice.geeksforgeeks.org/problems/count-pairs-in-array-divisible-by-k/1?page=1&difficulty[]=1&company[]=PayPal&company[]=Nvidia&company[]=KLA%20Tencor&sortBy=difficulty

Given an array & K
needed to find the pair of elements in the array which is divisible by K

time complexity: O(n)

"""


def countKdivPairs(arr, n, k):
    """
    Concept: Dictionary & list
            Dictionary is for keeping the reminder.
            
    Iterating through each elements in an array and looking for reminder;
    if reminder is 0 means, individual elements is itself a pair,
    If reminder is not equal to 0 then it counts how many reminder we have available.
    it substracts with K so that we can see the k-reminder is available or not.

    """
    dict_ = {} # keeping the reminder; It also count the number of reminder is available.
    count_of_pairs = 0 # It count the number of pair we do have
    for i in range(n):
        reminder = arr[i] % k
        if reminder == 0:
            count_of_pairs += dict_.get(0, 0)
        else:
            count_of_pairs += dict_.get(k-reminder, 0)

        dict_[reminder] = dict_.get(reminder, 0) + 1

    return count_of_pairs


arr = [10, 6, 3, 3]
n = len(arr)
k = 2
print(countKdivPairs(arr, n, k))
