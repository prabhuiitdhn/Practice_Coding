'''
https://practice.geeksforgeeks.org/problems/amend-the-sentence3235/1?page=1&company[]=Adobe&company[]=Samsung&company[]=Qualcomm&category[]=Strings&sortBy=difficulty
s = "BruceWayneIsBatman"
problem:
given a sentence without spaces between the words
first letter of word is capital
so, create a new string which includes space between the words and all the word should ne in in lowecases.

approach:
check each char in str and add to new string with spaces.
'''

s ='s'
s.isupper()
def amendSentence(s):


    new_str = ''

    for i in s:
        if i.isupper():
            new_str = new_str + ' ' + i
        else:
            new_str += i

    return new_str[1:].lower() if s[0].isupper() else new_str.lower()


s = "BruceWayneIsBatman"
amendSentence(s)