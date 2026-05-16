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

    def printList(self, head):
        # current = self.head
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def addTwoLists(self, first, second):

        def lengthOfList(head):
            count = 0
            current = head
            while current:
                count +=1
                current = current.next
            return count

        def calculateNum(head):
            sumOfList = 0
            length = lengthOfList(head)
            current = head
            while current:
                sumOfList += current.data * 10 ** (length-1)
                length -= 1
                current = current.next

            return sumOfList

        def convertNumberIntoList(number):
            s = str(number)
            l3 = LinkedList()
            for i in s:
                l3.insert(int(i))
            return l3.head

        def calculateStrNumber(head):
            current = head
            s = ''
            while current:
                s += str(current.data)
                current = current.next
            return int(s)

        number1 = calculateStrNumber(first)
        number2 = calculateStrNumber(second)
        number3 = number1 + number2
        listNode = convertNumberIntoList(number3)

        return listNode

if __name__ == "__main__":
    L1 = LinkedList()
    L1.insert(1)
    L1.insert(2)
    L1.insert(3)
    print("\nL1:")
    L1.printList(L1.head)
    L2 = LinkedList()
    L2.insert(3)
    L2.insert(2)
    L2.insert(1)
    print("\nL2:")
    L2.printList(L2.head)
    p = LinkedList().addTwoLists(L1.head, L2.head)
    print("\nLine no 75\n")
    L2.printList(p)