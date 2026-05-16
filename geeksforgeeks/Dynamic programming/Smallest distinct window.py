"""
https://practice.geeksforgeeks.org/problems/smallest-distant-window3132/1?page=3&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty

given a string 's' and needed to find the minimum window length of substring which contains all the characters of the given string at least one time.

String may contain both type of English Alphabets.
Example: AABBBCBBAC
output: 3 i.e. BAC is the smallest window length substring we have which contains all the characters.

Expected Time Complexity: O(256.N)
Expected Auxiliary Space: O(256)

"""


def findSubString(string):
    # Passed 30 / 140
    """
    Approach 1: Create a set which can have the unique elements and again,
                check the length of set
                again starts the window length from len(set) to all
                bcz it looks for minimum length substring & no of unique elements in the set will be the minimum window length
    @param string:
    @return:
    """

    setList = set(string)
    windowLength = len(setList)

    for window_length in range(windowLength, len(string)+1):
        for i in range(len(string)-window_length+1):
            current_string = string[i:i+window_length]
            if set(current_string) ==setList:
                return window_length
    return -1


def findSubStringOptimsed(string):
    # 30 / 140
    """
    Approach 1: Create a set which can have the unique elements and again,
                check the length of set
                again starts the window length from len(set) to all
                bcz it looks for minimum length substring & no of unique elements in the set will be the minimum window length
    @param string:
    @return:
    """

    # n = len(string)
    # setList = set(string)
    # windowLength = len(setList)
    #
    # startIndex =0
    # currentIndex = 0
    #
    # while currentIndex<n:
    #     if currentIndex - startIndex + 1 < windowLength:


# string: str = "GEEKSGEEKSFOR"
string ='B'
# print(findSubString(string))
print(findSubStringOptimsed(string))
