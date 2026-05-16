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

    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        def lengthofList(head):
            count = 0
            current = head
            while current:
                count += 1
                current = current.next
            return count

        lenofList = lengthofList(head)

        mid_element = lenofList // 2 + 1

        current = head
        # lengthofList= lengthofList(head)
        for i in range(1, mid_element+1):
            if i == mid_element:
                return current.data
            current = current.next

        return "-1"


if __name__ == "__main__":
    ll = LinkedList()
    ll.push(1)
    ll.push(9)
    ll.push(2)
    ll.push(3)
    ll.push(4)
    ll.push(5)
    # ll.push(10)
    # ll.push(9)
    ll.printList()
    print("Mid element")
    print(ll.findMid(ll.head))
    # node = ll.getNode(12)
    # ll.delete_node(node)
    # print(" ")
    # ll.printList()
