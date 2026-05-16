class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        '''
        Trying to push the data in front of the List
        @param data:
        @return:
        '''
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next

    def getNthnode(self, position):
        count = 1
        current = self.head
        while current:
            if count == position:
                return current.data
            count += 1
            current = current.next

        return "Not Nth Position in the LinkedList."


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(10)
    llist.push(9)
    llist.push(8)
    llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.printList()
    # this should print the value of Nth Node.
    print("\nFinding the Nth Element.")
    print(llist.getNthnode(position=3))
