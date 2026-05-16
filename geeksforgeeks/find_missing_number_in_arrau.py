# import numpy as np
#
#
# def find_missing(arr, n):
#     expected_sum = (n * (n + 1)) / 2
#     current_sum = sum(arr)
#     return int(expected_sum - current_sum)
#
#
# if __name__ == "__main__":
#     arr = np.array([1, 2, 3, 5])
#     a = find_missing(arr, 5)
#     print(a)





def get_sum_metrics(predictions, metrics=[]):
    for i in range(3):
        metrics.append(lambda x: x + i)

    sum_metrics = 0
    for metric in metrics:
        sum_metrics += metric(predictions)

    return sum_metrics


predictions = 0
p = get_sum_metrics(0)
print(p)