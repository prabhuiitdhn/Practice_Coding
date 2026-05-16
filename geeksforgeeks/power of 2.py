'''
this is about checking the number 'n' is the power of 2 or not?
Algo:
approach 1:

Approach 2:
n & n-1 == 0
If the logical operator between the number and number -1 is o
'''
#
# # approach 1
# def check_power_of_2(n):
#     if (n & n-1) == 0:
#         return True
#     return False

# approach 2
def check_power_of_2_2(n):
    bin_str = bin(n) # converting number to string ('0bXXXXXX')
    replaced_str = bin_str.replace("0b", "0")
    if (replaced_str.count('1') == 1):
        return True
    else:
        return False




print(check_power_of_2_2(32))