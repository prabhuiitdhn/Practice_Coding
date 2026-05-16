class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def addNode(self, val):
        node = Node(val)
        node.next = None
        self.head = Node


l1 = linkedlist()
l1.addNode(1)
