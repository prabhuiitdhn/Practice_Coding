"""
https://practice.geeksforgeeks.org/problems/count-of-strings-that-can-be-formed-using-a-b-and-c-under-given-constraints1135/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty

this is about given of length 'n' of string that can be made using 'a', 'b', 'c' with at-most one 'b' and two 'c' allowed.

n =1
possible string are: 'a', 'b', 'c'
output: 3; ['a', b, c]

n =2
possible string = [aa, ab, ac, ba, bc, ca, cb, cc] # considering only 'b' and maximum 2 'c' is allowed.


n = 3
number of string with 3 using a=1

aaa aab aac aba abc aca acb acc
baa bac bca bcc
caa cab cac cba cbc cca ccb

output: 19

"""


def countstr(n, bcount, ccount):
    # naive approach but it can solve using dp

    if bcount < 0 or ccount < 0:
        return 0
    if n == 0:
        return 1
    if bcount == 0 and ccount == 0:
        return 1
    result = countstr(n - 1, bcount, ccount)
    result += countstr(n - 1, bcount - 1, ccount)
    result += countstr(n - 1, bcount, ccount - 1)
    return result


"""
A solution that works in O(1) time : 

We can apply the concepts of combinatorics to solve this problem in constant time. we may recall the formula that the number of ways we can arrange a total of n objects, out of which p number of objects are of one type, q objects are of another type, and r objects are of third type is n!/(p!q!r!)

Let us proceed towards the solution step by step.

How many strings we can form with no 'b' and 'c' ? Answer is 1 because we can arrange a string consisting only 'a' in one way only and the string would be aaaa....(n times) .

How many strings we can form with one 'b' ? Answer is n because we can arrange a string consisting (n-1) 'a's and 1 'b' is n!/(n-1)! = n . Same goes for 'c' .

How many strings we can form with 2 places , filled up by 'b' and/or 'c' ?  Answer is n*(n-1) + n*(n-1)/2 . Because, that 2 place can be either 1 'b' and 1 'c'  or 2 'c' according to our given constrains. For first case, total number of arrangements is n!/(n-2)! = n*(n-1) and for second case that is n!/(2!(n-2)!) = n*(n-1)/2 .

Finally, how many strings we can form with 3 places , filled up by 'b' and/or 'c' ?  Answer is (n-2)*(n-1)*n/2 . Because, that 3 place can only be consisting of 1 'b' and 2'c'  according to our given constrains. So, total number of arrangements is n!/(2!(n-3)!) = (n-2)*(n-1)*n/2 .
"""

# A O(1) Python3 program to find
# number of strings that can be
# made under given constraints.

def countStrOptimisedCombinatorics(n):
    return (1 + (n * 2) +
                (n * ((n * n) - 1) // 2))


n = 4  # total number of character.
b = 1  # maximum number of 'b' is allowed
c = 2  # maximum number of 'c' is allowed.

print(countstr(n, 1, 2))
print(countStrOptimisedCombinatorics(n))
