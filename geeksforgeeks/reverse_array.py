import numpy as np


def reverse_array(arr):
    '''
    This is docstring where I could write something here about what function does.
    :param arr: arra
    :return: array
    '''
    length_array = arr.size
    for i in range(length_array // 2):  # n/2
        last = arr[length_array - i - 1]
        first = arr[i]
        arr[i] = last
        arr[length_array - i - 1] = first


if __name__ == "__main__":
    input = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9])
    reverse_array(input)
    print("Array:", input)
