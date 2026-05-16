"""
https://practice.geeksforgeeks.org/problems/knapsack-with-duplicate-items4201/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty

N set of items with weight (w)and value (val)
with Limiting weight W: ie.e maximum profit should not exceed this weigjt

The task is to fill the knapsack in such a way that we can get the maximum profit. Return the maximum profit.

Note: each item can be taken any number of times.


"""


def knapSack(N, W, val, wt):
    """
    Iterative approach
    @param N:
    @param W:
    @param val:
    @param wt:
    @return:
    """
    # code here
    t = [[-1 for _ in range(W + 1)] for _ in range(N + 1)]

    #  Initialization
    for i in range(N + 1):  # recursively looking for all the items
        for j in range(W + 1):  # it checks the maximumprofit is same or less than
            if i == 0 or j == 0:
                t[i][j] = 0

            # recursive to iterative
            #  coding choice diagram:
            elif wt[i - 1] <= j:  # if wt at particular index is less than W
                t[i][j] = max(val[i - 1] +
                              t[i][j - wt[i - 1]],  # subtracting the W to current weight
                              t[i - 1][j])
            else:
                t[i][j] = t[i - 1][j]
    return t[N][W]


N = 2  # total number of items
W = 3  # final weight limit
val = [1, 1]  # items
wt = [2, 1]  # weight og items
print(knapSack(N, W, val, wt))
