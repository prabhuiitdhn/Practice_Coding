"""
https://practice.geeksforgeeks.org/problems/max-length-chain/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=KLA%20Tencor&category[]=Greedy&sortBy=difficulty

problem:
given a N pair of numbers, in each pair first element < second element.
A pair (c, d) can be follow by (a, b) where b<c.
so needed to find the longest chain which can be created by given numbers of pairs

example:
Input:
N = 5
P[] = {5  24 , 39 60 , 15 28 , 27 40 , 50 90}
Output: 3
Explanation: The given pairs are { {5, 24}, {39, 60},
{15, 28}, {27, 40}, {50, 90} },the longest chain that
can be formed is of length 3, and the chain is
{{5, 24}, {27, 40}, {50, 90}}


approach: Two pointer approach.
"""


class pair:
    # Creating pair which will take first and second elements in the list
    def __init__(self, a, b):
        self.first = a
        self.second = b


def maxChainLen(Parr, n):
    list_of_elements = []
    for i in Parr:
        # adding all the elements in fresh list
        list_of_elements.append([i.first, i.second])

    list_of_elements = sorted(list_of_elements, key=lambda l: l[1])
    # Sorting the list by 2nd elements in the list.
    print(list_of_elements)

    current = 1 # current pointer
    prev = 0 # prev pointer
    count = 1
    while current < n:
        if list_of_elements[prev][1] < list_of_elements[current][0]:
            # Checking if second elements of the prev is less than current[first] the count
            count += 1
            prev = current
            current += 1
        else:
            # else traverse further by 1
            current += 1

    return count


N = 5
List = [pair(5, 24), pair(36, 60), pair(15, 28), pair(27, 40), pair(50, 90)]

print(maxChainLen(List, N))
