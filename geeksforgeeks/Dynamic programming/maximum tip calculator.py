"""
https://practice.geeksforgeeks.org/problems/maximum-tip-calculator2631/1?page=1&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty

The problem is to find the maximum tip can be collected by the 2 waiter in the resturant and each waiter will serve different-different table.
Rahul and Ankit are only two waiter in the restaurant and restaurant take 'n' order at a time.
Rahul can serve maximum X no of table
Ankit can server maximum Y no of table.

X+Y>= N i.e. the total sum of X and Y might be greater than N.

The amount of tips may differ when handled by different waiters, if Rahul takes the ith order, he would be tipped a_i rupees and if Ankit takes this order, the tip would be b_i rupees.
i.e. for Rahul : tip array is being given a_i = [.., .., ...]
for Ankit: tip array is being given b_i = [..., ...,..]


so needed to calculate the maximum tip collected by the Rahul & ankit from the waiter.
"""
import numpy as np


def maxTipNative(a, b, n, x, y):
    """
    @param a: This is tip array for Ankit
    @param b: this is tip array for rahul
    @param n: total number of order can be taken
    @param x: maximum order can be handled by Ankit
    @param y: maximum order can be handled by Rahul
    @return: maximum tip can be collected from
    """

    if n == 0:
        # this is the case when no order
        return 0
    if x != 0 and y != 0:
        # until x>0 or y>0 the combination of x+y will be going and calculating the maximum tip from rahul & ankit.
        return max(
            a[n - 1] + maxTipNative(a, b, n - 1, x - 1, y),  # This is the case when ankit's tip is consider
            b[n - 1] + maxTipNative(a, b, n - 1, x, y - 1)  # this is the case when rahul's tip is considered.
        )

    if x == 0:
        # No order is being left for the Ankit. only rahul's order is being left to collect the max tip
        return b[n - 1] + maxTipNative(a, b, n - 1, x, y - 1)
    if y == 0:
        # no order is being left for the Rahul, only ankit's order is being left to collect the max tip
        return a[n - 1] + maxTipNative(a, b, n - 1, x - 1, y)

    # return


def maxTipDPRecursive(a, b, n, x, y):
    """
    Using memoization technique in DP we can solve this: Using Dictionary which would search the items in the dictionary in O(1)
    Also, using 3D array, it will also search the elements in O(1)
    """
    # using dictionary
    dp = {}

    def helper(a, b, n, x, y):

        if (n, x, y) in dp:
            return dp[(n, x, y)]

        if n == 0:
            return 0
        if x > 0 and y > 0:
            if (n, y, x) not in dp:
                dp[(n, y, x)] = max(
                    a[n - 1] + helper(a, b, n - 1, x - 1, y),  # This is the case when ankit's tip is consider
                    b[n - 1] + helper(a, b, n - 1, x, y - 1)  # this is the case when rahul's tip is considered.
                )

        if x == 0:
            if (n, x, y) not in dp:
                dp[(n, x, y)] = b[n - 1] + helper(a, b, n - 1, x, y - 1)
        if y == 0:
            if (n, x, y) not in dp:
                dp[(n, x, y)] = a[n - 1] + helper(a, b, n - 1, x - 1, y)

        return dp[(n, x, y)]

    return helper(a, b, n, x, y)


def maxTipDPIterative(a, b, n, x, y):
    """
    Approach: fill the initial value which will help to calculate iteratively

    """
    dp = np.zeros(shape=(n + 1, x + 1, y + 1))
    for i in range(x + 1):
        for j in range(y + 1):
            # filling the initial value when n==0: the all index value should be 0
            dp[0][i][j] = 0

    for i in range(1, n + 1):  # this is for n
        for j in range(1, y + 1):  # this is for y
            # here the x is 0 so, when x=0 then we will put the b[i-1] bcz only b is left
            dp[i][0][j] = b[i - 1] + dp[i - 1][0][j - 1]

    for i in range(1, n + 1):
        for j in range(1, x + 1):  # this is for x
            # when y=0, then we will put a[i-1] bcz only a is left
            dp[i][j][0] = a[i - 1] + dp[i - 1][j - 1][0]

    for i in range(1, n + 1):
        for j in range(1, x + 1):
            for k in range(1, y + 1):
                '''
                once all the initial value is being filled, now iteratively we will put the other indices value iteratively
                '''
                dp[i][j][k] = max(
                    a[i - 1] + dp[i - 1][j - 1][k],
                    b[i - 1] + dp[i - 1][j][k - 1]
                )
    return int(dp[n][x][y])


def maxTipUsingSorting(a, b, n, x, y):
    """
    Approach: create a list and store the difference between tips between the customer for Ankit & rahul
    If the difference is too high then one of the customer have paid a higher number of amount for the tip.
    1. saved the difference between tips and store in list with index
    2. sort then
    """
    lis = []
    for i in range(n):
        lis.append([abs(a[i] - b[i]), i])

    lis.sort(key=lambda x: x[0], reverse=True)
    ans = 0
    for i in lis:
        idx = i[1]

        if x > 0 and y > 0:
            if a[idx] > b[idx]:
                ans += a[idx]
                x -= 1
            elif a[idx] == b[idx]:
                if x > y:
                    ans += a[idx]
                    x -= 1
                else:
                    ans += a[idx]
                    y -= 1
            else:
                ans += b[idx]
                y -= 1
        elif x > 0:
            ans += a[idx]
            x -= 1
        elif y > 0:
            ans += b[idx]
            y -= 1
    return ans


# # INPUT 1

# n = 8  # total number of order can be taken by restaurants.
# x = 4  # this many number of order/customer can be handled by Ankit
# y = 4  # this many number of order/customer can be handled by Rahul
# ankit = [1, 4, 3, 2, 7, 5, 9, 6]  # this is tip array can be assigned to Ankit
# rahul = [1, 2, 3, 6, 5, 4, 9, 8]

# # input 2
# n = 5
# x = 3
# y = 3
# ankit = [1, 2, 3, 4, 5]
# rahul = [5, 4, 3, 2, 1]

# # input 3
n = 7
x = 3
y = 4
ankit = [8, 7, 5, 9, 6, 6, 8]
rahul = [1, 7, 5, 1, 2, 3, 9]

print("The maximum tip can be calculated by Ankit & rahul.")
print(maxTipNative(ankit, rahul, n, x, y))  # NATIVE APPROACH FAILED IN TIME COMPLEXITY
# print(maxTipDPRecursive(ankit, rahul, n, x, y)) # RECURSIVE APPROACH FAILED IN TIME COMPLEXITY
print(maxTipDPIterative(ankit, rahul, n, x, y))  # EVEN ITERATIVE APPROACH FAILED IN TIME COMPLEXITY AND SPACE COMPLEXITY

print(maxTipUsingSorting(ankit, rahul, n, x, y))
