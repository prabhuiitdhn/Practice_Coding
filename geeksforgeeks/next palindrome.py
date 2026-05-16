def nextPalin(N):
    if (len(N) == 1):
        return -1
    if len(N) == 2:
        return N[::-1] if int(N[::-1]) > int(N) else -1
    else:
        def nextPalinHelper(N):
            if len(N) == 1:
                return N
            if len(N) == 2:
                return N[::-1]
            else:
                middle = int(len(N) / 2) + 1
                palindrome = nextPalinHelper(N[:middle - 1]) + N[middle - 1] + nextPalinHelper(N[middle:])
                return palindrome if int(palindrome) > int(N) else -1

        return nextPalinHelper(N)


N = "2598952"
print(nextPalin(N))
