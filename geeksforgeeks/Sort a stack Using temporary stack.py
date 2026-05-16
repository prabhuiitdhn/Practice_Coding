"""
https://practice.geeksforgeeks.org/problems/sort-a-stack/1?page=1&company[]=IBM&sortBy=submissions
Asked in IBM
Given a stack and needed to sort the elements in the stack
"""

from typing import List


class CreateStack:
    def __init__(self, length):
        self.stack = []
        self.stackLength = length

    def push(self, element):
        if len(self.stack) == self.stackLength:
            print("Stack is Full, Need to remove the element")
            return

        self.stack.append(element)
        return

    def isEmpty(self):
        if len(self.stack) == 0:
            return True

    def isFull(self):
        if len(self.stack) == self.stackLength:
            return True

    def remove(self):
        if len(self.stack) == 0:
            print("Stack is empty")
            return
        current_element = self.stack[-1]
        self.stack = self.stack[:-1]
        return current_element

    def printStack(self):
        for i in self.stack:
            print(i, '')

    def top(self):
        return self.stack[-1]

    def total_length(self):
        return len(self.stack)

    def sorting(self):
        temp = CreateStack(self.stackLength)
        while len(self.stack)>0:
            pop_top_element = self.remove()
            if temp.isEmpty():
                temp.push(pop_top_element)
            else:
                if pop_top_element>temp.top():
                    temp.push(pop_top_element)
                else:
                    while pop_top_element<temp.top():
                        self.push(pop_top_element)
        self.stack = temp
        return self.stack


if __name__ == "__main__":
    Stack = CreateStack(6)
    Stack.push(34)
    Stack.push(3)
    Stack.push(31)
    Stack.push(98)
    Stack.push(92)
    Stack.push(93)
    Stack.push(95)
    Stack.push(96)
    Stack.printStack()
    print("Top element on the stack:", Stack.top())
    print("Removed Element:", Stack.remove())
    Stack.printStack()
    print("After Sorting:")
    # temp = Stack.sorting()
    # temp.printStack()



