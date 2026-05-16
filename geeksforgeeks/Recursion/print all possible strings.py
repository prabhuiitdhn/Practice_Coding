"""
https://practice.geeksforgeeks.org/problems/print-all-possible-strings/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=KLA%20Tencor&category[]=Recursion&sortBy=difficulty

given a string str, needed to print all the possible string with spaced, and needed to print in lexigrocally increasing order.
  finds all possible strings that can be made by placing spaces (zero or one) in between them.

"""


def concatenate(l1, l2):
    l = []
    for i in range(len(l1)):
        for j in range(len(l2)):
            string = l1[i] + l2[j]
            l.append(string)
    return l


def spaceString(s):
    finalStr = [s]
    if len(s) == 1:
        return finalStr

    if len(s) == 2:
        # base condition
        spacedStr = s[0] + ' ' + s[1]
        finalStr.append(spacedStr)
        return finalStr[::-1]

    for i in range(len(s) - 1):
        spacedStr1 = concatenate(spaceString(s[:i + 1]), spaceString(s[i + 1:]))
        for j in range(len(spacedStr1)):
            finalStr.append(spacedStr1[j])

    allSpaced = ''
    for i in range(len(s)):
        allSpaced = allSpaced + s[i] + ' '

    finalStr.append(allSpaced[:-1])
    return sorted(list(set(finalStr)))


s = 'lw'
p = spaceString(s)
print("Line no 44:", p)
