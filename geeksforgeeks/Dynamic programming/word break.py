"""
https://practice.geeksforgeeks.org/problems/word-break1352/1?page=3&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty
given a string A without spaces and Dictionary where words will be there, Needed to find out If we separate the string A with spaces then whether substrings of A will be found on B or not?

Approach:
1. Bruteforce:
    create a prefix and suffix and check if prefix is found in the dictionary or not? If prefix found the work with suffix and try to find out if suffix is found or not?
2. DP can be used.

"""


def wordBreak(word, dictionary):
    """
    Approach: for each word looking for all combinations of prefix and suffix and check both are present in the dictionary or not
    assume in one itearation, suffix is not found the it again partitioned with prefix and suffix & check with both are available
    """
    if word == '':
        return True
    for i in range(1, len(word) + 1):  # this is upto len(word) bcz if prefix is whole word then suffix will '' (empty)
        prefix = word[0:i]  # extarcting the prefix from the
        suffix = word[i:]
        if prefix in dictionary and wordBreak(suffix, dictionary):
            return True

    return False


# n = 4
# B = {'ab', 'bcd', 'b', 'a'}
# A = "abcd"

n = 12
B = {"i", "like", "sam",
     "sung", "samsung", "mobile",
     "ice", "cream", "icecream",
     "man", "go", "mango"}
A = "ilikesamsung"
# A = "ilikesmobile"

print(wordBreak(A, B))
