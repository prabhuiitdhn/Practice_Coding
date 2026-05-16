# 
import numpy as np
import math
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        global perform
        stack = []
        operator = ['+', '-', '*', '/']
        for e in tokens:
            if e not in operator:
                stack.append(int(e))
            else:
                first = int(stack.pop())
                second = int(stack.pop())
                if e == '+':
                    perform = second + first
                if e == "-":
                    perform = second - first
                if e =="*":
                    perform = second * first
                if e == "/":
                    # perform = math.trunc(second/first)
                    perform = int(second/first)
                    if perform == -1:
                        perform = 0
                    print("perform", perform)

                stack.append(perform)
                print(stack)
        return int(np.ceil(stack[0]))


# tokens = ["2","1","+","3","*"]
# tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
tokens = ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
s = Solution()

print(s.evalRPN(tokens))
