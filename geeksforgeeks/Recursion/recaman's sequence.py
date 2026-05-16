def recamanSequence(n):
    l = []
    def rs(n):
        if n == 0:
            return 0
        else:
            if rs(n - 1) - n > 0:
                number = rs(n-1) - n
            else:
                number =  rs(n-1) + n

            l.append(number)

    return rs(n)

n = 6
list_ = recamanSequence(n)
print(list_)
