"""
https://practice.geeksforgeeks.org/problems/stickler-theif-1587115621/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty

this problem is about "a thief who wants to loot the money from n house with following the rules that he will not
looting consecutive home" if thief looted the money from ith home then it will loot i+2 but not i+1 bcz i & i+1 will
be consecutive house. At the same time, he wants to maximise the amount he loots. The thief knows which house has
what amount of money but is unable to come up with an optimal looting strategy. He asks for your help to find the
maximum money he can get if he strictly follows the rule. Each house has a[i]amount of money present in it.

"""


def FindMaxSum(a):
    """
    so, including includes the current value with maximum profit got until the last index.
    excluding: It is not including the current value so it is the same what we had have the maximum profit until the last
    profit.
    @param a: array
    @return:
    """

    # initialisation of the including, excluding and maximum profit.
    including = 0
    excluding = 0
    maxprofit = 0

    for i in a:
        # going for each array
        including = excluding + i  # this is including the current value with maximum profit we have had in last index.
        excluding = maxprofit  # not including i so, it will be the last maximum profit.
        maxprofit = max(including, excluding)  # again calculating the maximum profit.

    return max(including, excluding)  # final maximum profit between the inclduded and excluded.


n = 6
a = [5, 5, 10, 100, 10, 5]
print(FindMaxSum(a))
