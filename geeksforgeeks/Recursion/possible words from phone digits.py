"""
https://practice.geeksforgeeks.org/problems/possible-words-from-phone-digits-1587115620/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=KLA%20Tencor&category[]=Recursion&sortBy=difficulty

Problem: Given a keypad and N digits which is represented by an array a[]. the task is list all the possible words which are possible by pressing them

input: {2, 3, 4}

output: {adg adh adi aeg aeh aei afg afh afi
bdg bdh bdi beg beh bei bfg bfh bfi
cdg cdh cdi ceg ceh cei cfg cfh cfi }
"""


def possibleWords(a, N):
    keypad = {2: 'ABC', 3: 'DEF', 4: 'GHI', 5:'JKL', 6:'MNO',
              7:'PQRS', 8:'TUV', 9:'WXYZ'}


    def generate_list(list_to_be_generated, keypad, number):
        if len(list_to_be_generated) == 0:
            string = keypad[number]
            for i in string:
                list_to_be_generated.append(i)
        else:
            string = keypad[number]
            newlist = []
            for i in string:
                for j in range(len(list_to_be_generated)):
                    newlist.append(list_to_be_generated[j] + i)
            list_to_be_generated = newlist

        return list_to_be_generated

    generated_list  = []
    for number in range(N):
        generated_list = generate_list(generated_list, keypad, a[number])


    return generated_list

a = [2, 3, 4]
N = 3
print(sorted(possibleWords(a, N)))

