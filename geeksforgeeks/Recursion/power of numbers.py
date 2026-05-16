"""
https://practice.geeksforgeeks.org/problems/power-of-numbers-1587115620/1?page=1&category[]=Recursion&sortBy=difficulty
Given a number and its reverse. Find that number raised to the power of its own reverse.

"""

def power(N, R):
    if R == 1:
        return N
    temp = power(N, R // 2)
    temp = (temp * temp) % 1000000007
    if R % 2 == 0:
        return temp % 1000000007
    return N * temp % 1000000007

print(power(12, 21))