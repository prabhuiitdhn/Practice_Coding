# Enter your code here. Read input from STDIN. Print output to STDOUT


t = int(input())
for i in range(t):
    n = int(input())
    nums = list(
        map(
            int, input().split()
        )
    )
    nums = [2 * i for i in nums]
    # print(nums)
    total = 0
    for i in nums:
        total ^= i

    print(total)
