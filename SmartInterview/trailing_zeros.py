
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


# Enter your code here. Read input from STDIN. Print output to STDOUT
# t = int(input())


def calc_fact(num):
    store = [0]*(num+1)
    if n<3:
        return n
    store[1] = 1
    for i in range(2, num):
        store[i] = i * store[i-1]

    return store[num]

for i in range(1):
    n = 5
    fact_val = calc_fact(n)
    print(fact_val)
    # fact_val = str(calc_fact(n))
    # count_0 = 0

    # for i in range(len(fact_val)-1, -1, -1):
    #     if fact_val[i]== '0':
    #         count_0 +=1
    #     else:
    #         break
    # print(count_0)




