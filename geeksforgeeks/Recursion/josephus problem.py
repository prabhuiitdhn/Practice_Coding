"""
https://practice.geeksforgeeks.org/problems/josephus-problem/1?page=1&company[]=Amazon&company[]=Adobe&company[]=Samsung&company[]=Oracle&company[]=Qualcomm&company[]=Linkedin&company[]=KLA%20Tencor&category[]=Recursion&sortBy=difficulty

given a total number of people n and k which indicates k-1 people will be skipped and kth person will be killed.

"""
def josephus(n, k):
    """
    @param arr: input array which takes the elements
    @param n: total number of people in array
    @param k: kth person needed to be killed.
    @return: the position which is last and safe
    """
    list_of_elements = []
    for i in range(1, n+1):
        list_of_elements.append(i)

    start = 0
    while len(list_of_elements)!=1:
        index_to_be_deleted = (start + k) % len(list_of_elements)
        if index_to_be_deleted== 0:
            start = 0
            list_of_elements.remove(list_of_elements[-1])
        else:
            start = index_to_be_deleted - 1
            list_of_elements.remove(list_of_elements[index_to_be_deleted-1])


    print(list_of_elements)
    return list_of_elements[-1]






# arr = [1, 2, 3, 4, 5]
n = 17
k = 16
p = josephus(n, k)
print(p)