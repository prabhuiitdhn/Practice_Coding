class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class circularLinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        temp = self.head
        new_node.next = self.head
        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
        else:
            new_node.next = new_node
        self.head = new_node

    def printList(self):
        print("The circular data:")
        temp = self.head
        if self.head is not None:
            while True:
                print(temp.data)
                temp = temp.next
                if temp == self.head:
                    break


if __name__ == "__main__":
    cllist = circularLinkedList()
    # first = Node(10)
    # second = Node(20)
    # third = Node(30)
    # fourth = Node(40)
    # first.next = second
    # second.next = third
    # third.next = fourth
    # fourth.next = first
    # cllist.head = first
    # cllist.printList()
    cllist.push(5)
    cllist.push(10)
    cllist.push(15)
    # cllist.push(20)
    cllist.printList()
