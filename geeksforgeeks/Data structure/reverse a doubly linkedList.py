class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = Node(data)
            current.next = self.head
            current.prev = None
            # self.head.prev = current
            self.head = current

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    def reverseList(self):
        """
        Problem is to reverse the doubly linkedlist.
        3 node is required to reverse the LinkedList
        1. Current Node: It is for storing the current node
        2. prev Node: It is to store the previous node
        3. next_ Node: It is to store the next node
        @return:
        """
        # Store the self.head as current Node.
        current = self.head
        prev = None
        next_ = None
        while current:  # it is the current when we check if current Node is existed or not?
            # it always store the next pointer of the dll
            next_ = current.next
            # Linking the current to next and to prev [reversing is here.]
            current.next = prev
            current.prev = next_
            # this works for next iteration
            prev = current
            current = next_

        # prev will have all the reversed pointer
        self.head = prev


if __name__ == "__main__":
    dll = DLL()
    dll.push_at_beginning(12)
    dll.push_at_beginning(13)
    dll.push_at_beginning(14)
    dll.push_at_beginning(15)
    print("Original list printing.")
    dll.printList()
    print("\nReverse List Printing.\n")
    dll.reverseList()
    dll.printList()
