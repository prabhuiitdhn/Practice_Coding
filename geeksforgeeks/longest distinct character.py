'''
https://practice.geeksforgeeks.org/problems/longest-distinct-characters-in-string5848/1?page=1&company[]=Adobe&company[]=Samsung&company[]=Qualcomm&category[]=Strings&sortBy=difficulty

problem:
finding the length of longest substring with all distinct characters.
geeksforgeeks"
Output: 7
Explanation: "eksforg" is the longest substring.
approach:
1. 2 pointer approach
2. list slicing
3. deque
'''


from collections import deque
def longestSubstrDistinctChars(S):
    longest_length = 0
    d = []
    for i in S:
        if len(d) == 0: # this is in the case when list is empty
            d.append(i)
        else:
            if i in d: # this handles when the char is already in list
                index_i = d.index(i) # this finds the index of already existing char in the list
                longest_length = max(longest_length, len(d)) # find the maximum of longest length which is already calculated & the current list which has unique elements.
                d= d[index_i+1:] # after finding the repeated char in the list slicing the list from the char which is already existing
                d.append(i) # added the current char in the newly sliced list
            else: # if the element is not in the list
                d.append(i)


    return max(longest_length, len(d)) # It handles the case when all the char is an unique



S = "aldshflasghdfasgfkhgasdfasdgvfyweofyewyrtyefgv"
# S = "qwertyuioplkjh"
print(longestSubstrDistinctChars(S))
