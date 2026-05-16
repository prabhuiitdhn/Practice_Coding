'''

'''

def colName(n):
    s = ''
    while n:
        if n % 26 == 0:
            s = 'Z' + s
            n = (n - 1) // 26

        else:
            s = chr(n % 26 - 1 + 65) + s
            n = (n) // 26

    return s
print(colName(104))