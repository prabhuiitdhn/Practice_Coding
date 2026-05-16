"""
https://practice.geeksforgeeks.org/problems/fda70097eb2895ecfff269849b6a8aace441947c/1?page=3&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty
 Given A: string
       B: pattern
Needed to check that how many times we repeat string a so that we can find pattern b in the a
condition to be followed:
1. all character of pattern B should be in A
2. After repeating A anytimes, B has to be in A

"""


def minRepeatsNative(a, b):  # ALL TEST CASES NOT PASSED
    """
    Native approach: where I am just adding again and again and checking If B is in A or not? which is a bit costly
    a:string
    b: pattern
    """

    def checkIfAllCharacterMatching(a, b):
        # first condition: Check if all the character in B should in A then It does matter how many times we are
        # repeating it to find the substring B in repeated A
        len_b = len(b)
        for i in range(len_b):
            if b[i] not in a:
                return False

    if checkIfAllCharacterMatching(A, B) is False:
        # Checking condition1
        return -1
    else:
        # adding a to a until we find B is in new string.
        count = 1
        while b not in a:
            count += 1
            a = a + a
        return count


def minRepeatsNative2(a, b):  # ALL TEST CASES PASSED
    """
    Native approach 2: I am checking the minimum no of repeated possibities by len(b)//len(a) which tell the minimum repeatation
    but If still not work then repeat one or 2 more time to check it.
    a:string
    b: pattern
    """

    def checkIfAllCharacterMatching(a, b):
        # first condition: Check if all the character in B should in A then It does matter how many times we are
        # repeating it to find the substring B in repeated A
        len_b = len(b)
        for i in range(len_b):
            if b[i] not in a:
                return False

    if checkIfAllCharacterMatching(A, B) is False:
        # Checking condition1
        return -1
    else:
        # adding a to a until we find B is in new string.
        count = 1
        minimum_no_of_rotation_required = len(b) // len(a)
        newStr = ''
        i = minimum_no_of_rotation_required
        while i:
            newStr = newStr + a
            i -= 1

        if b in newStr:
            return minimum_no_of_rotation_required
        elif b in newStr + a:
            return minimum_no_of_rotation_required + 1
        elif b in newStr + a + a:
            return minimum_no_of_rotation_required + 2
        else:
            return -1


def minRepeatsOptimised(a, b):  # ALL TESTCASES PASSED
    """
    Approach:
    1. We check which is the index where first index of B is matching with A
    2. subtract the length of B with index: y = len(b)-index
        i.e. divide by len(a): this tells that minimum of repeatation (minimum_no_of_repeatation) possible for A to get B
    3. if not then, we will look for minimum_no_of_repeatation+1, minimum_no_of_repeatation+2
    """

    def checkIfAllCharacterMatching(a, b):
        # first condition: Check if all the character in B should in A then It does matter how many times we are
        # repeating it to find the substring B in repeated A
        len_b = len(b)
        for i in range(len_b):  # or |b|
            if b[i] not in a:
                return False

    if checkIfAllCharacterMatching(A, B) is False:
        return -1
    else:
        starting_index = 0
        for index in range(len(a)):
            # finding the index of A where first character of B is matching
            if a[index] == b[0]:
                starting_index = index
                break
        # mathematics
        y = len(b) - starting_index
        # subtracting with index so that we can finding the minimum rotation
        y = y // len(a)
        # dividing by len(a) which tells that minimum of rotation possible to get B in repeated A

        newstr = ""
        i = y
        while i:
            # creating repeated string.
            newstr += a
            i -= 1
        if b in newstr:
            # check if b is found or not?
            return y
        elif b in newstr + a:
            # check with one more repeatation
            return y + 1
        elif b in newstr + a + a:
            # check with one more repeation
            return y + 2
        else:
            # Still not the return -1 bcz this is not possible then
            return -1


# #
A = "abcd"
B = "cdabcdab"

# A = "wwwwwwww"
# B = "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww"
# A = "ab"
# B = "cab"
print(minRepeatsNative2(A, B))
