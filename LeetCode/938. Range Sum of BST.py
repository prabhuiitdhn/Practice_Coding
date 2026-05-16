class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(node, data):
    if node is None:
        return Node(data)
    else:
        if data > node.data:
            node.right = insert(node.right, data)
        else:
            node.left = insert(node.left, data)

    return node


def printInorder(node):
    if node is None:
        return None
    else:
        printInorder(node.left)
        print(node.data, end=" ")
        printInorder(node.right)


Final_sum = 0


def rangeSumBST(root, low, high):
    global Final_sum
    if root is None:
        return

    if root.data >= low and root.data <= high:
        print(root.data)
        Final_sum += root.data

    # if root.data > high:
    rangeSumBST(root.left, low, high)
    # if root.data < low:
    rangeSumBST(root.right, low, high)

    return Final_sum


if __name__ == "__main__":
    arr = [5, 3, 4, 1, 2, 6, 8, 9, 7]
    root = None
    for i in arr:
        root = insert(root, i)

    printInorder(root)

    # RAngeSume
    low = 7
    high = 15
    print(rangeSumBST(root, low, high))



