'''

https://practice.geeksforgeeks.org/problems/parenthesis-checker2744/1?page=1&company[]=Adobe&company[]=Samsung&company[]=Qualcomm&category[]=Strings&sortBy=difficulty
problem:
give the string with parenthesis pair, needed to check the order of parenthesis, If order of parenthesis is correct then It is a balanced string else not.
example: {([])}
approach: stack
'''

from collections import deque


def ispar(x):
    # checking the length of x should be even, otherwise pair will not form.
    open_sq_bracket = '['
    close_sq_bracket = ']'
    open_curly_bracket = '{'
    close_curly_bracket = '}'
    open_bracket = '('
    close_bracket = ')'

    if len(x) % 2 != 0:
        return False
    else:
        d = deque()
        for i in x:
            if len(d) == 0:
                d.append(i)
            else:
                if d[-1] == open_bracket:
                    if i == close_bracket:
                        d.pop()
                    else:
                        d.append(i)
                    continue
                if d[-1] == open_sq_bracket:
                    if i == close_sq_bracket:
                        d.pop()
                    else:
                        d.append(i)
                    continue
                if d[-1] == open_curly_bracket:
                    if i == close_curly_bracket:
                        d.pop()
                    else:
                        d.append(i)
                    continue
        if len(d) == 0:
            return True
        else:
            return False


# x = "{([])}{}"
x = "("
print(ispar(x))
