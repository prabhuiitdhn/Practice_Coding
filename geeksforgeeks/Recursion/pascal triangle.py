"""

"""


def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)


def binomialCoefficient(n, r):
    return int(fact(n) / (fact(n - r) * fact(r))) % (10 ** 9 + 7)


def pascalTriangle(n):
    temp = []
    for i in range(n + 1):
        number = binomialCoefficient(n, i)
        temp.append(number)
    # print(temp)
    return temp


def pascalTriangle2(n):
    temp = [0] * n
    if n == 2:
        a = [0]*2
        a[0] = 1
        a[1] = 1
        return a
    a = pascalTriangle2(n - 1)
    temp[0] = 1
    temp[n - 1] = 1
    for i in range(n - 2):
        temp[i + 1] = (a[i] + a[i + 1]) % (10 ** 9 + 7)

    # print(temp)
    return temp



p = pascalTriangle2(10)
q = pascalTriangle(9)
print("p:", p)
print("q:", q)
# pascalTriangle2()
