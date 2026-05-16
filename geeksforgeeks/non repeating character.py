def non_repeating(S):
    d = {}
    for i in S:
        if i not in d:
            d[i] =1
        else:
            d[i] +=1

    for i in S:
        if d[i] ==1:
            return i
# S = "zxvczbtxyzvy"
S ="hqghumeaylnlfdxfircvscxggbwkfnqduxwfnfozvs"
print(non_repeating(S))

