"""
https://www.geeksforgeeks.org/decimal-equivalent-of-binary-linked-list/

we will have a binary linked list with 0s and 1s and needed to convert into the decimal.
simple python function for binary to decimal: int(str(binary_value), 2)
                        decimal to binary: bin(decimal_value)
[binary value] n = 101
[decimal] int('101', 2) = 5

[decimal] n =5
[binary] bin(5) = '0b101'

left shift: a<<b : a * 2^b
right shift: a>>b : a / 2^b

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append_last(self, data):
        if self.head is None:
            current_node = Node(data)
            self.head = current_node
        else:
            current = self.head
            new_node = Node(data)
            while current.next:
                current = current.next
            current.next = new_node

    def append_first(self, data):
        if self.head is None:
            current_node = Node(data)
            self.head = current_node

        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def to_decimal(self):
        result = 0
        current = self.head
        while current:
            result = (result << 1) + current.data
            current = current.next

        return result

    def printList(self):
        head = self.head
        while head:
            print(head.data, end=" ")
            head = head.next


if __name__ == "__main__":
    list = LinkedList()
    list.append_first(0)
    list.append_first(0)
    list.append_first(0)
    list.append_first(0)
    list.append_first(1)
    print("Linked List:")
    list.printList()
    print()
    print("To_decimal.")
    print(list.to_decimal())
