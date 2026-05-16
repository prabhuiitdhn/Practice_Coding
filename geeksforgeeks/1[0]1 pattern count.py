'''
given a string, find the number of patterns of form 1[0]1 and [0] can be any numbers of 0s
example:
S = "100001abc101"
in this string, we have 2 1[0]1 pattern, 100001 and 101
approach:
1. can use used using 2 pointer approach
2. stack
3. tracking the string
'''

from collections import deque

def patternCount(S):
    pattern_count = 0
    d = deque()

    for i in S:
        if len(d)==0:
            if i == '1':
                d.append(i)
        else:
            if i != '0' or i != '1':
                if d[-1] == '1' and i== '1':
                    d.clear()
                    d.append(i)
                    continue
                if d[-1] == '1' and i== '0':
                    d.append(i)
                    continue
                if d[-1] == '0' and i=='0':
                    d.append(i)
                    continue
                if d[-1]=='0' and i == '1':
                    pattern_count +=1
                    d.clear()
                    d.append(i)
                    continue
            d.clear()

    return pattern_count

# S = "1001ab010abc01001"
# S = "100001abc101"
# S = "abc1010101bca10"
S ="0000001000000000101101"
print(patternCount(S))
