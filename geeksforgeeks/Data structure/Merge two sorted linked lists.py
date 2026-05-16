"""
https://practice.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1?page=1&company[]=Adobe&company[]=Samsung&company[]=Qualcomm&company[]=KLA%20Tencor&category[]=Linked%20List&sortBy=difficulty
problem: merging two sorted linkedlist
approach 1: add both the element in the new linkedlist and perform mergesort () # this approach may fail in some caes
so, approach 2: add the elements in list from both the list and comapre the elements.
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

def printList(n):
    current = n

    while current:
        print(current.data, end=' ')
        current= current.next

def getMiddleElements(head):
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

def sortedMergeHelper(head1, head2):
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
        mergedResult.next = sortedMergeHelper(head1.next, head2)
    else:
        mergedResult = head2
        mergedResult.next = sortedMergeHelper(head1, head2.next)

    return mergedResult

def mergeSort(headref):
    """
    @param headref: Head is input parameter for the LinkedList.
    @return: it should return the sorted LinkedList.
    """
    if headref is None or headref.next is None:
        # it shows only one elements in the linkedList.
        return headref

    # if more than one elements in the List
    middleElement = getMiddleElements(headref)
    # once we get middle element
    nextToMiddle = middleElement.next  # this will keep the next half of reference.
    middleElement.next = None  # until head to middleElement will have left half of referece.

    leftSplit = mergeSort(headref)  # it take cares of headref to middleElement becacuse middle.next is None
    rightSplit = mergeSort(nextToMiddle)  # It take cares of nextafterMiddle becase reference is stored.
    # if left split or rightsplit will have one element then return directly else again process the same for mergersorting.
    SortedmergedList = sortedMergeHelper(leftSplit, rightSplit)
    return SortedmergedList

def sortedMerge(head1, head2):
    # # # approach 1 using mergeSort()
    # l3 = LinkedList()
    # current_head1 = head1
    # current_head2 = head2
    # while current_head2:
    #     l3.append(current_head2.data)
    #     current_head2 = current_head2.next
    #
    # while current_head1:
    #     l3.append(current_head1.data)
    #     current_head1 = current_head1.next
    #
    # sortedListMerged = mergeSort(l3.head)
    # sortedListMergedreturn = LinkedList()
    # sortedListMergedreturn.head = sortedListMerged
    # return sortedListMergedreturn.head

    # # # approach 2 using adding the elements from the both linkedlist and comapre.
    if head1.data < head2.data:
        # check both elements (head) and check which is smallest.
        res = head1
        curr = head1
        head1 = head1.next
    else:
        res = head2
        curr = head2
        head2 = head2.next

    while True: #if one become none add all the elements from remaining elements from another list.

        if head1 == None:
            curr.next = head2
            return res
        elif head2 == None:
            curr.next = head1
            return res

        if head1.data < head2.data:
            curr.next = head1
            head1 = head1.next
            curr = curr.next
        else:
            curr.next = head2
            head2 = head2.next
            curr = curr.next


if __name__ == "__main__":
    l1 = LinkedList()
    l2 = LinkedList()
    l1.append(5)
    l1.append(10)
    l1.append(15)
    l1.append(40)
    l2.append(2)
    l2.append(3)
    l2.append(20)
    sortedList = sortedMerge(l1.head,l2.head)
    printList(sortedList)