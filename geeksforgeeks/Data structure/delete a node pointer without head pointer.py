class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # initializing the linkedList
    def __init__(self):
        self.head = None

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

    def printList(self):
        '''
        we don't require to have list[optional] because we are already into list.
        @return:
        '''
        temp = self.head  # assume the head of list is temp
        while temp:  # until the temp node is availabe in the linkedList
            print(temp.data, end=" ")  # print the temp data.
            temp = temp.next  # and passing to the next pointer of the current node.

    def delete_node(self, node):
        if node is None:
            return
        elif node.next is None:
            print("Last node")
        else:
            node.data = node.next.data
            node.next = node.next.next

    def getNode(self, value):
        current = self.head
        # node = None
        while current:
            if current.data == value:
                # node = current
                return current
            else:
                current = current.next
        return None

if __name__ == "__main__":
    ll = LinkedList()
    ll.push(15)
    ll.push(14)
    ll.push(13)
    ll.push(12)
    ll.push(11)
    ll.push(10)
    ll.printList()
    node = ll.getNode(12)
    ll.delete_node(node)
    print(" ")
    ll.printList()
