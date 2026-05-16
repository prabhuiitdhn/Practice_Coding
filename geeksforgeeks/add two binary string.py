"""
https://practice.geeksforgeeks.org/problems/add-binary-strings3805/1?page=2&company[]=Microsoft&company[]=Adobe&company[]=Google&category[]=Mathematical&sortBy=difficulty
given two binary number and add it

"""


def addBinaryString(A, B):
    """
    Adding two binary number is a equal to add converted decimal number from binary string
    @param A: Binary string
    @param B: Binary string
    @return: sum of binary string as binary
    """
    x_dec = int(A, 2)  # converting the binary string to decimal
    y_dec = int(B, 2)  # converting the binary string to decimal
    return format((x_dec + y_dec), 'b')  # converting decimal to binary


A = '1101'
B = '111'
print(addBinaryString(A, B))
