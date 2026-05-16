"""
Double LinkedList will have two pointer.
1. Previous pointer
2. Next pointer.
"""


class Node:
    """
    In the double LinkedList, the node is being created with two pointer.
    """

    def __init__(self, data):
        """
        Two pointer in the Node in the LinkedList.
        self.next is for referring the next pointer of the node.
        self.previous is for referring the previous pointer of the node.
        @param data:
        """
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        """
        Initialisation of Doubly Linked list.
        """
        self.head = None

    def push_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            current.previous = new_node
            new_node.previous = None
            new_node.next = self.head
            self.head = new_node
        return

    def push_at_end(self, data):
        new_node = Node(data)
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        new_node.previous = current
        new_node.next = None

    def push_after_given_node(self, position, data):
        '''
        @param position: Node is being given where exactly the data needs to be added.
        @param data: Node to be created.
        @return:
        '''
        if position.next is None:
            print("This is last of the element in the Doubly Linked List.")
            return

        # Creating new node using data
        new_node = Node(data)  # new node is being created.
        # keeping track of next_after
        next_after_current = position.next
        position.next = new_node
        new_node.next = next_after_current
        new_node.previous = position
        # this link is needed for connecting the previous node.
        if new_node.next:
            new_node.next.previous = new_node

    def push_before_given_node(self, position, data):
        # new_node = Node(data) # creating node.
        # previous_position = position.previous
        # new_node.next = position # keeping track of position.next(bcz this could be use it later.)
        # # position.previous = new_node
        # new_node.previous = previous_position
        # # position.next = new_node.next.next
        # if new_node.previous:
        #     new_node.next.previous = new_node
        new_node = Node(data)
        new_node.next = position
        new_node.previous = position.previous.previous
        position.next = new_node.next.next
        position.previous = new_node
        return

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
        while current:    # it is the current when we check if current Node is existed or not?
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

    def printDLL(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.push_at_beginning(10)
    dll.push_at_beginning(9)
    dll.push_at_beginning(8)
    print("\nPrinting the Doubly LinkedList.")
    dll.printDLL()
    print("\nAdding the element in the end.")
    dll.push_at_end(11)
    dll.push_at_end(12)
    print("\nPrinting element in the end.")
    dll.printDLL()
    print("\nAdding an element after the given node.")
    dll.push_after_given_node(dll.head.next.next, 18)
    dll.printDLL()
    print("\nAdding an element before given node.")
    dll.push_before_given_node(dll.head.next.next, 17) #[it is not working]
    dll.printDLL()
