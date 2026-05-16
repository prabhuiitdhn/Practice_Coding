"""
https://leetcode.com/problems/factorial-trailing-zeroes/
https://hive.smartinterviews.in/contests/smart-interviews-primary/problems/trailing-zeros?page=0&pageSize=10
https://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/

So basically needed to find the trailing zeros in n!; the easiest solution would be calculate the factorial and count the trailing 0 using bruteforce method but it will
fail for the large number so, Needed to optimise the code where we can find the trailing zeros in optimal way
so, optimal way is to find the total number of 5 in n!
example: 10= 10* 9 *7 *6*5*4*3*2
           = 5*2 (9 *7 *6*5*4*3*2)
           so, total number of 5 is 2
            so tailing zero will be 2 bcz 5 and 2 can give 0

but what if number is too large so, in this case, we need to find the number of prime of 5 until number number reaches to max
for 28: it can have 25, and 5 so, divinde 28/5 to get number of 5
       and divide 28/25 to get extra 5 and sum it.
"""

# # Brute force technique
# def calc_fact(num):
#     if n<3:
#         return n
#     val = num
#     while num>1:
#         val *= num-1
#         num -= 1
#
#     return val
# for i in range(1):
#     n = 100
#     fact_val = str(calc_fact(n))
#     count_0 = 0
#
#     for i in range(len(fact_val)-1, -1, -1):
#         if fact_val[i]== '0':
#             count_0 +=1
#         else:
#             break
#     print(count_0)
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 5:
            return 0
        count_0 = 0

        while (n >= 5):
            count_0 += n // 5
            n //= 5

        return count_0

n = 10
s = Solution()
print(s.trailingZeroes(n))