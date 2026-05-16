import numpy as np


def rotate(arr):
    len = arr.size
    arr[0], arr[len - 1] = arr[len - 1], arr[0]
    print(arr)

    i = 1
    while i < len-1:
        arr[len - i], arr[len - i - 1] = arr[len - i - 1], arr[len - i]
        i += 1

    # return


if __name__ == "__main__":
    arr = np.array([1, 2, 3, 4, 5, 6, 7])
    rotate(arr)
    print(arr)
