'''
https://practice.geeksforgeeks.org/problems/replace-a-word5553/1?page=1&company[]=Adobe&company[]=Samsung&company[]=Qualcomm&category[]=Strings&sortBy=difficulty
problem:
given 3 string S, oldWord, newWord, where oldWord has to replace with newWord in string s

S = "xxforxx xx for xx"
oldW = "xx"
newW = "Geeks"
Output:
"geeksforgeeks geeks for geeks"
'''

# s = "geeks"
# p  = "xxforxx"
# p.replace('xx', 'geeks')

def replaceAll (S, oldW, newW):
    return S.replace(oldW, newW)

S = "xxforxx xx for xx"
oldW = "xx"
newW = "Geeks"
print(replaceAll(S, oldW, newW))
