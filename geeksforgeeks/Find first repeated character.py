
# https://practice.geeksforgeeks.org/problems/find-first-repeated-character4108/1?page=1&company[]=Adobe&company[]=Samsung&company[]=Qualcomm&category[]=Strings&sortBy=difficulty
def firstRepChar(s):
    l = []
    for i in s:
        l.append(i)
        if l.count(i)>=2:
            return i
    return "-1"


S = "abcc"

print(firstRepChar(S))