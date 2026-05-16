# https://codeforces.com/problemset/problem/282/A
n = int(input())

x = 0
for i in range(n):
    sign = input().split()
    sign_ = list(sign[0])
    if sign_[1] == "+":
        x += 1
    else:
        x -= 1

print(x)
