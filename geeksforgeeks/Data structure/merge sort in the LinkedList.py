"""https://practice.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1?page=1&company[]=Adobe&company[
]=Samsung&company[]=Qualcomm&company[]=KLA%20Tencor&category[]=Linked%20List&sortBy=difficulty understanding:

https://www.geeksforgeeks.org/merge-sort-for-linked-list/

Algorithm:
 1. needed two pointer, headref (which takes care
of the head of the linkedList as reference. because as if head becomes the headNode for the linkedList then it will
reflect the list when it will not be the minimum element of the linkedList.)

2. Once headref is being found then, find the middle point of the linkedList and try to sort the leftsplit and rightSplit
3. sort the left and rightsplit and merge later, it will have sorted array in plate.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # push new value to linked list
    # using append method
    def append(self, new_value):

        # Allocate new node
        new_node = Node(new_value)

        # if head is None, initialize it to new node
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next

        # Append the new node at the end
        # of the linked list
        curr_node.next = new_node

    def getMiddleElements(self, head):
        """
        @param head: using head of linkedList, needed to find the middle element @return: middle elements
        approach 1: find the length of LinkedList and traverse the element until n/2 element of linkedList. approach
        2: using rabbit and tortoise technique, rabbit will move two pointer, and tortoise will move one pointer at a
        time, and somewhere one of the both will become none and will be middle elements of the list.
        """
        if head is None:
            return head

        tortoise = head
        rabbit = head

        # while tortoise.next is not None and rabbit.next.next is not None:#
        # this is not correct bcz tortoise.next is available bcz rabbit.next.next was available in the last loop, so next
        # to to check rabbit.next and rabbit.next.next is available or not? bcz toroise will always be there until rabbit.next.next is avialble.

        while rabbit.next is not None and rabbit.next.next is not None:
            tortoise = tortoise.next
            rabbit = rabbit.next.next

        return tortoise

    def sortedMerge(self, head1, head2):
        """
        @param head1:
        @param head2:
        @return:
        """
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        if head1.data < head2.data:
            mergedResult = head1
            mergedResult.next = self.sortedMerge(head1.next, head2)
        else:
            mergedResult = head2
            mergedResult.next = self.sortedMerge(head1, head2.next)

        return mergedResult

    def mergeSort(self, headref):
        """
        @param headref: Head is input parameter for the LinkedList.
        @return: it should return the sorted LinkedList.
        """
        if headref is None or headref.next is None:
            # it shows only one elements in the linkedList.
            return headref

        # if more than one elements in the List
        middleElement = self.getMiddleElements(headref)
        # once we get middle element
        nextToMiddle = middleElement.next  # this will keep the next half of reference.
        middleElement.next = None  # until head to middleElement will have left half of referece.

        leftSplit = self.mergeSort(headref)  # it take cares of headref to middleElement becacuse middle.next is None
        rightSplit = self.mergeSort(nextToMiddle)  # It take cares of nextafterMiddle becase reference is stored.
        # if left split or rightsplit will have one element then return directly else again process the same for mergersorting.
        SortedmergedList = self.sortedMerge(leftSplit, rightSplit)
        return SortedmergedList


def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end=" ")
        curr_node = curr_node.next
    print(' ')


if __name__ == '__main__':
    li = LinkedList()

    # Let us create a unsorted linked list
    # to test the functions created.
    # The list shall be a: 2->3->20->5->10->15
    li.append(15)
    li.append(10)
    li.append(5)
    li.append(20)
    li.append(3)
    li.append(2)

    print("Printing the List.\n")
    printList(li.head)
    print("\nApply merge sort.\n")
    # Apply merge Sort
    SortedNode = li.mergeSort(li.head)
    print("Sorted Linked List is:")
    printList(SortedNode)
