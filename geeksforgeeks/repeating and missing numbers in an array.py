'''
problem: Given an unsorted array Arr of size N of positive integers. One number 'A' from set {1, 2, N} is missing and one number 'B' occurs twice in array. Find these two numbers.
1. unsorted array
2. starts from [1, N]
3. one number is missing
4. one number is coming twice.
'''


def find_repeating_missing(arr, N):
    count_array = [0] * N # it is an array which fills with 0 and store the number of counts
    '''
    if the number of count > 1: called as repeating number
    number of count ==0: called as missing number
    '''
    missing_number = 0
    repeating_number = 0
    for i in range(N):
        count_array[arr[i]-1] += 1

    for i in range(N):
        if count_array[i] == 0:
            missing_number = i+1
        if count_array[i] == 2:
            repeating_number = i+1

    return missing_number, repeating_number


N =4 # this shows that number of elements in an array
arr = [1, 2, 4, 4]
a, b = find_repeating_missing(arr, N)

print(a, b)