'''
https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1?page=1&company[]=Samsung&company[]=Qualcomm&company[]=KLA%20Tencor&category[]=Strings&sortBy=difficulty
given an string and find the longest string which is palindrome
'''


def longestPalin(s):
    longest_palindrome_str = ''

    for i in range(len(s), 0, -1):
        window_length = len(s)-i
        for j in range(window_length+1):
            current_str = s[j:i+j]
            if current_str == current_str[::-1]:
                return current_str
    return s[0]


s = "aaaabbaa"
# s = "abc"
print(longestPalin(s))
