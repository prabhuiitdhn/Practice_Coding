# initialisation of the Node of the list.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# this is an initialisation of the head of the LinkedList.
class LinkedList:

    # initializing the linkedList
    def __init__(self):
        self.head = None

    # printing the linkedList

    def printList(self):
        '''
        we don't require to have list[optional] because we are already into list.
        @return:
        '''
        temp = self.head  # assume the head of list is temp
        while temp:  # until the temp node is availabe in the linkedList
            print(temp.data, end=" ")  # print the temp data.
            temp = temp.next  # and passing to the next pointer of the current node.

    # this function is used for pushing the data at the fron the LinkedList
    def push(self, new_data):
        '''
        It is being added in the front so, newly data would be head of the LinkedList.
        and previous head of the LinkedList would be 2nd element of current LinkedList
        @param data: is the new parameter for the node which will come & add to the front of the already existed list
        @return: new linkedlist where front node will be added.
        '''

        # change the data into Node
        current = Node(new_data)
        # current node would be pointing to previous linkedList head.
        current.next = self.head
        # current node will behave like head for newly formed LinkedList.
        self.head = current

    def insertAfter(self, prev_node, new_data):
        if prev_node.next == None:
            print("Given node's pointer is None, i.e. It is the last node of the LinkedList")
            return

        '''
        Before:
        prev_node -> next_node
        After:
        prev_node -> new_node -> next_node
        '''

        new_node = Node(new_data)
        # Creating new node.
        new_node.next = prev_node.next
        # Linking the new
        prev_node.next = new_node

    def append(self, new_data):
        '''
        @param new_data: is the parameter which behaves as node. which is append at last of the linkedList
        @return:
        '''
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def search(self, data):
        '''
        @param data: Data to be find in the LinkedList.
        @return: True If data is being found in LinkedList. False, If not.
        '''
        current = self.head

        while current:
            if current.data == data:
                return True
            current = current.next

        return False

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next

        return count

    def delete_at_beginning(self):
        current = self.head
        self.head = current.next

    def delete_node(self, key):
        '''
        Deleting the node after key which is given in the LinkedList.
        If given Key is not available then It should say "Given key is not available in the List."
        @param key:
        @return:
        '''

        current = self.head
        if current.data == key:
            self.head = current.next
        else:
            # prev_node = self.head
            # current = current.next
            while current.next:
                prev_node = current
                if current.next.data == key:
                    prev_node.next = current.next.next
                current = current.next

    def deleteNodeLast(self):
        '''
        Delete the last node of the List.
        @return:
        '''
        current = self.head
        if current.next is None:
            print("Only one node is there.")
            return

        while current.next:
            prev_node = current
            if current.next.next is None:
                prev_node.next = None
                return
            current = current.next

    def reverse(self):
        '''
        approach: prev, current, and next 3 pointer we used to keep track.
        @return:
        '''
        current = self.head
        prev_node = None  # initilaising the previous node
        while current is not None:
            next = current.next
            current.next = prev_node
            prev_node = current
            current = next
        self.head = prev_node


# construction of a simple linkedList with 3 nodes.

if __name__ == '__main__':
    # linkedList is being initialised.
    llist = LinkedList()
    # linkedList will have head in form of node and which will have data and points.
    # currently the data is being '1' but the points is None.
    llist.head = Node(1)  # this is the head of the list
    second = Node(2)  # this is another node of the list which comes after head
    third = Node(3)  # this is another node which will comes after second node
    fourth = Node(4)  # this next node after 3
    fifth = Node(
        5)  # this is the last node after 4 and last node of the list. & the next pointer of the this node should be None.

    # The above is being intialised the node but LinkedList is not being prepared, so preparing the linkedList we need to connect to the pointer to the next node.
    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = None  # It is not even require bcz for fifth node the next point is already initialised as None.

    # # LinkedList is being prepared. Next to print the elements in the list.
    print("Current LinkedList.")
    llist.printList()  # print the linkedList
    '''
    insertion of the node in the LinkedList.
    1. At the front of LinkedList
    2. After the given node
    3. At the end of the LinkedList
    '''
    # Pushing the elements in the front of LinkedList
    print("\nAdded the element in the front of LinkedList.")
    llist.push(0)
    # Print the newly added element list to the front of the linkedList
    llist.printList()

    # Add a node after the given node.
    # Trying to add the 28 value after the second node of the linkedList.
    llist.insertAfter(second, 20)
    print("\n After inserting the element after given node.")
    llist.printList()

    # Add the node at last.
    print("\n Appending the data to the last of LinkedList.")
    llist.append(100)
    llist.printList()

    # Search the data in the LinkedList
    print("Search the element in the LinkedList.")
    print(llist.search(4))
    print("Search the another element in the LinkedList.")
    print(llist.search(24))

    # Find the length of the LinkedList.
    print("Length of the LinkedList.")
    print(llist.length())

    # Delete the element in the List.
    '''
    1. Delete at beginning of the LinkedList
    2. Delete the element after the given node in the list
    3. Delete the last element of the LinkedList.
    '''
    # Deleting the element in the beginning of LinkedList.
    print("Deleting at the begining")
    llist.delete_at_beginning()
    llist.printList()

    print("\nDeleting at the element after given node.")
    llist.delete_node(20)
    llist.printList()

    print("\n Delete node at last of LinkedList")
    llist.deleteNodeLast()
    llist.printList()

    print("\nReverse the LinkedList.")
    llist.reverse()
    llist.printList()
