"""
https://practice.geeksforgeeks.org/problems/reverse-a-linked-list-in-groups-of-given-size/1?page=1&company[]=Adobe&company[]=Samsung&company[]=Qualcomm&company[]=KLA%20Tencor&category[]=Linked%20List&sortBy=difficulty
Problem:
Needed to reverse the linkedList in a group of given number.
exmple:  1->2->2->4->5->6->7->8
group size =4
output: (4->2->2->1)->(8->7->6->5) # Sorted in a group of 4 elements in the list.
approach: recursion
reverse first 4 element and again pass to reverse next 4 elements in list using same function.
"""

class Node:
    """
    Node representing the linkedList.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        # print()

    def reverse(self, head, k):
        count = 1 # start counting the no of group size.
        prev, current, next_ = None, head, None # initialise the pointer
        while current and count < k + 1: # check the condition where node should exist and element should in a group
            # process of reversing the elements in the list.
            next_ = current.next
            current.next = prev
            prev = current
            current = next_
            count += 1
        if next_:
            # the case when previous group finished.
            head.next = self.reverse(next_, k) # process next set of linkedList elements for reverse process.
            # so, current reverse element is being store and head.next represent the next set of prev it is based on recursion.
        return prev

        # print("\nPringing List, Line no 49\n")
        # self.printList()


if __name__ == "__main__":
    LL = LinkedList()
    LL.insert(1)
    LL.insert(2)
    LL.insert(2)
    LL.insert(4)
    LL.insert(5)
    LL.insert(6)
    LL.insert(7)
    LL.insert(8)
    LL.insert(9)
    LL.insert(10)
    print("\nPrint the given List:")
    LL.printList()
    print("\nReverse the LinkedList.\n")
    LL.head = LL.reverse(LL.head, 4)
    LL.printList()
    # LL
