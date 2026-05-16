"""
https://practice.geeksforgeeks.org/problems/shuffle-integers2401/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=KLA%20Tencor&category[]=Recursion&sortBy=difficulty
given an array of n elements and shuffle the array which outputs arrange out as a1, b1, a2, b2, a3,b2..an/2, bn/2
example:
n =6
array= [a1, a, a3, b1, b2, b3]
arr1 = [a1, a2, a3]
arr2 = [b1, b2, b3]

shuffle array = [a1, a2, a3, b1, b2, b3]
condition:
Expected time complexity: O(n)
Expected space = O(1)
"""


def shufflearray(arr, n):
    # it fails when number has 0, It will pass when number will have >0 elements.
    """
    this approach is failing some cases.
    https://www.youtube.com/watch?v=7HZmP8r1FBE
    @param arr:
    @param n:
    @return:
    """
    half = n // 2

    for i in range(n):
        currentPos = i
        currentNum = arr[i]

        while currentNum > -1:
            if currentPos < half:
                newPos = 2 * currentPos
            else:
                newPos = 2 * (currentPos - half) + 1

            newNum = arr[newPos]
            arr[newPos] = - currentNum
            currentNum = newNum
            currentPos = newPos

    for i in range(n):
        if arr[i] < 0:
            arr[i] = -(arr[i])

    print("Line no 48:", len(arr))
    return arr

def shufflearray2(arr, n):
    # using extra space.
    """
    this is not running in geeksforgeeks interpretor
    @param arr:
    @param n:
    @return:
    """
    temp = [-1] * n

    half = n//2
    forward = 0
    backward = half

    for i in range(n):
        if i%2 ==0:
            temp[i] = arr[half-backward]
            backward -= 1
        else:
            temp[i] = arr[half + forward]
            forward +=1
    return temp

def shufflearray3(arr, n):
    # using extra space.
    temp = []
    half = n//2
    for i in range(half):
        temp.append(arr[i])
        temp.append(arr[half+i])
    return temp

def shufflearray4(arr,n):
    # using O(1) space
    """
    problem is to shuffle the number without using extra space in an array
    @param arr:
    @param n:
    @return:
    """
    mid = n // 2 # find the half of the number
    a = arr[:mid] # divide this into two half [first half]
    b = arr[mid:] # divide this into two half [second half]

    # modifying the array
    arr[0::2] = a # From 0th to end but after each 2 elements will be replaced by elements in a (first half of array)
    arr[1::2] = b # From 1st index  to end but after each 2 elements will be replaced by elements in b (second half of array)
    return arr


# a = [31,40,38,25,42,3,37,11,16,8,6,37,20,20,22,16,7,1,8,31,
#      20,10,17,49,4,41,12,24,23,10,49,0,19,9,29,22,34,44,18,8]
# n = 40

a = [1, 2, 9, 15, 0, 7]
n =6
newarray = shufflearray4(a, n)
print(newarray)