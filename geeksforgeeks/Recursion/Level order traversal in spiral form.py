"""
https://practice.geeksforgeeks.org/problems/level-order-traversal-in-spiral-form/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=KLA%20Tencor&category[]=Recursion&sortBy=difficulty

complete the function to find the spiral order traversal of a tree.

TREE data structure.
"""

from collections import deque


# Tree node. Each tree will have 2 nodes [Left and Right]
class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


# function to build Tree
def buildTree(s):
    # corner cases
    if len(s) == 0 or s[0] == "N":
        return None

    # creating the list of strings from input
    # string after splitting by space.
    ip = list(map(str, s.split()))

    # creating root of the tree
    root = Node(int(ip[0]))
    # this is root node of the tree, where the data is being passed and pointer left and right is being assigned
    size = 0
    q = deque()

    # push the root in the queue
    q.append(root)
    size += 1

    # starting from the second elements.
    i = 1
    while (size > 0 and i < len(ip)):
        # Get and remove the front of the queue
        currentNode = q[0]
        q.popleft()
        size = size - 1
        currentVal = ip[i]

        # if the childNode is not none
        if currentVal != "N":
            currentNode.left = Node(int(currentVal))
            # push it to the queue.
            q.append(currentNode.left)
            size = size + 1

        # for the right child

        i = i + 1
        if i >= len(ip):
            break
        currentVal = ip[i]

        if currentVal != "N":
            currentNode.right = Node(int(currentVal))
            q.append(currentNode.right)
            size = size + 1
        i = i + 1

    return root


def findSpiral(s):
    l = []
    if s is None:
        return

    l.append(s.data)
    # l.append(findSpiral(s.right))
    # l.append(findSpiral(s.left))
    if s.right:
        # findSpiral(s.right)
        l.append(findSpiral(s.right))

    if s.left:
        # findSpiral(s.left)
        l.append(findSpiral(s.left))
    return l


if __name__ == "__main__":
    # t = int(input())
    t = 5
    for _ in range(0, t):
        # s = input()
        s = '10 30 20 40 60'
        root = buildTree(s)
        result = findSpiral(root)
        for value in result:
            print(value, end=" ")
        print()
