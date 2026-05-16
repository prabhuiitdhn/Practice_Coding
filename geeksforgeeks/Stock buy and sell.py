'''
https://practice.geeksforgeeks.org/problems/stock-buy-and-sell2615/1?page=1&company[]=Samsung&category[]=Arrays&sortBy=difficulty
problem statement:
input: arr//given the stock price on the given day.
output: needed to have the day pair which can give the maximum profits.
algo: find the local minima and local maxima for having maximum profit
example:arr = [23, 13, 25, 29, 33, 19, 34, 45, 65, 67]
output: (1, 4), (5, 9)
between [23, 13, 25, 29, 33]: local minimum is 13, and local maximum is 33
[19, 34, 45, 65, 67]: local minimum: 19 and local maximum is 67

algo: stack data structure.
'''

from collections import deque

# def stockBuySell(arr, n):
#     s = deque()
#     l = []
#     for i in range(1, n):
#         if arr[i-1]< arr[i]:
#             s.append(i-1)
#         else:
#             if len(s) == 0:
#                 continue
#             else:
#                 s.append(i-1)
#                 l.append([s[0], s[-1]])
#                 s.clear()
#     if arr[-2]< arr[-1]:
#         s.append(n-1)
#         l.append([s[0], s[-1]])
#         s.clear()
#
#     # print(l)
#     for i in range(len(l)):
#         print("({} {})".format(l[i][0], l[i][1]), end="")


def stockBuySell2(a, n):
    buy = 0
    sell = 0
    i = 1
    notPresent = True
    while i < n:
        buy = i - 1
        while i < n and a[i] > a[i - 1]:
            i += 1
        sell = i - 1
        if buy != sell:
            notPresent = False
            print("({} {})".format(buy, sell), end=" ")
        i += 1

    if notPresent:
        print("No Profit", end=" ")

    print()


def stockBuySell3(price, n):
    # Prices must be given for at least two days
    if (n == 1):
        return

    # Traverse through given price array
    i = 0
    while (i < (n - 1)):

        # Find Local Minima
        # Note that the limit is (n-2) as we are
        # comparing present element to the next element
        while ((i < (n - 1)) and
               (price[i + 1] <= price[i])):
            i += 1

        # If we reached the end, break
        # as no further solution possible
        if (i == n - 1):
            break

        # Store the index of minima
        buy = i
        i += 1

        # Find Local Maxima
        # Note that the limit is (n-1) as we are
        # comparing to previous element
        while ((i < n) and (price[i] >= price[i - 1])):
            i += 1

        # Store the index of maxima
        sell = i - 1

        print("Buy on day: ", buy, "\t",
              "Sell on day: ", sell)

# arr = [23, 13, 25, 29, 33, 19, 34, 45, 65, 67]
arr = [886, 2777, 6915, 7793, 8335, 5386, 492, 6649, 1421, 2362, 27, 8690, 59, 7763, 3926, 540, 3426, 9172, 5736, 5211,
       5368, 2567, 6429, 5782, 1530, 2862, 5123, 4067, 3135, 3929, 9802, 4022, 3058, 3069, 8167, 1393, 8456, 5011, 8042,
       6229, 7373, 4421,
       4919, 3784, 8537, 5198, 4324, 8315, 4370, 6413, 3526, 6091, 8980, 9956, 1873, 6862, 9170, 6996, 7281, 2305, 925,
       7084, 6327, 336, 6505,
       846, 1729, 1313, 5857, 6124, 3895, 9582, 545, 8814, 3367, 5434, 364, 4043, 3750, 1087, 6808, 7276, 7178, 5788]

n = len(arr)
stockBuySell2(arr, n)