"""
https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1?page=1&company[]=Adobe&company[]=Samsung&company[]=Qualcomm&company[]=KLA%20Tencor&category[]=Linked%20List&sortBy=difficulty
problem: The linkedlist will have two node next and bottom, and both will have elements and all the elements will be in sorted order.
return: needed to return the linkedList which will have all the elements flatten.

For understanding the problem better.
https://www.youtube.com/watch?v=ysytSSXpAI0
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None


def flatten(root):
    # Your code here
    head = root  # Head is for keeping the track till end
    a = root  # it is for traversing the linkedList.
    while a:
        # it is just to add all the element in bottom pointer.
        temp = a.next  # it represent the next linkedlIst
        while a.bottom:
            a = a.bottom
        a.bottom = temp
        a = a.bottom

    v = []
    while head is not None:
        # append all the elements in a V for sorting later.
        v.append(head.data)
        head = head.bottom

    # sorting the all the elements which is added in the head pointer (It is nothing but root/header)
    v.sort()

    # to return the Node() as linkedLinked where all the sorted elements to be added as bottom pointer.
    result = Node(-1)  # it is default Node created which will have next, and bottom pointer.
    temp = result  # it kept for removing default node while returning.
    for i in range(len(v)):
        result.bottom = Node(v[i])
        result = result.bottom
    temp = temp.bottom
    return temp

if __name__ == "__main__":
    head = None
