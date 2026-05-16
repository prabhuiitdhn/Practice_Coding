"""

https://practice.geeksforgeeks.org/problems/minimum-number-of-steps-to-reach-a-given-number5234/1?page=2&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=KLA%20Tencor&category[]=Recursion&sortBy=difficulty
https://www.geeksforgeeks.org/find-minimum-moves-reach-target-infinite-line/ Explaination

starting from 0, we can move to +ve side as  +1, +2, .....+n until infinity to reach the destination D
we can move +ve/-ve if required to reach the destination.

"""
import sys


def minSteps(D):
    def minStepsHelper(s, i, D):
        """
        Naive approach but time complexity is too too hight
        @param s:
        @param i:
        @param D:
        @return:
        """
        if s == D:
            return i  # this shows the steps that we have followed to reach to destinations.
        if abs(s) > D:
            return sys.maxsize  # this is for exit the -ve 's'

        return min(minStepsHelper(s + i, i + 1, D),
                   minStepsHelper(s - i, i + 1, D))  # this is for going into the -ve/+ve side from the current steps.

    start = 0
    i = 1

    return minStepsHelper(start, i, D) - 1  # -1 is used for in the last steps itself we reached to destination.


def minStepsOptimised(D):
    """
    Optimised approach
    @param D:
    @return:
    """
    steps, curr = 0, 0 # starting from here.
    while curr < D:  # until it reach to the destination in +ve side, increase the steps
        steps += 1
        curr += steps
    while curr - D & 1:  # going -ve side when it exceeds the destination.
                        # so it is basically going -ve side and checking whether the differnce is multiple of 2 bcz if the difference is 2 *i then we can easily go -ve of i and reach the destionation.
        '''
        if curr-D = 10
        to find the multiple of 2 
        is binary of 10 & 1: 1010 & 0001 = 0
        '''
        steps += 1
        curr += steps
    return steps


def minStepsOptimisedAnother(target):
    # Handling negatives by symmetry
    target = abs(target)

    # Keep moving while sum is
    # smaller or difference is odd.
    sum = 0
    step = 0
    while (sum < target or (sum - target) %
           2 != 0):
        step = step + 1
        sum = sum + step

    return step
D = 5
print(minSteps(D)) # naive approach
print(minStepsOptimised(D)) # optimised with & operation which check with & which check the difference as if it is multiple of 2
print(minStepsOptimisedAnother(D)) # without using & operator.