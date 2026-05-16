# Enter your code here. Read input from STDIN. Print output to STDOUT
# t = int(input())
t = 1
for i in range(t):
    # n = int(input())
    n = 8
    # nums = list(
    #     map(
    #         int, input().split()
    #     )
    # )
    nums = [176, -272, -272, -45, 269, -327, -945, 176]

    min_ = min(nums)
    max_ = max(nums)

    count = [0]*(max_- min_ + 1)
    for j in range(len(nums)):
        count[nums[j]-min_] += 1

    for k in range(len(count)):
        total = count[k]
        for l in range(total):
            print(k + min_)
    print()
