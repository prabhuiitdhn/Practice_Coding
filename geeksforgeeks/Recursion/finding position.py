"""
https://practice.geeksforgeeks.org/problems/finding-position2223/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=KLA%20Tencor&category[]=Recursion&sortBy=difficulty

given the number of people and selected every people who are in even position then again selected the even position
and continue until left with one person
"""


def nthPosition(n):
    """
    @param n: no of people
    @return: last person who left after selecting all the people in even manner
    """

    global newList

    def nthPosotionHelper(list):
        newList = []
        if len(list) == 2:
            return [list[1]]
        start = 1
        while start < len(list):
            newList.append(list[start])
            start = start + 2
        return newList

    l = []
    for i in range(1, n + 1):
        l.append(i)

    length = len(l)
    while length > 1:
        newList = nthPosotionHelper(l)
        length = len(newList)
        l = newList

    return newList[0]


def nthPosition2(n):
    """
    it is just to find the last element after selecting from the even number.
    So, always power of 2th element will be selected.
    last power of 2 near to n will be available till last.
    @param n:
    @return:
    """
    if n == 1:
        return n
    p = 1

    while p < n:
        p *= 2
        # it is for passing to power of 2
        if p == n:
            # if power of 2 is equal to n
            return p
    # else last power of 2/2
    return p / 2


n = 9
p = nthPosition2(n)
print(int(p))
