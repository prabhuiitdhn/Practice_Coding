"""
https://practice.geeksforgeeks.org/problems/interleaved-strings/1?page=2&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty

find the better explaination:
https://www.youtube.com/watch?v=3Rw3p9LrgvE
https://www.youtube.com/watch?v=EzQ_YEmR598


observation:
1. |s3| = |s1 + s2|
2. the formed string from the s1 and s2 into s3 should be ordered. i.e. either the substring from s1 with substring of s2 or substring of s2 with substring with s1
3. each character from s1 and s2 should be matched with s3 & with maintaining the order with s3
4. matching could start from s1 character or substrings or s2 substring.
5. but s3 = substring(s1)+ substring(s2)+ substring(s1)+substaring(s2) ...+...+
    or s3 = substring(s2)+ substring(s1)+ substring(s2)+substaring(s1) ...+...+

so, using matching each substring of s1 with each substring of s3 or vice versa with s2 with substring of s3 will be exponential order
so maintain the timecomplexity, we used dynamic programming concepts which works recursively to solved the problem.

input: s1, s2, s3
output: give s3 is interleave string of s1 and s2 or not? If yes, then return 1[True] else: false[0]

example:
s1 = xy
s2 = x
s3 = xxy
output: 1 bcz s2 + s1 formed here

s1= yx
s2=x
s3 = xxy
output: not possible if s1+s2 = (yxx) or s1+s2 =(xyx) bcz we should maintain the order of taking the character or substring from original string s1 or s2
"""


def isInterleave(a, b, c):
    """
    Approach:
    we create a len(b)X len(a) matrix as dp and filled with False
    then we started checking from the character from s1 or s2 to s3 if matches then passes to next character with matching string
    if character from both s1, and s2 are matching with s3 then recursively we work both for further and check which is matching finally with s3
    dp is being used here so that same calculation could not happen again in the case of recursive calculations.
    @param a: str1
    @param b: str2
    @param c: str3
    @return: true/false or 0/1
    """
    def isInterleaveHelper(a, b, c, p1, p2, p3, dp):
        """

        @param a: string s1
        @param b: string s2
        @param c: string s3
        @param p1: 0th index of string s1
        @param p2: 0th index of string s2
        @param p3: 0th index of string s3
        @param dp: it stores the calculation.
        @return:
        """
        if p3 == len(c) - 1:
            # It checks if the p3 [pointer/index of string s3 is reached to end]
            dp[p1][p2] = 1
        if dp[p1][p2] != -1:
            return dp[p1][p2]

        first = 0 # this is initialised for two possibilities when character from s1 and s2 both are matching with s3
        second = 0
        if len(a)>p1 >= 0 and a[p1] == c[p3]:
            # this is for string s1 where we check whether the character from string s1 is matching with s3
            # if yes, then we move forward
            first = isInterleaveHelper(a, b, c, p1 + 1, p2, p3 + 1, dp)
        if len(b)>p2 >= 0 and b[p2] == c[p3]:
            # this is for string s2 where we check whether the character from string s2 is matching with s3
            second = isInterleaveHelper(a, b, c, p1, p2 + 1, p3 + 1, dp)
        dp[p1][p2] = first or second # this is the case when we see that whether one of the True or both true

        return dp[p1][p2]

    dp = [[-1 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
    # creating the dp

    return isInterleaveHelper(a, b, c, 0, 0, 0, dp)


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

# s1 = "xy"
# s2 = "x"
# s3 = "xxy"

print(isInterleave(s1, s2, s3))
