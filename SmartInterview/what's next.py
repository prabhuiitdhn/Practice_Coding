while True:
    a, b, c = map(
        int, input().split()
    )

    if a == 0 and b == 0 and c == 0:
        print()
    if (b - a) == (c - b):
        print("AP", c + (c - b))
    else:
        print("GP", int(c * (c / b)))
