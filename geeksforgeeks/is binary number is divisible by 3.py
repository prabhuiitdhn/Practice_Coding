"""
https://practice.geeksforgeeks.org/problems/is-binary-number-multiple-of-30654/1?page=2&company[]=Microsoft&company[]=Adobe&company[]=Google&category[]=Mathematical&sortBy=difficulty

given a string as binary number, and needed to check whether the binary number is divisible by 3 or not
"""

def isBinaryDivisibleBy3(binary):
    """
    one approach just to convert the using int(BinaryNumber, power) which will convert it in decimal number.
    @param binary: binary string.
    @return: True if number is divisible by 3
    """
    number = int(binary, 2)
    if number%3 == 0:
        return True

    return False

s = '0101'
print(isBinaryDivisibleBy3(s))
