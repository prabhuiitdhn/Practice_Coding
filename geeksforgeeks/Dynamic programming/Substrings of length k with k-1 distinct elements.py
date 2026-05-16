"""
https://practice.geeksforgeeks.org/problems/substrings-of-length-k-with-k-1-distinct-elements/1?page=3&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty
Needed to findout the no of substring which will have K-1 unique character in K length substring.
Expected Time Complexity: O(|S|)
Expected Auxiliary Space: O(constant)

"""


def countOfSubstrings(string, k):
    # passed 212 / 222
    count = 0

    def checkKMinus1Distinct(string):
        setToCheck = set()

        for i in string:
            if i not in setToCheck:
                setToCheck.add(i)
        if len(setToCheck) == k - 1:
            return True
        else:
            return False

    for i in range(len(string) - k + 1):
        currentString = string[i: i + k]
        if checkKMinus1Distinct(currentString) is True:
            count += 1

    return count


def countOfSubstringsOptimised(string, k):
    n = len(string)
    l = 0
    d = {}
    r = 0
    c = 0
    while r < k:
        if string[r] not in d:
            d[string[r]] = 1
        else:
            d[string[r]] = d[string[r]] + 1
        r = r + 1
    if len(d) == k - 1:
        c = c + 1
    while r < n:
        d[string[l]] = d[string[l]] - 1
        if d[string[l]] == 0:
            d.pop(string[l])
        l = l + 1

        if string[r] not in d:
            d[string[r]] = 1
        else:
            d[string[r]] = d[string[r]] + 1
        if len(d) == k - 1:
            c = c + 1
        r = r + 1
    return c


def countOfSubstringsOptimised2(S, K):
    """
    To maintain the total length of substring is K; Used by starting_index, current_index
    To maintain the unique element, we have dictionary to track it.
    Count is for counting the no of substring which have unique length k-1
    Note: need to care about the charcater which are no in present in substring and already in dictionary so remove it from dictionary
    in the interval of K length substring.
    """
    count = 0  # this will maintain the total number of count of substring
    dic = dict()  # this keeps the unique element with Key as number of occurence.
    starting_index = 0 # this will keep track for starting index which will help to track the length.
    current_index = 0
    while current_index < len(S):
        if S[current_index] in dic:
            dic[S[current_index]] += 1
        else:
            dic[S[current_index]] = 1
        if current_index - starting_index + 1 == K:
            if len(dic) == K - 1:
                count += 1
        elif current_index - starting_index + 1 > K:
            dic[S[starting_index]] -= 1
            if dic[S[starting_index]] == 0:
                # at some point of time in the length of substring previous character will not be present.
                del dic[S[starting_index]]
            starting_index += 1
            if len(dic) == K - 1:
                count += 1
        current_index += 1
    return count


# S = "abcc"
# K = 2

S = "aabab"
K = 3
# print(countOfSubstrings(S, K))
# print(countOfSubstringsOptimised(S, K))
print(countOfSubstringsOptimised2(S, K))
