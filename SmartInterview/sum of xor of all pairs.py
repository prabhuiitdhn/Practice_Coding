# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
t = int(int(input()))
for i in range(t):
    sum = 0
    n = int(input())
    list_of_elements = list(
        map(
            int, input().split()
        )
    )

    max_bit_to_be_traversed = math.ceil(
        math.log(
            max(list_of_elements), 2
        )
    )

    sum = 0
    for i in range(max_bit_to_be_traversed):
        count_0 = 0
        count_1 = 0
        mask = 1<<i
        for j in range(len(list_of_elements)):
            if list_of_elements[j] & mask == 0:
                count_0 +=1
            else:
                count_1 +=1

        sum += (count_0 * count_1) * (1<<i)
    print(2 * sum)








