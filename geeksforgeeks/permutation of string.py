'''
https://practice.geeksforgeeks.org/problems/permutations-of-a-given-string-1587115620/1?page=1&company[]=Adobe&company[]=Samsung&company[]=Qualcomm&category[]=Strings&sortBy=difficulty
https://www.youtube.com/watch?v=GuTPwotSdYw
backtracking approach.

'''

def helper(s, p, ans):
    if len(s) == 0:
        ans.append(p)
        return
    for i in range(0, len(s)):
        ch = s[i]
        f = s[0:i]
        l = s[i + 1:]
        rest = f + l
        helper(rest, p + ch, ans)


def permutation(s):
    p = ''
    ans = []
    helper(s, p, ans)
    ans.sort()
    return ans


s = "ABC"
print(permutation(s))
