class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next


def printList(head):
    current = head
    while current:
        print(current.data, end=' ')
        current = current.next
    print()


def findIntersection2(head1, head2):
    current_1 = head1
    current_2 = head2

    third_linked_list = LinkedList()
    while current_1 and current_2:
        if current_1.data < current_2.data:
            current_1 = current_1.next
        elif current_1.data == current_2.data:
            third_linked_list.insert(current_1.data)
            current_2 = current_2.next
            current_1 = current_1.next
        else:
            current_2 = current_2.next

    return third_linked_list.head


def findIntersection(head1, head2):
    # THIS APPROACH WILL NOT WORK IN THE CASE WHERE ORDER OF ELEMENT MATTERS
    # return head
    set_head1 = ()
    set_head2 = ()

    current_1 = head1
    while current_1:
        set_head1.append(current_1.data)
        current_1 = current_1.next

    set_head1 = set(set_head1)

    current_2 = head2
    while current_2:
        set_head2.append(current_2.data)
        current_2 = current_2.next
    set_head2 = set(set_head2)

    final_common_elements = set_head1 | set_head2

    third_linked_list = LinkedList()
    for common_element in final_common_elements:
        third_linked_list.insert(common_element)

    return third_linked_list.head


if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()

    l1.insert(4)
    l1.insert(8)
    l1.insert(15)
    l1.insert(17)
    l1.insert(18)

    l2.insert(4)
    l2.insert(10)
    l2.insert(18)
    # l2.insert(8)

    print("L1 is available:\n")
    printList(l1.head)

    print("L2 is available:\n")
    printList(l2.head)

    h = findIntersection2(l1.head, l2.head)
    print("Common elements.")
    printList(h)
