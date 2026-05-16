# Node Initialisation
class Node:
    # function to initialise the node object
    def __init__(self, data):
        # assign data
        self.data = data
        # assign pointer as None
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        # list object
        self.head = None

    # Printing the node
    def printlist(self):
        print("The element in list:")
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


# Introduce a Linked List
# driver to run the program
if __name__ == '__main__':
    # initialising the list
    llist = LinkedList()
    # Creating a node first
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Need to linked them
    llist.head.next = second
    second.next = third
    third.next = None

    # Check the node
    print("LinkedList is completed:", llist)
    llist.printlist()