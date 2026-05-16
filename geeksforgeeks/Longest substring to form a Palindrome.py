'''
https://practice.geeksforgeeks.org/problems/longest-substring-whose-character-rearranged-can-form-a-palindrome/1?page=1&company[]=Samsung&company[]=Qualcomm&company[]=KLA%20Tencor&category[]=Strings&sortBy=difficulty
Problem: we have given string(contains only lowercase) and based on the given string, we needed to find the longest no of possible character which could make a palindrome.
approach:
1. Create a list [0-25]//each index will store the value of character
2. check no of times the char is present in the given string.
3. sort it, and check the 1 maximum odd, and all maximum no of even.
'''


def longestSubstring(S):
    l = [0] * 26  # this is the list which can store the no of possible character in the string
    odd = False
    for i in S:
        l[ord(i) - 97] += 1  # it it counting the number of all character in the string.

    sorted_list = sorted(l)[::-1]
    maximum_no_palindrome = 0

    for i in range(26):
        if sorted_list[i] % 2 == 0:  # handles the even number.
            maximum_no_palindrome += sorted_list[i]
            continue
        if sorted_list[i] >= 1 and sorted_list[i] % 2 == 1:
            maximum_no_palindrome += sorted_list[i] - 1
            odd = True
            continue

    return maximum_no_palindrome if odd is False else maximum_no_palindrome + 1


def longestSubstring2(s):
    ans = 1
    l = len(s)
    f = {0: -1}
    x = 0
    for i in range(l):
        z = ord(s[i]) - 97
        x = x ^ (1 << z)
        if x in f:
            ans = max(ans, i - f[x])
        for j in range(26):
            t = x ^ (1 << j)
            if t in f:
                ans = max(ans, i - f[t])
        if x not in f:
            f[x] = i
    return ans


# S = "aabe"
S = "rwkrnw"
# S ="adbabd"
print(longestSubstring2(S))
