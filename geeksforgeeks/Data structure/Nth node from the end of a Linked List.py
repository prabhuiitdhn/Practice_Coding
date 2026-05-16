class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        '''
        Push the data in the LinkedList.
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

    def length(self):
        '''
        Find the length of all the LinkedList.
        @return:
        '''
        count = 0
        current = self.head
        while current:
            count +=1
            current = current.next

        return count

    def nthElement(self, position):
        '''
        Find the Nth element in the LinkedList from the backside.
        @param position: this position is being written from the last.
        @return:
        '''
        index_from_start = llist.length() - position + 1
        current = self.head
        count =0
        while current:
            count +=1
            if count == index_from_start:
                return current.data
            current = current.next

        return "Position not found."

    def printList(self):
        '''
        Print the List element in the List.
        @return:
        '''
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next


if __name__ == "__main__":
    llist = LinkedList()
    llist.push(10)
    llist.push(9)
    llist.push(8)
    llist.push(7)
    llist.push(6)
    llist.push(5)
    # printing the element in the List.
    print("Print the List.")
    llist.printList()
    print("\nLength of List:", llist.length())
    print("\n3rd last element from the list:", llist.nthElement(position=3))

