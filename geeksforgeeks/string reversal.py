'''
this program is to find the unique character in string.
Or reverse the string, remove the space and avoid repeating character.
'''

def reverseString(s):
    l =len(s)
    new_str = ""
    for i in range(l-1, 0, -1):
        current_str = s[i]
        if current_str != " ":
            if (current_str != s[i-1] and current_str not in new_str):
                new_str += current_str
    print(new_str + s[0] if s[0] not in new_str else new_str)
    return new_str + s[0] if s[0] not in new_str else new_str

s = "I AM AWESOME"
# s = "GFB"
reverseString(s)