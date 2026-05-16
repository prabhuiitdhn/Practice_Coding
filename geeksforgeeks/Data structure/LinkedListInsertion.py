'''
Inserting the node:
    1. Inserting the node at header
    2. inserting the node at last pointer
    3. inserting the node in the middle; with index
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        element_list = []
        temp = self.head
        while temp:
            element_list.append(temp.data)
            temp = temp.next
        print("The elements:", element_list)

    def insert_at_first(self, value):
        new_node = Node(value)
        temp = self.head
        new_node.next = temp
        self.head = new_node

    def insert_at_last(self, val):
        new_node = Node(val)
        temp = self.head
        while temp:
            if temp.next is None:
                temp.next = new_node
                new_node.next = None
            temp = temp.next

    def insert_at_index(self, val, index):
        new_node = Node(val)
        count = 1
        temp = self.head
        while temp:
            temp = temp.next
            count += 1
            if count == index:
                p = temp.next
                temp.next = new_node
                new_node.next = p

    def deleteList(self, index):
        count = 1
        temp = self.head
        while temp:
            temp = temp.next
            count += 1
            if count == index-1:
                p = temp.next
                temp.next = p.next


if __name__ == '__main__':
    # initialising the linkedList
    llist = LinkedList()
    # intialing the node
    first, second, third, fourth, fifth = Node(10), Node(20), Node(30), Node(40), Node(50)
    llist.head = first
    first.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = None
    # printing the elements in the list
    llist.printList()
    # inserting new node in the list
    # insert 5 at first
    new_first = Node(5)
    llist.head = new_first
    new_first.next = first
    print("After inserting:")
    llist.printList()
    # inserting at end
    new_last = Node(55)
    fifth.next = new_last
    new_last.next = None
    print("After adding to the last:")
    llist.printList()
    # adding elements in the beginning
    print("Adding elements at beginning using the function:")
    llist.insert_at_first(100)
    llist.printList()
    print("Adding elements at last using the function:")
    llist.insert_at_last(105)
    llist.printList()
    print("Adding elements at index:")
    llist.insert_at_index(444, 3)
    llist.printList()
    print("Delete a key 4th key at the list:")
    llist.deleteList(4)
    llist.printList()