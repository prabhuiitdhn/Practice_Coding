"""
https://practice.geeksforgeeks.org/problems/maximum-product-subarray3604/1?page=1&company[]=Amazon&company[]=Microsoft&company[]=Adobe&company[]=Samsung&company[]=MakeMyTrip&company[]=Goldman%20Sachs&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=Nvidia&company[]=KLA%20Tencor&category[]=Dynamic%20Programming&sortBy=difficulty


Given an array with +ve, 0 and -ve numbers. Needed to find the maximum product of the subarray in an array
example: [6, -3, -10, 0, 2]
subarray [6, -3, -10] will have 180 which is maximum in an array

"""


def maxproduct2(arr, n):
    """

    @param arr: input as arr
    @param n: number of elements in an array
    @return:
    """
    # initialisation of initial minimum, initial maximum, and overallMaximum
    MN = arr[0]  # initial minimum
    MX = arr[0]  # initial maximum
    MXX = arr[0]  # Overall Maximum
    # count = 1
    # maxxcount = 1
    for i in range(1, n):
        # after initialing the inital min, max and overall max as arr[0] value
        # next to find the min and max between the next elements.

        if arr[i - 1] == 0:
            # this is the case when in-between elements comes as 0 bcz product with 0 is going to be 0 so
            # need to look into another sub array
            MX = arr[i]
            MN = arr[i]
            MXX = max(MXX, MX)
            # count = 1
            continue
        # count +=1
        # current elements needs to mulitply with min and max
        t1 = MN * arr[i]
        t2 = MX * arr[i]
        # find the multiplied min and max with current element
        MX = max(MX, max(t1, t2))
        # Check if current multiplication is max than previous max or not, If not then current max will be new max
        MN = min(MN, min(t1, t2))
        # Check if current multiplication is min than previous min or not, If not then current min will be new min
        MXX = max(MX, MXX)
        # maxxcount = max(maxxcount, count)
        # check which max is overall max.
    # print(maxxcount)
    return MXX


arr = [6, -3, -10, 0, 2]
# arr= [2, 3, 4, 5, -1, 0]
# arr= [0, 0,-5,0,0]
# arr=[25,10,-2,8,5,3]
# arr = [-4]

# arr=[0, 1, -2, -3, -4]
# arr=[-1, -2, 0, 1, 2]
n = len(arr)
print(maxproduct2(arr, n))
