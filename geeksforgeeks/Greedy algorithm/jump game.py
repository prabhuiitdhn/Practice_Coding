"""
https://practice.geeksforgeeks.org/problems/jump-game/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=KLA%20Tencor&category[]=Greedy&sortBy=difficulty

given an array where each elements says from that index this much of maximum index can be jumps.
so, check whether can be jumped to end of the array or not

thoughts:
From each index it tries to reach maximum jumps and If reaches to 0 then It would not reach to the end bcz from 0 it will not move so return -1
else: After tracing each index/jumping after each index, either will reach to end of the index or exceed the elements.
so, definitely It will reach.
"""


def canReach(A, N):
    # code here
    current = 0
    # it will keep track of current pointer.
    max_jumps = 0
    # it will keep track how far it can jumps

    for i in range(N):
        max_jumps = max(max_jumps, A[i] + i)
        # It is giving track that what could be the maximum jumps.
        # at one time, A[i]+i would be largest jumps which can be made.
        # if lrgest jumps reached to 0 and < N-1 then it will not reach to end of the array
        if current == i:
            # Each index it will calculating the maximum jumps.
            current = max_jumps

    if current < N - 1:
        return 0
    else:
        # it is the case when current position after the jump may reach to end of the array or exceed it.
        return 1


N = 6
A = [1, 2, 0, 3, 0, 0]

if canReach(A, N):
    print(" Possible to reach to the end")
else:
    print("Not possible to reach.")