"""
https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1?page=1&company[]=Adobe&company[]=Samsung&company[]=Qualcomm&company[]=KLA%20Tencor&category[]=Linked%20List&sortBy=difficulty
problem is: given a linkedList and needed to check if the LinkedList is palindrome or not
approach1:
concatenate all the elements in the linkedList in a string and check string is palindrome or not?

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
        # self.head = self.tail

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

    def checkPalindrome(self):
        string = ''
        current = self.head
        while current:
            string +=str(current.data)
            current = current.next

        if string == string[::-1]:
            return True

        return False


if __name__ == "__main__":
    l1 = LinkedList()
    l1.append(1)
    l1.append(3)
    l1.append(3)
    l1.append(1)
    l1.append(2)
    print("Printing LinkedList.\n")
    l1.printList()
    if l1.checkPalindrome():
        print("Yes")
    else:
        print("No")
