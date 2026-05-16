l = [1, 2, 3, 4, 5, 6]

def reverse(l, start, end):
    if start>end:
        return
    if start == end:
        return
    l[start], l[end] = l[end], l[start]
    reverse(l, start+1, end-1)
    return l

print(reverse(l, 0, 5))