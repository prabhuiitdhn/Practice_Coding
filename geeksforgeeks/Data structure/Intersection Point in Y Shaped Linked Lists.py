"""
https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1?page=1&company[]=Adobe&company[]=Samsung&company[]=Qualcomm&company[]=KLA%20Tencor&category[]=Linked%20List&sortBy=difficulty

Problem: Given in two linkedList, needed to find the common element which connects both the list in the linkedList. It will form Y shape where some node will represents as tail of Y
example:
LinkedList1: 3->6->9->15->30
LinkedList2: 10->15->30

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
        def lengthOfList(head):
            count = 0
            current = head
            while current:
                count += 1
                current = current.next
            return count

        list_of_element = []
        lengthHead1 = lengthOfList(head1)
        lengthHead2 = lengthOfList(head2)

        if lengthHead1 > lengthHead2:
            current = head2
            while current:
                list_of_element.append(current.data)
                current = current.next

            next_current = head1
            while next_current:
                if next_current.data in list_of_element:
                    return next_current.data
                next_current = next_current.next
        else:
            current = head1
            while current:
                list_of_element.append(current.data)
                current = current.next

            next_current = head2
            while next_current:
                if next_current.data in list_of_element:
                    return next_current.data
                next_current = next_current.next
        return "-1"


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
    L2.insert(12)
    L2.insert(32)
    print("\nPrint the second LinkedList.\n")
    L2.printList()
    print("\nPrint the common LinkedList")
    intersection_Point = L1.intersectionPoint(L1.head, L2.head)
    print("\nThe intersectionPoint:", intersection_Point)
