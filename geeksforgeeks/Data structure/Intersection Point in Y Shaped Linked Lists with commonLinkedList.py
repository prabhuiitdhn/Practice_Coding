"""
https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1?page=1&company[]=Adobe&company[]=Samsung&company[]=Qualcomm&company[]=KLA%20Tencor&category[]=Linked%20List&sortBy=difficulty

Problem: Given in two linkedList, needed to find the common element which connects both the list in the linkedList. It will form Y shape where some node will represents as tail of Y
example:
LinkedList1: 3->6->9->15->30
LinkedList2: 10->15->30
common linkedList = 15->30
common elements in the both LinkedList will have 15->30
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def printList(self):

        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def intersectionPoint(self, head1, head2):
        if head1 is None or head2 is None:
            # Check if anyone is None
            return -1

        def lengthOfList(head):
            count = 0
            current = head
            while current:
                count += 1
                current = current.next
            return count

        lengthHead1 = lengthOfList(head1)
        lengthHead2 = lengthOfList(head2)

        current_head1 = head1
        current_head2 = head2

        # reaching to the pointer where both linkedlist will have possibility to match.or where both might start to compare.
        if lengthHead1 > lengthHead2:
            for i in range(lengthHead1 - lengthHead2):
                current_head1 = current_head1.next

        if lengthHead2 > lengthHead1:
            for i in range(lengthHead2 - lengthHead1):
                current_head2 = current_head2.next

        # if the pointer is found where both pointer may match
        while current_head2 is not None and current_head1 is not None:
            if current_head1 == current_head2:
                # checking where the both pointer/address is matching
                return current_head1.data
            current_head1 = current_head1.next
            current_head2 = current_head2.next

        return -1


if __name__ == "__main__":
    L1 = LinkedList()
    L1.insert(3)
    L1.insert(6)
    L1.insert(9)
    L1.insert(15)
    L1.insert(30)
    print("\nPrint the first LinkedList.\n")
    L1.printList()
    L2 = LinkedList()
    L2.insert(10)
    L2.insert(15)
    L2.insert(30)
    print("\nPrint the second LinkedList.\n")
    L2.printList()
    print("\nPrint the common LinkedList")
    intersection_Point = L1.intersectionPoint(L1.head, L2.head)
    print("\nThe intersectionPoint:", intersection_Point)
