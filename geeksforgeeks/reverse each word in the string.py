'''

'''


def reverseWords(S):
    list_of_split_string = S.split('.')
    output_str = ''
    for i in range(len(list_of_split_string)):
        s = list_of_split_string[i]
        output_str += str(s[::-1]) + '.'

    return output_str[:-1]


S = "i.like.this.program.very.much"
# print(S[::-1])
print(reverseWords(S))
