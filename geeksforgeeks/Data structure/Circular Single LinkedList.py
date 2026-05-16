class Node:
    def __init__(self, data):
        self.data = data
        self.Next = None


class CircularLinkedList:
    """
    Insertion in the circular list: To insert an element we always keeps track of the last pointer, which gives O(1) time complexity to perform the insertion in the list.
    1. Insertion in an empty list: This is for an inserting an element in the empty list
    2. Insertion an element in the beginning of the list
    3. Insertion at the end of the list
    4. insertion in between the nodes.
    """

    def __init__(self):
        """
        self.last is the pointer which always keeps the track of last pointer of the circular list.
        It helps use to add the element in the O(1) time complexity
        1. It helps to add the element in the beginning without list traversing
        2. It also helps to add the element in the end without list traversing.
        """
        self.last = None

    def addToEmpty(self, data):
        """
        Initially, when the list is empty, the last pointer will be NULL.
        This is for adding an element when list is empty.
        last pointer: last of the list, it always keeps the track of last pointer in the list.
        @return:
        """
        # If self.last is not none, i.e list is not empty
        if self.last is not None:
            return self.last

        # if the list is empty
        temp = Node(data)  # creating the new node.
        self.last = temp  # linking the last node with newly created node.
        self.last.Next = self.last  # list with itself because It is circular linkedList.

    def addToBegin(self, data):
        if self.last is None:
            return self.addToEmpty(data)

        temp = Node(data)
        # linking the newly created node to start of the node.
        temp.Next = self.last.Next
        self.last.Next = temp

    def addToLast(self, data):
        if self.last is None:
            return self.addToEmpty(data)

        temp = Node(data)
        temp.Next = self.last.Next
        self.last.Next = temp
        self.last = temp

    def addAfter(self, item, data):
        """
        This is adding a new node after the item is being found in the circular list.
        @param item: The element which is already existed in the Circular linkedList.
        @param data: The data which needs to be added after the the item is being found.
        @return:
        """

        # creating the new node
        temp = Node(data)
        if self.last is None:
            # check If the self.last is None or not? If it is now
            print("List is empty")
            return self.addToEmpty(data)

        p = self.last.Next
        while p:
            if p.data == item:
                temp.Next = p.Next
                p.Next = temp

                if p == self.last:
                    # if p was the last node in the circular list
                    self.last = temp
                    return self.last
                    # now new node will be the last node of circular list.
            p = p.Next
            if p == self.last.Next:
                print("This given item is not there.")
                return

    def printCircularLinkedList(self):
        if self.last is None:
            print("List is empty")

        # it represents the first elements in the list.
        temp = self.last.Next

        while temp:
            print(temp.data, end=" ")
            temp = temp.Next
            if temp == self.last.Next:
                # breaking the loop after finding the node where it is started.
                break


if __name__ == "__main__":
    cll = CircularLinkedList()
    # addding the elements in the empty list
    print("Adding the initial Circular LinkedList.")
    cll.addToEmpty(10)
    # print the elements in the list
    cll.printCircularLinkedList()
    # adding the element in the beginning.
    cll.addToBegin(11)
    cll.addToBegin(12)
    print("\nPrinting the added element in the beginning.")
    cll.printCircularLinkedList()
    print("\nAdding the element in the last.")
    cll.addToLast(9)
    cll.addToLast(8)
    cll.printCircularLinkedList()
    print("\nAdding the elements after the item being found.")
    cll.addAfter(10, 11)
    cll.printCircularLinkedList()