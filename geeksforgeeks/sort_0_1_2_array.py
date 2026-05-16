import numpy as np


def sort_0_1_array(arr):
    count_0 = 0
    count_1 = 0
    count_2 = 0

    len = arr.size

    for i in range(len):
        if arr[i] == 0:
            count_0 += 1
        if arr[i] == 1:
            count_1 += 1
        if arr[i] == 2:
            count_2 += 1

    index = 0
    while count_0 > 0:
        arr[index] = 0
        index += 1
        count_0 -= 1

    while count_1 > 0:
        arr[index] = 1
        index += 1
        count_1 -= 1

    while count_2 > 0:
        arr[index] = 2
        index += 1
        count_2 -= 1


if __name__ == "__main__":
    arr = np.array([0, 1, 1, 2, 0, 1, 1, 0, 0, 2, 2])
    sort_0_1_array(arr)
    print("Sorted array:", arr)
