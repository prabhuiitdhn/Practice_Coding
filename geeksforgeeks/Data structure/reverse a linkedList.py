"""
Problem is reverse the LinkedList.
This linkedList is being created using self.head, and self.tail.
If node is new, then it is representing self.head.
if node is not new then adding the elements in the self.tail.next.
"""


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head

        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    # def reverseList(self, head):
    #     previous, current, Next = None, head, None
    #     while current:
    #         Next = current.next
    #         current.next = previous
    #         previous= current
    #         current= Next
    #     head = previous

    def reverseList(self):
        """
        previous takes the address of previous node[remember previous should be None]
        current takes the address of current node
        Next takes the address of next node.
        @return:
        """
        previous, current, Next = None, self.head, None
        while current: # it is for until current is there
            Next = current.next # Storing the next address of current.
            current.next = previous # Linking the current to previous node.
            previous = current # in the next iteration, current becomes the previous
            current = Next # next becomes the previous.

        # this is the case when current ends, meaning there is not more elements in the list remained to be reversed.
        self.head = previous # previous node will becomes head.


def printList(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print()


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(10)
    ll.insert(12)
    ll.insert(13)
    ll.insert(14)
    printList(ll.head)
    print("\nAfter reversong\n")
    ll.reverseList()
    printList(ll.head)
