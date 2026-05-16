'''
# https:///practice.geeksforgeeks.org/problems/recursively-remove-all-adjacent-duplicates0744/1?page=2&company[]=Samsung&sortBy=submissions
# https://www.youtube.com/watch?v=yJv_ltADGuA
recursively removing the dupplicates elements.
approach 1: using stack/deque
'''


# from collections import deque
#
# d = deque()
# s = "abccbccba"
# # s= "geeksforgeek"
# #
# # for i in range(len(s)):
# #     if len(d) == 0:
# #         # inserting the element in the deque. It works as stack
# #         d.append(s[i])
# #     else :
# #         # top element in the deque d[-1]
# #         #d.pop () will pop the first element of the deque.
# #         if d[-1] == s[i]:
# #             d.pop()
# #         else:
# #             d.append(s[i])
# # print(d)


def recursive_remove_duplicates(s):
    i = 0
    remain = ""
    while (s[i]):
        if s[i] != s[i + 1]:
            remain = remain + s[i]
            i = i + 1
        if (s[i + 1] and s[i] == s[i + 1]):
            while (s[i + 1] and (s[i] == s[i + 1])):
                i = i + 1
            i = i + 1
    return remain


# def recursive_remove_duplicates_2(s):
#     remain = ''
#     i = 0
#     while(i<len(s)):
#         if i==len(s)-1:
#             remain = remain + s[i]
#             i = i+1
#         else:
#             if s[i] != s[i+1]:
#                 remain = remain + s[i]
#                 i = i+1
#             else:
#                 while((i!=len(s)-1 ) and s[i]==s[i+1]):
#                     i = i+1
#                 i = i+1
#     return remain if len(remain)== len(s) else recursive_remove_duplicates_2(remain)


def rremove(S):
    # code here
    remain = ''
    i = 0
    while (i < len(S)):
        if i == len(S) - 1:
            remain = remain + S[i]
            i = i + 1
        else:
            if S[i] != S[i + 1]:
                remain = remain + S[i]
                i = i + 1
            else:
                while ((i != len(S) - 1) and (S[i] == S[i + 1])):
                    i = i + 1
                i = i + 1
    if len(remain) == len(S):
        return remain
    else:
        return rremove(remain)


# s = 'abccbccbcccbbbcbcbb'
s= 'geeksforgeek'
print(rremove(s))
