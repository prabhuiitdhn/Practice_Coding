# Enter your code here. Read input from STDIN. Print output to STDOUT

def power(a, b):
    if b == 0:
        return 1
    s = power(a, b // 2) % m
    if b % 2 == 0:
        return (s * s) % m
    else:
        return (s * s * a) % m


t = int(input())
for i in range(t):
    m = (10 ** 9) + 7
    a, b = map(
        int, input().split()
    )
    if b == 0:
        print(1)
    elif a == 0:
        print(0)
    else:
        print(power(a, b))

