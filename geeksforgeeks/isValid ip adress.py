'''
write a program which show the given IP address is valid.
ipv4 adresss: x1.x2.x3.x3 and all the 0<=(x1, x2, x3, x4)<=255

input: string s //IP address
output: return 1 if valid else 0
'''


def isValid(s):
    # code here
    def countZeros(list_str):
        count = 0
        for i in list_str:
            if i != '0':
                break
            count += 1
        return count

    isValid = False
    l = s.split('.')  # this is for splitting the string
    if len(l) != 4:  # If the length of list of string is more than 4 It is invalid.
        return isValid
    else:
        for i in range(4):  # tracking each elements in the list
            if l[i] != '' and l[i].isdigit():
                if 0 <= int(l[i]) <= 255:  # checking if the integer is in between of (0, 255)
                    if int(l[i]) == 0 and countZeros(l[
                                                         i]) != 1:  # this is for checking if the int(list) == 0 but not more than 1 0 should be there
                        isValid = False
                        return isValid
                    if 1 <= int(l[i]) <= 255 and countZeros(
                            l[i]) != 0:  # if the int(list) is between (1, 255) then not additional 0s should be there.
                        isValid = False
                        return isValid
                    isValid = True
                else:
                    isValid = False
                    return isValid
            else:
                isValid = False
                return isValid

    return isValid


# s ="0.0.0.0"
# s ="0.02.0.0"
# s ="1...1"
s = "a.b.c.d"

print(isValid(s))
