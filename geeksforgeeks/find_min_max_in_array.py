import numpy as np






def min_max_array(arr):
    '''
    one way of finding the min and max of an array it takes.
    It takes n no of comparison and also, o(1) in space
    :param arr:
    :return:
    '''
    min_ = -9999
    max_ = 9999

    for i in range(arr.size):
        if min_ < arr[i]:
            min_ = arr[i]
        if max_ > arr[i]:
            max_ = arr[i]

    return min_, max_


def min_max_array_2(arr):
    '''
    Algo:
    Intialise: mx  is the lowest, mn is largest value
    compare each element in array in pair. previous mx is lower than current element of array then assign new value to max and vice versa for min.

    :param arr:
    :return:
    '''
    mx = -9999
    mn = 9999
    if arr.size == 1:
        mx = arr[0]
        mn = arr[0]
    if arr.size == 2:
        mx = max(arr)
        mn = min(arr)

    if arr.size > 2:
        for i in range(arr.size):
            mx = max(mx, arr[i])
            mn = min(mn, arr[i])

    return mx, mn


def min_max_divide_conquer(arr):
    '''
    algo: this would solve the problem using divide and conquer technique.
    dividing the array as small as possible and find out which is
    :param arr:
    :return:
    '''
    start_index = 0
    last_index = arr.size-1
    def divide_array(arr, start_index, last_index):
        if start_index == last_index:
            return arr[start_index], arr[start_index]

        if start_index +1 == last_index:
            return max(arr[start_index], arr[last_index]), min(arr[start_index], arr[last_index])

        interval = start_index + last_index



if __name__ == '__main__':
    print("I am here.")
    arr = np.array([-1, 1333, 4, 5, 7999, 8, 1111, 2, 3, 0])
    # a, b = min_max_array(arr)
    # a, b = min_max_array_2(arr)
    a, b = min_max_divide_conquer(arr)
    print(a, b)
