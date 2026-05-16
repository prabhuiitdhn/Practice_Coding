import numpy as np


def move_negative_to_onse_side(arr):
    '''
    It is just to move all the -ve element at one side of array and +ve to another side of array
    :param arr:
    :return:
    '''
    len = arr.size
    pos_index = len - 1
    neg_idx = 0

    while neg_idx <= pos_index:
        if arr[neg_idx] < 0 and arr[pos_index] < 0:
            neg_idx += 1
        if arr[neg_idx] > 0 and arr[pos_index] < 0:
            arr[neg_idx], arr[pos_index] = arr[pos_index], arr[neg_idx]
            pos_index -= 1
            neg_idx += 1

        if arr[neg_idx] > 0 and arr[pos_index] > 0:
            pos_index -= 1

        if arr[neg_idx] < 0 and arr[pos_index] > 0:
            neg_idx += 1
            pos_index -= 1


if __name__ == "__main__":
    print("He")
    arr = np.array([-1, 10, 10, -1, 2, 3, 4, -3, 4])
    move_negative_to_onse_side(arr)
    print(arr)
    print("done")
