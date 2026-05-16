'''
https://practice.geeksforgeeks.org/problems/good-or-bad-string1417/1?page=1&company[]=Adobe&company[]=Samsung&company[]=Qualcomm&category[]=Strings&sortBy=difficulty

problem:
if more than 3 consonants and more 5 volwels are together then it is "BAD" string or "GOOD" string.
string will contains "?" which can be replaced with anyone.
'''



def isGoodorBad(S):
    vowels = "aeiou"
    vowels_continous = True
    consonant_continous= True
    count_vowels = 0
    count_consonant = 0
    BAD = 0
    GOOD = 1
    for i in range(len(S)):
        if S[i] in vowels or (S[i] is "?" and S[i-1] in vowels) and vowels_continous is True:
            count_vowels +=1
            count_consonant = 0
            consonant_continous = False
            vowels_continous = True
            if count_vowels>5 and vowels_continous is True:
                return BAD

        if S[i] not in vowels or (S[i] is "?" and S[i-1] not in vowels) and consonant_continous is True:
            count_consonant +=1
            vowels_continous = False
            consonant_continous = True
            count_vowels = 0
            if count_consonant>3 and consonant_continous is True:
                return BAD

    return GOOD




s = "c?zaicq"
print(isGoodorBad(s))