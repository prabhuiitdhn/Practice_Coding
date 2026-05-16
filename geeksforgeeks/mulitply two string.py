

def multiplyStrings_1(s1,s2):
    return str(int(s1) * int(s2))

def convert_to_int(number_in_list):
    number = 0
    for i in range(len(number_in_list)):
        number += int(number_in_list[i]) * 10**(len(number_in_list)-i-1)
    return number

def multiplyStrings_2(s1, s2):
    s1_list = list(s1)
    if s1_list[0] == '-':
        s1_number = -(convert_to_int(s1_list[1:]))
    else:
        s1_number = convert_to_int(s1_list)
    s2_list = list(s2)
    if s2_list[0] == '-':
        s2_number = -(convert_to_int(s2_list[1:]))
    else:
        s2_number = convert_to_int(s2_list)

    return str(s1_number * s2_number)


s1 = "-333"
s2 = "0"
print(multiplyStrings_2(s1, s2))