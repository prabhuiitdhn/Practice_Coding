class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyStack:
    def __init__(self):
        self.head = None

    def push(self, data):
        current = StackNode(data)
        current.next = self.head
        self.head = current
        # current = StackNode(data)
        # if self.head is None:
        #     self.head = current
        # else:
        #     p = self.head
        #     while p.next:
        #         p = p.next
        #     p.next = current
        #     current.next = None

    def pop(self):
        if self.head is None:
            return "-1"

        x = self.head.data
        self.head = self.head.next
        return x
        # # if self.head is None:
        # #     # it show no elements in the stack
        # #     return "-1"
        # p = self.head.next
        # if p is None:
        #     self.head = None
        #     return "-1"
        #
        # previous = self.head
        # while p.next:
        #     previous = p
        #     p = p.next
        # previous.next = None
        # return p.data

    def print(self):
        if self.head is None:
            print("No elements in the list.")
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next


if __name__ == "__main__":
    s = MyStack()
    s.push(10)
    s.push(12)
    s.push(13)
    s.push(14)
    print("\nPrinting the stack.")
    s.print()
    print("\n After poping the stack.")
    print(s.pop())
    print("\n")
    s.print()
    # s.pop()
    # print("\n")
    # s.print()
    # s.pop()
    # print("\n")
    # s.print()
    # s.pop()
    # print("\n")
    # s.print()

    # s.print()

