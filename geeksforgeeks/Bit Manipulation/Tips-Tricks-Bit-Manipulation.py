# 1. Create a number which has kth bit as set bit.
# k = 5
# print(
#     "generate a number which has 5th bit as set"
# )
# # print(1 << (k-1))
# # output: 16 in binary 10000 [5th bit is set.]


# # 2. Check whether the kth bit is set or not?
# k = 3
# n = 10
# if n & (1 <<(k-1)):
#     print("Set Bit")

# 3. Check if n is the power of 2 or not?
n = 8
# if not (n & (n-1)):
#     print("Yes")
# else:
#     print("no")

if n and (not (n & (n-1))):
    print("Yes")
else:
    print("not")