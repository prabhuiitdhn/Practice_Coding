"""
Generate Parentheses
https://practice.geeksforgeeks.org/problems/generate-all-possible-parentheses/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=KLA%20Tencor&category[]=Recursion&sortBy=difficulty
"""

from typing import List



def AllParenthesis2(n):
    # Code here
    # this is based on DFS [depth first search ]
    # Create a DFS tree and each node will have two possibilities '(' or ')'
    # for n == 2

    """
    needed to take left and right node
    Start from open, close as no of open and close bracket we have
    plot the tree and look for balanced generated parenthesis and add it.

                    (open:2, close:2)
                    /          \
                (open-1:1, close:2)
                /
               (open-1:0, close:2)
               /            \
    (open-1: -1, close:2)   (0:1)
                            /     \
                           (-1: 1)  (0:0)
               # this is not possible

    """

    def generate(openn, close, out, res):

        if openn == 0 and close == 0:
            # after coming to this, all open and close bracket will be finished.
            res.append(out)
            return

        if openn > 0:
            # if still open is available go for next node/level of tree
            out1 = out
            out1 = out1 + "("
            generate(openn - 1, close, out1, res)

        if close > openn:
            # this is mainly for backtracking which up a level  or same where ')' has to be added.
            out2 = out
            out2 = out2 + ")"
            generate(openn, close - 1, out2, res)
        return

    openn = n
    close = n
    out = ""
    res = []
    generate(openn, close, out, res)
    return res

def AllParenthesis(n) -> List:
    # it might work but It fails in some cases,
    # bruteforce approach which might not work for all
    # work with N = 4, it is loosing the combinations for  (2+2)
    if n == 0:
        return []

    AllString = []

    currentStr = ""
    for i in range(n):
        currentStr = currentStr + '('

    for j in range(n):
        currentStr = currentStr + ')'

    AllString.append(currentStr)

    L = AllParenthesis(n-1)
    for e in L:
        AllString.append('()' + str(e))

    for e in L:
        AllString.append(str(e) + '()')

    for e in L:
        currentStr = '(' + str(e) + ')'
        AllString.append(currentStr)


    return list(set(AllString))





n = 4
print(sorted(AllParenthesis2(n)))
print(len(sorted(AllParenthesis2(n))))
print(sorted(AllParenthesis(n)))
print(len(sorted(AllParenthesis(n))))
