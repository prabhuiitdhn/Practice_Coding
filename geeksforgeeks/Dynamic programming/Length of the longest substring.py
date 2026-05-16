"""
https://practice.geeksforgeeks.org/problems/length-of-the-longest-substring3036/1?page=3&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty

It basically looks for maximum no of character's substring which are not repeated in the string.
"""


def longestUniqueSubsttrNative(string):
    # passed 10020 / 10167
    # worst case O(n^2)
    string_length = len(string)

    def checkIfAllUnique(string):
        setToCheck = set()

        for i in string:
            if i not in setToCheck:
                setToCheck.add(i)
            else:
                return False

        return True

    for sliding in range(string_length, 0, -1):
        for index in range(string_length - sliding + 1):
            current_string = string[index:index + sliding]
            if checkIfAllUnique(current_string) is True:
                return sliding


def longestUniqueSubsttrOptimised2(string):
    # passed 10126 / 10167
    # worst case: O(N^2)
    setToCheck = set()
    setToCheck.add(string[0])

    maxx = 1
    currentmax = 1
    i = 1

    while i < len(string):
        if string[i] != string[i - 1] and string[i] not in setToCheck:
            setToCheck.add(string[i])
            currentmax += 1
            maxx = max(maxx, currentmax)
            i += 1
        else:
            if currentmax == 1:
                i += 1
            else:
                setToCheck.clear()
                i = i - currentmax + 1  # it is going to the index where we have already found the char
                currentmax = 0
                maxx = max(currentmax, maxx)

    return max(maxx, currentmax)


def longestUniqueSubsttrOptimised3(string):
    # passed10167 / 10167
    # worst case : O(N)
    setToCheck = {}
    maximum_length = 0

    # starting the initial point of window to index 0
    start = 0  # It basically reversed back to the character where current char is being foiund.

    for end in range(len(string)):

        # Checking if we have already seen the element or not
        if string[end] in setToCheck:
            # If we have seen the number, move the start pointer
            # to position after the last occurrence
            start = max(start, setToCheck[string[end]] + 1)  # it Checks the starting string

        # Updating the last seen value of the character
        setToCheck[string[end]] = end  # Saved the current index for found character
        maximum_length = max(maximum_length, end - start + 1)  # look for maximum number of non repeating character.
    return maximum_length


# S = "bbb"
# S = "qwerty"
# S = "geeksforgeeks"
S = "abcdhcbayr"
# S = "zyaaabcdefghijklmnopqrstuvwxyzgffg"

print(longestUniqueSubsttrNative(S))
print(longestUniqueSubsttrOptimised2(S))
print(longestUniqueSubsttrOptimised3(S))
