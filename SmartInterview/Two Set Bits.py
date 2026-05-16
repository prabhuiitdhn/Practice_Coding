
# # # TO SOLVE THIS WRITE BINARY REPRESENTATION FOR FEW NUMBER AND FIND THE PATTERN

# # t = 1
# t = int(input())
# for i in range(t):
#     n = int(input())
#     # n = 5
#     # find the nth two set bit
#     count = 0
#     l = []
#     startbit = 1
#     while n != count:
#         for j in range(startbit):
#             number = (1 << startbit) + (1 << j)
#             l.append(number)
#             count += 1
#             if count == n:
#                 print(number)
#                 break
#         startbit += 1
#     # print(l[n-1])

def findNthNum(N):
    bit_L = 1;
    last_num = 0;

    # Keep incrementing until
    # we reach the partition of 'N'
    # stored in bit_L
    while (bit_L * (bit_L + 1) / 2 < N):
        p = bit_L * (bit_L + 1) / 2
        last_num = last_num + bit_L;
        bit_L += 1;

    # set the rightmost bit
    # based on bit_R
    bit_R = N - last_num - 1;

    print((1 << bit_L) + (1 << bit_R));


# Driver code
if __name__ == '__main__':
    N = 5

    findNthNum(N);
