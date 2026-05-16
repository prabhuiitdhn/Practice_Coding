def isAnagram( a, b):
    # code here
    if len(a) != len(b):
        return False
    else:
        l = []
        anagram = False
        for i in a:
            if i not in l:
                l.append(i)

        for i in range(len(l)):
            if a.count(l[i])== b.count(l[i]):
                anagram = True
            else:
                return False

        if anagram is True:
            return True

a = "geeksforgeeks"
b = "forgeeksgeeks"
print(isAnagram(a, b))