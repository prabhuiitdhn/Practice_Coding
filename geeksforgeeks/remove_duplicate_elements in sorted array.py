'''
https://practice.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1?page=2&company[]=Samsung&sortBy=submissions
in a sorted array, needed to remove all the duplicate elements without using set and hashmap
approach: two pointer approach
'''


def remove_duplicates_1(arr, N):
    l = 0
    r = l+1
    lp = []
    while(r<N):
        if arr[l] != arr[r]:
            lp.append(arr[l])
            # l = l+1
            # r = l+1
        l = l+1
        r = l+1
    lp.append(arr[N-1])
    print(lp)

def remove_duplicates_2(A, N):
    l = 0
    r = 1

    while (r < N):
        if A[l] != A[r]:
            A[l + 1] = A[r]
            l = l + 1
        r = r + 1
    return (l + 1)


if __name__ == '__main__':
    arr = [1,3, 4 ,5 ,6, 12, 13, 17, 19, 22, 23, 25, 27, 28, 28, 35, 36, 37, 39, 43, 46, 48 ,54, 59, 62, 63, 65 ,68 ,68, 70, 70, 72, 79, 82, 83, 92, 92, 93, 95, 96, 96, 100]
    N = len(arr)
    new_size_of_array = remove_duplicates_2(arr, N)
    print(new_size_of_array)