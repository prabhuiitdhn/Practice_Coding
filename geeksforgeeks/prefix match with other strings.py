def klengthpref(arr, n, k, s):
    match_count = 0
    for i in range(n):
        current_str = arr[i]
        if len(arr[i]) >= k:
            if current_str[:k] == s[:k]:
                match_count += 1

    return match_count


arr = ["abba", "abbb", "abbc", "abbd", "abaa", "abca"]
str = "abbg"
k = 3

print(klengthpref(arr, len(arr), k, str))
