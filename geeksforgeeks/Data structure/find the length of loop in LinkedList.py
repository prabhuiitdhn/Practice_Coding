"""
https://www.geeksforgeeks.org/find-length-of-loop-in-linked-list/

problem:https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1?page=1&company[]=Samsung&company[]=Qualcomm&company[]=KLA%20Tencor&category[]=Linked%20List&sortBy=difficulty
Problem is to find the loop in linkedlist. so, if self.tail[Last node] of the list is connected with any node which is already visited then It detects the loop.
Approach:
    https://www.geeksforgeeks.org/detect-loop-in-a-linked-list/
    1. Detect loop using hashing
    2. Detect loop in a linked list by Modification In Node Structure:(add flag node in LinkedListNode)
    3. Detect loop in a linked list using Floyd’s Cycle-Finding Algorithm: using rabbit and tortoise pointer, rabbit goes 2 steps, and tortoise goes 1 steps
    4.Detect loop in a linked list by Marking visited nodes without modifying Node structure:
    5. Detect loop in a linked list by Modifying Value: (visited node should have data '-1')
"""


class Node:
    """
    Node representing the linkedList.
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    Linked list functions.
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        """
        It is for inserting the data in the linkedlist with two pointer in the algorithm
        @param data: input data which will create the linkedList node and add to list.
        @return:
        """
        if self.head is None:
            # if self.head is None, meaning "No elements in the list, then create a node and put into the self.head"
            self.head = Node(data)
            # for one element in the list will have self.tail and self.head at one reference.
            self.tail = self.head

        else:
            # this is the case It has more than one element.
            # self.head will always represents the first elements on the list
            # but self.tail will add an elements.
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def printList(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def loopHere(self, pos):
        """
        This function is for adding the loop/connection to the previous visited loop in the linkedList.
        @param pos: pos is the index where self.tail will connect which will form the loop
        @return:
        """
        if pos == 0:
            """
            It shows if the position is 0, meaning no connection will found
            """
            return
        walk = self.head
        # start index and walk till the position we found
        for i in range(1, pos):
            # walk till the pos is finished.
            walk = walk.next

        # add the links between the tail and position.
        self.tail.next = walk

    def countNodesinLoop(self, head):
        """
        approach 1: Based on modifying the data inside the list. but this will reflect the elements in the list
        approach 2: where no modification of data inside list will happen but can detects the loops
        @param head:
        @return:
        """
        # # # # this below steps takes care of whether the loop exists or not? If yes, then store the address where loop exist.
        rabbit = head
        tortoise = head
        store_address = []
        while tortoise and rabbit.next and rabbit.next.next:
            # Checking if current, current.next, and current.next.next is available or not?
            rabbit = rabbit.next.next  # worked 2 steps
            tortoise = tortoise.next  # worked 1 step
            if rabbit == tortoise:  # if both met at same point, we say that loops are available.
                # until loop is found rabbit and tortoise will move ahead with 2 and 1 steps.
                store_address.append(rabbit) # Storing the address where loop exist
                break

        # This is for counting the number in-between two loops.
        count = 0
        current = head
        while current:

            if current in store_address:
                # CHeck if node which is being connected is in stored place or not? if yes, count starts until last
                # where loop ends
                rabbit = current
                tortoise = current
                while tortoise and rabbit.next and rabbit.next.next:
                    rabbit = rabbit.next.next
                    tortoise = tortoise.next
                    count += 1
                    if rabbit == tortoise:
                        # again the loop run and finds here that both node matches and return the counts until now.
                        return count
            else:
                # if not stored in the stored list and move to next pointer.
                current = current.next

        return count


if __name__ == "__main__":
    LL = LinkedList()  # creating the LinkedList.
    LL.insert(25)  # insertion.
    LL.insert(14)
    LL.insert(19)
    LL.insert(33)
    LL.insert(10)
    LL.insert(21)
    LL.insert(39)
    LL.insert(90)
    LL.insert(58)
    LL.insert(45)
    # LL.insert(5)
    print("Printing the LinkedList.\n")
    LL.printList()  # printing the linkedList.
    print("Adding the Loop in the Linkedlist.\n")
    LL.loopHere(4)
    # if LL.detectLoop(LL.head) is True:
    #     print("Loop available")
    # else:
    #     print("No loop")

    print("\nLength\n")
    print(LL.countNodesinLoop(LL.head))