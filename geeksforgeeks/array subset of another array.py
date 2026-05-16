def isSubset(a1, a2, n, m):
    a1 = sorted(a1)
    a2 = sorted(a2)
    d = {}
    for i in range(n):
        d[i] = a1[i]

    checkSubset = False
    for i in range(m):
        if a2[i] in d.values():
            checkSubset = True
            key_list = list(d.keys())
            val_list = list(d.values())
            key = key_list[val_list.index(a2[i])]
            del d[key]
            continue
        else:
            return "No"

    if checkSubset is True:
        return "Yes"


a1 = [1, 1, 2, 3, 4, 5, 1, 1, 1]
a2 = [1, 2, 3, 1]
isSubset(a1, a2, len(a1), len(a2))
